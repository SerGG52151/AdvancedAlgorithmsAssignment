# DP Method - Sergio
from typing import List, Tuple
import matplotlib.pyplot as plt, time

# Global variables
W = (0, 5, 20, 35, 50, 65, 80, 95, 110, 140)

C1 = [("P01","Chips Box",1,6),("P02","Soda Crate",2,11),("P03","Candy Bulk",3,16),
 ("P04","Water Pack",4,21),("P05","Fruit Crate",5,26),("P06","Ice Cream Bin",6,31),
 ("P07","BBQ Sauce Case",7,36),("P08","Snack Variety",8,40),
 ("P09","Cleaning Supplies",9,45),("P10","First-Aid Kits",10,50)]

C2 = [("Q10","Assorted Gadgets",10,60),("Q20","Party Drinks Pallet",20,100),
 ("Q30","Outdoor Grill",30,120),("Q35","Mini Freezer",35,130),
 ("Q40","Tool Chest",40,135),("Q45","Camp Bundle",45,140),
 ("Q50","Generator",50,150)]

# Bottom-up (two-dimensional table / tabulation) DP solution
# Time complexity: O(n * W)
# Space complexity: O(n * W)
def solve_method(products: List[Tuple[str, str, int, int]], capacity_W: int) -> Tuple[int, List[str]]: 
    n = len(products)
    dp = [[[0, []] for _ in range(capacity_W + 1)] for _ in range(n + 1)]
    chosenIds = []
    
    for i in range(n + 1):
        for j in range(capacity_W + 1):

            if i == 0 or j == 0:
                dp[i][j][0] = 0
            else:
                pick = 0

                if products[i - 1][2] <= j:
                    pick = products[i - 1][3] + dp[i - 1][j - (products[i - 1][2])][0]

                notPick = dp[i - 1][j][0]

                dp[i][j][0] = max(pick, notPick)

                if products[i - 1][2] <= j and dp[i][j][0] == pick: 
                    dp[i][j][1] = dp[i - 1][j - (products[i - 1][2])][1].copy()
                    dp[i][j][1].append(products[i - 1][0])
                else:
                    dp[i][j][1] = dp[i - 1][j][1].copy()

    return dp[n][capacity_W]

# Testing function
def trials(results: List, attempts: int, catalogue: List[Tuple[str, str, int, int]]) -> List[Tuple[Tuple[int, List], float]]:
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

def plotDp(resultsC1: List, resultsC2: List):

    yC1 = [row[1] for row in resultsC1]
    yC2 = [row[1] for row in resultsC2]

    plt.plot(W, yC1, label='C1', color='blue', marker='o')
    plt.plot(W, yC2, label='C2', color='red', marker='o')
    plt.xlabel('Capacity')
    plt.ylabel('Runtime')
    plt.title('Runtime vs Capacity')
    plt.grid()
    plt.legend()
    plt.show()

    

if __name__ == "__main__":
    resultsC1 = []
    resultsC2 = []

    resultsC1 = trials(resultsC1, 5, C1)
    resultsC2 = trials(resultsC2, 5, C2)

    yC1 = [row[1] for row in resultsC1]
    yC2 = [row[1] for row in resultsC2]

    
    plt.plot(W, yC1, label='C1', color='blue', marker='o')
    plt.plot(W, yC2, label='C2', color='red', marker='o')
    plt.xlabel('Capacity')
    plt.ylabel('Runtime')
    plt.title('Runtime vs Capacity')
    plt.grid()
    plt.legend()
    plt.show()
    

    for row, w in zip(resultsC1, W):
        print(f"W = {w} | Value / IDs / Time: {row}")

    for row, w in zip(resultsC2, w):
        print(f"W = {w} | Value / IDs / Time: {row}")

