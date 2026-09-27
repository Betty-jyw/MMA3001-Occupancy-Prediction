# MMA3001 Occupancy Prediction

## Project Overview

The project investigates whether historical occupancy sensor data can be used to predict the future occupancy status of a selected building space.

The initial prediction task is to predict whether the selected space will be occupied 30 minutes into the future using historical occupancy information and time-related features.


## Engineering Problem and Aim

Building occupancy changes over time and can affect how building spaces and resources are managed. Being able to predict future occupancy may provide useful information for building operation and space management.

The aim of this project is to develop and evaluate a computational model that uses historical occupancy sensor data to predict whether a selected building space will be occupied 30 minutes into the future.

### Research Question

Can historical occupancy patterns be used to predict whether a selected building space will be occupied 30 minutes into the future?

## Dataset

The project uses occupancy sensor data provided for MMA3001. The main dataset contains time-stamped occupancy observations from building spaces.

The available occupancy data includes information such as:

- device ID
- floor-space ID
- occupancy status
- headcount
- collection timestamp
- occupancy-status change timestamp
- previous occupancy status

A separate sensor ID and location mapping file is also provided. This file contains building, room/area, sensor, floor, and space identification information. The mapping information will be investigated to determine whether occupancy records can be reliably associated with specific building spaces.

## Planned Methodology

The project will follow the workflow below:

1. **Data Exploration and Auditing**
   - Inspect the structure, time range, missing values, duplicate records, occupancy states, and available building spaces.
   - Investigate the sensor-location mapping and identify a suitable space with sufficient and reliable occupancy data.

2. **Data Preprocessing**
   - Convert timestamps into appropriate datetime formats.
   - Clean and organise occupancy records.
   - Define the occupancy prediction target.
   - Create time-related and historical occupancy features using information available at the time of prediction.

3. **Exploratory Data Analysis**
   - Analyse occupancy patterns by time of day and day of week.
   - Investigate occupancy-state and headcount distributions.
   - Examine temporal occupancy patterns for the selected building space.

4. **Future Occupancy Prediction**
   - Construct a 30-minute-ahead occupancy prediction task.
   - Develop a simple baseline model.
   - Develop and compare alternative machine-learning models.

5. **Validation and Model Comparison**
   - Use a time-based training and testing strategy to evaluate prediction on later observations.
   - Compare models using appropriate classification metrics such as accuracy, precision, recall, F1-score, and confusion matrices.
   - Compare computational performance where appropriate.

6. **Sensitivity and Performance Analysis**
   - Investigate how prediction performance changes with prediction horizon, such as 10, 30, and 60 minutes.
   - Investigate relevant model settings and computational cost where appropriate.

7. **Engineering Interpretation**
   - Interpret the results in the context of building-space occupancy prediction.
   - Identify limitations, failure cases, and possible improvements.
