---
id: roadmap
title: Roadmap
---
# Roadmap

## DataHub Examples 

Many financial service organizations face the same problems across common data sets. We aim for a good set of example problem and solutions

- Client Account Generation example
- Security Price generation
- Fixed Income vanilla swaps
- Client-centric OTC trading portfolios

## Extend core functionality 

Enhance DataHub core capabilities

- Extend samples to cover all useful distributions, normal, binominal, power etc with relevant tweaking parameters 
- Functionality to add adaptive noise to a model
- Parallelized execution
- Consistent Execution 

## UI and Service mode

Using the core library to synthetically generate data required direct scripting/coding. Man use-cases could be catered for by a UI Workflow

- Service API with Docker images
- Configuration language / specification
- UI Workflow 

## Agent-based modeling 

An agent-based model (ABM) is a class of computational models for simulating the actions and interactions of autonomous agents (both individual or collective entities such as organizations or groups) with a view to assessing their efforts on the system as a whole

- Full object generation 
- Agent generation 
- Model behavior helper - e.g. event generation from probability functions based on observations from real data - e.g. probability of client (x) making a trade of type (t) for a currency at given notional 

## Configuration based tooling

Not everyone wants to write code, so we should support a declarative based specification in a populate mark-up  language

- Implement data sinks to popular databases
- investigate adopting Data Helix specification language
