class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        node = TreeNode()
        node.data = data
        if self.root is None:
            self.root = node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # move
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

    def search(self,data):
        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self,data):
        self.root = self._delete(self.root,data)

    def _delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            successor = self._min_value_node(root.right)
            root.data = successor.data
            root.right = self._delete(root.right, successor.data)

        return root

    def _min_value_node(self,node):
        current = node
        while current.left is not node:
            current = current.left
        return current


if __name__ == "__main__":
    numbers = [10,15,8,3,9]
    bst = BST()

    for num in numbers:
        bst.insert(num)

    print("BST 구성 완료")

    find_group = int(input())
    current = bst.root

    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.right




