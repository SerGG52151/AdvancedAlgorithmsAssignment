from typing import List, Tuple

def solve_method(products: List[Tuple[str, str, int, int]],
                 capacity_W: int) -> Tuple[int, List[str]]:
    
    # Aplica la regla x[3]/x[2] a cada producto en la lista para sacar su ratio value-weight
    # Luego, los organiza empezando con el producto con el mejor ratio y terminando con el producto con peor ratio
    organized_product = sorted(products, key=lambda x: x[3]/x[2], reverse=True)
    length = len(organized_product)
    
    best_value = 0
    best_selection = []
    
    def upper_limit(index, leftover_weight, current_value):
        limit = current_value
        for i in range(index, length):
            pid, name, weight, value = organized_product[i]
            if weight <= leftover_weight:
                limit += value
                leftover_weight -= weight
            else: 
                #fractionally "filling" any remaining capacity by density
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

W = (0, 5, 20, 35, 50, 65, 80, 95, 110, 140)
        
C1 = [("P01","Chips Box",1,6),("P02","Soda Crate",2,11),("P03","Candy Bulk",3,16),
 ("P04","Water Pack",4,21),("P05","Fruit Crate",5,26),("P06","Ice Cream Bin",6,31),
 ("P07","BBQ Sauce Case",7,36),("P08","Snack Variety",8,40),
 ("P09","Cleaning Supplies",9,45),("P10","First-Aid Kits",10,50)]

C2 = [("Q10","Assorted Gadgets",10,60),("Q20","Party Drinks Pallet",20,100),
 ("Q30","Outdoor Grill",30,120),("Q35","Mini Freezer",35,130),
 ("Q40","Tool Chest",40,135),("Q45","Camp Bundle",45,140),
 ("Q50","Generator",50,150)]

value, product_list = solve_method(C1, W[3])
print("Mejor value:", value)
print("Productos seleccionados: ", product_list)