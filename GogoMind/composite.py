from abc import ABCMeta, abstractmethod
from typing import List


class Composite(metaclass=ABCMeta):

    def __init__(self, id_: int, desc: str):
        self._id = id_
        self._desc = desc
        self.children = []
        self.sibling = []
        self._parent = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def desc(self) -> str:
        return self._desc

    @abstractmethod
    def add_child(self, node) -> bool:
        if self == node or node in self.children:
            return False
        else:
            self.children.append(node)
            return True

    @abstractmethod
    def add_sibling(self, node) -> bool:
        if self == node or node in self.sibling:
            return False
        else:
            self.sibling.append(node)
            return True

    @abstractmethod
    def get_children(self) -> List['Composite']:
        return self.children

    @abstractmethod
    def get_sibling(self) -> List['Composite']:
        return self.sibling

    @abstractmethod
    def set_parent(self, parent: 'Composite') -> bool:
        if not self._parent and self != parent:
            self._parent = parent
            return True
        else:
            return False


class Root(Composite):
    def __init__(self, id_: int, desc: str):
        super().__init__(id_, desc)

    def add_child(self, node: Composite) -> bool:
        if isinstance(node, Node):
            return super().add_child(node)
        else:
            return False

    def add_sibling(self, node: Composite) -> None:
        raise ValueError('no sibling for root node')

    def get_children(self) -> List['Composite']:
        return super().get_children()

    def get_sibling(self) -> None:
        raise ValueError('no sibling for root node')

    def set_parent(self, parent: 'Composite') -> None:
        raise ValueError('root itself is already a prent')


class Node(Composite):
    def __init__(self, id_: int, desc: str):
        super().__init__(id_, desc)

    def add_child(self, node: Composite) -> bool:
        if isinstance(node, Node):
            return super().add_child(node)
        else:
            return False

    def add_sibling(self, node: Composite) -> bool:
        return super().add_sibling(node)

    def get_children(self) -> List['Composite']:
        return super().get_children()

    def get_sibling(self) -> List['Composite']:
        return super().get_sibling()

    def set_parent(self, parent: 'Composite') -> bool:
        return super().set_parent(parent)
