FROM python:3.8-slim-bullseye

# Install awscli and cleanup to reduce image size
RUN apt update -y && apt install -y awscli && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy rest of the app
COPY . .

# Default command
CMD ["python3", "app.py"]