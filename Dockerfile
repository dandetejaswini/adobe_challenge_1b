# Use lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Python libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make run.sh executable
RUN chmod +x run.sh

# Run script when container starts
CMD ["./run.sh"]
