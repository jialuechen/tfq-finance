import numpy as np

def place_order(order_type, quantity, price):
    if order_type == 'market':
        execution_price = price
    elif order_type == 'limit':
        execution_price = price  # For simplicity, assume limit orders are executed at the limit price
    else:
        raise ValueError("Invalid order type. Choose 'market' or 'limit'.")
    return execution_price, quantity

if __name__ == "__main__":
    order_type = 'market'
    quantity = 100
    price = 50.0

    execution_price, executed_quantity = place_order(order_type, quantity, price)
    print(f"Order Type: {order_type}")
    print(f"Execution Price: {execution_price}")
    print(f"Executed Quantity: {executed_quantity}")