from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import rag  # Import your rag.py script
import re
import requests
import base64
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

url = "https://api.sarvam.ai/text-to-speech"
headers = {
    "Content-Type": "application/json",
    "API-Subscription-Key": "Sarvam-API"  # Add your Sarvam API key
}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, question: str = Form(...)):
    # Check if the input is a valid question
    if not is_question(question):
        return templates.TemplateResponse("result.html", {
            "request": request,
            "question": question,
            "answer": "The given query is not a question."
        })
    
    else:
        answer, source_documents = rag.ask_question(question)
    print(f"the answer is  :{answer}")

    payload = {
        "target_language_code": "en-IN",
        "pitch": 0,
        "speaker": "meera",
        "inputs": [f"\"{answer}\""],
        "pace": 1.65,
        "loudness": 1.5,
        "speech_sample_rate": 8000,
        "enable_preprocessing": True,
        "model": "bulbul:v1"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    print(response.status_code)
    if response.status_code == 200:
        res = response.json()
        audio = res.get("audios")
        if audio:
            audio_bytes = base64.b64decode(audio[0])
            save_dir = os.path.join('static', 'response.wav')
            with open(save_dir, "wb") as f:
                f.write(audio_bytes)
            
            audio_url = "/static/response.wav"  # URL to access the saved audio file

            return templates.TemplateResponse("result.html", {
                "request": request,
                "question": question,
                "answer": answer,
                "audio_url": audio_url  # Pass the audio URL to the template
            })
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "question": question,
        "answer": answer,
        "audio_url": None
    })

def is_question(text: str) -> bool:
    return text.strip().endswith('?') or re.search(r'\b(what|who|where|when|why|how)\b', text, re.IGNORECASE) is not None

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
