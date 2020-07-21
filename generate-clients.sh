#!/bin/bash

rm -rf clients
mkdir clients

API_PATH="/local/openapi.yaml"
IMAGE="openapitools/openapi-generator-cli:v4.3.1"
COMMON_PARAMS="--api-package api --model-package model"

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

docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate \
      -i $API_PATH \
      -g typescript-angular \
      -o /local/clients/typescript-angular ${COMMON_PARAMS} \
      --additional-properties=npmName=pricemonitor-client \
      --additional-properties=ngVersion=10.0.0

# The generator inserts crappy typescript boundaries which only work for angualr 9. We need to update them.
sed -i 's/\"typescript\": \">=3.6.0 <3.8.0\"/\"typescript\": \">=3.9.2 <4.0.0\"/g' clients/typescript-angular/package.json
