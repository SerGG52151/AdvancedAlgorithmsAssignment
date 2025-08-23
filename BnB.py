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