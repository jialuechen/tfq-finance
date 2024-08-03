import numpy as np

def smart_order_routing(order, venues):
    best_venue = None
    best_price = float('inf')
    
    for venue, price in venues.items():
        if price < best_price:
            best_price = price
            best_venue = venue
            
    return best_venue, best_price

if __name__ == "__main__":
    order = {'quantity': 100, 'type': 'market'}
    venues = {'Venue A': 100.5, 'Venue B': 100.3, 'Venue C': 100.7}

    best_venue, best_price = smart_order_routing(order, venues)
    print(f"Best Venue: {best_venue}")
    print(f"Best Price: {best_price}")