import time
from locust import HttpUser, task, between, constant

class QuickstartUser(HttpUser):
    wait_time = constant(0)

    @task(1)
    def slow_backend(self):
        self.client.get("/?delay=5", headers={'Cookie': 'same=value'})
