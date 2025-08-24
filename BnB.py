import time
import statistics
import matplotlib.pyplot as plt
from typing import List, Tuple

C1 = [("P01", "Chips Box", 1, 6), ("P02", "Soda Crate", 2, 11), ("P03", "Candy Bulk", 3, 16),
      ("P04", "Water Pack", 4, 21), ("P05", "Fruit Crate", 5, 26), ("P06", "Ice Cream Bin", 6, 31),
      ("P07", "BBQ Sauce Case", 7, 36), ("P08", "Snack Variety", 8, 40),
      ("P09", "Cleaning Supplies", 9, 45), ("P10", "First-Aid Kits", 10, 50)]

C2 = [("Q10", "Assorted Gadgets", 10, 60), ("Q20", "Party Drinks Pallet", 20, 100),
      ("Q30", "Outdoor Grill", 30, 120), ("Q35", "Mini Freezer", 35, 130),
      ("Q40", "Tool Chest", 40, 135), ("Q45", "Camp Bundle", 45, 140),
      ("Q50", "Generator", 50, 150)]

W = (0, 5, 20, 35, 50, 65, 80, 95, 110, 140)


def solve_greedy(products: List[Tuple[str, str, int, int]], capacity_W: int) -> Tuple[int, List[str]]:
    # Calcular valor y peso para cada producto
    products_with_ratio = []
    for pid, name, weight, value in products:
        ratio = value / weight
        products_with_ratio.append((pid, name, weight, value, ratio))

    # Ordenar con los criterios
    products_with_ratio.sort(key=lambda x: (-x[4], x[2], x[0]))
    chosen_ids = []
    total_value = 0
    used_weight = 0

    for pid, name, weight, value, ratio in products_with_ratio:
        if used_weight + weight <= capacity_W:
            chosen_ids.append(pid)
            total_value += value
            used_weight += weight

    return total_value, chosen_ids


def solve_method(products: List[Tuple[str, str, int, int]], capacity_W: int) -> Tuple[int, List[str]]:
    # Aplica la regla x[3]/x[2] a cada producto en la lista para sacar su ratio value-weight
    # Luego, los organiza empezando con el producto con el mejor ratio y terminando con el producto con peor ratio
    organized_product = sorted(products, key=lambda x: x[3] / x[2], reverse=True)
    length = len(organized_product)

    best_value = 0
    best_selection = []

    def upper_limit(index, leftover_weight, current_value):
        # Define el limite superior
        limit = current_value
        for i in range(index, length):
            pid, name, weight, value = organized_product[i]
            # Se mete el item si cabe dentro de la capacidad restante
            if weight <= leftover_weight:
                limit += value
                leftover_weight -= weight
            else:
                # Esto es "fractionally filling" la capacidad que queda
                limit += value * (leftover_weight / weight)
                break
        return limit

    def backtrack(index, leftover_weight, current_value, selected_products):
        nonlocal best_value, best_selection

        # Caso base, llegamos al ultimo producto en la lista
        if index == length:
            #Adjustar si el presente valor es mayor que el mejor valor
            if current_value > best_value:
                best_value = current_value
                best_selection = selected_products[:]
            return

    
        ul = upper_limit(index, leftover_weight, current_value)
        # Si el limite superior del camino es menor o igual que el mejor valor que ya hemos encontrado, haz nada
        # Asi se corta ramas que no son prometedores
        if ul <= best_value:
            return

        #Checar si el producto en index cabe dentro de la capacidad restante.
        pid, name, weight, value = organized_product[index]
        if weight <= leftover_weight:
            selected_products.append(pid)
            backtrack(index + 1, leftover_weight - weight, current_value + value, selected_products)
            selected_products.pop()

        #Si todo lo anterior no aplica, se va al siguente producto
        backtrack(index + 1, leftover_weight, current_value, selected_products)

    #Edge-case cuando capacidad es 0 o la lista de productos esta vacia
    if capacity_W <= 0 or not products:
        return (0, [])

    backtrack(0, capacity_W, 0, [])
    return best_value, best_selection


def benchmarking(C_list, W, triaul=5):
    total_results = []
    for weight in W:
        result = []
        for _ in range(triaul):
            start = time.time()
            value, product_list = solve_method(C_list, weight)
            end = time.time()
            duration = (end - start) * 1000
            print("Maximum Weight: ", weight)
            print("Value: ", value)
            print("Product List: ", product_list)
            result.append(duration)
        total_results.append(statistics.median(result))
    return total_results


def greedy_benchmarking(C_list, W):
    result_BnB = []
    result_Greedy = []
    for weight in W:
        value1, _ = solve_method(C_list, weight)
        value2, _ = solve_greedy(C_list, weight)
        result_BnB.append(value1)
        result_Greedy.append(value2)
    return result_BnB, result_Greedy


def plot_runtime_results(total_results, W, catalog):
    plt.figure(figsize=(8, 5))
    plt.plot(W, total_results, marker='o', color='red', label='Branch & Bound Median Runtime')
    plt.yscale('linear')
    plt.xlabel('Weight Capacity')
    plt.ylabel('Median Runtime (ms)')
    plt.title(catalog)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_value_results(result_BnB, result_Greedy, W, catalog):
    plt.figure(figsize=(8, 5))
    plt.plot(W, result_BnB, marker='o', color='red', label='Branch & Bound Value')
    plt.plot(W, result_Greedy, marker='x', color='blue', label='Greedy Value')
    plt.yscale('linear')
    plt.xlabel('Weight Capacity')
    plt.ylabel('Value')
    plt.title(catalog)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Testing function
def trials(results: List, attempts: int, catalogue: List[Tuple[str, str, int, int]], W: Tuple) -> List[Tuple[Tuple[int, List], float]]:
    for capacity in W:
        addition = 0
        average = 0
        for attempt in range(attempts):
            start = time.time()
            result = solve_method(catalogue, capacity)
            end = time.time()
            addition += (end - start)
        average = addition / attempts
        results.append([result, average])
    return results

