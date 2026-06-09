from sympy import sympify
from sympy.core.sympify import SympifyError


def evaluate_expression(expression):

    try:
        # Allow users to type 2^10 instead of 2**10
        expression = expression.replace("^", "**")

        result = sympify(expression)

        return {
            "success": True,
            "expression": expression,
            "result": float(result)
        }

    except SympifyError:
        return {
            "success": False,
            "error": "Invalid expression"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }