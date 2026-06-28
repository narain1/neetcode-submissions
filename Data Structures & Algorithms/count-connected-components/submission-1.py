class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        for i,j in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)

        visited = set()
        def dfs(node):
            q = [node]
            while q:
                n = q.pop()
                for neighbor in neighbors[n]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)

        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count

