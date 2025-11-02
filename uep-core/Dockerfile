FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY src/uep_core ./src/uep_core
COPY pyproject.toml .
COPY setup.cfg .
COPY MANIFEST.in .
COPY README.md .

# Expose the necessary port for the gRPC server
EXPOSE 50051

# Command to run the application
CMD ["python", "-m", "src.uep_core.server"]