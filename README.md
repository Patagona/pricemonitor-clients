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
