from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_schema import UserInput
from models.predict import model,MODEL_VERSION, predict_output


app = FastAPI()

    

@app.get("/")
def hello():
    return {"message": "Welcome to Insurance Premium Prediction API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy",
            "model loaded": model is not None,
            "model type": str(type(model)),
            "version": "1.0.0"}
@app.post("/predict")
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))