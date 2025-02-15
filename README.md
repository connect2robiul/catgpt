# catgpt

# CatGPT - A Fun Flask Chatbot with NLP

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)

CatGPT is a chatbot built with Flask and SpaCy. It's designed to demonstrate basic natural language processing (NLP) capabilities in a conversational interface. 🐱💬

---

## Features
- **Flask-Based Web App**: Simple and lightweight backend for chat functionality.
- **NLP with SpaCy**: Processes user input using SpaCy's `en_core_web_sm` model.
- **Session-Based Chat History**: Stores chat history during a session for context.
- **Fun Responses**: (Make sure to describe how your bot generates fun or cat-themed responses!)

---

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.7 or higher
- Flask
- SpaCy (with the `en_core_web_sm` model)

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/connect2robiul/catgpt.git
cd catgpt
```
### Set Up Your Python Environment
```bash
conda create --name catgpt python=3.9 -y
conda activate catgpt
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### Install Dependencies 
```bash
pip install -r requirements.txt
```
### Download the SpaCy Model
```bash
python -m spacy download en_core_web_sm
```
### Run the Application
```bash
python app.py
```
### Access the App
```bash
http://127.0.0.1:8080
```

## File Structure 
```bash
catgpt/
├── app.py                 # Main Flask app
├── requirements.txt       # Dependencies for the project
├── templates/
│   └── chat.html          # Frontend for the chatbot
└── README.md              # Documentation
``` 
