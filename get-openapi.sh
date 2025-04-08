#!/bin/bash

# Wait for other workflows to create the combined OpenAPI specification file in the the patagona-api-docs repo.
sleep 60

# Download the combined OpenAPI specification file.
branch_name=release-general-${API_VERSION}
url=https://api.github.com/repos/Patagona/patagona-api-docs/contents/internal-api/omnia-internal.yaml?ref=${branch_name}
echo "Downloading file $url"

curl -v -H "Authorization: token $GITHUB_TOKEN" -H "Accept: application/vnd.github.v3.raw" $url -o openapi-internal.yaml
