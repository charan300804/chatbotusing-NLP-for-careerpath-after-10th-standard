import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        
counter = 0

def main():
    global counter
    st.title("Chat bot using NLP for Career guidance after 10th standard ")

    # Create a sidebar menu with options
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Home Menu
    if choice == "Home":
        st.write("Welcome to the Career Guidance Chatbot for post-10th students. Type your query, and we’ll guide you.")
        # Check if the chat_log.csv file exists, and if not, create it with column names
        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("user:", key=f"user_input_{counter}")
        if user_input:

            # Convert the user input to a string
            user_input_str = str(user_input)

            response = chatbot(user_input)
            st.text_area("Chatbot:", value=response, height=120, max_chars=None, key=f"chatbot_response_{counter}")

            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")

            # Save the user input and chatbot response to the chat_log.csv file
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input_str, response, timestamp])

            if response.lower() in ['goodbye', 'bye']:
                st.write("Thank you for chatting with me. Have a great day!")
                st.stop()

    # Conversation History Menu
    elif choice == "Conversation History":
        # Display the conversation history in a collapsible expander
        st.header("Conversation History")
        # with st.beta_expander("Click to see Conversation History"):
        with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                st.text(f"User: {row[0]}")
                st.text(f"Chatbot: {row[1]}")
                st.text(f"Timestamp: {row[2]}")
                st.markdown("---")

    elif choice == "About":
        st.write("The goal of this project is to develop a chatbot that provides career guidance for students after the 10th standard. The chatbot uses Natural Language Processing (NLP) and Logistic Regression to understand and respond to user queries by extracting relevant intents and entities. Built with Streamlit, a Python library for interactive web applications, the chatbot offers personalized career advice based on the user's input.")

        st.subheader("Project Summary:")

        st.write("""
        The project is divided into two parts:
        1.NLP & Logistic Regression: Used to train the chatbot on intents and entities related to career guidance after the 10th standard.
        2.Streamlit Interface: A web-based platform built with Streamlit for user interaction, providing personalized career advice.
        """)

        st.subheader("Data Details:")

        st.write("""
        The dataset used in this project consists of labeled intents and entities, stored in a structured list:

          Intents: Represents the user's career-related query or goal (e.g., "career options", "education path", "skills needed").
          Entities: Key details extracted from the user’s input (e.g., "What career options are available after 10th?", "What skills are needed for engineering?", "What are the study options after 10th?").
          Text: The user’s input text seeking career guidance after 10th standard.
        """)

        st.subheader("Career Guidance Chatbot Streamlit Interface")
        st.write("The chatbot interface is built using Streamlit, featuring a text input box for users to submit their queries and a chat window to display the chatbot’s responses. The interface utilizes the trained model to process user input and generate relevant career guidance.")

        st.subheader("Project Wrap-up:")

        st.write("This project developed a career guidance chatbot for students after the 10th standard, using NLP and Logistic Regression for understanding user queries. Built with Streamlit, the chatbot provides an interactive interface for exploring career options. Future work could include expanding the dataset and using advanced NLP and deep learning techniques to enhance its capabilities.")

if __name__ == '__main__':
    main()
