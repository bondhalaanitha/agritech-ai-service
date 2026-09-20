from decision_engine import compare_options
quantity = 500



options = [

    {
        "option_name": "Buyer A",
        "quantity": quantity,
        "price": 30,
        "transport_cost": 3000,
        "spoilage_percentage": 20,
        "demand_category": "High",
        "handling_cost": 500
    },

    {
        "option_name": "Buyer B",
        "quantity": quantity,
        "price": 27,
        "transport_cost": 1000,
        "spoilage_percentage": 5,
        "demand_category": "Medium",
        "handling_cost": 300
    },

    {
        "option_name": "Local Market",
        "quantity": quantity,
        "price": 25,
        "transport_cost": 500,
        "spoilage_percentage": 3,
        "demand_category": "High",
        "handling_cost": 200
    }
]


# -----------------------------------------
# Compare Options
# -----------------------------------------

results = compare_options(options)


# -----------------------------------------
# Display Results
# -----------------------------------------

print("\n")
print("==========================================")
print("      AGRISHIELD SELLING DECISION")
print("==========================================")


for result in results:

    print("\n------------------------------------------")

    print(
        "Rank:",
        result["rank"]
    )

    print(
        "Option:",
        result["option"]
    )

    print(
        "Price per kg: ₹",
        result["price_per_kg"]
    )

    print(
        "Revenue: ₹",
        result["revenue"]
    )

    print(
        "Transport Cost: ₹",
        result["transport_cost"]
    )

    print(
        "Handling Cost: ₹",
        result["handling_cost"]
    )

    print(
        "Spoilage:",
        result["spoilage_percentage"],
        "%"
    )

    print(
        "Spoiled Quantity:",
        result["spoiled_quantity"],
        "kg"
    )

    print(
        "Spoilage Loss: ₹",
        result["spoilage_loss"]
    )

    print(
        "Demand:",
        result["demand"]
    )

    print(
        "Expected Net Value: ₹",
        result["expected_net_value"]
    )

    print(
        "Decision Score:",
        result["decision_score"]
    )


# -----------------------------------------
# Display top option
# -----------------------------------------

best_option = results[0]

print("\n")

print("              RECOMMENDATION")


print(
    "Option:",
    best_option["option"]
)

print(
    "Expected Net Value: ₹",
    best_option["expected_net_value"]
)

print(
    "Decision Score:",
    best_option["decision_score"]
)
