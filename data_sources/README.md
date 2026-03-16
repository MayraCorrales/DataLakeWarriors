# NewsAPI Data Source

## Description
NewsAPI.org provides access to news headlines and articles from thousands of news sources worldwide through a REST API.

In this project, NewsAPI is used as a **dynamic data source** to capture major world events through news headlines and articles. These events are used as explanatory signals that may help explain changes in aviation activity.

## Data Access
The data is accessed through the NewsAPI REST API:

https://newsapi.org/

API documentation:

https://newsapi.org/docs

## Example Data Fields
Typical fields returned by the API include:

- article title
- source
- author
- publication date
- description
- article content
- URL

These fields allow further analysis such as keyword extraction, topic classification, or sentiment analysis.

## Role in the Project
NewsAPI provides the **event detection component** of the project.

It is used to:

- collect news related to major world events
- identify relevant event categories
- extract keywords and topics
- potentially perform sentiment analysis

The extracted event signals are later compared with aviation activity data to investigate whether major news events are associated with measurable changes in aviation indicators.

## Ingestion Process
Python scripts retrieve news articles from the NewsAPI endpoints and store the retrieved data for further processing and analysis.

## Storage
The raw data is stored in the project data lake under:

data_sources/newsapi/
