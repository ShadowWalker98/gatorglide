from internal.avlimpl.avltree import AvlTree

if __name__ == "__main__":
    avl_tree = AvlTree()
    avl_tree.insert(6)
    avl_tree.insert(2)
    avl_tree.insert(8)
    avl_tree.insert(4)
    avl_tree.delete_node(2)
    avl_tree.inorder()


