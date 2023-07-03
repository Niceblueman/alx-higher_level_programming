#!/usr/bin/python3
class Node:
    """_summary_
    """
    def __init__(self, data, next_node=None):
        """_summary_

        Args:
            data (_type_): _description_
            next_node (_type_, optional): _description_. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


class SinglyLinkedList:
    """_summary_
    """
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """_summary_
        """
        self.__head = None

    def sorted_insert(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        ptr = self.__head
        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node
        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
