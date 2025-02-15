from flask import Flask, render_template, request, session
import spacy
from cat_responses import generate_cat_response

app = Flask(__name__)
app.secret_key = 'your-secret-key-1234'  # Change for production

# Load NLP model
nlp = spacy.load("en_core_web_sm")

@app.before_request
def initialize_chat():
    if 'history' not in session:
        session['history'] = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['message']
        doc = nlp(user_input.lower())
        
        # Get cat response with NLP processing
        response = generate_cat_response(doc)
        
        session['history'].append(('user', user_input))
        session['history'].append(('bot', response))
        session.modified = True
    
    return render_template('chat.html', history=session['history'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,threaded=True, debug=True)