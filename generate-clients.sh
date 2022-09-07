#!/bin/bash

set -eux

# https://openapi-generator.tech/docs/generators
# https://openapi-generator.tech/docs/globals


rm -rf clients
mkdir clients

mkdir -p clients/akka

API_PATH="/local/openapi-internal.yaml"
IMAGE="openapitools/openapi-generator-cli:v4.3.1"
COMMON_PARAMS="--api-package api --model-package model --git-host github.com --git-repo-id pricemonitor-clients --git-user-id Patagona"

# Read api version from file.
# Note that it would be better to read it from the openapi yaml because it would only be one single sourcce of truth, and now we need to keep openapi.ymal and API_VERSIOn in sync.
# But reading from yaml is not an easy thing to do with grep and tools for reading yaml are not installed by default in linux.
API_VERSION=$(cat API_VERSION)

DOCKER_CMD="docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE generate -i $API_PATH"

log() {
      GREEN='\033[0;32m'
      NC='\033[0m'
      echo -e "${GREEN}//////////////////////// $@ ${NC}"
}


main() {
      log python
      (build_python)

      log scala-sttp
      (build_scala_sttp)

      log typescript-angular
      (build_typescript_angular)

      log typescript-angular-13
      (build_typescript_angular_13)


      #(build_others)

      # TODO: Generating scala clients is temporarily deactivated since they don't have priority
      # log scala-akka
      # (build_scala_akka)
}

build_python() {
      # https://openapi-generator.tech/docs/generators/python
      $DOCKER_CMD \
            -g python \
            -o /local/clients/python \
            --additional-properties=packageName=pricemonitor_api_client
}


build_typescript_angular() {
      PACKAGE_NAME=pricemonitor-internal-typescript-angular

      $DOCKER_CMD \
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

      for f in ./clients/${PACKAGE_NAME}/model/comPatagonaPricemonitorShareApi*; do
            mv "$f" "${f/comPatagonaPricemonitorShareApi/pricemonitor}"
      done
}

build_typescript_angular_13() {
      PACKAGE_NAME=pricemonitor-internal-typescript-angular-13

      $DOCKER_CMD \
            -g typescript-angular \
            -o /local/clients/${PACKAGE_NAME} ${COMMON_PARAMS} \
            --additional-properties=npmName=@Patagona/${PACKAGE_NAME} \
            --additional-properties=ngVersion=13.0.0 \
            --additional-properties=npmRepository=https://npm.pkg.github.com

      # The generator inserts crappy typescript boundaries which only work for angualr 9. We need to update them.
      ANGULAR_PACKAGE_JSON=clients/${PACKAGE_NAME}/package.json
      sed -i 's/\"typescript\": \">=3.6.0 <3.8.0\"/\"typescript\": \">=4.0.0 <5.0.0\"/g' ${ANGULAR_PACKAGE_JSON}
      # We want to publish the client as "typescript-angular". Therefore we have to add this repository entry.
      # See https://docs.npmjs.com/files/package.json#repository
      jq -M '. +{"repository": {"type" : "git","url" : "ssh://git@github.com/Patagona/pricemonitor-clients.git","directory": "clients/${PACKAGE_NAME}"}}' ${ANGULAR_PACKAGE_JSON} > ${ANGULAR_PACKAGE_JSON}.tmp
      mv ${ANGULAR_PACKAGE_JSON}.tmp ${ANGULAR_PACKAGE_JSON}

      # Shorten the prefix of generated model type names
      # We want to replace 'ComPatagonaPricemonitorShareApi' by 'Pricemonitor'
      find ./clients/${PACKAGE_NAME}/ -type f -exec sed -i 's/ComPatagonaPricemonitorShareApi/Pricemonitor/g' {} \;
      find ./clients/${PACKAGE_NAME}/ -type f -exec sed -i 's/comPatagonaPricemonitorShareApi/pricemonitor/g' {} \;

      for f in ./clients/${PACKAGE_NAME}/model/comPatagonaPricemonitorShareApi*; do
            mv "$f" "${f/comPatagonaPricemonitorShareApi/pricemonitor}"
      done
}


build_scala_akka() {
      $DOCKER_CMD \
            ${COMMON_PARAMS} \
            -g scala-akka \
            -o /local/clients/akka
}

build_scala_sttp() {
      $DOCKER_CMD \
            -g scala-sttp \
            -o /local/clients/pricemonitor-internal-scala-sttp \
            --additional-properties=jsonLibrary=circe \
            --additional-properties=mainPackage=com.patagona.pricemonitor.client

      STTP_PROJECT_PATH="clients/pricemonitor-internal-scala-sttp"

      # The generator for shhtp seems to use an old method for setting up authentication. We need do replace it.
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/.auth.withCredentials/.auth.basic/g' {} \;
      BUILD_SBT_PATH="${STTP_PROJECT_PATH}/build.sbt"
      sed -i 's/version := "1.0.0"/version := "'${API_VERSION}'"/g' ${BUILD_SBT_PATH}
      sed -i 's/name := "openapi-client"/name := "pricemonitor-client-internal-sttp"/g' ${BUILD_SBT_PATH}
      sed -i 's/organization := "org.openapitools"/organization := "patagona"/g' ${BUILD_SBT_PATH}

      mkdir ${STTP_PROJECT_PATH}/project
      cp templates/sttp/plugins.sbt ${STTP_PROJECT_PATH}/project
      cat templates/sttp/publishTo-part >> ${BUILD_SBT_PATH}
}


build_others() {
      for client in scala-gatling scalaz java; do
            log $client
            $DOCKER_CMD \
                  -g $client \
                  -o /local/clients/$client
      done
}


main