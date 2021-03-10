# Imports
import pandas as pd
import numpy as np

from functions import clean_string, remove_nan_from_list

# Variables
## Location of data file
DATA_LOC = r'datasets\NYC Motor Vehicle Crashes\data_1000000.csv'
## Columns to dorp
columns_drop = ['collision_id', 'on_street_name', 'off_street_name', 'cross_street_name', 'location']
columns_drop.extend([f'contributing_factor_vehicle_{i}' for i in range(1, 6)])

# Load data
df = pd.read_csv(DATA_LOC, dtype={'borough': 'string'})


# Cleaning
## Remove Duplicates
### There aren't any now but there might be in the future.
df.drop_duplicates(inplace=True)

## Unspecified = missing/nan
df.replace('Unspecified', np.NAN, inplace=True)

## Clean strings
df = df.applymap(lambda x: clean_string(x) if isinstance(x, str) else x)

# New Features
## Number of vehicles
vehicle_cols = []
for col in df.columns:
    if 'vehicle_type' in col:
        vehicle_cols.append(col)
columns_drop.extend(vehicle_cols)
df['n_vehicles'] = df[vehicle_cols].isna().sum(axis=1)*(-1) + 4

## Merge vehicle types
replace_diccie = {}
vehicle_set = set(df[vehicle_cols].values.flatten())
vehicle_set.remove(np.nan)
change = {'truck': ['tru'],
          'ambulance': ['amb'],
          'sedan': ['sedan'],
          'firetruck': ['fire'],
          'van': ['van'],
          'tractor': ['trac'],
          'station wagon': ['station']}
for key, value in change.items():
    for vehicle in vehicle_set:
        for val in value:
            if val in vehicle:
                replace_diccie[vehicle] = key
df[vehicle_cols] = df[vehicle_cols].replace(replace_diccie)

## list up streets streets
df['list_streets'] = df[['on_street_name', 'off_street_name', 'cross_street_name']].values.tolist()
df['list_streets'] = df['list_streets'].apply(remove_nan_from_list)

df['vehicles_list'] = df[vehicle_cols].values.tolist()
df['vehicles_list'] = df['vehicles_list'].apply(remove_nan_from_list)

# Drop columns
df.drop(columns_drop, axis=1, inplace=True)
df.dropna(inplace=True)

df.to_csv(f'datasets/results/results_{len(df)}')