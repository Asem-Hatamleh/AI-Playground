import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button
import re
import time  
import random

# Load data from JSON file
with open('intents.json', encoding='utf-8') as file:
    intents = json.load(file)

lemmatizer = WordNetLemmatizer()

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))

input_data = []
output_data = []

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    # Create bag of words
    bag = [1 if word in word_patterns else 0 for word in words]

    # Create one-hot encoded output
    output_row = np.zeros(len(classes))
    output_row[classes.index(document[1])] = 1

    # Append to input and output lists
    input_data.append(np.array(bag))
    output_data.append(output_row)

# Convert input and output lists to NumPy arrays
train_x = np.array(input_data)
train_y = np.array(output_data)

# Create model
model = Sequential()
model.add(Dense(128, input_shape=(len(words),), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(classes), activation='softmax'))

sgd = tf.keras.optimizers.legacy.SGD(learning_rate=0.001, decay=1e-5, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train model
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=2)
model.save('mikasa')
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words):
    bag = [0] * len(words)
    for w in sentence:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def get_bot_response(user_input):
    if any(operator in user_input for operator in ['+', '-', '*', '/']):
        return evaluate_math_expression(user_input)
    
    sentence_words = clean_up_sentence(user_input)
    input_bag = bag_of_words(sentence_words, words)

    # Predict class
    result = model.predict(np.array([input_bag]))[0]
    predicted_class_index = np.argmax(result)
    predicted_class = classes[predicted_class_index]

    # Get a random response from the predicted class
    for intent in intents['intents']:
        if intent['tag'] == predicted_class:
            responses = intent['responses']
            return [random.choice(responses)]

def evaluate_math_expression(user_input):
    # Extract numerical expressions using regular expression
    matches = re.findall(r'\b\d+\s*[\+\-\*/]\s*\d+\b', user_input)

    if matches:
        result = eval(matches[0])
        return str(result)
    else:
        # Check for additional expressions with addition or parentheses
        matches_additional = re.findall(r'\b\d+(\s*[\+\-\*/]\s*\d+|\s*\(\s*\d+(\s*[\+\-\*/]\s*\d+)*\s*\)\s*)+\b', user_input)
        if matches_additional:
            result = eval(matches_additional[0])
            return str(result)
        else:
            return "I'm not sure about that. Please enter a valid mathematical expression. O)"

def send_message(event=None):
    user_input = entry.get()
    if user_input.lower() == "quit":
        root.destroy()
    else:
        user_msg = f"You: {user_input}\n\n"
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, user_msg, 'user')  # 'user' tag for user messages

        bot_responses = get_bot_response(user_input)

        for response in bot_responses:
            # Display "Bot:" once at the beginning of the response
            bot_msg = "Bot:"
            chat_box.insert(tk.END, bot_msg, 'bot_name')  # 'bot_name' tag for bot's name
            chat_box.yview(tk.END)
            root.update()
            time.sleep(0.1)

            # Iterate over each response and then each word, appending them without delays
            bot_words = response.split()
            for word in bot_words:
                bot_msg = f" {word}"  # Space added before each word
                chat_box.insert(tk.END, bot_msg, 'bot_response')  # 'bot_response' tag for bot's responses
                chat_box.yview(tk.END)
                root.update()

            # Add an extra newline after each response
            chat_box.insert(tk.END, "\n\n", 'bot_response')  # 'bot_response' tag for bot's responses

        chat_box.config(state=tk.DISABLED)

        entry.delete(0, tk.END)

        # Scroll to the end of the chat box
        chat_box.yview(tk.END)

# Creating a new root window
root = tk.Tk()
root.title("Mikasa")

# Frame for the chat box and scrollbar
frame = tk.Frame(root, bg="#2C3E50")  # Dark Blue Background
frame.pack(pady=10)

# Scrollbar for the chat box
scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Text box for the chat with a larger size
chat_box = Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#34495E", fg="#ECF0F1", font=("Arial", 14), height=20, width=60)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
chat_box.config(state=tk.DISABLED)

# Configuring scrollbar for the chat box
scrollbar.config(command=chat_box.yview)

# Entry widget for user input
entry = Entry(root, font=("Arial", 20), width=40, bd=6)
entry.bind("<Return>", send_message)
entry.pack(pady=10, side=tk.LEFT)

# Send button next to the entry widget
send_button = Button(root, text="Send", command=send_message, bg="#3498DB", fg="#FFFFFF", font=("Arial", 14))  # Blue Background, White Text
send_button.pack(pady=10, side=tk.LEFT)

# Configuring tags for different message types
chat_box.tag_configure('user', foreground='#3498DB')       # Blue color for user messages
chat_box.tag_configure('bot_name', foreground='#27AE60', font=('Arial', 14, 'italic', 'bold'))  # Green color for bot's name
chat_box.tag_configure('bot_response', foreground='#27AE60', font=('Arial', 14))  # Green color for bot's responses

# Main loop to run the GUI
root.mainloop()
