from flask import Blueprint, jsonify

page_two = Blueprint('page_two', import_name=__name__, url_prefix="/prefix")

@page_two.route("/route_five",  methods=["GET"])
def route_five():
    return jsonify({"path": "5"}), 200