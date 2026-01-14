# Use official Python runtime as base image
FROM python:3.13-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy application files
COPY server.py .
COPY .env .

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "server.py"]
