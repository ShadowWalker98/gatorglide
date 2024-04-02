from internal.order.order import *


class Node:
    def __init__(self, order: Order, branching_attr: str):
        self.type_tree = branching_attr
        if branching_attr == BRANCH_EST_TOA:
            self.val = order.est_toa
        elif branching_attr == BRANCH_PRIORITY:
            self.val = order.priority
        self.order_info = {order.order_id: order}
        self.left = None
        self.right = None
        self.parent = None
        self.left_height = 0
        self.right_height = 0
        self.balance_factor = 0
        self.height = 0

    def __str__(self):
        node_str = ("value: " + str(self.val) + " bf: " + str(self.balance_factor) +
                    " type: " + str(self.type_tree) + " parent: ")
        if self.parent is not None:
            node_str += str(self.parent.val)
        return node_str

    def get_value(self) -> int:
        return self.val

    def set_left(self, left_root) -> None:
        self.left = left_root

    def set_right(self, right_root) -> None:
        self.right = right_root

    def get_height(self):
        self.height = max(self.left_height, self.right_height) + 1
        return self.height

    def compute_balance_factor(self) -> int:
        self.left_height = 0
        if self.left is not None:
            self.left_height = self.left.get_height()
        self.right_height = 0
        if self.right is not None:
            self.right_height = self.right.get_height()
        self.balance_factor = self.left_height - self.right_height
        return self.balance_factor

    def get_degree(self) -> int:
        degree = 0
        if self.left is not None:
            degree += 1
        if self.right is not None:
            degree += 1
        return degree

    def add_order(self, order: Order):
        self.order_info[order.order_id] = order

    def remove_order(self, order: Order):
        del self.order_info[order.order_id]

    def order_exists(self, order: Order) -> bool:
        return order.order_id in self.order_info.keys()

    def order_exists_id(self, order_id: int) -> bool:
        return order_id in self.order_info.keys()