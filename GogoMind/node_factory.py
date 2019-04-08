from composite import Composite
from composite import Root
from composite import Node

TYPE_ROOT = 0
TYPE_NODE = 1


class NodeFactory:

    @staticmethod
    def create_node(type_: int, node_id: int, desc: str) -> Composite:
        if type_ == TYPE_ROOT:
            return Root(node_id, desc)
        else:
            return Node(node_id, desc)
