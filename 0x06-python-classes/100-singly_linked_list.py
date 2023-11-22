#!/usr/bin/python3
"""Simulate a singly linked list with some functionality:
        -> Sorted insert
        -> Making it printable
"""


class Node:
    """Simulate the node"""
    def __init__(self, data, next_node=None):
        """initialise the object"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        """Set the value of next_node"""
        if node and (not isinstance(node, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = node


class SinglyLinkedList:
    """simulate the language itself"""
    def __init__(self):
        """initialize"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node in the right order"""
        node = Node(value)
        if not self.__head:
            self.__head = node
            return
        if value <= self.__head.data:
            node.next_node = self.__head
            self.__head = node
            return
        temp = self.__head
        while temp.next_node:
            if value <= temp.next_node.data:
                node.next_node = temp.next_node
                temp.next_node = node
                return
            temp = temp.next_node
        temp.next_node = node

    def __str__(self):
        string = ""
        temp = self.__head
        while temp and temp.next_node:
            string += str(temp.data) + '\n'
            temp = temp.next_node
        if temp:
            string += str(temp.data)
        return string
