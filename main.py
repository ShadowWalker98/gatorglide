from internal.avlimpl.avltree import AvlTree
from internal.constants import BRANCH_EST_TOA, BRANCH_PRIORITY
from internal.order.order import Order


def check_delete_leaf():
    avl_tree = AvlTree()
    avl_tree.insert(6)
    avl_tree.insert(4)
    avl_tree.insert(2)
    avl_tree.insert(8)
    avl_tree.delete_node(8)
    avl_tree.inorder()


def check_insertion():
    avl_tree = AvlTree()
    avl_tree.insert(6)
    avl_tree.insert(5)
    avl_tree.insert(8)
    avl_tree.insert(9)
    avl_tree.insert(13)
    avl_tree.insert(7)
    avl_tree.insert(10)
    avl_tree.insert(11)
    avl_tree.insert(12)
    avl_tree.insert(15)
    # avl_tree.delete_node(2)
    avl_tree.inorder()


def degree_two_deletion():
    avl_tree = AvlTree()
    avl_tree.insert(6)
    avl_tree.insert(2)
    avl_tree.insert(10)
    avl_tree.insert(4)
    avl_tree.insert(1)
    avl_tree.delete_node(2)
    avl_tree.inorder()


# def testing(order_param: Order, param: str):
#
#     val = None
#
#     if param == "priority":
#         val = "priority"
#     elif param == "eta":
#         val = "eta"
#
#     if val == "eta":
#         print(order_param.est_toa)
#     elif val == "priority":
#         print("priority " + str(order_param.order_value))
#

def print_attributes_except(order_param: Order, param: str):
    for attr in dir(order_param):
        if attr != param and not attr.startswith('_'):
            print(attr, getattr(order_param, attr))


def print_attributes(order_param: Order):
    for attr in dir(order_param):
        if not attr.startswith('_'):
            print(attr, getattr(order_param, attr))

if __name__ == "__main__":
    # print("Gatorglide services Ltd.")
    order1 = Order(1002, 1, 500, 4, 1)
    order2 = Order(1002, 1, 500, 4, 2)
    order3 = Order(1002, 1, 500, 4, 3)
    order4 = Order(1002, 1, 500, 4, 4)
    order5 = Order(1002, 1, 500, 4, 5)
    order6 = Order(1002, 1, 500, 4, 6)
    order7 = Order(1002, 1, 500, 4, 7)
    order8 = Order(1002, 1, 500, 4, 8)
    order9 = Order(1002, 1, 500, 4, 9)
    order10 = Order(1002, 1, 500, 4, 10)
    order11 = Order(1002, 1, 500, 4, 11)
    order12 = Order(1002, 1, 500, 4, 12)
    # driver code for ETA tree testing
    avl_tree = AvlTree(BRANCH_EST_TOA)
    avl_tree.insert(order1)
    avl_tree.insert(order2)
    avl_tree.insert(order3)
    avl_tree.insert(order4)
    avl_tree.insert(order5)
    avl_tree.insert(order6)
    avl_tree.insert(order7)
    avl_tree.insert(order8)
    avl_tree.insert(order9)
    avl_tree.insert(order10)
    avl_tree.insert(order11)
    avl_tree.insert(order12)
    avl_tree.delete_node(order10, False)
    avl_tree.delete_node(order11, False)
    avl_tree.delete_node(order12, False)
    avl_tree.inorder()




