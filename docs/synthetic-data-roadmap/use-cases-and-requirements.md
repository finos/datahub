# Use Cases and Requirements

The following use cases and requirements have been contributed through DataHub issue #30 and relates to the [DataHub](https://github.com/finos/datahub) and [DataHelix](https://github.com/finos/datahub) projects.
https://github.com/finos/datahub/issues/30

---
Originally contributed by @andrewcarrblue - https://github.com/finos/datahub/issues/30#issuecomment-651734549

## Use Cases
* High volume reasonably realistic data – typically used for soak tests, volume tests,
* Lower volume hyper realistic data – typically used to check system functionality
 
## Requirements for a Synthetic Data Generator
### Requirements around generating “similar” reasonably realistic data
| Requirement | Description | Priority | GitHub Issue |
|:-----|:-----|:-----|:-----|
| | Ability to look at some given data, maybe production data and observe some profile, shape and characteristics of that data.  Which can then be used to generate some “life like” synthetic data |
| | Ability to review the profile, shape and characteristics of the data observed, so sensitive enumerations, shapes, profiles, names etc can be removed, modified or changed |
| | Characteristics of data that would be good to be observable<ul><li>(Basic) Type of column – integer, float, string</li><li>Whether the column is an enum (enumeration) – a set of values from a given set</li><li>Whether the column is freeform text, and if so, what other characteristics does it have</li><li>Average length, min length, max length</li><li>Valid characters</li><li>Control characters (including end of line/return)</li></ul> |
| | Whether there are any relationships between the columns (combinations of valid enumerations, values related to enumerations)<ul><li>Any more advanced distributions in value columns, Poisson, normal and other distributions</li><li>Advanced recognition of data types</li><li>Recognising financial services specific values such as RICs, ISINs, CUSIPs</li><li>Ability to generate custom field values based on code</li></ul> |

### Requirements around generating “hyper” realistic data
| Requirement | Description | Priority | GitHub Issue |
|:-----|:-----|:-----|:-----|
| | Components with the ability to add code to generate data |
| | The code to be able to access business logic to generate data which matches given rules (maybe even share business logic with code from the system?) |

---
Contributed by @BenFielding - https://github.com/finos/datahub/issues/30#issuecomment-667943969

### Requirements 
Additional project requirements from Gensyn perspective (highly representative synthetic data).

| Requirement | Description | GitHub Issue Created |
|---------- |------------- |----------|
| Rules to pick generative models | Discover statistical properties that determine which generative models can re-create the source data most effectively. Particularly data volume. Key properties: Distribution, Sparsity, Discrete vs continuous, and Volume. | <ul><li>[ ] </li></ul> |
| Similarity-analysis | How closely does the generated data resemble the real data, does this prevent a privacy risk and can this be quantified? A common approach is Distance to Closest Record using Euclidean Distance. [Here](https://arxiv.org/abs/1806.03384). | <ul><li>[ ] </li></ul> |
| Missing value specification | Are missing values in a column MCAR, MAR, or MNAR? Important when using generative models and listwise deletion. | <ul><li>[ ] </li></ul> |

This also comes alongside an additional use case that we'd add to the above from @andrewcarrblue, which is:

- Machine learning feature engineering - medium volume, realistic data, with realistic statistical shapes

This would be used by a machine learning researcher/developer/engineer to perform exploratory data analysis (EDA) and to build a prototype model, before deploying over a federated learning infrastructure (e.g. as provided by Gensyn).