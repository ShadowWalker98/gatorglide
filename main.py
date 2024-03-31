from internal.avlimpl.avltree import AvlTree

if __name__ == "__main__":
    avl_tree = AvlTree()
    avl_tree.insert(6)
    avl_tree.insert(5)
    avl_tree.insert(8)
    avl_tree.delete_node(8)
    avl_tree.inorder()


