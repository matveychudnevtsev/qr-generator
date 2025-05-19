# QR Service Project

This repository contains multiple services for a QR code management system.

## Services
- **api-gateway** - FastAPI based gateway that routes requests to other services.
- **qr-generator** - Flask service for generating QR codes.
- **storage-service** - Simple file storage service for generated codes.
- **frontend** - React based web interface.

## Development
Dockerfiles for each service are located under the `docker/` folder. A `docker-compose.yml` file is provided for local development.
