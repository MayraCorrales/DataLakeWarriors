# DataLakeWarriors

Project for the course **Data Warehouse & Data Lake Systems – HSLU**

## Team
- Gence Gencehan (14-656-722)
- Cyriel Van Helleputte (24-867-715)
- Mayra Corrales (24-867-681)

## Data Sources
- AviationStack API
- NewsAPI
- Eurostat

## Project Goal
Design a data lake architecture that integrates multiple external data sources 
(AviationStack, NewsAPI, and Eurostat) and enables data exploration, querying, 
and analysis.

## Architecture
Data Source APIs  
↓  
Python ingestion pipelines  
↓  
AWS S3 (Data Lake storage)  
↓  
AWS Glue Catalog  
↓  
Amazon Athena queries  
↓  
Data analysis (Python / notebooks)
