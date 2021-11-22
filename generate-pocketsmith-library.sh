#!/usr/bin/env bash
set -o errexit
set -o xtrace

SCRIPT_DIR=$(cd "$(dirname "$0")"; pwd)
cd "$SCRIPT_DIR"

VERSION="$(poetry version --short)"

openapi-generator-cli generate \
  --input-spec ./pocketsmith-api-spec/dist/openapi.yaml \
  --generator-name python \
  --output ./build/pocketsmith \
  --package-name pocketsmith \
  --http-user-agent="python-pocketsmith/$VERSION" \
  --verbose \
  --additional-properties=packageVersion="$VERSION"

rsync --archive --progress ./build/pocketsmith/pocketsmith/ ./pocketsmith
rm -rf ./build/pocketsmith

cp ./_overrides/pocketsmith_client.py ./pocketsmith/pocketsmith_client.py
cat ./_overrides/_init_header_append.py >> ./pocketsmith/__init__.py
