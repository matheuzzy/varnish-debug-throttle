import time
from locust import HttpUser, task, between, constant

class QuickstartUser(HttpUser):
    wait_time = constant(0)

    @task(1)
    def fast_backend(self):
        self.client.get("/", headers={'Cookie': 'same=value'})

