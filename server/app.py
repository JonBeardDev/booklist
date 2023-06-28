from flask import Flask, jsonify, request
from flask_cors import CORS

BOOKS = [
    {
        "title": "On the Road", 
        "author": "Jack Kerouac",
        "date": "1957",
        "read": True
    },
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "date": "1997",
        "read": False,
    },
    {
        "title": "Green Eggs and Ham", 
        "author": "Dr. Seuss",
        "date": "1960",
        "read": True
    },
]

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# Sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


# Books route
@app.route("/books", methods=["GET", "POST"])
def all_books():
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        BOOKS.append(
            {
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "date": post_data.get("date"),
                "read": post_data.get("read"),
            }
        )
        response_object["message"] = "Book added!"
    else:
        response_object["books"] = BOOKS
    return jsonify(response_object)


if __name__ == "__main__":
    app.run()
