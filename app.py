from flask import Flask, render_template

app = Flask(__name__)

menu_items = [
    {
        "name": "Grilled Salmon",
        "desc": "Fresh Atlantic salmon with herbs and lemon.",
        "price": "$18.99",
        "image": "food.jpg"
    },
    {
        "name": "Pasta Primavera",
        "desc": "Seasonal vegetables in olive oil sauce.",
        "price": "$14.99",
        "image": "pizza.jpg"
    },
    {
        "name": "Chocolate Lava Cake",
        "desc": "Warm cake with molten chocolate center.",
        "price": "$8.99",
        "image": "burger.jpg"
    }
]

@app.route("/")
def home():
    return render_template("index.html", menu=menu_items)

if __name__ == "__main__":
    app.run(debug=True)

