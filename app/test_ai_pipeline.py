# -----------------------------------------
# AgriShield - Selling Decision Test
# -----------------------------------------

from ai_pipeline import run_ai_pipeline


# =========================================
# FARMER INPUT
# =========================================

temperature = 30

rainfall = 2

supply = 800

current_price = 25

crop_age = 3

shelf_life = 5

quality = "Average"


# =========================================
# SELLING OPTIONS
# =========================================

selling_options = [

    {
        "option_name": "Buyer A",
        "quantity": 500,
        "price": 30,
        "transport_cost": 3000,
        "handling_cost": 500
    },

    {
        "option_name": "Buyer B",
        "quantity": 500,
        "price": 27,
        "transport_cost": 1000,
        "handling_cost": 300
    },

    {
        "option_name": "Local Market",
        "quantity": 500,
        "price": 25,
        "transport_cost": 500,
        "handling_cost": 200
    }

]


# =========================================
# RUN AI PIPELINE
# =========================================

result = run_ai_pipeline(

    temperature=temperature,

    rainfall=rainfall,

    supply=supply,

    current_price=current_price,

    crop_age=crop_age,

    shelf_life=shelf_life,

    quality=quality,

    selling_options=selling_options
)


# =========================================
# COMPLETE RESULT
# =========================================

print("\n")
print("==========================================")
print("          COMPLETE SELLING RESULT")
print("==========================================")


print(
    "Next-day price: ₹",
    result[
        "predicted_next_day_price"
    ]
)


print(
    "Predicted demand:",
    result[
        "predicted_demand"
    ]
)


print(
    "Demand category:",
    result[
        "demand_category"
    ]
)


print(
    "Current spoilage risk:",
    result[
        "spoilage_percentage"
    ],
    "%"
)


print(
    "Next-day spoilage risk:",
    result[
        "next_day_spoilage_percentage"
    ],
    "%"
)


print(
    "Recommended buyer/market:",
    result[
        "recommendation"
    ][
        "option"
    ]
)


print(
    "Expected Net Value: ₹",
    result[
        "recommendation"
    ][
        "expected_net_value"
    ]
)


print(
    "Sell Now vs Wait:",
    result[
        "timing_decision"
    ][
        "recommendation"
    ]
)


print("\nExplanation:")

for reason in result["explanation"]:

    print(
        "•",
        reason
    )


print("\nTiming Explanation:")

for reason in result["timing_explanation"]:

    print(
        "•",
        reason
    )


print("==========================================")