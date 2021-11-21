# Trees

Create a Binary tree and a Binary Search tree.

## Challenge

Node

    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Binary Tree

    Create a Binary Tree class
        Define a method for each of the depth first traversals:
            pre order
            in order
            post order which returns an array of the values, ordered appropriately.
    Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Binary Search Tree

    Create a Binary Search Tree class
        This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
        Add
            Arguments: value
            Return: nothing
            Adds a new node with that value in the correct location in the binary search tree.
        Contains
            Argument: value
            Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

Classes and methods are used to solve this challenge.

Big O= O(n)

## API

* pre order: to create a tree in the pre-order style. It would look like this: ["1", "2", "4", "3"], which may look a lot like the ordenary style and order.
* in order: which look like this: ["4", "2", "1", "3"].
* post order: ["4", "2", "3", "1"], looks a lot deformed and twisted.

# Trees max

# Challenge Summary

Write the following method for the Binary Tree class

    find maximum value
        Arguments: none
        Returns: number
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

![whiteboard](img/code-challenge-16.jpg)

## Approach & Efficiency

The approach of creating a method was used.

## Solution

    def max_num(self):
        if not self.root:
            raise Exception("An Empty Tree")

        self.max_element=self.root.data

        def max_item(node):
            if node.data>self.max_element:
                self.max_element= node.data
            if node.left:
                max_item(node.left)
            if node.right:
                max_item(node.right)
            return self.max_element

        return max_item(self.root)
