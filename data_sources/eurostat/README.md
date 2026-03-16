# Eurostat Data Source

## Description
Eurostat is the official statistical office of the European Union and provides harmonised, high-quality data across EU member states.

In this project, Eurostat is used as the **static data source** and provides the **macro-level aviation baseline** for the analysis. It supports cross-country comparison by offering structured air transport statistics such as passenger volumes, freight volumes, and flight movements across European airports.

## Data Access
Eurostat data is accessed through the Eurostat API and official datasets.

## Role in the Project
Eurostat complements the two dynamic data sources in the project:

- **NewsAPI** captures major world events and media signals
- **AviationStack** captures flight activity and operational aviation data
- **Eurostat** provides harmonised long-run aviation statistics for comparison and contextualisation

This allows us to compare short-term event-driven signals with broader structural aviation patterns across EU countries.

## Example Data
Example variables or datasets include:

- passenger volumes
- freight transport volumes
- flight movements
- airport-level or country-level aviation statistics

## Ingestion Process
The data is retrieved, cleaned, and stored as part of the project data lake pipeline.

## Storage
The raw data is stored under:

`data_sources/eurostat/`
