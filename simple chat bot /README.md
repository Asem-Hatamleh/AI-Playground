# Mikasabot - AI Chatbot  

Mikasabot is a simple AI-powered chatbot that uses natural language processing and machine learning to engage with users. It can handle basic conversations, perform mathematical evaluations, and has a graphical user interface (GUI).  

## Features  
- **Natural Language Processing (NLP):** Uses NLTK for tokenization and lemmatization.  
- **Machine Learning:** Built with Keras and TensorFlow to classify user inputs based on a trained neural network model.  
- **Mathematical Expression Evaluation:** Can evaluate basic arithmetic expressions.  
- **Graphical User Interface (GUI):** Built with `tkinter` for an interactive chat experience.  

## Technologies Used  
- **NLTK** (Natural Language Toolkit)  
- **WordNetLemmatizer** (for word normalization)  
- **JSON & Pickle** (for storing intents and model data)  
- **Keras & TensorFlow** (for training the chatbot’s neural network)  
- **Tkinter** (for the chatbot’s GUI)  

## Training Process  
1. **Data Preparation:** Mikasabot is trained on a JSON dataset (`intents.json`). Words are tokenized, lemmatized, and converted into a bag-of-words representation.  
2. **Neural Network Model:**  
   - **Input Layer:** Processes the input text.  
   - **Hidden Layers:** Uses ReLU activation to learn patterns.  
   - **Output Layer:** Uses softmax activation to classify user intents.  
3. **Model Training:** The chatbot is trained using a stochastic gradient descent optimizer (SGD) with categorical cross-entropy loss.  

## Usage  
1. Run the chatbot script:  
   ```bash
   python chatbot.py
