# Use a minimal Python 3.13 base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Expose the port your app runs on
EXPOSE 8008

# Install the UV package manager
RUN pip install --no-cache-dir uv

# Install test dependencies
RUN pip install pytest

# Copy dependency management files to the container
COPY pyproject.toml uv.lock ./

# Install dependencies using UV
RUN uv sync

# Copy the rest of the application code
COPY . .

# Define the command to run the bot
CMD ["python", "./app/bot.py"]