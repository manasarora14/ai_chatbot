from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# ✅ Set API key BEFORE running anything
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual key

@app.route('/')
def home():
    return "Legal Assistant API is running!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Call GPT model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful legal assistant. Only answer based on Indian Law."},
            {"role": "user", "content": question}
        ]
    )

    answer = response['choices'][0]['message']['content']
    return jsonify({"answer": answer})

# ✅ Start server last
if __name__ == '__main__':
    app.run(debug=True)
