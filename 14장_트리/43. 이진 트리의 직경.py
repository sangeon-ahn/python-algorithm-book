import collections

class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

class Solution:
  # 첫번째 시도 풀이 실패
  def getDiameter(self, root):
    leftDepth = 0
    rightDepth = 0

    queue = collections.deque([root])

    while queue:
      node = queue.popleft()

      if node.left:
        leftDepth += 1
        queue.append(node.left)

      if node.right:
        rightDepth += 1
        queue.append(node.right)

    return leftDepth + rightDepth

  # 두번째 시도 풀이 성공
  def getDiameter2(self, root):
    def getDepth(root):
      if root == None:
        return 0

      queue = collections.deque([root])
      depth = 0

      while queue:
        depth += 1
        for _ in range(len(queue)):
          node = queue.popleft()

          if node.left:
            queue.append(node.left)

          if node.right:
            queue.append(node.right)

      return depth

    return getDepth(root.left) + getDepth(root.right)

root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5

s = Solution()

# print(s.getDiameter2(root))

# 예시 풀이 1. 상태값 누적 트리 DFS
class Solution2:
  # 중첩함수에서 부모 함수의 변수를 재할당하면 부모에 있는 변수에 할당되는게 아니라 중첩 함수 내에 지역변수가 생기고 이것에 할당을 하게 된다.
  # 따라서 바깥에 클래스 변수로 선언해서 자유롭게 할당할 수 있게 해준다.
  longest: int = 0

  def diameterOfBinaryTree(self, root: TreeNode) -> int:
    def dfs(node: TreeNode) -> int:
      if not node:
        return -1

      # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
      left = dfs(node.left)
      right = dfs(node.right)

      # 가장 긴 경로
      self.longest = max(self.longest, left + right + 2)

      # 상태값 리턴
      return max(left, right) + 1

    dfs(root)
    return self.longest

S = Solution2()

print(S.diameterOfBinaryTree(root))


# dfs 풀이 연습
# 푸는 방법
# 1. dfs로 맨 밑까지 탐색한다고 생각한다.
# 2. 탐색 결과 무엇을 리턴해야 할 지 생각한다. 리프노드와 인자로 받은 노드까지의 거리를 리턴한다.
# 3. 여기서는 리프 노드를 기준으로 깊이가 -1인 곳 까지 가기 때문에 max(left, right) + 1을 리턴한다. 이러면 리프 노드에서의 dfs 값은 0이 된다.
# 4. 최대 길이는 루트 노드의 두 자식 노드의 리프 노드까지의 거리 + 2이기 때문에 left + right + 2가 최대 길이이다.

class Practice:
  longest: int = 0

  def practice(self, root):
    def dfs(node: TreeNode):
      if not node:
        return -1

      left = dfs(node.left)
      right = dfs(node.right)

      self.longest = max(self.longest, left + right + 2)

      return max(left, right) + 1

    dfs(root)

    return self.longest



