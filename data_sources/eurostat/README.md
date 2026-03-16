# Eurostat Data Source

## Description
Eurostat is the official statistical office of the European Union and provides harmonised statistical data across EU member states.

In this project, Eurostat acts as the **static data source** and provides the **structural aviation baseline** used to contextualise the dynamic signals obtained from AviationStack and NewsAPI.

It provides aggregated aviation statistics such as passenger volumes, freight transport, and flight movements across European airports.

## Data Access
Eurostat datasets are accessed through the Eurostat API:

https://ec.europa.eu/eurostat/api/

Additional documentation:

https://ec.europa.eu/eurostat

## Example Datasets
Examples of relevant aviation datasets include:

- Air passenger transport statistics
- Airport traffic statistics
- Air freight volumes

These datasets allow cross-country comparison across EU member states.

## Role in the Project
Eurostat provides **long-run structured aviation statistics** that allow us to:

- compare aviation activity across EU countries
- contextualise changes observed in real-time flight data
- support statistical analysis together with AviationStack and NewsAPI

In the project architecture:

- **NewsAPI** captures major world events
- **AviationStack** captures operational flight activity
- **Eurostat** provides the macro-level aviation baseline

## Ingestion Process
The data is retrieved through API requests or official datasets and processed using Python scripts.

## Storage
The raw data is stored in the project data lake under:

data_sources/eurostat/
