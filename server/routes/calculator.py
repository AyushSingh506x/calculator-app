from flask import Blueprint, request, jsonify
from utils.calculator_engine import evaluate_expression

calculator_bp = Blueprint(
    "calculator",
    __name__
)

@calculator_bp.route("/calculate", methods=["POST"])
def calculate():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "No JSON data provided"
        }), 400

    expression = data.get("expression")

    if not expression:
        return jsonify({
            "success": False,
            "error": "Expression is required"
        }), 400

    result = evaluate_expression(expression)

    return jsonify(result)