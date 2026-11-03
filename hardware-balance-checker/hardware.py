from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# Sample customer balances (replace these with the shop's real records).
CUSTOMERS = {
    "John Kamau": 12500.00,
    "Mary Wanjiku": 8500.00,
    "Peter Otieno": 15000.00,
    "Grace Chebet": 6200.00,
    "David Mwangi": 9500.00,
}

HOME_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Eldoret Hardware | Credit Balance Checker</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f8; margin: 0;
               min-height: 100vh; display: grid; place-items: center; }
        main { background: white; width: min(90%, 460px); padding: 30px;
               border-radius: 12px; box-shadow: 0 5px 20px #0001; }
        h1 { color: #173b57; margin-top: 0; }
        p { color: #52616b; }
        form { display: flex; gap: 8px; }
        input { flex: 1; min-width: 0; padding: 12px; border: 1px solid #ccd4da;
                border-radius: 6px; font-size: 16px; }
        button { padding: 12px 16px; border: 0; border-radius: 6px;
                 background: #176b4d; color: white; cursor: pointer; }
        #result { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
<main>
    <h1>Eldoret Hardware</h1>
    <p>Customer Credit Balance Checker</p>
    <form id="search-form">
        <input id="customer-name" type="text" placeholder="Enter customer name"
               aria-label="Customer name" required>
        <button type="submit">Search</button>
    </form>
    <p id="result" aria-live="polite"></p>
</main>
<script>
document.getElementById("search-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const name = document.getElementById("customer-name").value.trim();
    const result = document.getElementById("result");
    result.textContent = "Searching...";
    try {
        const response = await fetch(`/api/balance?name=${encodeURIComponent(name)}`);
        const data = await response.json();
        if (!response.ok) {
            result.textContent = data.error;
            return;
        }
        result.textContent = `${data.customer} owes KES ${data.balance.toLocaleString("en-KE", {
            minimumFractionDigits: 2, maximumFractionDigits: 2
        })}.`;
    } catch (error) {
        result.textContent = "Could not reach the server. Please try again.";
    }
});
</script>
</body>
</html>
"""


@app.route("/")
def home():
    """Display the customer balance search page."""
    return render_template_string(HOME_PAGE)


@app.route("/api/balance")
def get_balance():
    """Return one customer's outstanding balance as JSON."""
    name = request.args.get("name", "").strip()

    if not name:
        return jsonify({"error": "Please provide a customer name."}), 400

    # Case-insensitive lookup while preserving the stored display name.
    customer = next(
        (stored_name for stored_name in CUSTOMERS if stored_name.casefold() == name.casefold()),
        None,
    )

    if customer is None:
        return jsonify({"error": "Customer not found."}), 404

    return jsonify({
        "customer": customer,
        "balance": CUSTOMERS[customer],
        "currency": "KES",
    })


if __name__ == "__main__":
    app.run(debug=True)
