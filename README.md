# SARVANA-AI-ABHYUDAY-ASSIGNMENT

## Project Overview
This project is an AI-powered question-answering system that uses RAG (Retrieval-Augmented Generation) to provide accurate answers. It also includes a text-to-speech feature to deliver audio responses.
```
1.) using llm for response"\n"
2.) tasken care of non question queries"\n"
3.) Used audio API for bonus points
4.) Did optimizations like usign faiss instead of Chroma db for precenting dying kernel, avoided llm call for lower latency for 2nd part using regex
5.)Have used Google Gemini API, but have MISTRAL folder and ran it on kaggle for showcASING THAT i CAN WORK WITH LOCAL LLMS AS WELL.
```
## Demo
[Click here to watch the demo video](./Working%20prototype.mkv)

*Note: The video is in .mkv format. If you're unable to play it directly, you may need to download and open it with a compatible video player like VLC.*

## Features
- Question answering using RAG technology
- Text-to-speech conversion for audio responses
- Web interface for easy interaction
- Input validation to ensure queries are in question format

## Project Structure
```
SARVANA-AI-ABHYUDAY-ASSIGNMENT/
│
├── _pycache_/
├── audio_files/
├── MISTRAL/
├── pdfs/
├── static/
├── templates/
├── dummy.py
├── main.py
├── rag.py
├── requirements.txt
├── response.wav
├── test.ipynb
├── test.py
├── README.md
└── Working prototype.mkv
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/SARVANA-AI-ABHYUDAY-ASSIGNMENT.git
   cd SARVANA-AI-ABHYUDAY-ASSIGNMENT
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your API key:
   ```
   API_SUBSCRIPTION_KEY=your_sarvam_api_key_here
   ```

## Usage

1. Run the main application:
   ```
   python main.py
   ```
   ```
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

2. Open your web browser and navigate to `http://127.0.0.1:8000`

3. Enter your question in the provided form and submit.

4. View the text answer and listen to the audio response.

## Technical Details

### RAG (Retrieval-Augmented Generation)
This project uses RAG to enhance the accuracy of answers. The `rag.py` file contains the implementation details.

### FastAPI Web Application
The `main.py` file sets up a FastAPI application to handle web requests and serve the user interface.

### Text-to-Speech
We use the Sarvam AI API for text-to-speech conversion. The audio response is generated and saved as a .wav file.


## Contact

Abhyuday Singh - singhabhyuday2003@gmail.com - +91 9340319558

Project Link: [https://github.com/Abhyuday0409/SARVANA-AI-ABHYUDAY-ASSIGNMENT](https://github.com/Abhyuday0409/SARVANA-AI-ABHYUDAY-ASSIGNMENT)