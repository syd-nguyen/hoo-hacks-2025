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
    user_message = data.get("message", "")
    return jsonify({"response": generate_ai_response(user_message)})
    

def generate_ai_response(user_message):
    #generate ai response
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["Generate a short response (2-3 sentences) to this message: " + user_message + ". Use the japanese language with an elementary school level proficiency. "]
    )
    return response.text
