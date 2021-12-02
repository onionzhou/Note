import logging
import random

from locust import HttpUser, TaskSet, task, between

from httprunner.exceptions import MyBaseError, MyBaseFailure
from httprunner.ext.locusts.utils import prepare_locust_tests
from httprunner.runner import Runner

logging.getLogger().setLevel(logging.CRITICAL)
logging.getLogger('locust.main').setLevel(logging.INFO)
logging.getLogger('locust.runners').setLevel(logging.INFO)


class WebPageTasks(TaskSet):
    def on_start(self):
        config = {}
        self.test_runner = Runner(config, self.client)

    @task
    def test_any(self):
        test_dict = random.choice(self.locust.tests)
        self.test_runner.run_test(test_dict)


class WebPageUser(HttpUser):
    host = ""
    task_set = WebPageTasks
    wait_time = between(1, 2)

    # file_path is generated on locusts startup
    file_path = "./testcases/dashboard.yaml"
    tests = prepare_locust_tests(file_path)


if __name__ == '__main__':
    import os
    os.system('locust  -f dash_locustfile.py')
