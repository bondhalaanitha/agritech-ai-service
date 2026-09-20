from spoilage_prediction import calculate_spoilage_risk


result = calculate_spoilage_risk(
    crop_age=1,
    shelf_life=7,
    temperature=24,
    quality="Good"
)


print("\nSpoilage Risk Result")
print("-------------------------")

print("Risk Percentage:", result["risk_percentage"], "%")
print("Risk Category:", result["risk_category"])

print("\nRisk Breakdown")
print("-------------------------")

print("Age Risk:", result["age_risk"])
print("Temperature Risk:", result["temperature_risk"])
print("Quality Risk:", result["quality_risk"])