from .base import BaseGenerator
import random


test_config = {
    "task_count": 1,
    "tasks": [
        {
            "question": "Даны высказывания:<br>1) То, что N делится на 15, есть необходимое условие того, чтобы N делилось на 3.<br>2) То, что N не делится на 3, влечёт то, что N не делится на 15.<br>3) N делится на 3 при условии, что N делится на 15.<br>4) N не делится на 3 только тогда, когда N не делится на 15.<br>5) N делится на 3 тогда и только тогда, когда N делится на 15.<br>Какие из них следуют из высказывания N делится на 15, то N делится на 3?<br>",
            "checks": ["1", "2", "3", "4", "5"],
            "answer": [1, 2, 3],
        },
    ],
}


class Sample(BaseGenerator):
    def generate_tasks(config: dict):
        tasks = config["tasks"]
        task_count = config["task_count"]
        selected_tasks = random.sample(tasks, task_count)
        secret = [task["answer"] for task in selected_tasks]
        for i in range(len(selected_tasks)):
            selected_tasks[i].pop("answer")
        return selected_tasks, secret

    def check_task(task: dict, secret: dict, answer: dict):
        score = 0
        for check in secret:
            if check in answer:
                score += 1
        score /= len(secret)
        return score
