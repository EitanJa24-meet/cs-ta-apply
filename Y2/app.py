from flask import Flask, render_template, request, redirect, url_for
from flask import session
import pyrebase
import difflib

firebaseConfig = {
    "apiKey": "AIzaSyBdB_yZcgOQIL_H_yeL0EdfPgiH6URi3TU",
    "authDomain": "cs-ta-apply.firebaseapp.com",
    "databaseURL": "https://cs-ta-apply-default-rtdb.firebaseio.com",
    "projectId": "cs-ta-apply",
    "storageBucket": "cs-ta-apply.firebasestorage.app",
    "messagingSenderId": "1007222885184",
    "appId": "1:1007222885184:web:e3190b58a65f62dedbc8a5",

  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db= firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'



@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    username= request.form['name']
    try:
      user = auth.create_user_with_email_and_password(email, password)
      session['localId'] = user['localId']
      uid = session.get('localId')
      name = {"name": username}
      db.child("users").child(uid).set(name)
      return redirect(url_for('chat'))
    except Exception as e:
        print(e) 
        return redirect(url_for('error'))

  else:
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['localId'] = user['localId']
            return redirect(url_for('chat'))
        except Exception as e:
            print(e) 
            return redirect(url_for('error'))
    else:
        return render_template('login.html')


# @app.route("/", methods=["GET", "POST"])
# def chat():
#     if "localId" not in session:
#         return redirect(url_for('login'))
    
#     if "conversation" not in session:
#         session["conversation"] = [] 

#     if request.method == "POST":
#         user_prompt = request.form['user_prompt']
#         matches = difflib.get_close_matches(user_prompt, [k.lower() for k in keys], n=1, cutoff=0.45)
#         if matches:
#             for k in keys:
#                 if k.lower() == matches[0]:
#                     output = data[k]
#                     break
#         else:
#             output = "Sorry, I don't understand that question. Try again"

#         session['conversation'].append({"user": user_prompt, "bot": output})

#     # return render_template("library.html", user_ideas = user_ideas)
#     return render_template("chat.html", conversation=session.get("conversation"))

@app.route("/", methods=["GET", "POST"])
def chat():
    if "localId" not in session:
        return redirect(url_for('login'))

    # fetch existing conversation from DB
    uid = session.get('localId')
    stored_convo = db.child("conversations").child(uid).get().val()
    
    if stored_convo is None:
        session["conversation"] = []
    else:
        session["conversation"] = stored_convo  # load previous conversation

    # fetch latest dictionary from Firebase
    data = db.child("data").get().val() or {}
    keys = list(data.keys())

    if request.method == "POST":
        user_prompt = request.form['user_prompt'].strip()
        matches = difflib.get_close_matches(user_prompt, [k.lower() for k in keys], n=1, cutoff=0.55)

        if matches:
            for k in keys:
                if k.lower() == matches[0]:
                    output = data[k]
                    break
        else:
            output = "Sorry, I don't understand that question. Try again."

        # append new Q&A
        session['conversation'].append({"user": user_prompt, "bot": output})

        # update DB without overwriting old conversation
        db.child("conversations").child(uid).update({str(len(session['conversation'])-1): {"user": user_prompt, "bot": output}})

    # get username
    user_data = db.child("users").child(uid).get().val()
    username = user_data.get('name') if user_data else "Guest"

    return render_template("chat.html", conversation=session.get("conversation"), name=username)



@app.route('/signout', methods=['POST'])
def signout():
  session.pop('localId', None)

  return redirect(url_for('login'))

# @app.route('/submit_answer', methods=['POST'])
# def submit_answer():
#     if "localId" not in session:
#         return redirect(url_for('login'))

#     question = request.form['question']
#     answer = request.form['user_answer']

#     # save new Q&A in DB
#     db.child("data").child(question).set(answer)

#     # update session keys if needed
#     global keys
#     keys.append(question)

#     # save to user's conversation
#     user_id = session['localId']
#     session['conversation'].append({"user": question, "bot": answer})
#     db.child("conversations").child(user_id).set(session['conversation'])

#     return redirect(url_for('chat'))

if __name__ == '__main__':
  app.run(debug=True)
