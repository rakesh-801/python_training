from flask import Flask, Response, jsonify, request

app = Flask(__name__)

# Dummy weather data for 30 cities
weather_data = {
    "hyderabad": {
        "heat": "high",
        "temperature": "30C",
        "watervapour": "5%",
        "humidity": "60%"
    },
    "newyork": {
        "heat": "medium",
        "temperature": "20C",
        "watervapour": "3%",
        "humidity": "50%"
    },
    "london": {
        "heat": "low",
        "temperature": "15C",
        "watervapour": "4%",
        "humidity": "70%"
    },
    "paris": {
        "heat": "medium",
        "temperature": "18C",
        "watervapour": "2%",
        "humidity": "65%"
    },
    "tokyo": {
        "heat": "high",
        "temperature": "25C",
        "watervapour": "6%",
        "humidity": "75%"
    },
    "berlin": {
        "heat": "low",
        "temperature": "12C",
        "watervapour": "3%",
        "humidity": "60%"
    },
    "mumbai": {
        "heat": "high",
        "temperature": "32C",
        "watervapour": "7%",
        "humidity": "80%"
    },
    "sydney": {
        "heat": "medium",
        "temperature": "22C",
        "watervapour": "5%",
        "humidity": "55%"
    },
    "dubai": {
        "heat": "very high",
        "temperature": "38C",
        "watervapour": "1%",
        "humidity": "40%"
    },
    "toronto": {
        "heat": "medium",
        "temperature": "10C",
        "watervapour": "4%",
        "humidity": "50%"
    },
    "moscow": {
        "heat": "low",
        "temperature": "5C",
        "watervapour": "2%",
        "humidity": "65%"
    },
    "beijing": {
        "heat": "medium",
        "temperature": "20C",
        "watervapour": "3%",
        "humidity": "55%"
    },
    "delhi": {
        "heat": "high",
        "temperature": "35C",
        "watervapour": "6%",
        "humidity": "70%"
    },
    "singapore": {
        "heat": "high",
        "temperature": "28C",
        "watervapour": "8%",
        "humidity": "85%"
    },
    "shanghai": {
        "heat": "medium",
        "temperature": "22C",
        "watervapour": "5%",
        "humidity": "60%"
    },
    "chicago": {
        "heat": "medium",
        "temperature": "12C",
        "watervapour": "4%",
        "humidity": "55%"
    },
    "losangeles": {
        "heat": "medium",
        "temperature": "24C",
        "watervapour": "3%",
        "humidity": "50%"
    },
    "bangkok": {
        "heat": "high",
        "temperature": "30C",
        "watervapour": "7%",
        "humidity": "75%"
    },
    "istanbul": {
        "heat": "medium",
        "temperature": "18C",
        "watervapour": "4%",
        "humidity": "60%"
    },
    "seoul": {
        "heat": "medium",
        "temperature": "20C",
        "watervapour": "5%",
        "humidity": "65%"
    },
    "cairo": {
        "heat": "high",
        "temperature": "28C",
        "watervapour": "2%",
        "humidity": "45%"
    },
    "madrid": {
        "heat": "medium",
        "temperature": "19C",
        "watervapour": "3%",
        "humidity": "55%"
    },
    "rome": {
        "heat": "medium",
        "temperature": "20C",
        "watervapour": "4%",
        "humidity": "60%"
    },
    "amsterdam": {
        "heat": "low",
        "temperature": "14C",
        "watervapour": "5%",
        "humidity": "70%"
    },
    "vienna": {
        "heat": "low",
        "temperature": "13C",
        "watervapour": "4%",
        "humidity": "65%"
    },
    "prague": {
        "heat": "low",
        "temperature": "12C",
        "watervapour": "3%",
        "humidity": "60%"
    },
    "warsaw": {
        "heat": "low",
        "temperature": "10C",
        "watervapour": "4%",
        "humidity": "65%"
    },
    "budapest": {
        "heat": "medium",
        "temperature": "16C",
        "watervapour": "5%",
        "humidity": "70%"
    },
    "athens": {
        "heat": "medium",
        "temperature": "22C",
        "watervapour": "3%",
        "humidity": "55%"
    }
}

@app.route("/weather", methods=['GET'])
def weather():
    city = request.args.get('city', '').lower()
    format_type = request.args.get('type', 'json')

    if city not in weather_data:
        return Response(response="City not found", status=404)

    data = weather_data[city]

    if format_type == 'json':
        return jsonify(data)
    elif format_type == 'xml':
        response = f"""<?xml version="1.0"?>
                     <weather>
                     <city>{city}</city>
                     <heat>{data['heat']}</heat>
                     <temperature>{data['temperature']}</temperature>
                     <watervapour>{data['watervapour']}</watervapour>
                     <humidity>{data['humidity']}</humidity>
                     </weather>"""
        return Response(response=response, status=200, mimetype="application/xml")
    else:
        return "Format not recognized", 400

if __name__ == '__main__':
    app.run(debug=True)