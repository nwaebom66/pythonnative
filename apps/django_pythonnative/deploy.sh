#!/bin/bash

# https://cloud.google.com/python/django/run#deploy

# Using the supplied cloudmigrate.yaml, use Cloud Build to build the image, run
# the database migrations, and populate the static assets
gcloud builds submit --config cloudmigrate.yaml

# When the build is successful, deploy the Cloud Run service for the first time,
# setting the service region, base image, and connected Cloud SQL instance
gcloud run deploy pythonnative-service \
    --platform managed \
    --region us-central1 \
    --image gcr.io/pythonnative/pythonnative-service \
    --add-cloudsql-instances pythonnative:us-central1:pythonnative-instance \
    --allow-unauthenticated
