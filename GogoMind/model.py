from composite import Root
from composite import Node
from composite import Composite
from node_factory import NodeFactory


class MindMapModel:

    def __init__(self):
        self._root = None
        # self._serialId = -1
        self._composite = {}

    def get_node(self, id_: int) -> Node:
        if not id_ in self._composite:
            return None
        else:
            return self._composite[id_]

    @property
    def root(self) -> Root:
        return self._root

    def create_mind_map(self, desc) -> bool:
        if self.root:
            print('MindMapModel', 'root already exist')
            return False
        else:
            return self.insert_node(self._create_node(0, desc), None)

    def insert_node(self, node: Composite, parent_id: int) -> bool:
        if isinstance(node, Root):
            if self._root:
                raise Exception('Root already exist')
                return False
            else:
                self._root = node
        else:
            if not node:
                raise Exception('node cannot be None')
                return False
            if parent_id not in self._composite:
                raise Exception('no parent')
                return False
            if node.id in self._composite:
                raise Exception('this node already exist')
                return False
            parent = self._composite[parent_id]
            parent.add_child(node)
            node.set_parent(parent)

        self._composite[node.id] = node
        return True


    def save_mind_map(self):
        print('saveMindMap')

    # def create_node(self, desc: str, new_id_: int) -> Composite:
        # self._serialId += 1
        # return self._create_node(new_id_, desc)

    def _create_node(self, id_: int, desc: str) -> Composite:
        type_ = TYPE_ROOT if (id == 0) else TYPE_NODE
        return NodeFactory.create_node(type_, id_, desc)
