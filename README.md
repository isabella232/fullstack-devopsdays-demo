# Feature Flag - Configure Logging Demo

This demo shows how Optimizely Fullstack can be used to control one (or multiple) logging service's batch sizes.

## Getting Started with this Example Application

1. Clone this repo
2. Navigate to the root of the repo
3. Create a virtual environment `venv`:
  - `virtualenv venv`
  - `. venv/bin/activate`
4. Install the Optimizely Python SDK:
  - `pip install optimizely-sdk`
5. To run a single logging service: 
  - `python run.py`
   To run multiple logging services: 
  - `python run_multiple.py`

## Getting Started with your Optimizely Fullstack Project
1. Sign up for a free trial of Optimizely Fullstack [here](optimizely.com/free-trial)
  - Follow all of the prompts
2. Create your first Optimizely Fullstack Project, name it whatever you like


### Configure your Feature Flag
1. Find your production SDK key under 'Settings'
  - update the SDK key on line 7 of `logging_service.py` (aside: move this to an environment variable if you plan on committing your example app)
2. Create a Feature Flag
  - 'Features' > 'Create New Feature'
  - Enter `log_batching` as the feature key
  - Add a feature variable called `batch_size`
    - `Variable Key: batch_size`, `Type: Integer`, `Default Value: 20`

### Toggle your Feature Flag On/Off
1. Select 'Environment' as `Production`
2. Toggle the feature `on`
3. Roll it out to 100% of traffic
4. See what happens :) 

### Optional: Partial Rollout 
1. Roll out your feature to some percentage (try 50%) of traffic
  - maybe change your `batch_size` to 10 to speed up the demo 
2. run `python run_multiple.py` to see what happens

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

