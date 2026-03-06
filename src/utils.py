import random
import numpy as np

def calculate_route_distance(route, dist_matrix):
    total = 0
    for i in range(len(route)):
        a = route[i]
        b = route[(i + 1) % len(route)]
        total += dist_matrix[a][b]
    return total

def create_random_route(n):
    route = list(range(n))
    random.shuffle(route)
    return route
