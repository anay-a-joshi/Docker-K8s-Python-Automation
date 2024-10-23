# Name: Anay Abhijit Joshi

# Using the official Python image from the Docker Hub
FROM python:3.9-alpine

# Setting the working directory to /home/data
WORKDIR /home/data

# Now, let's copy the Python script and the text files to the working directory
COPY scripts.py IF.txt AlwaysRememberUsThisWay.txt /home/data/

# Install any necessary Python packages (if any, in future)
# RUN pip install --no-cache-dir <dependencies>

# Finally, let's run the Python script using the CMD command
CMD ["python", "/home/data/scripts.py"]
