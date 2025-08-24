from typing import List, Tuple
import time


def resolver_mochila(productos: List[Tuple[str, str, int, int]], 
                     capacidad: int) -> Tuple[int, List[str]]:
    # Acomodamos los productos de acuerdo a su valor/peso
    # Si hay empate, se prefiere el más ligero y después el id
    productos_acomodados = sorted(
        productos, 
        key=lambda x: (x[3]/x[2], -x[2], x[0]), 
        reverse=True
    )

    n = len(productos_acomodados)   
    valor_maximo = 0                
    productos_elegidos: List[str] = []  

    # Esta función calcula una "cota superior" (límite) de lo mejor que se podría conseguir
    # aunque sea llenando la mochila con fracciones de productos.
    def calcular_cota(indice: int, peso_actual: int, valor_actual: int) -> float:
        if peso_actual >= capacidad:
            return 0
        valor_total = valor_actual
        peso_total = peso_actual
        for j in range(indice, n):
            idp, nombre, peso, valor = productos_acomodados[j]
            if peso_total + peso <= capacidad:
                peso_total += peso
                valor_total += valor
            else:
                # Si ya no cabe completo, agregamos solo una fracción
                valor_total += valor * (capacidad - peso_total) / peso
                break
        return valor_total

    # Esta función hace el backtracking: prueba incluir o no cada producto
    def backtracking(indice: int, peso_actual: int, valor_actual: int, elegidos: List[str]):
        nonlocal valor_maximo, productos_elegidos

        # Caso base: ya revisamos todos los productos
        if indice == n:
            # Si el valor que conseguimos es mejor, lo guardamos
            if valor_actual > valor_maximo:
                valor_maximo = valor_actual
                productos_elegidos = elegidos[:]
            return

        # Si ni con la mejor cota posible podemos superar lo que ya tenemos, cortamos aquí
        if calcular_cota(indice, peso_actual, valor_actual) <= valor_maximo:
            return

        idp, nombre, peso, valor = productos_acomodados[indice]

        # Opción 1: intentamos meter este producto (si cabe en la mochila)
        if peso_actual + peso <= capacidad:
            elegidos.append(idp)  # lo agregamos
            backtracking(indice + 1, peso_actual + peso, valor_actual + valor, elegidos)
            elegidos.pop()        # quitamos el producto (backtrack)

        # Opción 2: no metemos este producto
        backtracking(indice + 1, peso_actual, valor_actual, elegidos)

    # Aquí arranca el proceso con mochila vacía
    backtracking(0, 0, 0, [])

    # Al final regresamos el mejor valor y la lista de productos elegidos
    return valor_maximo, productos_elegidos

start_time = time.time()


C1 = [("P01","Chips Box",1,6),("P02","Soda Crate",2,11),("P03","Candy Bulk",3,16),
    ("P04","Water Pack",4,21),("P05","Fruit Crate",5,26),("P06","Ice Cream Bin",6,31),
    ("P07","BBQ Sauce Case",7,36),("P08","Snack Variety",8,40),
    ("P09","Cleaning Supplies",9,45),("P10","First-Aid Kits",10,50)]

C2 = [("Q10","Assorted Gadgets",10,60),("Q20","Party Drinks Pallet",20,100),
    ("Q30","Outdoor Grill",30,120),("Q35","Mini Freezer",35,130),
    ("Q40","Tool Chest",40,135),("Q45","Camp Bundle",45,140),
    ("Q50","Generator",50,150)]

    
# Caso sencillo
caso = C2
capacidad_carga = 10

val, items = resolver_mochila(caso, capacidad_carga)
print("Capacidad 10, Catálogo C1 ->", val, items)

print("--- %s seconds ---" % (time.time() - start_time))



