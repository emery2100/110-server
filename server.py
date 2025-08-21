from flask import Flask 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello World, Ch59!</p>"

@app.route("/cohort59")
def hi():
    return "<h1>Hello Cohort 59!</h1>"

@app.get("/home")
def home():
    print("Home endpoint accessed")
    return "Welcome to the Home Page!"

@app.get("/api/students")
def students():
    print("Students endpoint accessed")
    student_names = ["Britney", "Tatiana", "Alexander", "James", "Ray", "Britney", "David","Maryna", "Yaquelin"]
    return student_names

# Path Parameter
@app.get("/greet/<string:name>")
def greet(name):
    return f"Hello, {name}!"

@app.get("/contact")
def contact_api():
    print("Contact endpoint accessed")
    user = {"name": "Peter", "age": 35,}
    return user

@app.get("/api/products")
def products():
    print("Products endpoint accessed")
    product_list = ["Laptop", "Smartphone", "Tablet", "Headphones"]
    return product_list

@app.get("/api/products/count")
def products_count():
    print("Products count endpoint accessed")
    product_list = ["Laptop", "Smartphone", "Tablet", "Headphones"]
    return {"count": len(product_list)}


app.run(debug=True)