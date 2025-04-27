import numpy as np, random

d = np.array([[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]])
n, ants, iters = len(d), 10, 50
pheromone, vis = np.ones((n,n)), 1/(d + np.eye(n)*1e10)
best_route, best_dist = None, float('inf')

for _ in range(iters):
    routes = []
    for _ in range(ants):
        route, unvisited = [], list(range(n))
        cur = random.choice(unvisited); route.append(cur); unvisited.remove(cur)
        while unvisited:
            probs = [pheromone[cur][j] * vis[cur][j] for j in unvisited]
            cur = random.choices(unvisited, weights=probs)[0]
            route.append(cur); unvisited.remove(cur)
        routes.append(route)

    pheromone *= 0.5
    for route in routes:
        length = sum(d[route[i]][route[(i+1)%n]] for i in range(n))
        for i in range(n):
            a, b = route[i], route[(i+1)%n]
            pheromone[a][b] += 1/length; pheromone[b][a] += 1/length
        if length < best_dist: best_dist, best_route = length, route

print("Best route:", best_route)
print("Shortest distance:", best_dist)
