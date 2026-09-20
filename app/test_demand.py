from demand_prediction import predict_demand


result = predict_demand(
    temperature=30,
    rainfall=2,
    supply=800,
    current_price=25
)


print("Predicted demand:", result)