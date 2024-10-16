# Step 1: Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Step 2: Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove --purge -y gcc && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Step 3: Expose port 8000
EXPOSE 8000

# Step 4: Set the command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "run:app"]