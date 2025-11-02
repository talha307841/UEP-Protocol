FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the necessary ports (adjust as needed)
EXPOSE 50051 8080

# Command to run the application (adjust as needed)
CMD ["python", "-m", "uep_core.server"]