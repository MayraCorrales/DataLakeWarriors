# Data Ingestion Pipelines

## Overview
This folder contains the data ingestion pipelines used to retrieve data from the external APIs and load it into the project data lake.

Each data source has its own Python ingestion script.

## Pipeline Structure
The pipelines follow a simple ingestion workflow:

1. Connect to the external API  
2. Retrieve the requested data  
3. Process and clean the retrieved data  
4. Store the raw data in the project data lake structure  

## Implemented Pipelines

### Eurostat Pipeline
File: `eurostat_pipeline.py`

This pipeline retrieves aviation-related datasets from the Eurostat API and prepares them for analysis.

The pipeline performs the following steps:

- sends requests to the Eurostat API  
- retrieves aviation statistics datasets  
- converts the response into structured data  
- stores the retrieved data in the project data structure  

## Future Pipelines
Additional ingestion pipelines will be implemented for:

- **NewsAPI** (news event data)
- **AviationStack** (flight activity data)

## Storage Location
The retrieved datasets are stored under:

`data_sources/`

Each data source has its own folder:

- `data_sources/eurostat`
- `data_sources/newsapi`
- `data_sources/aviationstack`

## Purpose
The ingestion pipelines allow the project to systematically collect and organise data from multiple external sources so that it can later be queried, analysed, and compared.
