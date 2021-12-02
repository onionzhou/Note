import time

from locust import HttpUser, task, between,TaskSet
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/",verify=False)
        # self.client.get("/world")


    @task
    def view_item(self):
        self.client.get('/index.php/login',verify=False)
        # for item_id in range(10):
        #     self.client.get(f"/item?id={item_id}", name="/item")
        #     time.sleep(1)

    def on_start(self):
        # self.client.post("/login", json={"username":"foo", "password":"bar"})
        with self.client.get("/",catch_response=True,verify=False) as re:
            print(re.text)




if __name__ == '__main__':
    import os
    os.system('locust  -f locustfile.py')