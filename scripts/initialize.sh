#!/bin/bash

SERVER=http://localhost:8000

while :
do
    response=$(curl -X POST --silent $SERVER/init/)

    if [[ "$response" == *"Application already initialized"* ]]
    then
        echo "Application already initialized."
        exit 0
    elif [[ "$response" == *"\"key\":"* ]]
    then
        echo "Application initialized."
        exit 0
    elif [[ "$response" == "" ]]
    then
        echo "Server not running, waiting..."
        sleep 10
    else
        echo "Unknown error."
        echo "$response"
        exit 1
    fi
done