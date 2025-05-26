from flask import Flask, render_template
import pandas as pd

# Create Website object instances
app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]


# Connect HTML pages
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# To run the app if only main.py is executed directly
# nd check for any errors in the web page
if __name__ == "__main__":
    app.run(debug=True)
