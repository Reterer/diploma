from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    @abstractmethod
    def generate_tasks(count_tasks: int, config: dict):
        pass

    @abstractmethod
    def check_task(task: dict, secret: dict, answer: dict):
        pass
