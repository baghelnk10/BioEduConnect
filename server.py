from flask import Flask, render_template, request, session, jsonify, redirect, url_for
import openai
from openai import OpenAI # for calling the OpenAI API
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Configure the Flask app with your database URI
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Adjust the URI as needed
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable the modification tracking

# Initialize the Flask-SQLAlchemy extension
#db = SQLAlchemy(app)

#class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #email = db.Column(db.String(120), unique=True, nullable=False)
    #password = db.Column(db.String(60), nullable=False)

# Set your OpenAI API key
openai.api_key = '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'

# Your GPT model
GPT_MODEL = "gpt-3.5-turbo"

# Set a secret key for session management
#app.secret_key = 'your-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/content')
def content():
    return render_template('content.html')

@app.route('/chap1')
def chap1():
    return render_template('chap1.html')

@app.route('/chap3')
def chap3():
    return render_template('chap3.html')

@app.route('/chap2')
def chap2():
    return render_template('chap2.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')  


EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"


@app.route('/process_query', methods=['POST'])
def process_query():
    user_query = request.json.get('user_query', '')

    # Use the OpenAI GPT-3 Turbo model for a simple chat response
    # models
    response = openai.chat.completions.create(
        messages=[
            {'role': 'system', 'content': 'You are responsible for responding to High School-level questions pertaining to the chapter titled "The Fundamental Unit of Life: Cell." If users inquire about topics other than this or seek responses unrelated to the specified chapter, kindly inform them that you can only address questions related to the designated subject. Please adhere to the provided guidelines.'},
            {'role': 'user', 'content': f"{user_query}"},
            ],
        model=GPT_MODEL,
        temperature=0,
    )
    model_reply = response.choices[0].message.content

    return jsonify({'response': model_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
