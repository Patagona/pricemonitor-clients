#!/bin/bash

set -eux

# https://openapi-generator.tech/docs/generators
# https://openapi-generator.tech/docs/globals


rm -rf clients
mkdir clients

mkdir -p clients/akka

API_SOURCE_FILE="openapi-internal.yaml"
API_FIXEDUP_FILE="openapi-internal-fixedup.yaml"
API_PATH="/local/$API_FIXEDUP_FILE"
IMAGE_431="openapitools/openapi-generator-cli:v4.3.1"
IMAGE_601="openapitools/openapi-generator-cli:v6.0.1"
COMMON_PARAMS="--api-package api --model-package model --git-host github.com --git-repo-id pricemonitor-clients --git-user-id Patagona"

# Read api version from file.
# Note that it would be better to read it from the openapi yaml because it would only be one single sourcce of truth, and now we need to keep openapi.ymal and API_VERSIOn in sync.
# But reading from yaml is not an easy thing to do with grep and tools for reading yaml are not installed by default in linux.
API_VERSION=$(cat API_VERSION)

DOCKER_CMD="docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE_431 generate -i $API_PATH --skip-validate-spec"

log() {
      GREEN='\033[0;32m'
      NC='\033[0m'
      echo -e "${GREEN}//////////////////////// $@ ${NC}"
}

main() {
      log fixup-api-file
      (fixup_api_file)

      log scala-sttp
      (build_scala_sttp)

      log python
      (build_python)

      log typescript-angular
      (build_typescript_angular)

      log typescript-angular-13
      (build_typescript_angular_13)


      #(build_others)

      # TODO: Generating scala clients is temporarily deactivated since they don't have priority
      # log scala-akka
      # (build_scala_akka)
}

fixup_api_file() {
      cp $API_SOURCE_FILE $API_FIXEDUP_FILE
      # Change the OAS version from 3.1.0 to 3.0.0 as the old generator version being used doesn't support 3.1
      sed -i '1s/3.1.0/3.0.0/' $API_FIXEDUP_FILE

      # Remove the first summary: block occurence as
      # it is not supported in OAS 3.0
      awk '
            /servers:/ && summaryDeleted {print; summaryDeleted=0; serversSeen=1; next}
            /servers:/ {serversSeen=1}
            !serversSeen && /summary:/ {summaryDeleted=1; next}
            summaryDeleted && (/^[[:space:]]*[a-zA-Z]+:/) {summaryDeleted=0; next}
            summaryDeleted {next}
            !summaryDeleted' $API_FIXEDUP_FILE > tmp.yaml && mv tmp.yaml $API_FIXEDUP_FILE
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
      # Fix @types/node version to work around breaking change: https://github.com/DefinitelyTyped/DefinitelyTyped/discussions/64262
      sed -i '/"devDependencies".*/a "@types/node": "^17.0.41",' ${ANGULAR_PACKAGE_JSON}
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

      DOCKER_CMD_601="docker run --rm -v $(pwd):/local -u $(id -u ${USER}):$(id -g ${USER}) $IMAGE_601 generate -i $API_PATH --skip-validate-spec"

      $DOCKER_CMD_601 \
            -g typescript-angular \
            -o /local/clients/${PACKAGE_NAME} ${COMMON_PARAMS} \
            --additional-properties=npmName=@Patagona/${PACKAGE_NAME} \
            --additional-properties=ngVersion=13.0.0 \
            --additional-properties=npmRepository=https://npm.pkg.github.com \
            --additional-properties=supportsES6=true

      # The generator inserts crappy typescript boundaries which only work for angualr 9. We need to update them.
      ANGULAR_PACKAGE_JSON=clients/${PACKAGE_NAME}/package.json
      sed -i 's/\"typescript\": \">=3.6.0 <3.8.0\"/\"typescript\": \">=4.0.0 <5.0.0\"/g' ${ANGULAR_PACKAGE_JSON}
      # Fix @types/node version to work around breaking change: https://github.com/DefinitelyTyped/DefinitelyTyped/discussions/64262
      sed -i '/"devDependencies".*/a "@types/node": "^17.0.41",' ${ANGULAR_PACKAGE_JSON}
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
      API_INVOKER_PATH="${STTP_PROJECT_PATH}/src/main/scala/com/patagona/pricemonitor/client/core/ApiInvoker.scala"

      # The generator for sttp seems to use an old method for setting up authentication. We need do replace it.
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/.auth.withCredentials/.auth.basic/g' {} \;

      # The next replacements convert the api methods to allow specifying a single authentication method instead of both.
     
      # new:
      # 69 ~ │   def apiV3ManufacturerContractsContractIdOffersPricedumpingstatsPost(contractId: String, priceDumpingStatsRequest: PriceDumpingStatsRequest)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[QueryPriceDumpingStatsApiResponse] =
      # 70 ~ │ {
      # 71 ~ │     var r = basicRequest
      # 72   │       .method(Method.POST, uri"$baseUrl/api/v3/manufacturer/contracts/${contractId}/offers/pricedumpingstats")
      # 73   │       .contentType("application/json")
      # 74 ~ │       basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      # 75 ~ │       bearerToken.foreach(b => r = r.auth.bearer(b.token))
      # 76 ~ │       r=r.body(priceDumpingStatsRequest)
      # 77 ~ │       r.response(asJson[QueryPriceDumpingStatsApiResponse])
      # 78 ~ │ }

      # old:
      # 69   │   def apiV3ManufacturerContractsContractIdOffersPricedumpingstatsPost(contractId: String, priceDumpingStatsRequest: PriceDumpingStatsRequest)(implicit basicAuth: BasicCredentials, bearerToken: BearerToken): ApiRequestT[QueryPriceDumpingStatsApiResponse] =
      # 70   │     basicRequest
      # 71   │       .method(Method.POST, uri"$baseUrl/api/v3/manufacturer/contracts/${contractId}/offers/pricedumpingstats")
      # 72   │       .contentType("application/json")
      # 73   │       .auth.basic(basicAuth.user, basicAuth.password)
      # 74   │       .auth.bearer(bearerToken.token)
      # 75   │       .body(priceDumpingStatsRequest)
      # 76   │       .response(asJson[QueryPriceDumpingStatsApiResponse]) 

      
      # Wrap the method content for the endpoints in a curly brace block.
      # This allows us to set authentication conditionally on which of the fields (basicAuth or bearerToken) is used.
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i '/basicRequest/i \\{' {} \;
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i '/response(asJson/a \\}' {} \;

      # Make the two authentication parameters optional.
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/implicit basicAuth: BasicCredentials, bearerToken: BearerToken/implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]/g' {} \;

      # Assign the request builder to 'r'.
      # The value of r will be overwritten based on the specified authentication method.
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/basicRequest/var r = basicRequest/g' {} \;

      # Conditionally adds basicAuth to the requestBuilder 'r'
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/.auth.basic(basicAuth.user, basicAuth.password)/basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))/g' {} \;
      # Conditionally adds bearerToken to the requestBuilder 'r'
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/.auth.bearer(bearerToken.token)/bearerToken.foreach(b => r = r.auth.bearer(b.token))/g' {} \;
      # Adds the body to the requestBuilder 'r'
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/.body(/r=r.body(/g' {} \;
      # Use the requestBuilder 'r' to build the request.
      find ./clients/pricemonitor-internal-scala-sttp/ -type f -exec sed -i 's/.response(/r.response(/g' {} \;

      BUILD_SBT_PATH="${STTP_PROJECT_PATH}/build.sbt"
      sed -i 's/version := "1.0.0"/version := "'${API_VERSION}'"/g' ${BUILD_SBT_PATH}
      sed -i 's/name := "openapi-client"/name := "pricemonitor-client-internal-sttp"/g' ${BUILD_SBT_PATH}
      sed -i 's/organization := "org.openapitools"/organization := "patagona"/g' ${BUILD_SBT_PATH}
      sed -i 's/"com.softwaremill.sttp.client" %% "core" % "2.0.0"/"com.softwaremill.sttp.client" %% "core" % "2.2.9"/g' ${BUILD_SBT_PATH}
      sed -i 's/"com.softwaremill.sttp.client" %% "json4s" % "2.0.0"/"com.softwaremill.sttp.client" %% "json4s" % "2.2.9"/g' ${BUILD_SBT_PATH}
      # Export project for test subproject as client
      sed -i -e '$a lazy val client = (project in file("."))' ${BUILD_SBT_PATH}
      # Retouches ApiInvoker.result code to handle the case when response is an error, since calling body on ResponseError in sttp > 2.2.0 causes NoSuchMethodError.
      # See: https://github.com/OpenAPITools/openapi-generator/issues/7181
      sed -i 's/case Left(ex).*/case Left(ex) => ex match \n \t\t\t\t\t\t\t\t\t { \n \t\t\t\t\t\t\t\t\t\t case e:HttpError => ME.error[T](new HttpException(response.code, response.statusText, e.body)) \n \t\t\t\t\t\t\t\t\t\t case e:DeserializationError[_] => ME.error[T](new HttpException(response.code, response.statusText, e.body)) \n \t\t\t\t\t\t\t\t\t  }/g' ${API_INVOKER_PATH}
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