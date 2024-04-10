# Use Python 3.9.10 slim version as a starting point
FROM python:3.9.10-slim-buster

# Set our working directory inside the container to /app
WORKDIR /app

# Copy the list of required Python packages from our project to the container
COPY requirements.txt ./

# Install all the Python packages listed in requirements.txt
# Additionally, install the python-dotenv package to manage environment variables
RUN pip install -r requirements.txt && pip install python-dotenv

# Copy all of our project's files into the /app directory in the container
COPY . .

# Expose port 3000 to allow external connections
EXPOSE 3000

# Define the default command to run when the container starts
# Start our Flask application and make it accessible from all network interfaces on port 3000
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
