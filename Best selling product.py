import pandas as pd

# Prompt the user for the file name
file_name = input()

try:
    # Load the data from the CSV file
    df = pd.read_csv(file_name)

    # Group the data by 'Product' and sum the 'Quantity' for each
    # This creates a Series where index is Product and values are total quantities
    product_totals = df.groupby('Product')['Quantity'].sum()

    # Find the product name with the highest total quantity sold
    best_product = product_totals.idxmax()

    # Get the actual maximum quantity value

    highest_quantity = product_totals.max()

    # Display the result in the exact format required by the test cases
    print(f"Best selling product: {best_product}")
    print(f"Total quantity sold: {highest_quantity}")

except Exception as e:
    # Handle cases where the file might not exist or is corrupted
    pass
	
