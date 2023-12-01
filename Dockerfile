# Use an official Python runtime as a parent image with better multithreading support
FROM tiangolo/uwsgi-nginx-flask:python3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to allow external access
EXPOSE 80

# Command to run the application
CMD ["python", "app.py"]
