
from datetime import date
from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory storage
egg_records = []


@app.route("/api/eggs", methods=["POST"])
def log_eggs():
    """Record daily egg production for a poultry shed."""

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "A valid JSON request is required."}), 400

    shed = data.get("shed")
    production_date = data.get("date")
    count = data.get("count")

    # Validate shed name
    if not isinstance(shed, str) or not shed.strip():
        return jsonify({"error": "Shed name is required."}), 400

    # Validate date
    try:
        date.fromisoformat(production_date)
    except (ValueError, TypeError):
        return jsonify({
            "error": "Invalid date. Use YYYY-MM-DD format."
        }), 400

    # Validate egg count
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        return jsonify({
            "error": "Egg count must be a non-negative integer."
        }), 400

    # Create and store production record
    record = {
        "id": len(egg_records) + 1,
        "shed": shed.strip(),
        "date": production_date,
        "count": count
    }

    egg_records.append(record)

    running_total = sum(item["count"] for item in egg_records)

    return jsonify({
        "message": "Egg production recorded successfully.",
        "record": record,
        "running_total": running_total
    }), 201


@app.route("/api/eggs", methods=["GET"])
def get_eggs():
    """Retrieve all egg production records and calculate totals."""

    running_total = 0
    records_with_totals = []
    shed_totals = {}

    for record in egg_records:
        running_total += record["count"]

        shed = record["shed"]
        shed_totals[shed] = shed_totals.get(shed, 0) + record["count"]

        records_with_totals.append({
            **record,
            "running_total": running_total
        })

    return jsonify({
        "total_records": len(egg_records),
        "total_eggs": running_total,
        "shed_totals": shed_totals,
        "records": records_with_totals
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
