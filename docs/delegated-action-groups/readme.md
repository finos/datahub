# Delegate Action Groups

Delegate Action groups are used to officially delegate decision making responsibility to address a specific challenge or problem in an open manner. The mandate for a dag is outlined in a POST document (Problem, Outcomes Structure, Timeline)

## Book of DAG

| Status | Chair        | Link/Description                                                               |
|-----------------------|--------------------------------------------------------------------------------|
| Draft  | James McLeod | [Datahub-datahelix-collaboration](./datahub-datahelix-collaboration/readme.md) |
| Draft  | James McLeod | [synthetic-data-architecture](./synthetic-data-architecture/readme.md)     |

## Structure

``` bash
├── DELEGATE_ACTION_GROUP
│   ├── post-short-description 1
│   │     ├── POST.md   << Master document
│   │     ├── outcomes
│   │     │   ├── outcome-1.md  
│   │     │   ├── outcome-2.md
│   │     │   ├── outcome-3.md
│   │     ├── descisions
│   │     │   ├── descision-1.md  
│   │     │   ├── descision-2.md
│   │     │   ├── descision-3.md
│   │
│   ├── post-short-description 2
│   │    ├── POST.md   << Master document
│   │    ├── outcomes
│   │    │   ├── outcome-1.md  
│   │    │   ├── outcome-2.md
│   │    ├── descisions
│   │    │   ├── descision-1.md  
│   │    │   ├── descision-2.md
│
```

## Templates

### POST documents

``` markdown

# TITLE

Status: Draft|In-Progress|Complete

## Problem

Describe the problem in 2/3 paragraphs

## Outcome

* [link] Short description of outcome 1
* [link] Short description of outcome 2
* [link] Short description of outcome 3

## Structure / Skills

- [Chair] - <name> - [Data Science]
- Fred Morris - [Big Data Export]
- Someone Else - [Stakeholder 1]
- A.Stakeholder - [Stakeholder 2]
- B.Stakeholder - [Stakeholder 3] 
- C.Stakeholder - [Stakeholder 3] 

## Timelines and Constraints

Declare what is out of scope, urgency capacity from teams to contribute,

## Decisions

* [link] Short description of outcome 1  [Aproved|InProgress]
* [link] Short description of outcome 2  [Aproved|InProgress]
* [link] Short description of outcome 3  [Aproved|InProgress]

```

### Objectives

Objectives are written and approved as part of the DAG. While the DAG is in draft mode the objectives are fine-tuned. Once all objectives are agreed the DAG moves from Draft to 'In Progress' While the DAG is in draft - Create an issue for tracking the conversation.

Once the objective is agreed then the issue is closed the finalized objective text from the issue should be transferred to the objective document The 'issue' can then be 'closed' the /dag-name/objective/objective-name.md file becomes the final document.
The Issue remains closed, re-opening the objective to make a major changes means the entire DAG moves back to DRAFT status.

```markdown

# Title

[Link] to the Github Issue for conversation[Link] to the associated decision when it's made

## Abstract

2/3 paragraphs on the outcome and what it achieves

```

### Decision

Decisions are made by the working group and correspond with the scope of the DAG and the declared objectives Decisions are the output of the DAG. Once all decisions are approved the DAG is 'complete' decisions are binding for the future of the project.

Create an issue for tracking the conversation. Once the issue is closed the finalized decision text from the issue should be transferred to the decision document The issue can then be 'closed' the decision md file becomes the final document.

``` markdown

# Title

Status: In-Progress | Complete

[Link] to the Github Issue for conversation[Link] to the associated objective

## Abstract

2/3 paragraphs on the outcome and what it achieves

## Consequences of the Decision

What is the consequence of this decision being made - will it lead to a specific implementation, resourcing etc.

## Alternatives?

Document any alternative decisions that could have been made

## Decision Outcome

Document the decisions that were made
```
