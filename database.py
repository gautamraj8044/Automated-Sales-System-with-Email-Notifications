# database.py
import mysql.connector
from email_fun import send_email  # Import the send_email function

def create_connection():
    """Create a connection to MySQL database"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mysql@2002",
            database="order"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def insert_order(conn, data):
    """Insert a new order into orderDetails table and send confirmation email"""
    try:
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO orderDetails 
            (customer_name, restaurant_id, order_date, quantity, amount, payment_mode, delivery_time, 
             customer_rating_food, customer_rating_delivery, email, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            data['customer_name'], data['restaurant_id'], data['order_date'], data['quantity'],
            data['amount'], data['payment_mode'], data['delivery_time'],
            data['customer_rating_food'], data['customer_rating_delivery'], data['email'], 'pending'
        ))
        conn.commit()
        print(f"Inserted order successfully with ID: {cursor.lastrowid}")

        # After successful insert, send confirmation email
        send_email(
            customer_name=data['customer_name'],
            customer_email=data['email'],
            order_id=cursor.lastrowid,  # Use last inserted ID as order ID
            order_total=data['amount'],
            delivery_time=data['delivery_time']
        )
    except mysql.connector.Error as e:
        print(f"Error inserting order: {e}")
    except Exception as e:
        print(f"Error sending email: {e}")
