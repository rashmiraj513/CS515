import threading
import time
from queue import Queue

class FoodOrderingSystem:
    def __init__(self, orders):
        self.order_queue = Queue()
        self.orders = orders

    def place_order(self):
        for order in self.orders:
            self.order_queue.enqueue(order)
            print(f"Placed order: {order}")
            time.sleep(0.5)

    def serve_order(self):
        # Wait for 1 second before starting to serve orders
        time.sleep(1)  
        while not self.order_queue.is_empty():
                order = self.order_queue.front()
                self.order_queue.dequeue()
                print(f"Serving order: {order}")
                time.sleep(2)

if __name__ == "__main__":
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    food_ordering_system = FoodOrderingSystem(orders)

    place_order_thread = threading.Thread(target=food_ordering_system.place_order)
    serve_order_thread = threading.Thread(target=food_ordering_system.serve_order)

    place_order_thread.start()
    serve_order_thread.start()

    place_order_thread.join()
    serve_order_thread.join()