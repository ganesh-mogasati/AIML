class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None
def isSymmetric(root):
    if not root:
        return True
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.key == right.key and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    return isMirror(root.left, root.right)
def build_tree(values, index):
    if index >= len(values) or values[index] == -1:
        return None
    root = Node(values[index])
    root.left = build_tree(values, 2 * index + 1)
    root.right = build_tree(values, 2 * index + 2)
    return root
input_str = input("Enter binary tree values -1 for null nodes: ")
values = list(map(int, input_str.split()))
root = build_tree(values, 0)
if isSymmetric(root):
    print("TRUE")
else:
    print("FALSE")