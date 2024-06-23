import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(customer_name, customer_email, order_id, order_total, delivery_time):
    """Send purchase confirmation email"""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "gautam.raj4595@gmail.com"
    smtp_password = "taer umkt psfw mpgu"

    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = customer_email
    msg["Subject"] = "Purchase Confirmation"

    body = f"""Dear {customer_name},

Thank you for your purchase. Your order (ID: {order_id}) of ₹{order_total:.2f} has been confirmed.
Expected delivery time: {delivery_time}

Sincerely,
Your Name
"""

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, customer_email, msg.as_string())
        server.quit()
        print(
            f"Purchase confirmation email sent to {customer_email} for order {order_id}."
        )
    except Exception as e:
        print(f"Error sending email: {e}")
