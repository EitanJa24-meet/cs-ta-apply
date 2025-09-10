import difflib

print ("Welcome, This is the MEET chatbot")
data = {
    "What is MEET?": "MEET (Middle East Entrepreneurs of Tomorrow) is a non-profit that brings together young Israeli and Palestinian leaders to learn tech, entrepreneurship, and leadership.",
    "What does MEET stand for?": "Middle East Entrepreneurs of Tomorrow, a non-profit uniting young Israeli and Palestinian leaders.",
    "What is MEET's main goal?": "To build a network of Israeli and Palestinian leaders who use tech for regional change.",
    "Who can join MEET?": "Motivated Israeli and Palestinian high school students interested in tech and leadership.",
    "What subjects are taught?": "Advanced computer science, entrepreneurship, and leadership, often with instructors from MIT.",
    "How long is the program?": "A three-year program with intensive summer sessions and year-round project work.",
    "What is the teaching language?": "English is the official language, providing a neutral ground for communication.",
    "What happens after graduation?": "Graduates join a lifelong alumni network for continued support and collaboration."}

# data = {"1": "1.1", "2": "2.2"}
keys = list(data.keys())


while True:
    intial_prompt = "What would you like to know about MEET (Enter 'help' for questions list or enter 'bye' to exit.): "
    user_prompt = input(intial_prompt).lower()
    if user_prompt == "bye":
        print("\n","Goodbye", "\n")
        break
    elif user_prompt == "help":
        print("\n","Available questions:")
        for h in keys:
            print ("-", h)
        print('\n')
        continue

    matches = difflib.get_close_matches(user_prompt, [k.lower() for k in keys], n=1, cutoff=0.5)
    
# because empty list is falsy, if its empty will skip this part
    if matches:
        for k in keys:
            if k.lower() == matches[0]:
                print("\n" + data[k] + "\n")
                break
    else:
        print("\n","Sorry, I don't understand that question. Try 'help' for the questions list","\n")

        