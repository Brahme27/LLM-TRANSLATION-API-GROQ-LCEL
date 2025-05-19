# LLM Translation API using Groq and LCEL

This is a simple translation tool built using:

- FastAPI
- LangChain
- LangServe
- Groq (Gemma2-9b-It model)
- Python

## What It Does

You send a sentence and the language you want it translated into.  
It uses an AI model from Groq to give you the translated sentence.

## How It Works

- FastAPI runs the app as an API.
- LangChain formats the input.
- Groq's AI model does the translation.

## How to Run

1. Clone this repo
2. Install requirements  
   `pip install -r requirements.txt`
3. Create a `.env` file and add:  
   `GROQ_API_KEY=your_api_key_here`
4. Run the app  
   `uvicorn main:app --reload`

## API Endpoint

- URL: `http://127.0.0.1:8000/chain`
- Method: POST
- Sample input:
  json
  {
    "input": {
      "text": "Hello",
      "language": "French"
    }
  }
