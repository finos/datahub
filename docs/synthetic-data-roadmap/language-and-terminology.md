# Language and Terminology

The following language and terminology has been contributed through DataHub issue [#30](https://github.com/finos/datahub/issues/30) and relates to the [DataHub](https://github.com/finos/datahub) and [DataHelix](https://github.com/finos/datahub) projects.

---

Contributed by [@andrewcarrblue](https://github.com/andrewcarrblue) - https://github.com/finos/datahub/issues/30#issuecomment-664355125

To help us have a common language, would be great for us to agree terminology, use cases

## Types of data

- Reference data 
  - (slow to change).  
  - (1) Publicly available  
  - (2) Private ref data
- Event data 
  - (transaction logs, web logs, trade events, etc etc)
- System data 
  - (configuration data for the system itself)

## Type of event data

- Independent events 
  - (rows which have no dependency on each other) / Dependent events
- Rules based columns 
  - (columns which have dependencies/relationships on each other)
- Linked events 
  - rows which have a connection, relationship to data external to this table

## Use Cases

- Volume/throughput/stress testing 
  - high volume, reasonably realistic data
- Functional/feature 
  - low volume, super accurate/realistic data
- Machine learning training 
  - volume, realistic data, with realistic statistical shapes

## Attributes
- Statistical profiles
- Rules