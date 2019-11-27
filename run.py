import logging_service
import services
import time

app = services.App(service="app_server")
app.deploy()
