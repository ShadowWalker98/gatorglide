class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.left_height = 0
        self.right_height = 0
        self.balance_factor = 0
        self.height = 0

    def __str__(self):
        node_str = "value: " + str(self.val) + " bf: " + str(self.balance_factor) + " parent: "
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
        return max(self.left_height, self.right_height) + 1

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

