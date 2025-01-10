# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /code

# Copy the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /code/requirements.txt

# Check network connectivity before installing
RUN apt-get update && apt-get install -y curl
RUN curl -I https://pypi.org

# Install Python dependencies with verbose output
RUN pip install -v --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the project files
COPY . /code

# Expose port 7860 for the FastAPI app
EXPOSE 7860

# Command to start the FastAPI app using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
