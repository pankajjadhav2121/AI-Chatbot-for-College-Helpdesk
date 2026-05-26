# AI Chatbot for College Helpdesk

A simple AI-based College Helpdesk Chatbot built using Python and JSON.  
This chatbot answers common student queries related to college information such as fees, admission, courses, timings, and contact details.

---

## Project Overview

This project is a console-based chatbot created using Python.

The chatbot reads predefined responses from a JSON file and matches keywords entered by the user to provide appropriate answers.

It is a beginner-friendly Artificial Intelligence project that demonstrates the basics of:

- Chatbot development
- JSON data handling
- String matching
- Python loops and conditions

---

## Features

- Simple AI chatbot
- College helpdesk system
- Reads responses from JSON file
- Keyword-based response matching
- Beginner-friendly Python project
- Console-based interaction
- Easy to customize

---

## Technologies Used

- Python
- JSON

---

## Concepts Used

This project helps in learning:

- Python Basics
- Loops
- Conditional Statements
- File Handling
- JSON Handling
- Dictionaries
- String Operations
- Basic AI Chatbot Logic

---

## Project Structure

```text
AI-Chatbot-College-Helpdesk/
│
├── chatbot.py
├── responses.json
└── README.md
```

---

## responses.json Example

Create a file named `responses.json`

```json
{
    "hello": "Hello! How can I help you?",
    "admission": "Admissions are open now.",
    "fees": "The fee structure is available on the college website.",
    "courses": "We offer B.Tech, BCA, MCA, and MBA courses.",
    "timing": "College timing is 9 AM to 5 PM."
}
```

---

## How the Chatbot Works

1. The chatbot loads responses from a JSON file.
2. The user enters a question.
3. The chatbot searches for matching keywords.
4. If a keyword matches:
   - Bot gives the related response.
5. If no keyword matches:
   - Bot shows a default message.

---

## Requirements

Make sure Python is installed on your system.

### Check Python Version

```bash
python --version
```

or

```bash
python3 --version
```

---

## How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/AI-Chatbot-College-Helpdesk.git
```

---

### Step 2: Open Project Folder

```bash
cd AI-Chatbot-College-Helpdesk
```

---

### Step 3: Run the Python File

```bash
python chatbot.py
```

If `python` does not work, use:

```bash
python3 chatbot.py
```

---

## Example Output

```text
==============================
 College Helpdesk Chatbot
Type 'exit' to close chatbot
==============================

You: hello
Bot: Hello! How can I help you?

You: fees
Bot: The fee structure is available on the college website.

You: exit
Bot: Thank you!
```

---

## Future Improvements

- GUI using Tkinter
- Voice-based chatbot
- NLP integration
- Database connectivity
- Web version using Flask
- Machine Learning chatbot

---

## Learning Outcomes

By building this project, you can learn:

- Basic AI chatbot development
- Python file handling
- JSON data management
- User input handling
- Logic building
- Beginner AI concepts

---
