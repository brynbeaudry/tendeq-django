#!/bin/bash
docker run --name tendeq-postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=1 -e POSTGRES_DB=tendeq -p 35432:5432 postgres:latest