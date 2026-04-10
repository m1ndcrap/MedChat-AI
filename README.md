# MedChat AI — Medical Chatbot

## Description

MedChat AI is a web-based medical chatbot that simulates a consultation with Dr. Chat, an AI physician. The chatbot is built on a prompt given to gemini to mimic a physician, adapted into a full-stack web application. Users can describe symptoms, ask medical questions, and receive thoughtful responses.

The chatbot:

- Maintains multi-turn conversation history for contextual responses
- Reminds users to seek professional medical care when appropriate
- Provides quick-question shortcuts for common medical topics

## Technologies Used

| Layer    | Technology                               |
| :------- | :--------------------------------------- |
| Frontend | HTML, CSS, JavaScript (vanilla)          |
| Backend  | Python (Flask + flask-cors)              |
| AI Model | Anthropic Claude API                     |
| Fonts    | Google Fonts (DM Serif Display, DM Sans) |

## Project Structure

```
medical-chatbot/
├── frontend/
│   └── index.html          # Single-page chat UI
├── backend/
│   ├── app.py              # Flask API server
│   └── requirements.txt    # Python dependencies
└── README.md
```

## Setup & Run Instructions

### Prerequisites

- Python 3.8+
- An Gemini API key ([get one here](https://aistudio.google.com/app/apikey))

### 1. Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Set your API key

Make a copy of `.env.example` and rename it to `.env`. Open the .env and paste your API key so it looks like the example below:

```bash
GEMINI_API_KEY=your_api_key_here
```

### 3. Start the backend server

```bash
python app.py
```

The server runs on `http://localhost:5000`.

### 4. Open the frontend

Open `frontend/index.html` directly in your browser (no build step required).

> **Note:** Make sure the backend is running before opening the frontend.

## API Used

**Google Gemini API**
Model: `gemini-2.5-flash`

The system prompt instructs the model to act as Dr. Chat, a professional AI physician who provides calm, evidence-based medical guidance while always recommending in-person care.

## API Endpoints

| Method | Endpoint  | Description                        |
| ------ | --------- | ---------------------------------- |
| POST   | `/chat`   | Send a message and receive a reply |
| GET    | `/health` | Health check                       |

### Request body (`/chat`)

```json
{
  "message": "I have a headache and fever.",
  "history": [
    { "role": "user", "content": "..." },
    { "role": "assistant", "content": "..." }
  ]
}
```

### Response

```json
{
  "reply": "Dr. Chat's response here..."
}
```

## Error Handling

- Empty or missing messages return a `400` error
- API failures return a `500` error with a user-friendly message
- Rate limiting returns a `429` error
- All errors are displayed gracefully in the chat UI without crashing

## Example Output

**User:** I've been having chest pain for the past hour and feel short of breath.

**Dr. Chat:** I'm very sorry to hear you're experiencing chest pain and shortness of breath. These symptoms can be quite serious and require immediate medical attention.

**Please call emergency services (like 911 in the US) or have someone take you to the nearest emergency room right away.**

Chest pain, especially when accompanied by shortness of breath and lasting for an hour, can be a sign of a critical condition such as a heart attack, a serious lung problem, or other urgent issues. A medical professional needs to evaluate your symptoms in person, perform diagnostic tests, and determine the cause to ensure you receive appropriate treatment as quickly as possible.

As an AI, I cannot diagnose or treat you, and it's crucial that you seek professional medical help without delay. Please prioritize getting to an emergency room immediately.
