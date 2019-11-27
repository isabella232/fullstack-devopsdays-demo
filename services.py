from threading import Timer
import json
import random
import time
import logging_service

data = []
with open('mock_logs.json') as json_file:
    data = json.load(json_file)

class App:
  """
  Fake application which simulates making fake logs
  """
  def __init__(self, service='', num_services=1):
    self._timer = None
    self.is_running = False
    self.service = service
    self.num_services = num_services
    self.logger = logging_service.Logger(
      service=service
    )

  def _run(self):
    self.is_running = False
    self.start(interval=self.num_services)
    self.log()

  def start(self, interval=1):
    if not self.is_running:
      self._timer = Timer(interval, self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False

  def deploy(self):
    print('[DEBUG] Starting up %s' % self.service)
    print('[DEBUG] Expect to see logs soon ...')
    time.sleep(1)
    self.start(interval=self.num_services)

  def log(self):
    log = random.choice(data)
    self.logger.log(log['level'], log['message'])


