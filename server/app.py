from flask import Flask
from routes.calculator import calculator_bp

app = Flask(__name__)

# Register calculator routes
app.register_blueprint(calculator_bp)

@app.route("/")
def home():
    return {
        "message": "Smart Calculator Backend Running",
        "status": "success"
    }

if __name__ == "__main__":
    app.run(debug=True)