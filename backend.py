from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google import genai

#initialize flask
app = Flask(__name__)
CORS(app)

#initialize gemini
client = genai.Client(api_key="AIzaSyBmfWgIR1BCF66sLIU3RqVODQFM3ybyqsk")


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
    ai_response= generate_ai_response(user_message)
    return jsonify({"response": ai_response })
    

def generate_ai_response(user_message):
    #generate ai response
    if isinstance(user_message, dict):
        print("user_message is a dictionary:", user_message)
        # Extract the string or handle it accordingly, e.g., take the first string value
        user_message = str(user_message.get("text", ""))
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["Generate a short response (2-3 sentences) to this message: " + user_message + ". Use the japanese language with an elementary school level proficiency. "]
    )
    print("Generated response:", response)  # Check what `response` is
    return response.text
