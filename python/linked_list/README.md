# Singly Linked List

A task to create a linked list to get used to.

## Challenge

Node

    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

Linked List

    Create a Linked List class
    Within your Linked List class, include a head property.
        Upon instantiation, an empty Linked List should be created.
    The class should contain the following methods
        insert
            Arguments: value
            Returns: nothing
            Adds a new node with that value to the head of the list with an O(1) Time performance.
        includes
            Arguments: value
            Returns: Boolean
                Indicates whether that value exists as a Node’s value somewhere within the list.
        to string
            Arguments: none
            Returns: a string representing all the values in the Linked List, formatted as:
            "{ a } -> { b } -> { c } -> NULL"
    Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
    Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).


## Approach & Efficiency

The approach of classes and methods were emplemented in the task.

Big O = O(n)

## API

Insert method:
    this method is responsible to ad new node to the list.

Includes method:
    this method is used to check if the node's value is already exited within the list or not.

To sting method:
    this method is made to convert the whole list to a more readable version of list in the way you want.
