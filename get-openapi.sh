#!/bin/bash

# First try original method

json=$( curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/Patagona/Patagona-API/releases/tags/${API_VERSION} | jq '.assets[] | select(.name|test("openapi.yaml"))')
url=$( echo $json | jq -r '.url')
echo "Downloading file $url"
curl -LJ --header "Authorization: token $GITHUB_TOKEN" -H 'Accept: application/octet-stream' $url > openapi.yaml


# Wait for other workflows to create the combined OpenAPI specification file in the the patagona-api-docs repo.
sleep 60

# Download the combined OpenAPI specification file.
branch_name=staging-${API_VERSION}
url=https://api.github.com/repos/Patagona/patagona-api-docs/contents/assets-joined/internal-with-scheduler-openapi.yaml?ref=${branch_name}
echo "Downloading file $url"

curl -s -H "Authorization: token $GITHUB_TOKEN" $url > openapi-internal.yaml || true
