from abc import abstractmethod, ABC

from config.settings import Settings


class Context(ABC):
    def __init__(self, settings: Settings):
        self.settings = settings

    @abstractmethod
    def start(self, job_id):
        """Start the job with the given job_id"""

        pass

    @abstractmethod
    def stop(self, job_id):
        """Stop the job with the given job_id"""

        pass