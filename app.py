from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/save", methods=["POST"])
def save_to_excel():
    data = request.json
    approved_pairs = data.get("approvedPairs", [])
    if not approved_pairs:
        return jsonify({"message": "No approved lines to save"}), 400

    df = pd.DataFrame(approved_pairs)
    # Save to Excel without the encoding parameter
    df.to_excel("approved_data.xlsx", index=False, engine="openpyxl")
    return jsonify({"message": "Approved data saved successfully!"})


if __name__ == "__main__":
    app.run(debug=True)
