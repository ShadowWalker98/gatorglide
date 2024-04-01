from internal.avlimpl.avltree import AvlTree


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


if __name__ == "__main__":
    print("Welcome to Gator Glide services!")

