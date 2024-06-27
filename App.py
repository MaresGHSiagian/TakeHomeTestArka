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

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
