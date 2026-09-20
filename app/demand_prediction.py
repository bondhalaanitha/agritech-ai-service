# -----------------------------------------
# AgriShield - Demand Prediction
# -----------------------------------------

import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


DATA_PATH = "data/datasets/agri_price_1000_records.csv"
MODEL_PATH = "models/demand_model.pkl"


# =========================================
# GET DEMAND CATEGORY
# =========================================

def get_demand_category(demand):

    if demand >= 1000:
        return "High"

    elif demand >= 500:
        return "Medium"

    else:
        return "Low"


# =========================================
# TRAIN DEMAND MODEL
# =========================================

def train_demand_model():

    data = pd.read_csv(
        DATA_PATH
    )


    print("\nDataset loaded successfully!")
    print("Number of rows:", len(data))


    print("\nColumns:")
    print(data.columns.tolist())


    print("\nMissing values:")
    print(data.isnull().sum())


    # -------------------------------------
    # Features
    # -------------------------------------

    X = data[
        [
            "temperature",
            "rainfall",
            "supply",
            "current_price"
        ]
    ]


    # Target
    y = data["demand"]


    # -------------------------------------
    # Train / Test split
    # -------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,
        test_size=0.2,
        random_state=42
    )


    print("\nTraining data:", len(X_train))
    print("Testing data:", len(X_test))


    # -------------------------------------
    # Random Forest
    # -------------------------------------

    model = RandomForestRegressor(

        n_estimators=100,
        random_state=42
    )


    model.fit(
        X_train,
        y_train
    )


    print("\nDemand model training completed!")


    # -------------------------------------
    # Evaluation
    # -------------------------------------

    predictions = model.predict(
        X_test
    )


    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )


    print("\nDemand Model Evaluation")
    print("-------------------------")

    print("MAE :", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R2  :", round(r2, 2))


    # -------------------------------------
    # Save model
    # -------------------------------------

    os.makedirs(
        "models",
        exist_ok=True
    )


    joblib.dump(
        model,
        MODEL_PATH
    )


    print("\nDemand model saved successfully!")
    print("Location:", MODEL_PATH)


# =========================================
# PREDICT DEMAND
# =========================================

def predict_demand(
    temperature,
    rainfall,
    supply,
    current_price
):

    model = joblib.load(
        MODEL_PATH
    )


    input_data = pd.DataFrame([

        {
            "temperature": temperature,
            "rainfall": rainfall,
            "supply": supply,
            "current_price": current_price
        }

    ])


    prediction = model.predict(
        input_data
    )[0]


    return round(
        prediction,
        2
    )


# =========================================
# RUN TRAINING
# =========================================

if __name__ == "__main__":

    train_demand_model()