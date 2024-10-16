# Step 1: Use an official Ubuntu runtime as a base image
FROM ubuntu:20.04

WORKDIR /app

COPY . /app


RUN apt-get update && \
    apt-get install -y python3.10 python3-pip git cmake && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Step 5: Install virtual environment and dependencies
RUN pip install -r requirements.txt

# Step 6: Expose port 8000
EXPOSE 8000

CMD ["/gunicorn", "--bind", "0.0.0.0:8000", "run:app"]