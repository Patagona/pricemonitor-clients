# pricemonitor-clients
Clients for accessing the Pricemonitor API

# Workflow for new client version
1. Patagona-API publishes a new openapi-internal.yaml
1. Patagona-API triggers jenkins job "generate-pricemonitor-clients"
1. Jenkins job "generate-pricemonitor-clients"
   1. fetches openapi-internal.yaml
   1. writes api version into API_VERSION file
   1. generates clients using generate-lients.sh
   1. commits and pushes the new generated clients
1. Github actions get notified by push and generate build new clients

# Scala sttp

To use the scala sttp client you need to add the following dependencies to your build.sbt:

```scala
// The following 4 dependencies are used to interact with the pricemonitor api via the generated client.
// https://github.com/Patagona/pricemonitor-clients/tree/master/clients/pricemonitor-internal-scala-sttp
"com.softwaremill.sttp.client"     %% "core"                              % "2.2.9",
"com.softwaremill.sttp.client"     %% "async-http-client-backend-future"  % "2.2.9",
"com.softwaremill.sttp.client"     %% "json4s"                            % "2.2.9",
"patagona"                         %% "pricemonitor-client-internal-sttp" % "See version under releases on the right",
 ```

When calling an api endpoint with the sttp client, you need the following parameters:

```scala
import com.patagona.pricemonitor.client.core.ApiInvoker._
import sttp.client.SttpBackend
import sttp.client.asynchttpclient.WebSocketHandler
import scala.concurrent.Future
import com.patagona.pricemonitor.client.core.BasicCredentials
import com.patagona.pricemonitor.client.core.BearerToken


private implicit val serializer: SttpSerializer = new SttpSerializer()

// You need to define both authenticaion methods, however only one of them must be 'Some', the other must be 'None':
private implicit val auth: Option[BasicCredentials] = Some(BasicCredentials("user", "password"))
private implicit val noToken: Option[BearerToken] = Some(BearerToken("token"))

private implicit val httpClient: SttpBackend[Future, Nothing, WebSocketHandler]
```

Example for api call:
```scala
val result: Future[QueryProductsVendorV3ApiResponse] = com.patagona.pricemonitor.client.api.ProductsApi().queryProductsVendorV3("contractId", None).result
```

## Adjustments to the generated code (scala sttp)
Please note that we are adjusting the generated code with a few sed commands. For specifics on the adjustments please take a look at the [generate-clients.sh](generate-clients.sh) script.
In summary, we fix basicAuth method for our sttp version and we adjust the function signature to allow choosing which of the possible authentication methods to use.
The adjustments break if we update the code generator (uses different sttp version) or if we add another authentication method.
The breakage should prevent compilation as far as we can tell. Runtime issues after an update seem unlikely.
