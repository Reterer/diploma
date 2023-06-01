from .base import BaseGenerator
import random

import networkx as nx


class InvGraph(BaseGenerator):
    def generate_tasks(config: dict):
        # task_count = config["task_count"]

        # min_v = config["min_v"]
        # max_v = config["max_v"]

        # min_e = config["min_v"]
        # max_e = config["max_v"]

        # min_c = config["min_v"]
        # max_c = config["max_v"]

        # def gen_task():
        #     v = random.randint(min_v, max_v)
        #     e = random.randint(min_e, max_e)
        #     G = nx.gnm_random_graph(v, e)

        #     compo = nx.algorithms.components.number_connected_components(G)
        #     while min_c > compo or max_c < compo:
        #         G = nx.gnm_random_graph(v, e)
        #         compo = nx.algorithms.components.number_connected_components(G)

        #     return G

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
