# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy files into container
COPY . .

# Run the app
CMD ["python", "app.py"]
