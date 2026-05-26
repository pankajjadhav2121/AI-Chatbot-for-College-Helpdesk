# AI Chatbot for College Helpdesk

# Import json module for read data
import json

# Open JSON file and load responses
with open("responses.json", "r") as file:
    responses = json.load(file)

print("==============================")
print(" College Helpdesk Chatbot ")
print("Type 'exit' to close chatbot")
print("==============================")

#loop for chatbot conversation
while True:

    # Take user input
    student_input= input("You: ").lower()

    # Exit condition
    if student_input == "exit":
        print("Bot: Thank you!")
        break

    # Flag variable
    found = False

    # Check keywords in user input
    for key in responses:

        # If keyword found
        if key in student_input:
            print("Bot:", responses[key])
            found = True
            break

    # keywords not match
    if not found:
        print("Bot: Sorry, I don't understand your question.")