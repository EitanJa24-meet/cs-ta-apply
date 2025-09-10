running = True
print ("Welcome, This is the MEET chatbot")
data = {
    "What does MEET stand for?": "Middle East Entrepreneurs of Tomorrow, a non-profit uniting young Israeli and Palestinian leaders.",
    "What is MEET's main goal?": "To build a network of Israeli and Palestinian leaders who use tech for regional change.",
    "Who can join MEET?": "Motivated Israeli and Palestinian high school students interested in tech and leadership.",
    "What subjects are taught?": "Advanced computer science, entrepreneurship, and leadership, often with instructors from MIT.",
    "How long is the program?": "A three-year program with intensive summer sessions and year-round project work.",
    "What is the teaching language?": "English is the official language, providing a neutral ground for communication.",
    "What happens after graduation?": "Graduates join a lifelong alumni network for continued support and collaboration."}

# data = {"1": "1.1", "2": "2.2"}

while running == True:
    user_prompt = input("What would you like to know about MEET: ").lower()
    try:
        for i in data:
            if i.lower() == user_prompt:
                output = data[i]
    except KeyError:
        print("error, your input is not in my databse. Try asking a different question")
    else:
        print("\n",output, "\n")
        