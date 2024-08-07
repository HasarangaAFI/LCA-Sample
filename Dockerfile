# # Use the official Python image from the Docker Hub
# FROM python:3.10-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install the dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire project into the container
# COPY . .

# # Accept build arguments and set them as environment variables
# ARG MONGODB_URI
# ARG SECRET_KEY
# ARG ALGORITHM
# ARG ACCESS_TOKEN_EXPIRE_MINUTES

# ENV MONGODB_URI=$MONGODB_URI
# ENV SECRET_KEY=$SECRET_KEY
# ENV ALGORITHM=$ALGORITHM
# ENV ACCESS_TOKEN_EXPIRE_MINUTES=$ACCESS_TOKEN_EXPIRE_MINUTES

# # Expose the port the app runs on
# EXPOSE 8000

# # Run the application
# CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "main:app"]

# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy application files
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app.main:app"]
