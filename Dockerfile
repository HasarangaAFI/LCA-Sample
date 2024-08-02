# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

ENV MONGODB_URI=mongodb+srv://rumesh:cluster0@cluster0.sdus7hk.mongodb.net/?retryWrites=true&w=majority
ENV SECRET_KEY=f9c91f73545e5ae78b9d105b431d464568921adbc517148313980bccf344d950
ENV ALGORITHM=HS256
ENV ACCESS_TOKEN_EXPIRE_MINUTES=30

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
