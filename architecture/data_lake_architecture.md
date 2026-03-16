# Data Lake Architecture

## Data Sources
The project integrates three external data sources:

- AviationStack API
- NewsAPI
- Eurostat API

## Data Ingestion
Python scripts retrieve the data from the APIs.

Each data source has its own ingestion pipeline.

## Storage
The ingested datasets are stored in a data lake storage layer.

The raw data is organized by source:

data_sources/
- aviationstack
- newsapi
- eurostat

## Metadata Catalog
Metadata is organized to allow efficient discovery and querying of the datasets.

## Query Layer
A query engine is used to explore and analyze the stored datasets.

## Analysis
Jupyter notebooks are used for data exploration, analysis, and visualization.

## Conceptual Architecture

AviationStack API  
NewsAPI  
Eurostat API  
        ↓  
Python ingestion pipelines  
        ↓  
Data Lake storage layer  
        ↓  
Metadata catalog  
        ↓  
Query engine  
        ↓  
Jupyter notebooks for analysis
