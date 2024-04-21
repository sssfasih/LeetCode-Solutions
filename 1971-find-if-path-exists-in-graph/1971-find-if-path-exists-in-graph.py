class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, seen):
            if node == destination:
                return True
            
            if node in seen:
                return False
            
            seen.add(node)
            
            for n_ in adj[node]:                
                if dfs(n_, seen):
                    return True
                
            return False
        
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        return dfs(source, set())
        