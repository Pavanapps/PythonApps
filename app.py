from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# GST Calculator
@app.route("/gst", methods=["POST"])
def gst():
    result = None
    gst_amount = None

    try:
        amount = float(request.form["amount"])
        gst_rate = float(request.form["gst_rate"])
        action = request.form["action"]

        if action == "add":
            gst_amount = amount * gst_rate / 100
            result = amount + gst_amount
        else:
            gst_amount = amount * gst_rate / (100 + gst_rate)
            result = amount - gst_amount

    except Exception as e:
        return f"Error: {str(e)}"

    return render_template("index.html", result=result, gst_amount=gst_amount)


# Test route
@app.route("/search")
def search():
    return "API working"


if __name__ == "__main__":
    app.run(debug=False)