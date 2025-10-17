#!/bin/bash
# redeploy_model.sh
# Stop old container, rebuild Docker image, and start new API

set -e  # Exit immediately if a command fails

IMAGE="phdata-housing-api"
CONTAINER="phdata-housing-api"



# 1️⃣ Detect latest model version automatically
LATEST_VERSION=$(ls model/v* 2>/dev/null | sed 's/[^0-9]*//g' | sort -n | tail -n 1)

if [ -z "$LATEST_VERSION" ]; then
  echo "❌ No models found in models/ directory."
  exit 1
fi

echo "🚀 Latest model detected: v${LATEST_VERSION}"

# 2️⃣ Build image tagged with version
IMAGE_NAME="${IMAGE}:v${LATEST_VERSION}"
CONTAINER_NAME="${CONTAINER}-v${LATEST_VERSION}"

echo "Starting model redeployment process..."


# 2️⃣ Build new image (assumes Dockerfile in current directory)
echo "🔨 Building new Docker image: $IMAGE_NAME"
docker build -t "$IMAGE_NAME" .

# 3️⃣ Run new container
echo "🚢 Starting new container..."
docker run -d -p 8001:8000 --name "$CONTAINER_NAME" "$IMAGE_NAME"
docker start "$CONTAINER_NAME"

# 4️⃣ Verify it's running
echo "🔍 Checking running containers..."
docker ps | grep "$CONTAINER_NAME"
docker start "$CONTAINER_NAME"

echo "Redeployment complete. API should be live at http://127.0.0.1:8000"
