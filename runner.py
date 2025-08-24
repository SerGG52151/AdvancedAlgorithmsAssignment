from dp import trials as solve_dp, plotDp
from mochilagreedy import trials as solve_greedy
from BnB import trials as solve_backtracking
import matplotlib.pyplot as plt
import numpy as np


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


# Calculate Greedy Solution
resultsGC1 = []
resultsGC2 = []
resultsGC1 = solve_greedy(resultsGC1, 5, C1, W)
resultsGC2 = solve_greedy(resultsGC2, 5, C2, W)

# Calculate DP Solution
resultsDPC1 = []
resultsDPC2 = []
resultsDPC1 = solve_dp(resultsDPC1, 5, C1, W)
resultsDPC2 = solve_dp(resultsDPC2, 5, C2, W)

# Calculate Backtracking Solution
resultsBTC1 = []
resultsBTC2 = []
resultsBTC1 = solve_backtracking(resultsBTC1, 5, C1, W)
resultsBTC2 = solve_backtracking(resultsBTC2, 5, C2, W)


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. DP Algorithm")
        print("2. Backtracking Algorithm")
        print("3. Greedy Algorithm")
        print("4. Greedy Value Gap vs Capacity")
        print("5. Runtime vs Capacity")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1': # DP
            while True:
                print("\nDP")
                print("1. Results")
                print("2. Exit")
                choice = input("Select an option: ")

                if choice == '1':
                    for row, w in zip(resultsDPC1, W):
                        print('C1: ')
                        print(f"W = {w}")
                        print(f"Value: {row[0][0]}")
                        print(f"IDs: {row[0][1]}")
                        print(f"Time: {row[1]}")

                    print('_____')
                    for row, w in zip(resultsDPC2, W):
                        print('C2: ')
                        print(f"W = {w}")
                        print(f"Value: {row[0][0]}")
                        print(f"IDs: {row[0][1]}")
                        print(f"Time: {row[1]}")
                elif choice == '2':
                    break
                else:
                    print("Invalid option. Please try again.")

        elif choice == '2':
            while True:
                print("\nBacktracking")
                print("1. Results")
                print("2. Exit")
                choice = input("Select an option: ")

                if choice == '1':
                    for row, w in zip(resultsBTC1, W):
                        print('C1: ')
                        print(f"W = {w}")
                        print(f"Value: {row[0][0]}")
                        print(f"IDs: {row[0][1]}")
                        print(f"Time: {row[1]}")

                    print('_____')
                    for row, w in zip(resultsBTC2, W):
                        print('C2: ')
                        print(f"W = {w}")
                        print(f"Value: {row[0][0]}")
                        print(f"IDs: {row[0][1]}")
                        print(f"Time: {row[1]}")
                elif choice == '2':
                    break
                else: 
                    print("Invalid option. Please try again.")
            
        elif choice == '3':
            while True:
                print("Greedy")
                print("1. Results")
                print("2. Exit")
                choice = input("Select an option: ")

                if choice == '1':
                    for row, w in zip(resultsGC1, W):
                        print('C1: ')
                        print(f"W = {w}")
                        print(f"Value: {row[0][0]}")
                        print(f"IDs: {row[0][1]}")
                        print(f"Time: {row[1]}")

                    print('_____')
                    for row, w in zip(resultsGC2, W):
                        print('C2: ')
                        print(f"W = {w}")
                        print(f"Value: {row[0][0]}")
                        print(f"IDs: {row[0][1]}")
                        print(f"Time: {row[1]}")
                elif choice == '2':
                    break
                else: 
                    print("Invalid option. Please try again.")
            
        elif choice == '4':
            yDPC1 = [row[0][0] for row in resultsDPC1]
            yDPC2 = [row[0][0] for row in resultsDPC2]
            yBTC1 = [row[0][0] for row in resultsBTC1]
            yBTC2 = [row[0][0] for row in resultsBTC2]
            yGC1 = [row[0][0] for row in resultsGC1]
            yGC2 = [row[0][0] for row in resultsGC2]
            
            x = np.arange(len(W))
            width = 0.25

            plt.bar(x - width, yDPC1, width, label='DP', color='blue')
            plt.bar(x,        yBTC1, width, label='BT', color='red')
            plt.bar(x + width, yGC1, width, label='G', color='green')
            plt.xlabel('Capacity')
            plt.ylabel('Value')
            plt.title('C1 Greedy Value Gap vs Capacity')
            plt.xticks(x, W)
            plt.grid()
            plt.legend()
            plt.show()

            plt.bar(x - width, yDPC2, width, label='DP', color='blue')
            plt.bar(x,        yBTC2, width, label='BT', color='red')
            plt.bar(x + width, yGC2, width, label='G', color='green')
            plt.xlabel('Capacity')
            plt.ylabel('Value')
            plt.title('C2 Greedy Value Gap vs Capacity')
            plt.xticks(x, W)
            plt.grid()
            plt.legend()
            plt.show()

        elif choice == '5':
            yDPC1 = [row[1] for row in resultsDPC1]
            yDPC2 = [row[1] for row in resultsDPC2]
            yBTC1 = [row[1] for row in resultsBTC1]
            yBTC2 = [row[1] for row in resultsBTC2]
            yGC1 = [row[1] for row in resultsGC1]
            yGC2 = [row[1] for row in resultsGC2]

            plt.plot(W, yDPC1, label='DP', color='blue', marker='o')
            plt.plot(W, yBTC1, label='BT', color='red', marker='o')
            plt.plot(W, yGC1, label='G', color='green', marker='o')
            plt.xlabel('Capacity')
            plt.ylabel('Runtime')
            plt.title('C1 Runtime vs Capacity')
            plt.grid()
            plt.legend()
            plt.show()

            plt.plot(W, yDPC2, label='DP', color='blue', marker='o')
            plt.plot(W, yBTC2, label='BT', color='red', marker='o')
            plt.plot(W, yGC2, label='G', color='green', marker='o')
            plt.xlabel('Capacity')
            plt.ylabel('Runtime')
            plt.title('C2 Runtime vs Capacity')
            plt.grid()
            plt.legend()
            plt.show()

        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()