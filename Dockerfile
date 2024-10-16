# Step 1: Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Step 2: Install dependencies
RUN apt-get update && \ 
    pip install -r requirements.txt

# Step 3: Expose port 8000
EXPOSE 8000

# Step 4: Use the full path to gunicorn if necessary
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]