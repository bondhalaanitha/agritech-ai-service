from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.decision_engine import (
    calculate_spoilage_percentage,
    calculate_demand_category,
    predict_next_day_price,
    compare_options,
    compare_sell_now_vs_wait
)


app = FastAPI(
    title="AgriShield AI Service"
)
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

# =========================================================
# REQUEST MODEL
# =========================================================

class DecisionRequest(BaseModel):

    crop: str
    quantity: float
    temperature: float
    rainfall: float
    supply: float
    current_price: float
    crop_age: float
    shelf_life: float
    quality: str


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():

    return {
        "message": "AgriShield AI Service is running"
    }


# =========================================================
# SELLING DECISION
# =========================================================

@app.post("/decision")
def decision(request: DecisionRequest):

    # -----------------------------------------------------
    # 1. Calculate spoilage
    # -----------------------------------------------------

    spoilage_percentage = calculate_spoilage_percentage(
        temperature=request.temperature,
        crop_age=request.crop_age,
        shelf_life=request.shelf_life,
        quality=request.quality
    )


    # -----------------------------------------------------
    # 2. Predict demand
    # -----------------------------------------------------

    demand_category = calculate_demand_category(
        supply=request.supply,
        quantity=request.quantity,
        rainfall=request.rainfall
    )


    # -----------------------------------------------------
    # 3. Predict next day price
    # -----------------------------------------------------

    predicted_next_day_price = predict_next_day_price(
        current_price=request.current_price,
        demand_category=demand_category,
        rainfall=request.rainfall
    )


    # -----------------------------------------------------
    # 4. Create market options
    #
    # These are temporary demo market values.
    # Later we will replace them with actual market data.
    # -----------------------------------------------------

    options = [

        {
            "option_name": "Local Market",
            "quantity": request.quantity,
            "price": request.current_price,
            "transport_cost": 300,
            "spoilage_percentage": spoilage_percentage,
            "demand_category": demand_category,
            "handling_cost": 100
        },

        {
            "option_name": "Wholesale Market",
            "quantity": request.quantity,
            "price": request.current_price + 3,
            "transport_cost": 800,
            "spoilage_percentage": spoilage_percentage + 2,
            "demand_category": demand_category,
            "handling_cost": 150
        },

        {
            "option_name": "Direct Buyer",
            "quantity": request.quantity,
            "price": request.current_price + 5,
            "transport_cost": 1200,
            "spoilage_percentage": spoilage_percentage + 1,
            "demand_category": demand_category,
            "handling_cost": 100
        }

    ]


    # -----------------------------------------------------
    # 5. Compare markets
    # -----------------------------------------------------

    selling_options = compare_options(options)


    # -----------------------------------------------------
    # 6. Compare sell now vs wait
    # -----------------------------------------------------

    next_day_spoilage = min(
        spoilage_percentage + 5,
        100
    )


    timing_decision = compare_sell_now_vs_wait(

        quantity=request.quantity,

        current_price=request.current_price,

        predicted_next_day_price=predicted_next_day_price,

        current_spoilage_percentage=spoilage_percentage,

        next_day_spoilage_percentage=next_day_spoilage,

        transport_cost=selling_options[0]["transport_cost"],

        handling_cost=selling_options[0]["handling_cost"]
    )


    # -----------------------------------------------------
    # 7. Best recommendation
    # -----------------------------------------------------

    recommended = selling_options[0]


    # -----------------------------------------------------
    # 8. Explanation
    # -----------------------------------------------------

    explanation = [

        f"Current crop quality is {request.quality}.",

        f"Predicted demand is {demand_category}.",

        f"Estimated spoilage risk is "
        f"{spoilage_percentage}%."
        ,

        f"Recommended option is "
        f"{recommended['option']} "
        f"based on expected net value.",

        "Transportation cost and spoilage risk "
        "were considered along with market price."
    ]


    # -----------------------------------------------------
    # 9. FINAL RESPONSE
    # -----------------------------------------------------

    return {

        "predicted_next_day_price":
            predicted_next_day_price,

        "predicted_demand":
            demand_category,

        "demand_category":
            demand_category,

        "spoilage_percentage":
            spoilage_percentage,

        "spoilage_category":
            (
                "High"
                if spoilage_percentage >= 30
                else "Medium"
                if spoilage_percentage >= 15
                else "Low"
            ),

        "timing_decision":
            timing_decision,

        "recommendation":
            recommended,

        "selling_options":
            selling_options,

        "explanation":
            explanation
    }