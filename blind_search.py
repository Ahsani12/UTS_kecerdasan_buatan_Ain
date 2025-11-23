# =============================================
# IMPLEMENTASI BLIND SEARCH: BFS, DFS, dan UCS
# Contoh: Peta Rumania (A → G)
# =============================================

# Graf (kota dan jarak antar kota)
graph = {
    'A': {'Z': 75, 'T': 118, 'S': 140},
    'Z': {'A': 75, 'O': 71},
    'O': {'Z': 71, 'S': 151},
    'T': {'A': 118, 'L': 111},
    'L': {'T': 111, 'M': 70},
    'M': {'L': 70, 'D': 75},
    'D': {'M': 75, 'C': 120},
    'C': {'D': 120, 'R': 146, 'P': 138},
    'R': {'C': 146, 'S': 80, 'P': 97},
    'S': {'A': 140, 'O': 151, 'R': 80, 'F': 99},
    'F': {'S': 99, 'B': 211},
    'P': {'C': 138, 'R': 97, 'B': 101},
    'B': {'F': 211, 'P': 101, 'G': 90, 'U': 85},
    'U': {'B': 85, 'H': 98, 'V': 142},
    'H': {'U': 98, 'E': 86},
    'E': {'H': 86},
    'G': {'B': 90}
}

# 1. BREADTH-FIRST SEARCH (BFS)
from collections import deque

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, {}):
                new_path = path + [neighbor]
                queue.append(new_path)
    return None

# 2. DEPTH-FIRST SEARCH (DFS) - versi iteratif (biar tidak stack overflow)
def dfs(start, goal):
    stack = [[start]]
    visited = set()
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, {}):
                new_path = path + [neighbor]
                stack.append(new_path)
    return None

# 3. UNIFORM COST SEARCH (UCS) - versi Dijkstra
import heapq

def ucs(start, goal):
    priority_queue = [(0, start, [start])]  # (cost, node, path)
    visited = set()
    
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
            
        visited.add(node)
        
        if node == goal:
            return cost, path
        
        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path + [neighbor]))
    
    return -1, None

# =============================================
# JALANKAN SEMUA METODE
# =============================================
start_city = 'A'
goal_city = 'G'

print("="*60)
print("          IMPLEMENTASI BLIND SEARCH".center(60))
print("="*60)

print(f"Mencari rute dari {start_city} → {goal_city}\n")

# BFS
path_bfs = bfs(start_city, goal_city)
print("1. BREADTH-FIRST SEARCH (BFS)")
print(f"   Rute ditemukan: {' → '.join(path_bfs) if path_bfs else 'Tidak ditemukan'}")
print(f"   Jumlah kota dilalui: {len(path_bfs) if path_bfs else 0}\n")

# DFS
path_dfs = dfs(start_city, goal_city)
print("2. DEPTH-FIRST SEARCH (DFS)")
print(f"   Rute ditemukan: {' → '.join(path_dfs) if path_dfs else 'Tidak ditemukan'}")
print(f"   Jumlah kota dilalui: {len(path_dfs) if path_dfs else 0}\n")

# UCS
cost_ucs, path_ucs = ucs(start_city, goal_city)
print("3. UNIFORM COST SEARCH (UCS)")
if path_ucs:
    print(f"   Rute terbaik   : {' → '.join(path_ucs)}")
    print(f"   Total jarak    : {cost_ucs} km")
else:
    print("   Rute tidak ditemukan")
print("="*60)