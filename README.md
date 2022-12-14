# Authorization API

This is a basic API created in Python using Django Rest Framework to manage clients and permissions for those clients. This allows you to restrict which clients have access to certain services available.

### Usage

I use docker to build and run the API. Run the following commands to get it up and running:

```
docker build -t auth-api:latest .
docker run --rm -it \
    -p 8000:8000/tcp \
    -v <LOCAL_DATA_DIR>:/mnt/data \
    auth-api:latest
```

Where `<LOCAL_DATA_DIR>` is a directory on your local machine to persist the data of the application.

### Client Libraries

I have generated the following client libraries using `openapi-generator`:

- [Python](clients/python/client)
- [Swift](clients/swift5/client)