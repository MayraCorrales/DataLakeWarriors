# AviationStack Data Source

## Description
AviationStack is a REST API that provides real-time and historical aviation data, including information about flights, airlines, routes, and airports.

In this project, AviationStack is used as a **dynamic data source** to capture aviation activity and operational flight patterns.

## Data Access
The data is accessed through the AviationStack API:

https://aviationstack.com/

API documentation:

https://aviationstack.com/documentation

## Example Data Fields
Typical fields available in the API include:

- flight status
- departure and arrival airports
- airline information
- flight number
- route information
- departure and arrival times

These variables allow the analysis of aviation activity and operational patterns.

## Role in the Project
AviationStack provides the **aviation-side response variables** for the project.

It is used to:

- monitor flight activity
- observe changes in flight frequency
- detect disruptions or anomalies in aviation operations
- compare aviation activity with major news events

Together with NewsAPI and Eurostat, AviationStack helps evaluate whether major world events are statistically associated with changes in aviation performance.

## Ingestion Process
Python scripts retrieve the data through the AviationStack API and store the raw output in the project pipeline.

## Storage
The raw data is stored in the project data lake under:

data_sources/aviationstack/
