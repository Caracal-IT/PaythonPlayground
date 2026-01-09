import threading
from abc import abstractmethod, ABC
from threading import Event


class Task(ABC):
    def __init__(self):
        self.event = None

    def __set_event__(self, event: Event):
        self.event = event

    @abstractmethod
    def execute(self):
        """Execute the action"""
        pass

    @abstractmethod
    def cancel(self):
        """Cancel the task"""
        pass

class LambdaTask(Task):
    def __init__(self, action):
        super().__init__()
        self.action = action

    def execute(self):
        """Execute the action"""
        self.action()

    def cancel(self):
        """Cancel the task"""
        print("Cancelling job")
        pass

    def __repr__(self):
        return f"LambdaTask(action={self.action.__name__})"