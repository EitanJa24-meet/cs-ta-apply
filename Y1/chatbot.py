# importing library that helps compare sequences (for input case sensetivity)
import difflib

#welcome message
print ("Welcome, This is the MEET chatbot")
# main data dictionary with all questiosn and answers
data = {
    "What is MEET?": "MEET (Middle East Entrepreneurs of Tomorrow) is a non-profit that brings together young Israeli and Palestinian leaders to learn tech, entrepreneurship, and leadership.",
    "What does MEET stand for?": "Middle East Entrepreneurs of Tomorrow, a non-profit uniting young Israeli and Palestinian leaders.",
    "What is MEET's main goal?": "To build a network of Israeli and Palestinian leaders who use tech for regional change.",
    "Who can join MEET?": "Motivated Israeli and Palestinian high school students interested in tech and leadership.",
    "What subjects are taught?": "Advanced computer science, entrepreneurship, and leadership, often with instructors from MIT.",
    "How long is the program?": "A three-year program with intensive summer sessions and year-round project work.",
    "What is the teaching language?": "English is the official language, providing a neutral ground for communication.",
    "What happens after graduation?": "Graduates join a lifelong alumni network for continued support and collaboration."}

# defining a list of all the dictionary's  keys for later use
keys = list(data.keys())

# main while loop that keeps the chatbot running
while True:
    # what the the user is prompted
    initial_prompt = "What would you like to know about MEET (Enter 'help' for questions list or enter 'bye' to exit.): "
    # user inputs his question and it becomes all lower for less case sensetivity
    user_prompt = input(initial_prompt).lower()
    # if enters "bye" then says goodbye amd stops running
    if user_prompt == "bye":
        print("\n","Goodbye", "\n")
        # ending the while loop
        break
    # if user inputs "help", shows available questions
    elif user_prompt == "help":
        print("\n","Available questions:")
        #displays the keys of the dictionary for all possible questions
        print(keys, '\n')
        #keeps the while loop running
        continue

    # uses difflib library to find the best match based on user prompt, all the keys in the dictionary in lower case. 
    # it outputs a list with the mathces and "n=1" makes it have 1 result and "cutoff=0.45" determines how similar it needs to be (for exp. here 45% match)
    # [what it does is find the amount of matching charecters and finds the pair with the most similarity]
    matches = difflib.get_close_matches(user_prompt, [k.lower() for k in keys], n=1, cutoff=0.45)
    
# because empty list is falsy, if its empty will skip this part
    if matches:
        #goes through keys and finds the value that matches the key outputed from the "get_close_matches" function
        for k in keys:
            if k.lower() == matches[0]:
                print("\n" + data[k] + "\n")
                #stops if finds a result
                break
    #if nothing wrks will say error that doesnt understand
    else:
        print("\n","Sorry, I don't understand that question. Try 'help' for the questions list","\n")


# add for more functionability:
# add an api for getting more live data into the dictionary
# using a database and not having the data hardcoded 
# adding translation features so it is accessable in all languages (using api or database)
# having a proper frontend for entering data
