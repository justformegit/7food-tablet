#!/usr/bin/env bash
SFOOD_FRIDGE_TAG="1.1.0"

# Check if the environment variable is set
if [ -z "$SFOOD_FRIDGE_TAG" ]; then
  echo "Error: SFOOD_FRIDGE_TAG is not set or is empty."
  exit 1
fi

# Continue with the rest of your script if the environment variable is set
echo "tag: $SFOOD_FRIDGE_TAG"

# Check for V4L2 devices
CONTAINER="my-python-app"
RESTART_ARG="no"
if [ $# -ne 0 ] && [ "$1" = "-a" ]; then
  echo "docker-run: restart=always"
  RESTART_ARG="always"
fi

V4L2_DEVICES=""
V4L2_DEVICES_TTY=""

for i in {0..9}; do
  if [ -a "/dev/video$i" ]; then
    V4L2_DEVICES="$V4L2_DEVICES --device /dev/video$i "
  fi
  if [ -a "/dev/ttyTHS$i" ]; then
    V4L2_DEVICES_TTY="$V4L2_DEVICES_TTY --device /dev/ttyTHS$i "
  fi
done

echo "docker-run: V4L2_DEVICES:  $V4L2_DEVICES"
echo "docker-run: V4L2_DEVICES_TTY:  $V4L2_DEVICES_TTY"

# Share display (Uncomment if needed)
# xhost +local:docker

# Run Docker container
sudo docker run --privileged -it \
    --name=7food-test21 \
    --restart=$RESTART_ARG \
    $CONTAINER

# Check if the container is running
if [ $? -ne 0 ]; then
  echo "Error: Docker container failed to start."
  exit 1
fi
