from typing import List, Tuple

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


#DATOS!!

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

#empieza lo chido
capacities = [0, 15, 50, 100]   
print("Catalog C1:")
for W in capacities:
    val, ids = solve_greedy(C1, W)
    print(f" W={W} -> value={val}, ids={ids}")

print("\nCatalog C2:")
for W in capacities:
    val, ids = solve_greedy(C2, W)
    print(f" W={W} -> value={val}, ids={ids}")


val, ids = solve_greedy(C2, 5)
print("\nCatalog C2 (capacity=5, all too heavy):", val, ids)