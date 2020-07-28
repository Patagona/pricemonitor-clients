#!/bin/bash
release=$( curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/Patagona/Patagona-API/releases/tags/${API_VERSION} )
json=$( echo $release | jq '.assets[] | select(.name|test("openapi-internal.yaml"))')
url=$( echo $json | jq -r '.url')
echo "Downloading file $url"
curl -LJ --header "Authorization: token $GITHUB_TOKEN" -H 'Accept: application/octet-stream' $url > openapi-internal.yaml
