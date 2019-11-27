# Feature Flag - Configure Logging Demo

## Getting Started

- Clone the repo
- Navigate to the root of the repo
- `pip install optimizely-sdk`
- `python run.py`
- or to run multiple services, run `python run_multiple.py`

## Configuration

### with your own Optimizely Project

- Create a Full Stack project
- Change the SDK key in `logging_service.py`
- Create a feature flag called `log_batching`
- Create a feature variable for the above feature called `batch_size`

## Under the Hood

### logging_service.py
A service which logs to console and has Optimizely configured so that feature flags and variables can control the behavior of the logging service.

### services.py
Mock services which sends fake logs to the logging service

### run.py
Entrypoint to a simple 'one service' demo. Bootstraps one mock service called `app_server`.

### run_multiple.py
Entrypoint for running multiple services at once. This is useful to show off a targeting feature, targeting individual
named services.

