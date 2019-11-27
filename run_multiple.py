import logging_service
import services
import time

services_list = [
  "app_server",
  "crypto_miner",
  "ml_model",
  "event_processor",
]

for service in services_list:
  app = services.App(
    service=service,
    num_services=len(services_list)
  )
  app.deploy()
