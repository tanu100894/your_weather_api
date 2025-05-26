# 🌦️ Your Weather API

A RESTful Flask-based API that provides historical weather data (mean daily temperatures) for European climate stations. This project reads from pre-downloaded CSV files and delivers weather data for a specific station and date, the full station history, or yearly data.

---

## 🚀 Features

- 🔎 Query temperature by station and date
- 📆 Retrieve full historical records per station
- 📅 Fetch all temperature records for a given station and year
- 🖥️ View station metadata via the browser

---

## 🗂️ Project Structure

```text
your-weather-api/
│
├── data_small/
│ ├── stations.txt # Metadata for all climate stations
│ └── TG_STAIDxxxxx.txt # Daily temperature data for each station
│
├── templates/
│ └── home.html # HTML page displaying stations and API usage
│
├── main.py # Flask app defining API endpoints
└── README.md # Project documentation
```

---

## 🌐 API Endpoints

| Method | Endpoint                             | Description                                    |
|--------|--------------------------------------|------------------------------------------------|
| GET    | `/`                                  | Home page with station table                   |
| GET    | `/api/v1/<station>/<date>/`          | Get temperature for a specific station & date  |
| GET    | `/api/v1/<station>/`                 | Get all data for a specific station            |
| GET    | `/api/v1/yearly/<station>/<year>/`   | Get all data for a station in a specific year  |

---

## 🚀 Running the Project
- Run the Flask App
```bash
python main.py
```
- Then open your browser and visit:
http://127.0.0.1:5000

---

## 💡 Example Usage

- Get temperature for station 10 on 1990-10-25:  
http://127.0.0.1:5000/api/v1/10/1990-10-25
<br><br>
- Get all data for station 10:  
http://127.0.0.1:5000/api/v1/10/
<br><br>
- Get data for station 10 for year 1990:  
http://127.0.0.1:5000/api/v1/yearly/10/1990
<br><br>
---

## 📄 Data Format

### 📍 stations.txt

This file contains metadata for weather stations in the following format:
```yaml
01-05  STAID   : Station ID  
07-46  STANAME : Station name  
48-49  CN      : Country code (ISO 3166)  
51-59  LAT     : Latitude (degrees:minutes:seconds) 
61-70  LON     : Longitude (degrees:minutes:seconds)  
72-76  HGHT    : Elevation in meters  
```
**Sample:**  
```text
 STAID,STANAME                                 ,CN,      LAT,       LON,HGHT
     1,VAEXJOE                                 ,SE,+56:52:00,+014:48:00,  166
     2,FALUN                                   ,SE,+60:37:00,+015:37:00,  160
```

### 🌡️ TG_STAIDxxxxx.txt

These files contain temperature data per station:

```yaml
01-06 STAID : Station ID  
08-13 SOUID : Source ID  
15-22 DATE  : Date in YYYYMMDD format  
24-28 TG    : Mean temperature in 0.1 °C (e.g., 31 = 3.1°C)  
30-34 Q_TG  : Quality flag (0=valid, 1=suspect, 9=missing)
```
**Sample:**  
```text
STAID, SOUID,    DATE,   TG, Q_TG
    1, 35381,18600101,   21,    0
    1, 35381,18600102,   46,    0
    1, 35381,18600103,   31,    0
```
**Notes:** 
- Missing values are represented as `-9999`.
- Temperature values (TG) are in tenths of degrees Celsius (e.g., 75 means 7.5°C).
- The `stations.txt` and all required station data files (e.g., `TG_STAID000010.txt`) should be located in a `data_small` folder.

---

## 📚 License & Attribution
This project uses open climate data from the European Climate Assessment & Dataset (ECA&D).

**Reference:**  
- Klein Tank, A.M.G. and Coauthors, 2002. Daily dataset of 20th-century surface air temperature and precipitation series for the European Climate Assessment. Int. J. of Climatol., 22, 1441-1453.

More info at: https://www.ecad.eu
