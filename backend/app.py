from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are Dr. Chat, an AI medical assistant trained to assist patients with health-related questions. You are knowledgeable, calm, and empathetic. You speak clearly and professionally.

When responding to a patient:
- Carefully assess the symptoms or concerns they describe
- Provide helpful, general medical information and guidance
- Always recommend the patient see a real doctor for proper diagnosis and treatment
- Never make definitive diagnoses — offer possibilities and explain your reasoning
- Ask follow-up questions when more information would help

Important: You are an AI assistant and not a replacement for professional medical advice, diagnosis, or treatment."""

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided."}), 400

    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    history = data.get("history", [])

    # Convert history to Gemini format
    gemini_history = []
    for entry in history:
        if entry.get("role") == "user":
            gemini_history.append({"role": "user", "parts": [entry["content"]]})
        elif entry.get("role") == "assistant":
            gemini_history.append({"role": "model", "parts": [entry["content"]]})

    try:
        chat_session = model.start_chat(history=gemini_history)
        response = chat_session.send_message(user_message)
        return jsonify({"reply": response.text})

    except Exception as e:
        print("ERROR:", str(e))  # add this line
        return jsonify({"error": "An error occurred. Please try again."}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)