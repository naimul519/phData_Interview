from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib
import json
from utils import get_next_version
#from pydantic import BaseModel

app = FastAPI()

# Load model and demographic data
version = get_next_version() # Load the latest version
model = joblib.load(f"./model/v{version}/model_v{version}.pkl")
zipcode_data = pd.read_csv("data/zipcode_demographics.csv")


@app.post("/predict")
def predict(input_data: dict) -> dict:
    """
    A mock prediction endpoint that simulates loading a model and making a prediction.
    
    Args:
        data (dict): Input data for prediction.
    Returns:
        dict: A JSON response with the prediction result.
    """

    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data])

    with open("./model/model_features.json") as f:
        model_features = json.load(f)
        
    try:

        input_df['zipcode'] = input_df['zipcode'].astype(str)
        zipcode_data['zipcode'] = zipcode_data['zipcode'].astype(str)


        fe_df = input_df.merge(zipcode_data, on="zipcode", how="left")

        model_df = fe_df[model_features]

        
        
        prediction = model.predict(model_df)[0]

        
        return {"success": 200, "prediction": prediction, "model_version": version}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

