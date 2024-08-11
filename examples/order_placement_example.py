from tfq_finance.execution.order_placement import place_order

def order_placement_example():
    order_details = {'symbol': 'AAPL', 'quantity': 100, 'order_type': 'market'}

    order_confirmation = place_order(order_details)
    print("Order Confirmation:", order_confirmation)

if __name__ == "__main__":
    order_placement_example()