print(" \t🔶 WELCOME TO TASK 2 : STOCK TOTAL INVESTMENT 🔶 \n")

print("RULE : ENTER THE PRICE FOR EACH PRODUCT OF THE STOCK AND THE QUANTITY OF EACH PRODUCT TO CALCULATE THE TOTAL INVESTMENT OR USE PREDEFINED PRODUCTS\n")

def stock_investment():
    products = {}
    predefined_products = {
        "Product A": {"price": 10.0, "quantity": 5},
        "Product B": {"price": 15.0, "quantity": 3},
        "Product C": {"price": 20.0, "quantity": 2}
    }
    answer = input("DO YOU WANT TO USE PREDEFINED PRODUCTS? (Y/N): ").lower().strip()
    if answer == 'y':
        products = predefined_products
        total_investment = sum(item["price"] * item["quantity"] for item in products.values())
        print(f"\nTOTAL INVESTMENT FOR PREDEFINED PRODUCTS: ${total_investment:.2f}\n")
    else:
        while True:
            product_name = input("ENTER PRODUCT NAME (or type 1 to finish): ").strip()
            if product_name == '1':
                break
            try:
                price = float(input(f"ENTER PRICE FOR {product_name}: ").strip())
                quantity = int(input(f"ENTER QUANTITY FOR {product_name}: ").strip())
                products[product_name] = {"price": price, "quantity": quantity}
            except ValueError:
                print("INVALID INPUT! PLEASE ENTER A VALID NUMBER FOR PRICE AND QUANTITY.")
                continue

        total_investment = sum(item["price"] * item["quantity"] for item in products.values())
        print(f"\nTOTAL INVESTMENT FOR ENTERED PRODUCTS: ${total_investment:.2f}\n")

        with open("stock_investment.txt", "w") as file:
            file.write("STOCK INVESTMENT DETAILS\n")
            file.write("------------------------\n")
            file.write(f" TOTAL PRODUCTS : {len(products)}\n")
            file.write(f" TOTAL INVESTMENT: ${total_investment:.2f}\n")

        replay = input("DO YOU WANT TO CALCULATE AGAIN? (Y/N): ").lower().strip()
        if replay == 'y':
            stock_investment()

        else:
            print("THANK YOU FOR USING THE STOCK INVESTMENT CALCULATOR! GOODBYE!\n")


        