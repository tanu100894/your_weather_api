from flask import Flask, render_template
import pandas as pd

# Create Website object instances
app = Flask(__name__)

# Connect HTML pages
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}

# To run the app if only main.py is executed directly
# nd check for any errors in the web page
if __name__ == "__main__":
    app.run(debug=True)