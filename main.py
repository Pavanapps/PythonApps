from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def gst():
    result = None
    gst_amount = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        gst_rate = float(request.form["gst_rate"])
        action = request.form["action"]

        if action == "add":
            gst_amount = amount * gst_rate / 100
            result = amount + gst_amount
        else:
            gst_amount = amount * gst_rate / (100 + gst_rate)
            result = amount - gst_amount

    return render_template("index.html", result=result, gst_amount=gst_amount)

if __name__ == "__main__":
    app.run()