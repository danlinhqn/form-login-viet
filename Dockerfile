# Use a lightweight base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install only necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
