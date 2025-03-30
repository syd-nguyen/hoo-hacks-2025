from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

#initialize flask
app = Flask(__name__)
CORS(app)

#initialize gemini
client = genai.Client(api_key="AIzaSyBmfWgIR1BCF66sLIU3RqVODQFM3ybyqsk")

@app.route("/chat", methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    #generate ai response
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["give me 5 elementary german sentences"]
    )

    return response.text