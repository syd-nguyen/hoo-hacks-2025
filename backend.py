import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

#initialize flask
app = Flask(__name__)
CORS(app)

#initialize gemini
client = genai.Client(api_key=API_KEY)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    # Check if data is not None and contains the 'message' key
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400
    user_message = data.get("message", "")
    language = data.get("language", "english")
    ai_response= generate_ai_response(user_message,language)
    return jsonify({"response": ai_response })
    

def generate_ai_response(user_message,language):
    #generate ai response
    if isinstance(user_message, dict):
        print("user_message is a dictionary:", user_message)
        # Extract the string or handle it accordingly, e.g., take the first string value
        user_message = str(user_message.get("text", ""))
        print(f"User input: {user_message}")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["Imagine you're having a conversation with a user. The user just said: '{user_message}'. Now, respond in " + language ", acknowledging what the user said, and continue the conversation in a friendly manner."]
    )
    # print("Generated response:", response)   Check what `response` is
    return response.text

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)

