from collections import deque
import matplotlib.pyplot as plt

def solve_puzzle(initial_state):
    def is_valid(x, y):
        return 0 <= x < 6 and 0 <= y < 6

    def get_next_states(current_state):
        x, y = current_state[0], current_state[1]
        next_states = []

        moves = [(0, -5), (0, 1), (-1, 2), (1, 0)]  # Izquierda, Derecha, Arriba, Abajo

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_state = (new_x, new_y)
                next_states.append(new_state)

        return next_states

    queue = deque()
    visited = set()

    start = (2, 4)  # Coordenadas iniciales de 7
    queue.append((start, 0))  # Estado inicial y costo inicial

    path = []  # Almacenar el camino para el gráfico
    path.append(start)

    while queue:
        current_state, cost = queue.popleft()

        if current_state == (4, 2):  # Coordenadas finales de 7
            return cost, path

        visited.add(current_state)

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, cost + 1))
                path.append(next_state)

    return None

initial_state = (0, 0)  # Coordenadas iniciales de 7
result = solve_puzzle(initial_state)

if result:
    cost, path = result
    print("Costo de movimientos realizados:", cost)
    print("Coordenadas finales del valor 7:", path[-1])

    # Crear gráfico
    x, y = zip(*path)
    plt.plot(x, y, marker='o')
    plt.title('Recorrido del valor 7 en el Puzzle')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid()
    plt.show()
else:
    print("No se encontró una solución.")