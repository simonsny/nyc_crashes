# New York City Crashes

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Folder Structure](#folder-structure)

## Introduction

This project is created with the goal of preprocessing a dataset which will in turn give .


## Requirements
1. Pandas
2. numpy
2. re

## Folder Structure

- `datasets`: All data will be stored in this folder
    - `NYC Motor Vehicle Crashes`
        - `data_{number of rows}.csv`: contains dataset provided by new york city with the number of rows you want, 
        dowloaded by the script `download.py`
        - `download.py`: script that downloads a dataset with th enumber of rows provided.
    - `results`: results we got from the `script.py`
- `README.md`
- `script.py`: If you run this script, it will preprocess the dataset given by the city of new york
into a usable dataset for machiene learning. It is saved in folder `datasets/results/'
- `functions.py`: Some Usefull functions for the script.