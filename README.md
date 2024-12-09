
# Chatbot using NLP for carrier after 10th standard

## Overview
This project implements a chatbot using Natural Language Processing (NLP) techniques for getting the guidence on the carrier after passing out your 10th standard. The chatbot is designed to understand user intents and provide appropriate responses based on predefined patterns and responses. It utilizes the `nltk` library for natural language processing, `scikit-learn` for machine learning, and `streamlit` for creating an interactive web interface.

---

## Specifications
- Understands User Intents:
The system is capable of recognizing various user intentions, such as:
Greetings (e.g., "Hello," "Hi there").
Farewells (e.g., "Goodbye," "See you later").
Expressions of Gratitude (e.g., "Thank you," "Thanks a lot").
Other Common Intents (e.g., asking for help, making requests).
- Provides Relevant Responses:
Based on the input provided by the user, the system generates appropriate and meaningful replies, ensuring a smooth and coherent conversation.
- Maintains Conversation History:
Keeps track of the ongoing conversation to provide context-aware responses.
Allows the user to review past interactions if needed, creating a personalized and connected experience.
- Technology and Frameworks Used:
Built using Python, a versatile and widely-used programming language.
Utilizes popular libraries and frameworks for Natural Language Processing (NLP) and Machine Learning to enhance understanding and response generation. Examples might include libraries like NLTK, spaCy, or TensorFlow.

---

## Implementation Tools
- **Python**
- **NLTK**
- **Scikit-learn**
- **Streamlit**
- **JSON** for intents data

---

## Process of Installation

### 1. Clone the Repository from the Github
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages to run the Program with out any inconvenience
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
```python
import nltk
nltk.download('punkt')
```

---

## Utilization
To run the chatbot application, execute the following command:
```bash
streamlit run app.py
```

Once the application is running, you can interact with the chatbot through the web interface. Type your message in the input box and press Enter to see the chatbot's response.

---

## Intents Data
The chatbot's behavior is defined by the `intents.json` file, which contains various tags, patterns, and responses. You can modify this file to add new intents or change existing ones.

---

## Interaction Records
The chatbot saves the conversation history in a CSV file (`chat_log.csv`). You can view past interactions by selecting the "Conversation History" option in the sidebar.

---

## Contributing
Contributions to this project are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **NLTK** for natural language processing.
- **Scikit-learn** for machine learning algorithms.
- **Streamlit** for building the web interface.

---

Replace `<repository-url>` and `<repository-directory>` with the actual URL of your repository and the name of the directory where the project is located. Adjust any sections as necessary to better fit your project's specifics.
