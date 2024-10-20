from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/rules", methods=["GET"])
def get_rules():
    # Return a list of rules
    return jsonify([{"id": 1, "name": "Rule 1"}])

if __name__ == "__main__":
    app.run(debug=True)