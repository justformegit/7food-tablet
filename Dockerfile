# Use a Debian-based image for ARM64
FROM arm64v8/debian:bullseye-slim

WORKDIR /bluedot

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-pip \
    libdbus-1-dev \
    libdbus-glib-1-dev \
    libgpiod-dev \
    swig \
    git \
    python3-gpiozero \
    python3-rpi.gpio \
    python3-pigpio \
    && ln -s /usr/bin/python3 /usr/bin/python

# Copy the requirements file into the container
COPY requirements.txt .

# Create and activate a virtual environment, then install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install RPIO

# Copy the current directory contents into the container
COPY . .

# Set environment variables for pigpio
ENV PIGPIO_ADDR=host.docker.internal
ENV PIGPIO_PORT=8888

# Run the application
CMD ["python", "-m", "my_module.main"]
