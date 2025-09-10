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
    intial_prompt = "What would you like to know about MEET (Enter 'help' for questions list or enter 'bye' to exit.): "
    user_prompt = input(intial_prompt).lower()
    if user_prompt == "bye":
        break
    elif user_prompt == "help":
        output = data.keys()
        print("\n",output, "\n")
    else:
        found = False
        for i in data:
            if i.lower() == user_prompt:
                output = data[i]
                print("\n",output, "\n")
                found = True
        if not found:
            print("\n","error, your input is not in my databse. Try asking a different question","\n")

        