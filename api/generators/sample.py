from .base import BaseGenerator
import random


class Sample(BaseGenerator):
    def generate_tasks(config: dict):
        tasks = config["tasks"]
        task_count = config["task_count"]
        print(tasks)
        selected_tasks = random.sample(tasks, task_count)
        secret = [task["answer"] for task in selected_tasks]
        for i in range(len(selected_tasks)):
            # selected_tasks[i].pop("answer")
            pass
        return selected_tasks, secret

    def check_task(task: dict, secret: dict, answer: dict):
        score = 0
        for check in secret:
            print(check, answer, check in answer)
            if check in answer:
                score += 1
        score /= len(secret)
        return score
