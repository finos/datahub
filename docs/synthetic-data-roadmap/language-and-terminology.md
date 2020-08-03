# Language and Terminology

The following language and terminology has been contributed through DataHub issue [#30](https://github.com/finos/datahub/issues/30) and relates to the [DataHub](https://github.com/finos/datahub) and [DataHelix](https://github.com/finos/datahub) projects.

---

Contributed by [@andrewcarrblue](https://github.com/andrewcarrblue) - https://github.com/finos/datahub/issues/30#issuecomment-664355125

To help us have a common language, would be great for us to agree terminology, use cases

## Types of data

- **Reference data** 
  - Slow to change  
  - (1) Publicly available  
  - (2) Private ref data
- **Event data** 
  - Transaction logs, web logs, trade events, etc
- **System data** 
  - Configuration data for the system itself

## Type of event data

- **Independent events** 
  - Rows which have no dependency on each other) _verses_ Dependent events
- **Rules based columns** 
  - Columns which have dependencies / relationships on each other
- **Linked events** 
  - Rows which have a connection, relationship to data external to this table

## Use Cases

- **Volume/throughput/stress testing** 
  - High volume, reasonably realistic data
- **Functional/feature** 
  - Low volume, super accurate / realistic data
- **Machine learning training** 
  - Volume, realistic data, with realistic statistical shapes

## Attributes
- **Statistical profiles**
- **Rules**