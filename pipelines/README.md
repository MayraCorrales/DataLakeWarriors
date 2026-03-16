# Eurostat Data Source

## Description
Eurostat provides harmonised statistical data across all EU member states.

In this project, Eurostat serves as the **structural aviation dataset**, providing
aggregated statistics such as passenger volumes, freight transport, and flight
movements across European airports.

These data act as a **baseline layer** that complements the dynamic signals
captured from AviationStack (flight data) and NewsAPI (news events).

## Data Access
Eurostat datasets are accessed through the Eurostat API:

https://ec.europa.eu/eurostat/api/

## Example Dataset
Example datasets used in this project:

- Air passenger transport statistics
- Airport traffic statistics
- Air freight volumes

These datasets allow cross-country comparison across EU member states.

## Role in the Project
Eurostat provides **long-run structured aviation statistics** that allow us to:

- compare aviation activity across EU countries
- contextualize changes observed in real-time flight data
- test whether news events correlate with aviation performance indicators

## Storage
The raw data retrieved from Eurostat is stored in the data lake under:

data_sources/eurostat/
