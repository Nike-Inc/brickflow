---
hide:
  - navigation
---

# BrickFlow

BrickFlow is a CLI tool for development and deployment of Python based Databricks Workflows in a declarative way.

## Concept

`brickflow` aims to improve development experience for building any pipelines on databricks via:

- Providing a declarative way to describe workflows via decorators
- Provide intelligent defaults to compute targets
- Provide a code and git first approach to managing and deploying workflows
- Use databricks asset bundles to deploy workflows seamlessly. It is powered using terraform which helps manage state
  across deployments.
- CLI tool helps facilitate setting up a projects
- Provides additional functionality through the context library to be able to do additional things for workflows.


## Feedback

Issues with `brickflow`? Found a :octicons-bug-24: bug?
Have a great idea for an addition? Want to improve the documentation? Please feel
free to file an [issue](https://github.com/Nike-Inc/brickflow/issues/new/choose).

## Contributing

To contribute please fork and create a pull request. Here is
a [guide](https://github.com/Nike-Inc/brickflow/blob/main/CONTRIBUTING.md) to help you through this process.