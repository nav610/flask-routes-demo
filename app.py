from flask import Flask
from flask import jsonify
from page_two import page_two

app = Flask(__name__)
app.register_blueprint(page_two)

@app.route("/route_one")
def route_one():
    return jsonify({"path": "1"}), 200

@app.route("/route_two", methods=["GET"])
def route_two():
    return jsonify({"path": "2"}), 200


@app.route("/route_three", methods=["POST"])
def route_three():
    return jsonify({"path": "3"}), 200


@app.route("/route_four", methods=["PUT"])
def route_four():
    return jsonify({"path": "4"}), 200


@app.route("/list_routes")
def list_routes():
    routes = []
    for route in app.url_map.iter_rules():
        routes.append({
            "rule": route.rule,
            "endpoint": route.endpoint,
            "methods": list(route.methods),
        })

    return jsonify(routes), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8888)

