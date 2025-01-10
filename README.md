# Text2Text Generator with HuggingFace-Model

This project demonstrates a **text-to-text generation application** using FastAPI, Docker, and Hugging Face. The deployed application is live and uses the `google/flan-t5-small` model for text generation.

## Features

- **FastAPI Backend**: A lightweight, efficient, and easy-to-use Python framework for serving the application.
- **Hugging Face Model**: Utilizes the `google/flan-t5-small` model for generating responses based on input text.
- **Dockerized Deployment**: The application is containerized for portability and ease of deployment.
- **Deployed on Hugging Face Spaces**: Available online for demonstration.

## Links

- **Docker Hub Repository**: [arpitkadam/text2text-generator](https://hub.docker.com/r/arpitkadam/text2text-generator)
- **Deployed Application**: [Text2Text Generator on Hugging Face Spaces](https://arpitkadam-text2text-generator-with-docker-and-h-582ac6f.hf.space/)

---

## Getting Started

### Clone the Repository
To clone the repository, use the following command:

```bash
git clone https://github.com/ArpitKadam/text2text-generator-with-HuggingFace-Model.git
cd text2text-generator-with-HuggingFace-Model
```

### Build and Run with Docker

#### Build the Docker Image
```bash
docker build -t arpitkadam/text2text-generator .
```

#### Run the Docker Container
```bash
docker run -p 7860:7860 arpitkadam/text2text-generator
```

### Pull the Prebuilt Docker Image
To pull the prebuilt image from Docker Hub:

```bash
docker pull arpitkadam/text2text-generator
```

Run the container:

```bash
docker run -p 7860:7860 arpitkadam/text2text-generator
```

---

## Application Details

### Hugging Face Model
The application uses the Hugging Face model **`google/flan-t5-small`**. This model is a lightweight variant of the T5 (Text-to-Text Transfer Transformer) family, designed for various text generation tasks.

#### Steps to Use the Model

1. **Install Transformers**:
   Ensure the `transformers` library is installed:
   ```bash
   pip install transformers
   ```

2. **Load the Model**:
   Use the following Python code to load the model and perform text generation:
   ```python
   from transformers import pipeline

   # Load the model
   pipe = pipeline("text2text-generation", model="google/flan-t5-small")

   # Generate text
   input_text = "Explain the importance of Docker in DevOps."
   output = pipe(input_text)

   print(output[0]['generated_text'])
   ```

---

## Project Structure

```
text2text-generator/
├── app.py                # FastAPI application
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
└── .gitignore            # Files to ignore in version control
```

---

## Requirements

Ensure the following are installed:

- Python 3.9+
- Docker

Install project dependencies locally using:

```bash
pip install -r requirements.txt
```

---

## Contributions
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

