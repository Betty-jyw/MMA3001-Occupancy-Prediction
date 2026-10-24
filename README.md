
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

---

## Computational Methodology

### Data Preprocessing

The raw occupancy records were processed to construct a regular five-minute time series.

The main preprocessing steps included:

1. Converting timestamps into datetime format.
2. Selecting one building space for analysis.
3. Converting occupancy states into binary values.
4. Resampling observations at five-minute intervals.
5. Applying limited forward filling for gaps of up to 10 minutes.
6. Constructing a 30-minute-ahead prediction target.
7. Removing observations with invalid or missing features and targets.

### Feature Engineering

Ten input features were constructed using:

- Current occupancy state
- Occupancy states from 5, 10, 15, 20, 25, and 30 minutes earlier
- Recent occupancy rate
- Hour of day
- Day of week

Historical features were constructed using information available at prediction time to avoid future information leakage.

### Machine Learning Models

Three approaches were evaluated:

**1. Persistence Baseline**

Predicts that the occupancy state 30 minutes ahead will remain the same as the current occupancy state.

**2. Logistic Regression**

Uses historical occupancy and temporal features to estimate the probability of future occupancy.

**3. Random Forest**

Uses an ensemble of decision trees to capture potentially nonlinear relationships between features and future occupancy.

### Training and Testing

A chronological 80/20 train-test split was used to preserve temporal ordering.

The final test dataset contained **21,412 observations**.

The test period extended from **September 2025 to April 2026**.

Training observations whose future target timestamps overlapped the test period were excluded.

---

## Model Evaluation and Results

The models were evaluated using accuracy, precision, recall, F1-score, and confusion matrices.

### Final Model Performance

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Persistence Baseline | 0.6740 | **0.7511** | 0.7634 | 0.7572 |
| Logistic Regression | **0.7168** | 0.7430 | **0.8788** | **0.8052** |
| Random Forest | 0.6898 | 0.7359 | 0.8332 | 0.7815 |

**Logistic Regression achieved the highest overall accuracy and F1-score.**

Compared with the Persistence Baseline, Logistic Regression improved accuracy by **4.28 percentage points**.

### Classification Errors

| Model | False Positives | False Negatives | Total Errors |
|---|---:|---:|---:|
| Persistence Baseline | 3,607 | 3,374 | 6,981 |
| Logistic Regression | 4,335 | 1,728 | **6,063** |
| Random Forest | 4,264 | 2,379 | 6,643 |

Although Logistic Regression produced the fewest total errors, its false positive rate was relatively high at **60.62%**.

### Occupancy Prediction Bias

The actual occupancy rate in the test dataset was approximately **66.60%**.

| Model | Predicted Occupancy Rate | Bias |
|---|---:|---:|
| Persistence Baseline | 67.69% | +1.09 percentage points |
| Logistic Regression | 78.78% | +12.18 percentage points |
| Random Forest | 75.41% | +8.80 percentage points |

All three models overestimated the overall proportion of occupied states.

### Temporal Performance

Monthly performance was evaluated from September 2025 to April 2026.

Logistic Regression achieved the highest accuracy and F1-score among the evaluated models in every month.

However, its monthly accuracy varied between **63.70% and 78.02%**, demonstrating that predictive performance was not constant over time.


---

## Repository Structure

- `data/` — Project datasets and data information
- `notebooks/` — Five Jupyter notebooks covering the complete workflow
- `src/` — Reusable Python source code
- `tests/` — Automated pytest tests
- `docs/` — HTML source code documentation generated using pdoc
- `results/` — Experimental outputs and test reports

## Installation

The project was developed using Python and Google Colab.

Main dependencies:

- NumPy
- pandas
- scikit-learn
- Matplotlib
- pytest
- pdoc

Install dependencies using:

```bash
pip install numpy pandas scikit-learn matplotlib pytest pdoc
```

## How to Run

1. Obtain the authorised MMA3001 occupancy sensor dataset.
2. Prepare the Google Drive project directory and update file paths if necessary.
3. Open the notebooks in Google Colab.
4. Execute the notebooks in the following order:
   - `01_data_exploration.ipynb`
   - `02_feature_engineering.ipynb`
   - `03_model_development.ipynb`
   - `04_model_evaluation.ipynb`
   - `05_final_results.ipynb`

To run the automated tests:

```bash
python -m pytest tests/test_occupancy.py -v
```

The recorded test results were **3 passed**.

HTML documentation is available in `docs/index.html`.

The raw sensor data are subject to the original data access and redistribution conditions.

The study uses historical data and does not demonstrate real-time building system deployment.
