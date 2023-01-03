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

## Adjustments to the generated code (scala sttp)
Please note that we are adjusting the generated code with a few sed commands. For specifics on the adjustments please take a look at the [generate-clients.sh](generate-clients.sh) script.
In summary, we fix basicAuth method for our sttp version and we adjust the function signature to allow choosing which of the possible authentication methods to use.
The adjustments break if we update the code generator (uses different sttp version) or if we add another authentication method.
The breakage should prevent compilation as far as we can tell. Runtime issues after an update seem unlikely.
