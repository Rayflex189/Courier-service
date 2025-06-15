#!/bin/bash

FROM python:3.11-slim

WORKDIR /app

# Copy project files into /app
COPY . .

# Make sure scripts are executable and run the build
RUN chmod +x build.sh && bash -x build.sh

RUN chmod +x entrypoint.sh

EXPOSE 8080

CMD ["./entrypoint.sh"]

