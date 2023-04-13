import unittest
from src.tasks import Task

class TestTasks(unittest.TestCase):

    def setUp(self):
        self.first_task = Task("wash dishes", "15 minutes")
        self.second_task = Task("cook dinner", "1 hour")
        self.third_task = Task("clean windows", "1 hour 15 minutes")

    def test_task_has_a_name(self):
        self.assertEqual("wash dishes", self.first_task.description)


    