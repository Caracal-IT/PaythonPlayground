from abc import abstractmethod, ABC
from threading import Event

from utils.context import Context


class Task(ABC):
    def __init__(self):
        self.event = None

    @abstractmethod
    def execute(self, ctx: Context):
        """Execute the action"""
        pass

    @abstractmethod
    def cancel(self, ctx: Context):
        """Cancel the task"""
        pass

    def __set_event__(self, event: Event):
        self.event = event

class LambdaTask(Task):
    def __init__(self, action):
        super().__init__()
        self.action = action

    def execute(self, ctx: Context):
        """Execute the action"""
        self.action()

    def cancel(self, ctx: Context):
        """Cancel the task"""
        print("Cancelling job")
        pass

    def __repr__(self):
        return f"LambdaTask(action={self.action.__name__})"