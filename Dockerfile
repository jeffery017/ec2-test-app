# Step 1: Use an official Ubuntu runtime as a base image
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y python3.10 python3-pip git cmake && \
    apt-get clean

# Step 5: Install virtual environment and dependencies
RUN pip install -r requirements.txt

# Step 6: Expose port 8010
EXPOSE 8010

CMD ["/gunicorn", "--bind", "0.0.0.0:8000", "run:app"]