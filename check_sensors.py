import yaml
import pandas as pd

# Read settings from the YAML configuration file
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# Get values from the configuration file
max_days = config["max_days_since_calibration"]
output_file = config["output_file"]

print(max_days)
print(output_file)



# Read sensor information from the Excel file
sensors = pd.read_excel("sensors.xlsx")

# Read calibration information from the CSV file
calibrations = pd.read_csv("calibrations.csv")

print(sensors)
print(calibrations)