from internal.avlimpl.node import Node


class AvlTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value_to_insert):
        if self.root is None:
            self.root = Node(value_to_insert)
            return
        self.__insert_helper(self.root, value_to_insert)

    def __insert_helper(self, root: Node, value_to_insert: int):
        if root is None:
            return
        else:
            # if the root is not None, we check whether the value to be inserted is less than the current
            # value at the root
            if root.val > value_to_insert:
                if root.left is None:
                    # if the left subtree is empty then we can just add it to the left
                    root.left = Node(value_to_insert)
                    root.left.parent = root
                else:
                    # insert it into the left subtree
                    self.__insert_helper(root.left, value_to_insert)

                root.left_height = root.left.height + 1
                root.height = max(root.left_height, root.right_height)
                bf = root.compute_balance_factor()
                # TODO: replace this with a balance factor check
                if bf < -1 or bf > 1:
                    # balance the tree
                    self.__balance(root)

            elif root.val < value_to_insert:
                if root.right is None:
                    # if the right subtree is empty then we can just add it to the right subtree
                    root.right = Node(value_to_insert)
                    root.right.parent = root
                else:
                    # insert it into the right subtree
                    self.__insert_helper(root.right, value_to_insert)

                root.right_height = root.right.height + 1
                root.height = max(root.left_height, root.right_height)
                bf = root.compute_balance_factor()
                #TODO: replace this with a balance factor check
                if bf < -1 or bf > 1:
                    # balance the tree
                    self.__balance(root)

    def preorder(self):
        def preorder_helper(root: Node):
            if root is not None:
                print(root)
                preorder_helper(root.left)
                preorder_helper(root.right)

        preorder_helper(self.root)

    def inorder(self):
        if self.root is None:
            print("The tree is empty")
            return

        def inorder_helper(root: Node):
            if root is not None:
                inorder_helper(root.left)
                print(root)
                inorder_helper(root.right)
        inorder_helper(self.root)

    def postorder(self):
        def postorder_helper(root: Node):
            if root is not None:
                postorder_helper(root.left)
                postorder_helper(root.right)
                print(root)
        postorder_helper(self.root)

    def __balance(self, root: Node):
        bf = root.balance_factor
        # this is the node where the balance factor has become either < -1 or > 1
        # we first check if the height of left subtree > height of right subtree
        # or vice versa
        # then we appropriately check which case of imbalance it is
        if bf < -1:
            # balance factor < -1 means the tree is either RR or RL case
            if root.right.balance_factor < 0:
                # if bf of right child < 0 then it is RR
                self.__left_rotate(root)
            else:
                # if bf of right child > 0 then it is RL
                self.__right_rotate(root.right)
                self.__left_rotate(root)
        elif bf > 1:
            # balance factor > 1 means the tree is either LL or LR case
            if root.left.balance_factor > 0:
                self.__right_rotate(root)
            else:
                self.__left_rotate(root.left)
                self.__right_rotate(root)

    def __right_rotate(self, root: Node):
        has_parent = root.parent is not None
        root_left = root.left
        root_parent = root.parent
        root_left_right = root.left.right
        if root_left_right is not None:
            root_left_right.parent = root
        root.left = root_left_right
        if has_parent:
            left_child = root_parent.left == root
            root_left.parent = root_parent
            if left_child:
                root_parent.left = root_left
            else:
                root_parent.right = root_left
        else:
            self.root = root_left
            root_left.parent = None

        root.parent = root_left
        root_left.right = root
        root.compute_balance_factor()
        root_left.compute_balance_factor()

    def __left_rotate(self, root: Node):
        has_parent = root.parent is not None
        root_right = root.right
        root_parent = root.parent
        root_right_left = root.right.left
        if root_right_left is not None:
            root_right_left.parent = root
        root.right = root_right_left
        if has_parent:
            left_child = root_parent.left == root
            root_right.parent = root_parent
            if left_child:
                root_parent.left = root_right
            else:
                root_parent.right = root_right
        else:
            self.root = root_right
            root_right.parent = None

        root.parent = root_right
        root_right.left = root
        root.compute_balance_factor()
        root_right.compute_balance_factor()

    # delete node from avl tree
    # at this point just checks if the values match and deletes the node from the tree
    def delete_node(self, value_to_be_deleted: int) -> bool:
        print("Have to delete node with value: " + str(value_to_be_deleted))
        # we check if tree has any nodes
        if self.root is None:
            return False
        # we check if the node being deleted is present in the tree
        # if it is not, then we return False or an error
        node_to_delete = self.search_key(value_to_be_deleted)
        if node_to_delete is None:
            return False
        # if it is, we check if it is a leaf, a degree one node or a degree 2 node
        # call the helper function
        degree = self.root.get_degree()

        if degree == 0:
            parent = self.__delete_leaf(node_to_delete)
            self.__delete_balance_helper(parent)

        return True

    # TODO: complete helper function for deletion and balancing of nodes
    def __delete_balance_helper(self, root: Node):
        bf = root.compute_balance_factor()
        if self.is_imbalanced(root):
            if bf < -1:
                if root.right.balance_factor < 0:
                    # RR rotation
                    self.__left_rotate(root)
                else:
                    self.__right_rotate(root.left)
                    self.__left_rotate(root)

    # returns parent of the deleted node
    def __delete_leaf(self, root: Node) -> Node | None:
        if root.parent is None:
            self.root = None
            return root.parent
        else:
            is_left_child = root.parent.left == root
            if is_left_child:
                root.parent.left = None
            else:
                root.parent.right = None
            return root.parent
    def search_key(self, key: int) -> Node | None:
        return self.__search_helper(self.root, key)

    def __search_helper(self, root: Node, key: int) -> Node | None:
        if root is None:
            return root
        if root.val == key:
            return root
        elif root.val > key:
            return self.__search_helper(root.left, key)
        else:
            return self.__search_helper(root.right, key)

    # helper method for finding the inorder successor for a node being deleted
    # returns the node to the calling function
    @staticmethod
    def __find_inorder_successor(root: Node) -> Node:
        inorder_successor = root.right
        while inorder_successor.left is not None:
            inorder_successor = inorder_successor.left
        return inorder_successor

    @staticmethod
    def is_imbalanced(root: Node) -> bool:
        return root.balance_factor < -1 or root.balance_factor > 1

    @staticmethod
    def degree(root: Node) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
            return 1
        else:
            return 2
