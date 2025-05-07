import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env (optional for local dev)

app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "Legal Assistant API is running!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful legal assistant. Only answer based on Indian Law."},
            {"role": "user", "content": question}
        ]
    )

    answer = response['choices'][0]['message']['content']
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)

