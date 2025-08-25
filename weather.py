import requests
from datetime import date, timedelta

# --- Configuration for Hyderabad ---
LOCATION_NAME = "Hyderabad, India"
LATITUDE = 17.41
LONGITUDE = 78.48

# Climate normals for Hyderabad in late August (historical averages)
# Used for more accurate anomaly detection.
NORMAL_MAX_TEMP_HYD = 29.5
NORMAL_MIN_TEMP_HYD = 22.5
# Anomaly is significant if a day is more than 2.5°C away from the normal temp.
ANOMALY_THRESHOLD_DEGREES = 2.5


def fetch_weather_data(latitude, longitude):
    """
    Fetches weather data for the last 7 completed days from the Open-Meteo API.
    """
    today = date.today()
    end_date = today - timedelta(days=1)
    start_date = today - timedelta(days=7)

    api_url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={latitude}&longitude={longitude}&"
        f"start_date={start_date.strftime('%Y-%m-%d')}&end_date={end_date.strftime('%Y-%m-%d')}&"
        f"daily=temperature_2m_max,temperature_2m_min&"
        f"timezone=auto"
    )

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def analyze_weather_data(weather_data):
    """
    Analyzes weather data to print records, find extremes, and spot anomalies
    against historical averages for Hyderabad.
    """
    if not weather_data or 'daily' not in weather_data:
        print("No valid weather data to analyze.")
        return

    daily_records = weather_data['daily']
    dates = daily_records['time']
    max_temps = daily_records['temperature_2m_max']
    min_temps = daily_records['temperature_2m_min']

    # 1. Print the weather records from the last 7 days
    print("--- 🌡️ Weather Records for the Last 7 Days ---")
    for i in range(len(dates)):
        print(f"{dates[i]}: Max Temp: {max_temps[i]}°C, Min Temp: {min_temps[i]}°C")

    # 2. Find the highest and lowest recorded temperatures
    highest_temp = max(max_temps)
    lowest_temp = min(min_temps)

    # 3. Find the dates for the highest and lowest temperatures
    date_of_highest = dates[max_temps.index(highest_temp)]
    date_of_lowest = dates[min_temps.index(lowest_temp)]

    print("\n--- 📊 Extreme Temperatures (Last 7 Days) ---")
    print(f"Highest Temperature: {highest_temp}°C (on {date_of_highest})")
    print(f"Lowest Temperature:  {lowest_temp}°C (on {date_of_lowest})")

    # 4. Spot anomalies based on historical climate data
    print("\n--- 🧐 Anomaly Detection (Compared to Climate Normals) ---")
    print(f"Normal for this time of year in Hyderabad: Max ~{NORMAL_MAX_TEMP_HYD}°C, Min ~{NORMAL_MIN_TEMP_HYD}°C")
    print(f"(An anomaly is a day >{ANOMALY_THRESHOLD_DEGREES}°C hotter or colder than normal)\n")

    anomalies_found = False
    for i in range(len(dates)):
        # Check for days unusually hotter than normal
        if max_temps[i] > NORMAL_MAX_TEMP_HYD + ANOMALY_THRESHOLD_DEGREES:
            diff = max_temps[i] - NORMAL_MAX_TEMP_HYD
            print(f"🔥 Unusually Hot Day: {dates[i]}. Max temp was {max_temps[i]}°C ({diff:.1f}°C above normal).")
            anomalies_found = True

        # Check for days unusually colder than normal
        if min_temps[i] < NORMAL_MIN_TEMP_HYD - ANOMALY_THRESHOLD_DEGREES:
            diff = NORMAL_MIN_TEMP_HYD - min_temps[i]
            print(f"❄️ Unusually Cold Day: {dates[i]}. Min temp was {min_temps[i]}°C ({diff:.1f}°C below normal).")
            anomalies_found = True

    if not anomalies_found:
        print("No significant temperature anomalies detected compared to historical norms.")


if __name__ == "__main__":
    print(f"Fetching weather data for {LOCATION_NAME}...\n")
    data = fetch_weather_data(LATITUDE, LONGITUDE)
    if data:
        analyze_weather_data(data)