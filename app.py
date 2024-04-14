from flask import Flask, render_template, request, session, jsonify, redirect, url_for
import os
from openai import OpenAI
import openai
app = Flask(__name__)

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Your GPT model
GPT_MODEL = "gpt-3.5-turbo"

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
            {'role': 'system', 'content': 'You are responsible for responding to High School-level Biology related questions only. If users inquire about topics other than this or seek responses unrelated to the specified topic, kindly inform them that you can only address questions related to the designated subject. Please adhere to the provided guidelines.'},
            {'role': 'user', 'content': f"{user_query}"},
            ],
        model=GPT_MODEL,
        temperature=0,
    )
    model_reply = response.choices[0].message.content

    return jsonify({'response': model_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
