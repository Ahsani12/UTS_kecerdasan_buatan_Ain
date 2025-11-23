# =============================================
# IMPLEMENTASI A* (A-STAR) — VERSI BENAR & OPTIMAL
# Mencari rute dari Arad (A) ke Bucharest (G)
# =============================================

from heapq import heappush, heappop

# Graf: kota dan jarak antar kota (undirected)
graph = {
    'A': {'S': 140, 'T': 118, 'Z': 75},
    'S': {'A': 140, 'O': 151, 'F': 99,  'R': 80},
    'T': {'A': 118, 'L': 111},
    'Z': {'A': 75,  'O': 71},
    'O': {'Z': 71,  'S': 151},
    'L': {'T': 111, 'M': 70},
    'M': {'L': 70,  'D': 75},
    'D': {'M': 75,  'C': 120},
    'C': {'D': 120, 'R': 146, 'P': 138},
    'R': {'S': 80,  'C': 146, 'P': 97},
    'F': {'S': 99,  'B': 211},
    'P': {'R': 97,  'C': 138, 'B': 101},
    'B': {'F': 211, 'P': 101, 'G': 90,  'U': 85},
    'U': {'B': 85,  'H': 98,  'V': 142},
    'H': {'U': 98,  'E': 86},
    'E': {'H': 86},
    'G': {'B': 90}
}

# Heuristik: Straight-Line Distance ke Bucharest (G) — dari buku AI resmi
heuristic = {
    'A': 366, 'S': 253, 'T': 329, 'Z': 374, 'O': 380,
    'L': 244, 'M': 241, 'D': 242, 'C': 160, 'R': 193,
    'F': 176, 'P': 100, 'B': 0,   'U': 80,  'H': 151,
    'E': 161, 'V': 199, 'G': 0
}

# =============================================
# ALGORITMA A* — VERSI BENAR & CEPAT
# =============================================
def a_star(start, goal):
    open_list = []                              # Priority queue
    heappush(open_list, (heuristic[start], 0, start, [start]))  # (f, g, node, path)
    
    g_score = {start: 0}                        # Biaya dari start ke node
    came_from = {}                              # Untuk rekonstruksi path
    
    while open_list:
        f, g, current, path = heappop(open_list)
        
        if current == goal:
            return g, path                       # Total jarak + rute terbaik
        
        for neighbor, cost in graph.get(current, {}).items():
            new_g = g + cost
            
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                f_score = new_g + heuristic[neighbor]
                came_from[neighbor] = current
                heappush(open_list, (f_score, new_g, neighbor, path + [neighbor]))
    
    return -1, None  # Tidak ada jalur

# =============================================
# JALANKAN PROGRAM
# =============================================
start = 'A'      # Arad
goal  = 'G'      # Bucharest

print("="*70)
print("          IMPLEMENTASI HEURISTIC SEARCH: A* (A-STAR)".center(70))
print("="*70)

total_cost, route = a_star(start, goal)

if route:
    print(f"\nRUTE TERBAIK DITEMUKAN!")
    print(f"   Dari           : {start} (Arad)")
    print(f"   Tujuan         : {goal} (Bucharest)")
    print(f"   Jalur          : {' → '.join(route)}")
    print(f"   Total Jarak    : {total_cost} km")
    print(f"   Jumlah Kota    : {len(route)}")
else:
    print("Tidak ada rute ditemukan!")
