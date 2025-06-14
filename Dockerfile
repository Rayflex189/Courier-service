# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your project files into the image
COPY shipping_site/ /app/

# Install dependencies (build.sh handles this)
RUN chmod +x /shipping_site/build.sh
RUN /shipping_site/build.sh

# Make the entrypoint script executable
RUN chmod +x /shipping_site/entrypoint.sh

# Expose Django port
EXPOSE 8080

# Use entrypoint.sh to run commands
CMD ["/shipping_site/entrypoint.sh"]
