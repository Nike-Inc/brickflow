# BrickFlow v1.3.1 Quickstart Guide

This guide will help you get started with BrickFlow v1.3.1, walking you through project setup and deployment.

## Prerequisites

1. Local environment setup:
   - Python >= 3.8
   - Databricks CLI configured with access token
   - BrickFlow CLI

### Installation Steps

1. Install Databricks CLI and configure it:
```bash
pip install databricks-cli
databricks configure -t
```

2. Install BrickFlow CLI:
```bash
pip install brickflows
```

3. Verify your installation:
```bash
bf --help
databricks workspace list /  # Add --profile <profile> if using specific profile
```

## Creating Your First Project

1. Navigate to your repository root (where `.git` folder is located)

2. Initialize a new BrickFlow project:
```bash
bf projects add
```

3. Follow the prompts:
   - Project Name: Enter your desired project name
   - Path from repo root to project root: Press Enter for default (`.`) or specify path
   - Path from project root to workflows dir: Enter the directory for your workflows
   - Git https url: Enter your repository URL
   - Brickflow version: Enter `1.3.1` (or press Enter for `auto`)
   - Spark expectations version: Press Enter for default (`0.8.0`)
   - Skip entrypoint: Choose `N` unless you have a specific reason to skip

4. Update your `.gitignore` file:
```
**/bundle.yml
.databricks/
```

## Project Structure

Your project will follow either a monorepo or polyrepo style:

### Monorepo Structure Example:
```
repo-root/
├── .git
├── projects/
│   ├── project_abc/
│   │   ├── lib/
│   │   │   ├── __init__.py
│   │   │   └── shared_functions.py
│   │   ├── workflows/
│   │   │   ├── __init__.py
│   │   │   ├── entrypoint.py
│   │   │   └── workflow_abc.py
│   │   └── .brickflow-project-root.yml
```

### Polyrepo Structure Example:
```
repo-root/
├── .git
├── src/
│   ├── lib/
│   │   ├── __init__.py
│   │   └── shared_functions.py
│   ├── workflows/
│   │   ├── __init__.py
│   │   ├── entrypoint.py
│   │   └── workflow.py
├── .brickflow-project-root.yml
```

## Validating Your Project

1. Synthesize your project configuration:
```bash
bf projects synth --project <project_name> --profile <profile>
```

2. Verify the output shows:
```
SUCCESSFULLY SYNTHESIZED BUNDLE.YML FOR PROJECT: <project_name>
```

## Deploying Your Project

### Development Deployment
```bash
bf projects deploy --project <project> -p <profile> --force-acquire-lock
```

### Environment-Specific Deployments
```bash
# Dev environment
bf projects deploy --project <project> -p <profile> -e dev --force-acquire-lock

# Test environment
bf projects deploy --project <project> -p <profile> -e test --force-acquire-lock

# Production environment
bf projects deploy --project <project> -p <profile> -e prod --force-acquire-lock
```

### Release Candidate Deployments
For testing specific versions or pull requests:

```bash
# Deploy RC version
BRICKFLOW_WORKFLOW_SUFFIX="1.3.1-rc1" bf projects deploy --project <project> -p <profile> -e test --force-acquire-lock

# Deploy PR version
BRICKFLOW_WORKFLOW_SUFFIX="1.3.1-pr34" bf projects deploy --project <project> -p <profile> -e test --force-acquire-lock
```

## Cleaning Up

### Destroying Deployments
```bash
# Destroy main deployment
bf projects destroy --project <project> -p <profile> --force-acquire-lock

# Destroy RC deployment
BRICKFLOW_WORKFLOW_SUFFIX="1.3.1-rc1" bf projects destroy --project <project> -p <profile> -e test --force-acquire-lock

# Destroy PR deployment
BRICKFLOW_WORKFLOW_SUFFIX="1.3.1-pr34" bf projects destroy --project <project> -p <profile> -e test --force-acquire-lock
```

## Troubleshooting

1. If synthesis fails:
   - Verify you're in the repository root directory
   - Check that all paths in configuration files are correct
   - Ensure all required __init__.py files exist

2. If deployment fails:
   - Verify Databricks CLI configuration
   - Check permissions in your Databricks workspace
   - Verify environment variables are set correctly

## Next Steps

After successful deployment:
1. Monitor your workflows in the Databricks workspace
2. Set up CI/CD pipelines for automated deployments
3. Configure environment-specific variables
4. Set up monitoring and alerting