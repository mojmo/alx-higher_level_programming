#!/usr/bin/python3

"""Defines Node and SinglyLinkedList classes
to implement a singly linked list."""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The reference to the
                                        next node in the linked list.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data stored in the node.

        Returns:
            int: The data stored in the node.
        """

        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the provided value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Gets the reference to the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the reference to the next node in the linked list.

        Args:
            value (Node): The reference to the next node in the linked list.

        Raises:
            TypeError: If the provided value is not a Node object.
        """

        if ((value is not None) and
                (not isinstance(value, Node))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList."""

        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """

        nodes = []
        curr_node = self.__head

        while (curr_node is not None):
            nodes.append(str(curr_node.data))
            curr_node = curr_node.next_node

        return '\n'.join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the
        linked list in sorted order.

        Args:
            value (int): The value to be inserted into the linked list.
        """

        new_node = Node(value)

        if (self.__head is None):
            new_node.next_node = None
            self.__head = new_node
        elif (self.__head.data > value):
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr_node = self.__head
            while (curr_node.next_node is not None and
                   curr_node.next_node.data < value):
                curr_node = curr_node.next_node

            new_node.next_node = curr_node.next_node
            curr_node.next_node = new_node
