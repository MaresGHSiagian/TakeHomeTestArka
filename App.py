from flask import Flask, jsonify
import mysql.connector

# Initialize Flask application
app = Flask(__name__)

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mares30",
    database="company"
)

# Create cursor object
cursor = mydb.cursor()

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mares30",
    database="company"
)

# Create cursor object
cursor = mydb.cursor()

# Function to remove duplicates from a list while preserving order
def remove_duplicates(input_list):
    seen = set()
    unique_list = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list

# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        # Execute SQL query to retrieve all products
        cursor.execute("SELECT * FROM Products")
        
        # Fetch all products
        products = cursor.fetchall()

        # Convert products to JSON format
        products_json = []
        seen_product_names = set()  # To track seen product names
        for product in products:
            product_id = product[0]
            product_name = product[1]
            description = product[2]
            price = float(product[3])  # Convert DECIMAL to float
            
            # Only add to JSON if product_name not seen before
            if product_name not in seen_product_names:
                product_data = {
                    'product_id': product_id,
                    'product_name': product_name,
                    'description': description,
                    'price': price
                }
                products_json.append(product_data)
                seen_product_names.add(product_name)

        return jsonify(products_json)

    except mysql.connector.Error as err:
        return jsonify({'error': f"Database error: {err}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)


# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        # Execute SQL query to retrieve all products
        cursor.execute("SELECT * FROM Products")
        
        # Fetch all products
        products = cursor.fetchall()

        # Convert products to JSON format
        products_json = []
        for product in products:
            product_data = {
                'product_id': product[0],
                'product_name': product[1],
                'description': product[2],
                'price': float(product[3])  # Convert DECIMAL to float
            }
            products_json.append(product_data)

        return jsonify(products_json)

    except mysql.connector.Error as err:
        return jsonify({'error': f"Database error: {err}"}), 500

# API endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        # Execute SQL query to retrieve all users
        cursor.execute("SELECT * FROM Users")
        
        # Fetch all users
        users = cursor.fetchall()

        # Convert users to JSON format
        users_json = []
        for user in users:
            user_data = {
                'user_id': user[0],
                'name': user[1],
                'email': user[2],
                # You might not want to return the password in a real API
                'password': user[3]
            }
            users_json.append(user_data)

        return jsonify(users_json)

    except mysql.connector.Error as err:
        return jsonify({'error': f"Database error: {err}"}), 500

# API endpoint to get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    try:
        # Execute SQL query to retrieve all clients
        cursor.execute("SELECT * FROM Clients")
        
        # Fetch all clients
        clients = cursor.fetchall()

        # Convert clients to JSON format
        clients_json = []
        for client in clients:
            client_data = {
                'service_id': client[0],
                'user_id': client[1],
                'start_date': client[2].isoformat(),  # Convert DATE to ISO format
                'contract_value': float(client[3])  # Convert DECIMAL to float
            }
            clients_json.append(client_data)

        return jsonify(clients_json)

    except mysql.connector.Error as err:
        return jsonify({'error': f"Database error: {err}"}), 500

# Run the Flask application
if __name__ == '__main__':
    # Delete duplicates from Products table before starting Flask app
    delete_duplicates() # type: ignore
    
    # Run Flask app
    app.run(debug=True)
