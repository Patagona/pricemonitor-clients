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
      -o /local/clients/akka'

docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
      -i $API_PATH \
      -g scala-sttp \
      -o /local/clients/pricemonitor-internal-scala-sttp \
      --additional-properties=jsonLibrary=circe \
      --additional-properties=mainPackage=com.patagona.pricemonitor.client

# The generator for shhtp seems to use an old method for setting up authentication. We need do replace it.
find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/.auth.withCredentials/.auth.basic/g' {} \;


'docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
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

# Shorten the prefix of generated model type names
# We want to replace 'ComPatagonaPricemonitorShareApi' by 'Pricemonitor'
find ./clients/${PACKAGE_NAME}/ -type f -exec sed -i 's/ComPatagonaPricemonitorShareApi/Pricemonitor/g' {} \;
find ./clients/${PACKAGE_NAME}/ -type f -exec sed -i 's/comPatagonaPricemonitorShareApi/pricemonitor/g' {} \;
for f in ./clients/${PACKAGE_NAME}/model/comPatagonaPricemonitorShareApi*; do mv "$f" "${f/comPatagonaPricemonitorShareApi/pricemonitor}";done
