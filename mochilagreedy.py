from typing import List, Tuple
import time

def solve_method(products: List[Tuple[str, str, int, int]], capacity_W: int) -> (int, List[str]):
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


# DATOS!!

C1 = [
    ("P01","Chips Box",1,6),("P02","Soda Crate",2,11),("P03","Candy Bulk",3,16),
    ("P04","Water Pack",4,21),("P05","Fruit Crate",5,26),("P06","Ice Cream Bin",6,31),
    ("P07","BBQ Sauce Case",7,36),("P08","Snack Variety",8,40),
    ("P09","Cleaning Supplies",9,45),("P10","First-Aid Kits",10,50)
]

C2 = [
    ("Q10","Assorted Gadgets",10,60),("Q20","Party Drinks Pallet",20,100),
    ("Q30","Outdoor Grill",30,120),("Q35","Mini Freezer",35,130),
    ("Q40","Tool Chest",40,135),("Q45","Camp Bundle",45,140),
    ("Q50","Generator",50,150)
]


