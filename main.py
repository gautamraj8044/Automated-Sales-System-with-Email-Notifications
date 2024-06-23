# main.py
import requests
from database import create_connection, insert_order

def fetch_data_from_api():
    """Fetch data from API"""
    url = "http://127.0.0.1:5000/orders"  # Replace with actual API endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["orders"]
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

def main():
    conn = create_connection()
    
    if conn is not None:
        api_data = fetch_data_from_api()
        if api_data:
            for order in api_data:
                data = {
                    "customer_name": order['customer_name'],
                    "restaurant_id": order['restaurant_id'],
                    "order_date": order['order_date'],  # Ensure correct format
                    "quantity": order['quantity'],
                    "amount": order['amount'],
                    "payment_mode": order['payment_mode'],
                    "delivery_time": order['delivery_time'],  # Ensure correct format
                    "customer_rating_food": order['customer_rating_food'],
                    "customer_rating_delivery": order['customer_rating_delivery'],
                    "email": order['email'],
                    "status": order.get('status', 'pending')
                }
                insert_order(conn, data)
        
        conn.close()

if __name__ == "__main__":
    main()
