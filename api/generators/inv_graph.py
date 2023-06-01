from .base import BaseGenerator
import random

# import networkx as nx


class InvGraph(BaseGenerator):
    def generate_tasks(config: dict):
        public = [
            {
                "nodes": {
                    "node1": {"name": "Node 1"},
                    "node2": {"name": "Node 2"},
                    "node3": {"name": "Node 3"},
                    "node4": {"name": "Node 4"},
                },
                "edges": {
                    "edge1": {"source": "node1", "target": "node2"},
                    "edge2": {"source": "node2", "target": "node3"},
                    "edge3": {"source": "node3", "target": "node4"},
                },
            }
        ]
        secret = [{}]
        return public, secret

    def check_task(task: dict, secret: dict, answer: dict):
        score = 0
        return score
