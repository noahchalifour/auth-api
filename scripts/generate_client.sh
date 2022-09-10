#!/bin/sh

# Client type can by 'python'
CLIENT_TYPE="$1"

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

ROOT_DIR="$SCRIPTPATH/.."

python $ROOT_DIR/src/manage.py generateschema --file $ROOT_DIR/openapi-schema.yml

rm -r $ROOT_DIR/clients/$CLIENT_TYPE/client
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/openapi-schema.yml \
    -g $CLIENT_TYPE \
    -c /local/clients/$CLIENT_TYPE/config.yaml \
    -o /local/clients/$CLIENT_TYPE/client