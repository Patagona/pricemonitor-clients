#!/bin/bash

rm -rf clients
mkdir clients

API_PATH="/local/openapi-internal.yaml"
IMAGE="openapitools/openapi-generator-cli:v4.3.1"
COMMON_PARAMS="--api-package api --model-package model --git-host github.com --git-repo-id pricemonitor-clients --git-user-id Patagona"

# Generating scala clients is temporarily deactivated since they don't have priority
'docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
      -i $API_PATH ${COMMON_PARAMS} \
      -g scala-akka \
      -o /local/clients/akka

docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
      -i $API_PATH \
      -g scala-sttp \
      -o /local/clients/scala-sttp

docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
      -i $API_PATH \
      -g scala-gatling \
      -o /local/clients/scala-gatling

docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
      -i $API_PATH \
      -g scalaz \
      -o /local/clients/scalaz

docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
      -i $API_PATH \
      -g java \
      -o /local/clients/java '

PACKAGE_NAME=pricemonitor-internal-typescript-angular

docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
      -i $API_PATH \
      -g typescript-angular \
      -o /local/clients/${PACKAGE_NAME} ${COMMON_PARAMS} \
      --additional-properties=npmName=@Patagona/${PACKAGE_NAME} \
      --additional-properties=ngVersion=10.0.0 \
      --additional-properties=npmRepository=https://npm.pkg.github.com

# The generator inserts crappy typescript boundaries which only work for angualr 9. We need to update them.
ANGULAR_PACKAGE_JSON=clients/${PACKAGE_NAME}/package.json
sed -i 's/\"typescript\": \">=3.6.0 <3.8.0\"/\"typescript\": \">=3.9.2 <4.0.0\"/g' ${ANGULAR_PACKAGE_JSON}
# We want to publish the client as "typescript-angular". Therefore we have to add this repository entry.
# See https://docs.npmjs.com/files/package.json#repository
jq -M '. +{"repository": {"type" : "git","url" : "ssh://git@github.com/Patagona/pricemonitor-clients.git","directory": "clients/${PACKAGE_NAME}"}}' ${ANGULAR_PACKAGE_JSON} > ${ANGULAR_PACKAGE_JSON}.tmp
mv ${ANGULAR_PACKAGE_JSON}.tmp ${ANGULAR_PACKAGE_JSON}
