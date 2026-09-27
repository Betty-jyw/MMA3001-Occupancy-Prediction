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
