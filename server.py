from flask import Flask, request

app = Flask(__name__)

#http://127.0.0.1:5000/ 
@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello World, Ch59!</p>"

#http://127.0.0.1:5000/cohort59
@app.route("/cohort59")
def hi():
    return "<h1>Hello Cohort 59!</h1>"

#http://127.0.0.1:5000/home
@app.get("/home")
def home():
    print("Home endpoint accessed")
    return "Welcome to the Home Page!"

#http://127.0.0.1:5000/api/students
@app.get("/api/students")
def students():
    print("Students endpoint accessed")
    student_names = ["Britney", "Tatiana", "Alexander", "James", "Ray", "Britney", "David","Maryna", "Yaquelin"]
    return student_names

# Path Parameter
#http://127.0.0.1:5000/greet/<name>
@app.get("/greet/<string:name>")
def greet(name):
    return f"Hello, {name}!"

#http://127.0.0.1:5000/contact
@app.get("/contact")
def contact_api():
    print("Contact endpoint accessed")
    user = {"name": "Peter", "age": 35,}
    return user

#http://127.0.0.1:5000/about
@app.get("/about")
def about_api():
    print("About endpoint accessed")
    info = {"version": "1.0"}
    return info

#http://127.0.0.1:5000/api/products
@app.get("/api/products")
def products():
    print("Products endpoint accessed")
    product_list = ["Laptop", "Smartphone", "Tablet", "Headphones"]
    return product_list

#http://127.0.0.1:5000/api/products/count
@app.get("/api/products/count")
def products_count():
    print("Products count endpoint accessed")
    product_list = ["Laptop", "Smartphone", "Tablet", "Headphones"]
    return {"count": len(product_list)}


students = [
    {"id": 1, "name": "Bruce", "age": 54, "email": "batman@gmail.com"},
    {"id": 2, "name": "Clark", "age": 29, "email": "superman@gmail.com"},
]

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def add_student():
    data = request.json
    students.append(data)
    return "Student added"

products = [
    {"id": 1, "title": "Laptop", "category": "Electronics", "price": 899.99},
    {"id": 2, "title": "Headphones", "category": "Electronics", "price": 199.99},
    {"id": 3, "title": "Coffee Mug", "category": "Kitchen", "price": 12.50},
    {"id": 4, "title": "Notebook", "category": "Stationary", "price": 5.99},
]

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def save_product():
    data = request.json
    products.append(data)
    return "Product added", 201

@app.get("/products/<category>")
def get_products_by_category(category):
    filtered_products = [product for product in products if product["category"] == category]
    return filtered_products

@app.get("/products/price/<float:price>")
def get_products_by_price(price):
    filtered_products = [product for product in products if product["price"] == price]
    return filtered_products

@app.get("/products/title/<string:title>")
def get_products_by_title(title):
    filtered_products = [product for product in products if product["title"] == title]
    return filtered_products

coupons = [
    {"id": 1, "code": "save10", "discount": 0.10},
    {"id": 2, "code": "save50", "discount": 0.50},
]
@app.get("/coupons")
def get_coupons():
    return coupons

@app.post("/coupons")
def save_coupons():
    data = request.json
    coupons.append(data)
    return "Coupon added"


@app.get("/searchcoupons/<string:code>")
def search_coupons(code):
    filtered_coupons = [coupons for coupons in coupons if coupons["code"] == code]
    return filtered_coupons

app.run(debug=True)
#app.run(port=5001)  # Run on a different port if needed