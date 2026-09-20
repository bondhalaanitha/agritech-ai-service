# -----------------------------------------
# AgriShield - Spoilage Risk Prediction
# -----------------------------------------

def calculate_spoilage_risk(
    crop_age,
    shelf_life,
    temperature,
    quality
):

    # -------------------------------------
    # Validation
    # -------------------------------------

    if crop_age < 0:

        raise ValueError(
            "Crop age cannot be negative."
        )


    if shelf_life <= 0:

        raise ValueError(
            "Shelf life must be greater than 0."
        )


    if temperature < -50 or temperature > 70:

        raise ValueError(
            "Please enter a realistic temperature."
        )


    quality = quality.strip().lower()


    if quality not in [
        "good",
        "average",
        "poor"
    ]:

        raise ValueError(
            "Quality must be Good, Average, or Poor."
        )


    # =====================================
    # AGE RISK
    # =====================================

    age_ratio = crop_age / shelf_life

    age_risk = age_ratio * 60


    # =====================================
    # TEMPERATURE RISK
    # =====================================

    temperature_risk = 0


    if temperature > 35:

        temperature_risk = 30

    elif temperature > 30:

        temperature_risk = 20

    elif temperature > 25:

        temperature_risk = 10


    # =====================================
    # QUALITY RISK
    # =====================================

    quality_risk = 0


    if quality == "poor":

        quality_risk = 20

    elif quality == "average":

        quality_risk = 10


    # =====================================
    # TOTAL RISK
    # =====================================

    risk = (

        age_risk
        + temperature_risk
        + quality_risk

    )


    # Keep between 0 and 100

    risk = max(
        0,
        min(risk, 100)
    )


    # =====================================
    # CATEGORY
    # =====================================

    if risk < 30:

        category = "Low"

    elif risk < 60:

        category = "Medium"

    else:

        category = "High"


    return {

        "risk_percentage": round(
            risk,
            2
        ),

        "risk_category": category,

        "age_risk": round(
            age_risk,
            2
        ),

        "temperature_risk": round(
            temperature_risk,
            2
        ),

        "quality_risk": round(
            quality_risk,
            2
        )
    }