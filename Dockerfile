# Name: Anay Abhijit Joshi
# Date: October 9, 2024

# Using the official Python image from the Docker Hub (latest)
FROM python:alpine

# Setting the working directory to /home/data
WORKDIR /home/data

# Now, let's copy the Python script and the text files to the working directory
COPY scripts.py IF.txt AlwaysRememberUsThisWay.txt /home/data/

# Finally, let's run the Python script using the CMD command
CMD ["python", "/home/data/scripts.py"]
