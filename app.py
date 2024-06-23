from flask import Flask, request, jsonify
import mysql.connector
from database import create_connection, insert_order
from datetime import datetime  # Import datetime module

app = Flask(__name__)

# Database connection
conn = create_connection()

@app.route("/")
def home():
    return "Welcome to Sales Data Automation API"

@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM orderDetails")
            rows = cursor.fetchall()

            orders_list = []
            for row in rows:
                order = {
                    "order_id": row[0],
                    "customer_name": row[1],
                    "restaurant_id": row[2],
                    "order_date": row[3].strftime('%Y-%m-%d %H:%M:%S') if isinstance(row[3], datetime) else str(row[3]),
                    "quantity": row[4],
                    "amount": row[5],
                    "payment_mode": row[6],
                    "delivery_time": row[7].strftime('%Y-%m-%d %H:%M:%S') if isinstance(row[7], datetime) else str(row[7]),
                    "customer_rating_food": row[8],
                    "customer_rating_delivery": row[9],
                    "email":row[10],
                    "status": row[11]
                }
                orders_list.append(order)

            return jsonify({"orders": orders_list})
        except mysql.connector.Error as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == "POST":
        try:
            # Extract form data using request.form
            customer_name = request.form.get("customer_name")
            restaurant_id = int(request.form.get("restaurant_id"))
            order_date = request.form.get("order_date")
            quantity = int(request.form.get("quantity"))
            amount = float(request.form.get("amount"))
            payment_mode = request.form.get("payment_mode")
            delivery_time = request.form.get("delivery_time")
            customer_rating_food = int(request.form.get("customer_rating_food"))
            customer_rating_delivery = int(request.form.get("customer_rating_delivery"))
            email= request.form.get("email")
            status = request.form.get("status", "pending")  # Default status to 'pending' if not provided

            # Validate required fields
            if not all([customer_name, order_date, payment_mode, delivery_time]):
                return jsonify({"error": "Missing required fields"}), 400

            # Insert order into database
            data = {
                "customer_name": customer_name,
                "restaurant_id": restaurant_id,
                "order_date": order_date,
                "quantity": quantity,
                "amount": amount,
                "payment_mode": payment_mode,
                "delivery_time": delivery_time,
                "customer_rating_food": customer_rating_food,
                "customer_rating_delivery": customer_rating_delivery,
                "email":email,
                "status": status
            }

            insert_order(conn, data)
            return jsonify({"message": "Order added successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
