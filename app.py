from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(_name_)

# OpenAI API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('query')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that solves user queries in a helpful and accurate way."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=500
        )
        answer = response.choices[0].message['content']
    except Exception as e:
        answer = f"Error: {str(e)}"
    return jsonify({"answer": answer})

if _name_ == '_main_':
    app.run(debug=True)
