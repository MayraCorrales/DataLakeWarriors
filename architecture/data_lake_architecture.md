# Data Lake Architecture

## Data Sources
- AviationStack API
- NewsAPI
- Eurostat API

## Pipeline
Python scripts retrieve the data from the APIs and ingest it into the data lake.

## Storage
The ingested datasets are stored in a data lake storage layer.

## Catalog
Metadata is organized to allow efficient querying and discovery of the datasets.

## Query
A query engine is used to explore and analyze the stored data.

## Analysis
Jupyter notebooks are used for data exploration, analysis, and visualization.
