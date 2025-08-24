<<<<<<< HEAD
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

def solve_greedy(products: List[Tuple[str, str, int, int]], capacity_W: int) -> (int, List[str]):
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
    organized_product = sorted(products, key=lambda x: x[3]/x[2], reverse=True)
    length = len(organized_product)
    
    best_value = 0
    best_selection = []
    
    def upper_limit(index, leftover_weight, current_value):
        #Define e
        limit = current_value
        for i in range(index, length):
            pid, name, weight, value = organized_product[i]
            if weight <= leftover_weight:
                limit += value
                leftover_weight -= weight
            else: 
                #Esto es "fractionally filling" la capacidad que queda
                limit += value * (leftover_weight/weight)
                break
        return limit
    
    def backtrack(index, leftover_weight, current_value, selected_products):
        nonlocal best_value, best_selection
        
        if index == length:
            if current_value > best_value:
                best_value = current_value
                best_selection = selected_products[:]
            return
        
        ls = upper_limit(index, leftover_weight, current_value)
        if ls <= best_value:
            return
        
        pid, name, weight, value = organized_product[index]
        
        if weight <= leftover_weight:
            selected_products.append(pid)
            backtrack(index+1, leftover_weight - weight, current_value + value, selected_products)
            selected_products.pop()
            
        backtrack(index+1, leftover_weight, current_value, selected_products)        
    
    if capacity_W <= 0 or not products:
        return (0, [])
    
    backtrack(0, capacity_W, 0, [])
    return best_value, best_selection

def benchmarking(C_list, W, trials=5):
    total_results = []
    for weight in W:
        result = []
        for _ in range(trials):
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
    plt.figure(figsize=(8,5))
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
    plt.figure(figsize=(8,5))
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

results_C1 = benchmarking(C1, W)
results_C2 = benchmarking(C2, W)

plot_runtime_results(results_C1, W, "Runtime vs Capacity Catalog 1")
plot_runtime_results(results_C2, W, "Runtime vs Capacity Catalog 2")

result_BnB_C1, result_Greedy_C1 = greedy_benchmarking(C1, W)
result_BnB_C2, result_Greedy_C2  = greedy_benchmarking(C2, W)

plot_value_results(result_BnB_C1, result_Greedy_C1, W, "Value vs Capacity Catalog 1")
plot_value_results(result_BnB_C2, result_Greedy_C2, W, "Value vs Capacity Catalog 2")
=======
from typing import List, Tuple

def solve_method(products: List[Tuple[str, str, int, int]],
                 capacity_W: int) -> Tuple[int, List[str]]:
    
    # Aplica la regla x[3]/x[2] a cada producto en la lista para sacar su ratio valor-peso
    # Luego, los organiza empezando con el producto con el mejor ratio y terminando con el producto con peor ratio
    producto_organizado = sorted(products, key=lambda x: x[3]/x[2], reverse=True)
    longitud = len(producto_organizado)
    
    valor_final = 0
    seleccion_final = []
    
    def limite_superior(index, peso_restante, current_valor):
        limite = current_valor
        for i in range(index, longitud):
            pid, nombre, peso, valor = producto_organizado[i]
            if peso <= peso_restante:
                limite += valor
                peso_restante -= peso
            else: 
                #fractionally "filling" any remaining capacity by density
                limite += valor * (peso_restante/peso)
                break
        return limite
    
    def backtrack(index, peso_restante, current_valor, ids_seleccionados):
        nonlocal valor_final, seleccion_final
        
        if index == longitud:
            if current_valor > valor_final:
                valor_final = current_valor
                seleccion_final = ids_seleccionados[:]
            return
        
        ls = limite_superior(index, peso_restante, current_valor)
        if ls <= valor_final:
            return
        
        pid, nombre, peso, valor = producto_organizado[index]
        
        if peso <= peso_restante:
            ids_seleccionados.append(pid)
            backtrack(index+1, peso_restante - peso, current_valor + valor, ids_seleccionados)
            ids_seleccionados.pop()
            
        backtrack(index+1, peso_restante, current_valor, ids_seleccionados)        
    
    if capacity_W <= 0 or not products:
        return (0, [])
    
    backtrack(0, capacity_W, 0, [])
    return (valor_final, seleccion_final)

W = (0, 5, 20, 35, 50, 65, 80, 95, 110, 140)
        
C1 = [("P01","Chips Box",1,6),("P02","Soda Crate",2,11),("P03","Candy Bulk",3,16),
 ("P04","Water Pack",4,21),("P05","Fruit Crate",5,26),("P06","Ice Cream Bin",6,31),
 ("P07","BBQ Sauce Case",7,36),("P08","Snack Variety",8,40),
 ("P09","Cleaning Supplies",9,45),("P10","First-Aid Kits",10,50)]

C2 = [("Q10","Assorted Gadgets",10,60),("Q20","Party Drinks Pallet",20,100),
 ("Q30","Outdoor Grill",30,120),("Q35","Mini Freezer",35,130),
 ("Q40","Tool Chest",40,135),("Q45","Camp Bundle",45,140),
 ("Q50","Generator",50,150)]

valor, lista_productos = solve_method(C1, W[3])
print("Mejor valor:", valor)
print("Productos seleccionados: ", lista_productos)
>>>>>>> 53b134eeeb4dfbd6fa391fbcf7f6ce6d11609832
