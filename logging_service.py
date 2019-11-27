import logging
from datetime import datetime
from optimizely import optimizely
from optimizely.config_manager import PollingConfigManager

#### OPTIMIZELY IMPLEMENTATION #####
sdk_key = '<YOUR PRODUCTION SDK KEY GOES HERE>'
config_manager = PollingConfigManager(
  sdk_key = sdk_key,
  update_interval = 2
)
####################################

optimizely_client = optimizely.Optimizely(config_manager=config_manager)


class Logger:
  def __init__(self, service=''):
    self.service = service
    self.batch_queue = []


  def log_to_console(self, date, level, message):

    #### OPTIMIZELY FEATURE FLAG ####
    # Implement a feature flag for log filtering
    is_filtering_enabled = optimizely_client.is_feature_enabled('log_filtering', self.service, { 'service': self.service })
    #################################

    # If the feature is enabled, filter logs based on level
    if is_filtering_enabled:
      min_level = optimizely_client.get_feature_variable('log_filtering', 'min_level', self.service, { 'service': self.service })
    else:
      min_level = 0

    if min_level <= logging._nameToLevel[level]:
      print('%s: %s [%s] %s' % (date, self.service, level, message))


  def log(self, level, message):
    now = datetime.now()

    #### OPTIMIZELY FEATURE FLAG ####
    # Implement a feature flag for batching
    is_batching_enabled = optimizely_client.is_feature_enabled('log_batching', self.service, { 'service': self.service })

    # If the feature is enabled, batch the logs
    if is_batching_enabled:
      self.log_in_batch(now, level, message)
    else:
      self.flush_queue()
      self.log_to_console(now, level, message)


  def log_in_batch(self, date, level, message):

    #### OPTIMIZELY FEATURE VARIABLE ####
    # Implement a feature variable for batch size
    batch_size = optimizely_client.get_feature_variable('log_batching', 'batch_size', self.service, { 'service': self.service })

    if len(self.batch_queue) < batch_size:
      self.batch_queue.append({
        "date": date,
        "level": level,
        "message": message,
      })
    else:
      print('[DEBUG] Batch Feature Enabled. Sending batch of %s logs at a time' % len(self.batch_queue))
      self.flush_queue()


  def flush_queue(self):
    while len(self.batch_queue) > 0:
      log = self.batch_queue.pop(0)
      self.log_to_console(log["date"], log["level"], log["message"])
