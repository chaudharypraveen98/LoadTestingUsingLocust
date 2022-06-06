from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def get_bitcoin_prices(self):
        self.client.get("/v1/bpi/currentprice.json")