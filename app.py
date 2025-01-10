from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Use a pipeline for text generation
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Render the home page with an input form for text generation.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, text: str = Form(...)):
    """
    Generate text based on user input and render the result.
    """
    output = pipe(text)
    generated_text = output[0]["generated_text"]
    return templates.TemplateResponse("index.html", {"request": request, "input_text": text, "generated_text": generated_text})
