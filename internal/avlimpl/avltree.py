from internal.avlimpl.node import Node
from internal.constants import *
from internal.order.order import Order


class AvlTree:

    def __init__(self, type_tree: str):
        if type_tree == BRANCH_PRIORITY:
            self.type_tree = BRANCH_PRIORITY
        elif type_tree == BRANCH_EST_TOA:
            self.type_tree = BRANCH_EST_TOA
        self.root = None
        self.size = 0

    def insert(self, value_to_insert: Order):
        if self.root is None:
            self.root = Node(value_to_insert, self.type_tree)
            return
        # if there is a node already with the same priority, we just need to add order id : order in order_info dic
        # we don't need to create a new node
        if self.type_tree == BRANCH_PRIORITY:
            node_if_present = self.search_key(value_to_insert)
            if node_if_present is not None:
                # add order info to the hashmap
                node_if_present.add_order(value_to_insert)
            return
        # we proceed as normal otherwise
        node_to_insert = Node(value_to_insert, self.type_tree)
        self.__insert_helper(self.root, node_to_insert)

    def __insert_helper(self, root: Node, node_to_insert: Node):
        if root is None:
            return
        else:
            # if the root is not None, we check whether the value to be inserted is less than the current
            # value at the root
            if root.val > node_to_insert.val:
                if root.left is None:
                    # if the left subtree is empty then we can just add it to the left
                    root.left = node_to_insert
                    root.left.parent = root
                else:
                    # insert it into the left subtree
                    self.__insert_helper(root.left, node_to_insert)

                root.left_height = root.left.height + 1
                root.height = max(root.left_height, root.right_height)
                root.compute_balance_factor()
                if self.is_imbalanced(root):
                    # balance the tree
                    self.__balance(root)

            elif root.val < node_to_insert.val:
                if root.right is None:
                    # if the right subtree is empty then we can just add it to the right subtree
                    root.right = node_to_insert
                    root.right.parent = root
                else:
                    # insert it into the right subtree
                    self.__insert_helper(root.right, node_to_insert)

                root.right_height = root.right.height + 1
                root.height = max(root.left_height, root.right_height)
                root.compute_balance_factor()
                if self.is_imbalanced(root):
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
    def delete_node(self, value_to_be_deleted: Order, inorder_flag: bool) -> bool:
        # if the tree is based on priorities we first check if the order_priority is present in the tree
        # if it is then we check if the order_id list becomes empty after deleting the specific order_id provided
        # if the tree is based on eta, then there are no duplicates
        # we just proceed like normal as we do in a normal avl tree

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
        degree = node_to_delete.get_degree()
        parent = None
        # only the priority type tree can have duplicates.
        # if we do find that a particular priority value is present twice then we can just delete the order id
        # from the order info dictionary and return, as we don't have to remove the priority value itself.
        # if the order_info dic is empty after deletion of the order id then we have to remove this node from the tree
        # this means we have to either delete a leaf, a degree one node or a degree two node. So we proceed as how we
        # would in a normal AVL tree deletion.
        if self.type_tree == BRANCH_PRIORITY and not inorder_flag:
            node_to_delete.remove_order(value_to_be_deleted)
            if len(node_to_delete.order_info) > 0:
                return True
        if degree == 0:
            # deleting the leaf
            parent = self.__delete_leaf(node_to_delete)

        elif degree == 1:
            # we delete the node and the child of the node being deleted is attached to the parent
            # then we recompute the balance factor for the parent and balance if needed
            parent = self.__delete_degree_one_helper(node_to_delete)
        else:
            # find the inorder successor then replace the node with it
            # then the node which is physically deleted is the inorder successor
            # and is always a degree one or degree zero node

            inorder_successor = self.__find_inorder_successor(node_to_delete)
            # swap the values and then physically delete the node at the inorder_successor
            temp_val = inorder_successor.val
            temp_order_info = inorder_successor.order_info
            # update this to make the node have a hashmap of order_ids: order_info - DONE
            # TODO: test the following implementation and think over it a little
            # when we are replacing the node to be deleted with its inorder successor then we want to copy the entire
            # order info dic. We therefore maintain a flag in the parameters which when true means we don't check for
            # duplicates and just delete the node
            # deleting the node having an order id which is present in order_info of the inorder_successor
            # and since inorder flag is true we delete it directly.
            self.delete_node(inorder_successor.order_info[next(iter(inorder_successor.order_info))], True)
            # copy the values of the inorder successor's values into the node which was "deleted"
            node_to_delete.val = temp_val
            node_to_delete.order_info = temp_order_info
        # balancing the resulting tree after node deletion
        if parent is not None:
            while parent is not None:
                parent.compute_balance_factor()
                if self.is_imbalanced(parent):
                    self.__delete_balance_helper(parent)
                parent = parent.parent
        return True

    def __delete_balance_helper(self, root: Node):
        bf = root.compute_balance_factor()
        if self.is_imbalanced(root):
            # L Rotation
            if bf < -1:
                # L0 rotation
                if root.right.balance_factor == 0:
                    self.__left_rotate(root)
                # L-1 rotation
                elif root.right.balance_factor < 0:
                    self.__left_rotate(root)
                # L1 rotation
                else:
                    self.__right_rotate(root.right)
                    self.__left_rotate(root)
            # R Rotation
            elif bf > 1:
                # RO rotation
                if root.left.balance_factor == 0:
                    self.__right_rotate(root)
                # R1 rotation
                elif root.left.balance_factor > 0:
                    self.__right_rotate(root)
                # R-1 rotation
                else:
                    self.__left_rotate(root.left)
                    self.__right_rotate(root)

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
            parent = root.parent
            root.parent = None
            return parent

    def __delete_degree_one_helper(self, node) -> Node | None:
        node_parent = node.parent
        # checking if the deleted node has a left child or right child and setting it accordingly
        node_child = node.left if node.left is not None else node.right
        if node_parent is not None:
            # checking if the node being deleted is the left child or not
            is_left_child = node.parent.left == node
            if is_left_child:
                # setting the left child of the parent to be the deleted node's only child
                node_parent.left = node_child
            else:
                # setting the right child of the parent to be the deleted node's only child
                node_parent.right = node_child
        else:
            # if the node being deleted is the root and is degree one
            # then we set the root of the avl tree itself to be the child
            self.root = node_child

        # setting the new child's parent to be the parent of the deleted node
        node_child.parent = node_parent
        # unlinking the deleted node from the tree
        node.parent = None
        return node_parent

    def search_key(self, key: Order) -> Node | None:
        # check if this particular priority is present in the tree if the tree type is BRANCH_PRIORITY
        # check if this particular eta is present in the tree if the tree type is BRANCH_EST_TOA
        if self.type_tree == BRANCH_PRIORITY:
            return self.__search_helper(self.root, key.priority, key.order_id)
        if self.type_tree == BRANCH_EST_TOA:
            return self.__search_helper(self.root, key.est_toa, key.order_id)

    def __search_helper(self, root: Node, key: int, order_id: int) -> Node | None:
        if root is None:
            return root
        if ((root.val == key and self.type_tree == BRANCH_EST_TOA)
                or (root.val == key and self.type_tree == BRANCH_PRIORITY and root.order_exists_id(order_id))):
            return root
        elif root.val > key:
            return self.__search_helper(root.left, key, order_id)
        else:
            return self.__search_helper(root.right, key, order_id)

    def get_order_info(self, order_id: int) -> (Order, int):
        if self.root == None:
            return None, None
        node = self.root
        while node is not None:
            if node.order_exists_id(order_id):
                return node.order_info[order_id], node.val

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
