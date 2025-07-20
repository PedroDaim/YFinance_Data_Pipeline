# Use an official Python runtime as a parent image
# Changed from buster to bullseye, and Python version for compatibility
FROM python:3.11-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container at /app
COPY app/ .

# Command to run the Python script when the container starts
CMD ["python", "pipeline.py"]