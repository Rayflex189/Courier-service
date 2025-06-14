# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your project files into the image
COPY . .

# Install dependencies (build.sh handles this)
RUN chmod +x /build.sh
RUN /build.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Expose Django port
EXPOSE 8080

# Use entrypoint.sh to run commands
CMD ["/entrypoint.sh"]
