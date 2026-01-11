# FastAPI B2C Platform

This repository contains a starter structure for a FastAPI-based B2C platform.

Structure highlights:
- `app/` - application source
- `docker/` and `k8s/` - containerization and deployment manifests

To run locally (after installing dependencies):

1. Install Python packages:

   pip install -r requirements.txt

2. Start the app:

   uvicorn app.startup:create_app --reload

