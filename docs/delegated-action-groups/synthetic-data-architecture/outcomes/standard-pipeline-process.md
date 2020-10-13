# Title

__Parent:__ [Synthetic Data Architecture DAG](../readme.md)

__Discussion:__ [issue-50](https://github.com/finos/datahub/issues/50)

__status:__ DRAFT

## Abstract

Synthetic data processes should have a defined set of steps

- Analyse data - Classifiers, Identifiers, and Discreet values.
  - Financial organization have common classifiers (curves, tenors, countries, currencies, etc)
  - Identifiers to public external entities (LEI, ISIN, CUSIP)
  - Identifiers to private internal entities (account codes, trading books)

- Decide on best 'analysis' module (Sikmepl Bucketing, GAN)
- Parametertise the model (apply noise, fuzziness, generalize/normalize distributions as not to leak sensitive data)
- Run the model on the production set
- Use the model-data, and any additional properties to synthetically produce an artificial set
- Do something with the synthetic dataset
