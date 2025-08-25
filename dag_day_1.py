import requests
from datetime import date, timedelta
import statistics

# --- Configuration ---
# You can change the location by updating the latitude and longitude.
# Default location is New York City, USA.
LOCATION_NAME = "New York City"
LATITUDE = 40.71
LONGITUDE = -74.01
ANOMALY_THRESHOLD_DEGREES = 5.0  # Threshold in Celsius for detecting an anomaly


def fetch_weather_data(latitude, longitude):
    """
    Fetches weather data for the last 7 completed days from the Open-Meteo API.
    """
    # Define the date range for the last 7 days (from 7 days ago to yesterday)
    today = date.today()
    end_date = today - timedelta(days=1)
    start_date = today - timedelta(days=7)

    # Format dates for the API URL
    api_url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={latitude}&longitude={longitude}&"
        f"start_date={start_date.strftime('%Y-%m-%d')}&end_date={end_date.strftime('%Y-%m-%d')}&"
        f"daily=temperature_2m_max,temperature_2m_min&"
        f"timezone=auto"
    )

    try:
        response = requests.get(api_url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def analyze_weather_data(weather_data):
    """
    Analyzes the weather data to print records, find extremes, and spot anomalies.
    """
    if not weather_data or 'daily' not in weather_data:
        print("No valid weather data to analyze.")
        return

    daily_records = weather_data['daily']
    dates = daily_records['time']
    max_temps = daily_records['temperature_2m_max']
    min_temps = daily_records['temperature_2m_min']

    # --- 1. Print the weather records from the last 7 days ---
    print("--- 🌡️ Weather Records for the Last 7 Days ---")
    for i in range(len(dates)):
        print(f"{dates[i]}: Max Temp: {max_temps[i]}°C, Min Temp: {min_temps[i]}°C")

    # --- 2. Find the highest and lowest temperatures ---
    highest_temp = max(max_temps)
    lowest_temp = min(min_temps)

    # --- 3. Find the dates for the highest and lowest temperatures ---
    date_of_highest = dates[max_temps.index(highest_temp)]
    date_of_lowest = dates[min_temps.index(lowest_temp)]

    print("\n--- 📊 Extreme Temperatures ---")
    print(f"Highest Temperature: {highest_temp}°C (on {date_of_highest})")
    print(f"Lowest Temperature:  {lowest_temp}°C (on {date_of_lowest})")

    # --- 4. Spot the anomalies ---
    avg_max_temp = statistics.mean(max_temps)
    avg_min_temp = statistics.mean(min_temps)

    print("\n--- 🧐 Anomaly Detection ---")
    print(f"Average Max Temp: {avg_max_temp:.2f}°C | Average Min Temp: {avg_min_temp:.2f}°C")
    print(
        f"(An anomaly is a day where the temperature is {ANOMALY_THRESHOLD_DEGREES}°C different from the weekly average)\n")

    anomalies_found = False
    for i in range(len(dates)):
        # Check for unusually hot days
        if max_temps[i] > avg_max_temp + ANOMALY_THRESHOLD_DEGREES:
            print(
                f"🔥 Hot Anomaly: {dates[i]} had a max temp of {max_temps[i]}°C, which is significantly above the average.")
            anomalies_found = True
        # Check for unusually cold days
        if min_temps[i] < avg_min_temp - ANOMALY_THRESHOLD_DEGREES:
            print(
                f"❄️ Cold Anomaly: {dates[i]} had a min temp of {min_temps[i]}°C, which is significantly below the average.")
            anomalies_found = True

    if not anomalies_found:
        print("No significant temperature anomalies were detected in the last 7 days.")


if __name__ == "__main__":
    print(f"Fetching weather data for {LOCATION_NAME} (Lat: {LATITUDE}, Lon: {LONGITUDE})...\n")
    data = fetch_weather_data(LATITUDE, LONGITUDE)
    if data:
        analyze_weather_data(data)
