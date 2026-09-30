import yaml
import pandas as pd
import json

# Read settings from the YAML configuration file
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# Get values from the configuration file
max_days = config["max_days_since_calibration"]  # Maximum number of days since the last calibration
output_file = config["output_file"]  # Output file name for the results

print(max_days)
print(output_file)



# Read sensor information from the Excel file
sensors = pd.read_excel("sensors.xlsx")

# Read calibration information from the CSV file
calibrations = pd.read_csv("calibrations.csv")

print(sensors) # Display sensor information
print(calibrations) # Display calibration information

# Combine sensor information with calibration data (match each sensor with its corresponding calibration data)
sensor_data = pd.merge(
    sensors,
    calibrations,
    on="sensor_id"
)

print(sensor_data) # Display combined sensor and calibration information

# Filter sensors that are overdue for calibration (those that have not been calibrated within the specified maximum number of days)
overdue_sensors = sensor_data[
    sensor_data["days_since_calibration"] > max_days
]

print(overdue_sensors) # Display sensors that are overdue for calibration


# Select the columns needed for the JSON output
overdue_data = overdue_sensors[
    ["sensor_id", "lab_room", "owner", "days_since_calibration"]
]

# Convert the DataFrame to a list of dictionaries
overdue_records = overdue_data.to_dict(orient="records")

# Save the overdue sensors to the JSON file
with open(output_file, "w") as file:
    json.dump(overdue_records, file, indent=2)
    