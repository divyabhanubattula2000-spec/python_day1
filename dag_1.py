import requests
import pandas as pd
from datetime import date, timedelta


def get_weather_data(latitude, longitude, days=7):
    """
    Fetches historical weather data for a given location and number of days.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        days (int): The number of past days to retrieve data for.

    Returns:
        pandas.DataFrame: A DataFrame containing the weather data, or None if an error occurs.
    """
    try:
        # Calculate the date range for the API call
        end_date = date.today()
        start_date = end_date - timedelta(days=days - 1)

        # Format dates for the API URL
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        # Construct the API URL for the Open-Meteo Historical Weather API
        # This API provides historical data and doesn't require an API key for basic use.
        api_url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={latitude}&longitude={longitude}&"
            f"start_date={start_date_str}&end_date={end_date_str}&"
            f"daily=temperature_2m_max,temperature_2m_min&"
            f"timezone=auto"
        )

        print(f"Fetching data from: {api_url}\n")

        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Parse the JSON response
        data = response.json()

        # Check if daily data is present in the response
        if 'daily' not in data:
            print("Error: 'daily' data not found in the API response.")
            return None

        # Convert the data into a pandas DataFrame for easier analysis
        df = pd.DataFrame(data['daily'])
        df.rename(columns={
            'time': 'date',
            'temperature_2m_max': 'max_temp_celsius',
            'temperature_2m_min': 'min_temp_celsius'
        }, inplace=True)

        # Convert date column to datetime objects for better handling
        df['date'] = pd.to_datetime(df['date'])

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def analyze_weather_data(df):
    """
    Analyzes the weather data DataFrame to find key statistics and anomalies.

    Args:
        df (pandas.DataFrame): The DataFrame containing weather data.
    """
    if df is None or df.empty:
        print("No data available to analyze.")
        return

    print("--- Weather Records for the Last 7 Days ---")
    print(df.to_string(index=False))
    print("\n" + "=" * 50 + "\n")

    # --- Find Highest and Lowest Temperatures ---
    # Find the row with the highest temperature
    highest_temp_record = df.loc[df['max_temp_celsius'].idxmax()]
    highest_temp = highest_temp_record['max_temp_celsius']
    date_of_highest_temp = highest_temp_record['date'].strftime('%Y-%m-%d')

    # Find the row with the lowest temperature
    lowest_temp_record = df.loc[df['min_temp_celsius'].idxmin()]
    lowest_temp = lowest_temp_record['min_temp_celsius']
    date_of_lowest_temp = lowest_temp_record['date'].strftime('%Y-%m-%d')

    print("--- Temperature Extremes ---")
    print(f"Highest Temperature Recorded: {highest_temp}°C on {date_of_highest_temp}")
    print(f"Lowest Temperature Recorded:  {lowest_temp}°C on {date_of_lowest_temp}")
    print("\n" + "=" * 50 + "\n")

    # --- Spot Anomalies ---
    # An "anomaly" can be defined in many ways. Here, we'll identify:
    # 1. The day with the largest temperature fluctuation (difference between max and min).
    df['temp_fluctuation'] = df['max_temp_celsius'] - df['min_temp_celsius']

    anomaly_record = df.loc[df['temp_fluctuation'].idxmax()]
    max_fluctuation = anomaly_record['temp_fluctuation']
    date_of_anomaly = anomaly_record['date'].strftime('%Y-%m-%d')

    # 2. Calculate the average max temperature and find days that deviate significantly.
    avg_max_temp = df['max_temp_celsius'].mean()
    df['deviation_from_avg'] = abs(df['max_temp_celsius'] - avg_max_temp)

    print("--- Anomaly Detection ---")
    print(f"Average maximum temperature over the last 7 days: {avg_max_temp:.2f}°C")
    print(f"\nAnomaly 1: Largest Daily Temperature Fluctuation")
    print(f"The largest temperature fluctuation was {max_fluctuation:.2f}°C, which occurred on {date_of_anomaly}.")
    print("This indicates a significant change in temperature within a single day.\n")

    print("Anomaly 2: Days with Significant Deviation from Average Max Temperature")
    # We'll consider a deviation of more than 2°C as noteworthy for this example.
    significant_deviations = df[df['deviation_from_avg'] > 2.0]

    if not significant_deviations.empty:
        for index, row in significant_deviations.iterrows():
            day_temp = row['max_temp_celsius']
            day_date = row['date'].strftime('%Y-%m-%d')
            deviation = row['deviation_from_avg']
            direction = "above" if day_temp > avg_max_temp else "below"
            print(
                f"- On {day_date}, the temperature was {day_temp}°C, which is {deviation:.2f}°C {direction} the average.")
    else:
        print("- No days had a maximum temperature deviation of more than 2.0°C from the average.")


if __name__ == "__main__":
    # Coordinates for Hyderabad, Telangana, India
    HYDERABAD_LAT = 17.3850
    HYDERABAD_LON = 78.4867

    # Fetch and analyze the data
    weather_df = get_weather_data(HYDERABAD_LAT, HYDERABAD_LON)

    if weather_df is not None:
        analyze_weather_data(weather_df)