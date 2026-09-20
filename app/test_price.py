from price_prediction import predict_price


result = predict_price(
    temperature=30,
    rainfall=2,
    supply=800,
    demand=900,
    current_price=25
)


print("Predicted next-day price:", result)