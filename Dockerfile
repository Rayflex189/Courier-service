#!/bin/bash

FROM python:3.11-slim

WORKDIR /app

# Copy only necessary files first
COPY build.sh /build.sh
COPY entrypoint.sh /entrypoint.sh
COPY . .

RUN chmod +x /build.sh
RUN /build.sh

RUN chmod +x /entrypoint.sh

EXPOSE 8080

CMD ["/entrypoint.sh"]
