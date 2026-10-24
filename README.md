
# MMA3001 Occupancy Prediction

## Project Overview

This project develops and evaluates machine learning models to predict room occupancy **30 minutes into the future** using historical occupancy sensor data.

The project was completed as part of **MMA3001 — Numerical Methods and Machine Learning** at Monash University.

The computational workflow includes:

- Data exploration
- Data preprocessing
- Feature engineering
- Model development
- Model validation
- Performance evaluation
- Interpretation of results

Three prediction approaches were evaluated:

1. **Persistence Baseline**
2. **Logistic Regression**
3. **Random Forest**

**Logistic Regression achieved the highest overall test accuracy (71.68%) and F1-score (0.8052).**

---

## Engineering Problem and Aim

Building occupancy varies throughout the day and can influence the operation of:

- Heating systems
- Ventilation systems
- Air conditioning systems
- Lighting systems
- Space management systems

Predicting future room occupancy may help building management systems anticipate changes in space usage.

The aim of this project is to **develop and evaluate a reproducible machine learning workflow** for predicting whether a selected building space will be occupied 30 minutes into the future.

### Research Question

**Can historical occupancy patterns and time-related features improve 30-minute-ahead room occupancy prediction compared with a simple persistence baseline?**

---

## Dataset

The project uses occupancy sensor data provided for **MMA3001**.

The original occupancy dataset contains approximately **9.09 million time-stamped records** across five floor spaces.

One building space was selected for detailed analysis.

The raw occupancy observations were processed into a regular **five-minute time series**, and a binary occupancy target was constructed for **30 minutes into the future**.

The final feature dataset contains **107,059 valid observations**, including historical occupancy features and time-related variables.

### Input Features

The models use **10 input features**, including:

- **Current occupancy state**
- **Historical occupancy states** at 5-minute intervals
- **Recent occupancy rate**
- **Hour of day**
- **Day of week**

### Prediction Output

The model predicts a **binary room occupancy state 30 minutes ahead**:

- `0` — **Unoccupied**
- `1` — **Occupied**

### Data Limitations

Environmental sensor data were not incorporated because a reliable spatial match to the selected occupancy space could not be established.

The study uses historical data and does not demonstrate real-time building system deployment.
