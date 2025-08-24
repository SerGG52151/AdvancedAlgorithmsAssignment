from dp import trials as solve_dp, plotDp
from Backtracking_Mochila import resolver_mochila as solve_backtracking
from mochila_greedy import solve_greedy

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


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. DP Algorithm")
        print("2. Backtracking Algorithm")
        print("3. Greedy Algorithm")
        print("4. Greedy Value Gap vs Capacity")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1': # DP
            resultsC1 = []
            resultsC2 = []
            resultsC1 = solve_dp(resultsC1, 5, C1)
            resultsC2 = solve_dp(resultsC2, 5, C2)

            while True:
                print("\nDP")
                print("1. Graph Runtime vs Capacity")
                print("2. Results")
                print("3. Exit")
                choice = input("Select an option: ")

                if choice == '1':
                    plotDp(resultsC1, resultsC2)
                elif choice == '2':
                    for row, w in zip(resultsC1, W):
                        print('C1: ')
                        print(f"W = {w} | Value / IDs / Time: {row}")

                    print('_____')
                    for row, w in zip(resultsC2, W):
                        print('C2: ')
                        print(f"W = {w} | Value / IDs / Time: {row}")
                    pass
                elif choice == '3':
                    break
                else:
                    print("Invalid option. Please try again.")

            
        elif choice == '2':
            pass
            
        elif choice == '3':
            pass
            
        elif choice == '4':
            pass
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()