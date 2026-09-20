# =========================================================
# AGRISHIELD SELLING DECISION ENGINE
# =========================================================


# =========================================================
# SPOILAGE CALCULATION
# =========================================================

def calculate_spoilage_percentage(
    temperature,
    crop_age,
    shelf_life,
    quality
):

    spoilage = 5


    # Temperature effect

    if temperature >= 35:

        spoilage += 20

    elif temperature >= 30:

        spoilage += 10

    elif temperature >= 25:

        spoilage += 5


    # Crop age effect

    if shelf_life > 0:

        age_ratio = crop_age / shelf_life

        if age_ratio >= 0.8:

            spoilage += 20

        elif age_ratio >= 0.5:

            spoilage += 10


    # Quality effect

    quality = quality.lower()

    if quality == "poor":

        spoilage += 20

    elif quality == "average":

        spoilage += 10


    return min(
        round(spoilage, 2),
        100
    )


# =========================================================
# DEMAND CALCULATION
# =========================================================

def calculate_demand_category(
    supply,
    quantity,
    rainfall
):

    if supply <= 0:

        return "Medium"


    supply_ratio = quantity / supply


    if supply_ratio >= 0.8:

        demand = "Low"

    elif supply_ratio >= 0.5:

        demand = "Medium"

    else:

        demand = "High"


    # Rainfall can affect market demand

    if rainfall > 50 and demand == "Low":

        demand = "Medium"


    return demand


# =========================================================
# NEXT DAY PRICE PREDICTION
# =========================================================

def predict_next_day_price(
    current_price,
    demand_category,
    rainfall
):

    if demand_category == "High":

        predicted_price = current_price * 1.08

    elif demand_category == "Medium":

        predicted_price = current_price * 1.03

    else:

        predicted_price = current_price * 0.97


    # Heavy rainfall may affect tomorrow's market

    if rainfall > 50:

        predicted_price *= 0.98


    return round(
        predicted_price,
        2
    )


# =========================================================
# EXPECTED NET VALUE
# =========================================================

def calculate_expected_net_value(
    quantity,
    price,
    transport_cost,
    spoilage_percentage,
    handling_cost=0
):

    revenue = quantity * price


    spoiled_quantity = (
        quantity
        * spoilage_percentage
        / 100
    )


    spoilage_loss = (
        spoiled_quantity
        * price
    )


    net_value = (
        revenue
        - transport_cost
        - handling_cost
        - spoilage_loss
    )


    return round(
        net_value,
        2
    )


# =========================================================
# DECISION SCORE
# =========================================================

def calculate_decision_score(
    net_value,
    demand_category,
    spoilage_percentage,
    transport_cost,
    quantity
):

    financial_score = net_value / 100


    demand_category = demand_category.lower()


    if demand_category == "high":

        demand_score = 10

    elif demand_category == "medium":

        demand_score = 5

    else:

        demand_score = 0


    spoilage_penalty = (
        spoilage_percentage / 5
    )


    if quantity > 0:

        transport_per_kg = (
            transport_cost / quantity
        )

    else:

        transport_per_kg = 0


    if transport_per_kg <= 1:

        transport_score = 5

    elif transport_per_kg <= 3:

        transport_score = 3

    else:

        transport_score = 0


    score = (
        financial_score
        + demand_score
        + transport_score
        - spoilage_penalty
    )


    return round(
        score,
        2
    )


# =========================================================
# EVALUATE ONE OPTION
# =========================================================

def evaluate_option(
    option_name,
    quantity,
    price,
    transport_cost,
    spoilage_percentage,
    demand_category,
    handling_cost=0
):

    revenue = (
        quantity
        * price
    )


    spoiled_quantity = (
        quantity
        * spoilage_percentage
        / 100
    )


    spoilage_loss = (
        spoiled_quantity
        * price
    )


    net_value = calculate_expected_net_value(

        quantity=quantity,

        price=price,

        transport_cost=transport_cost,

        spoilage_percentage=spoilage_percentage,

        handling_cost=handling_cost
    )


    decision_score = calculate_decision_score(

        net_value=net_value,

        demand_category=demand_category,

        spoilage_percentage=spoilage_percentage,

        transport_cost=transport_cost,

        quantity=quantity
    )


    return {

        "option": option_name,

        "quantity": quantity,

        "price_per_kg":
            round(price, 2),

        "revenue":
            round(revenue, 2),

        "transport_cost":
            round(transport_cost, 2),

        "handling_cost":
            round(handling_cost, 2),

        "spoilage_percentage":
            round(
                spoilage_percentage,
                2
            ),

        "spoiled_quantity":
            round(
                spoiled_quantity,
                2
            ),

        "spoilage_loss":
            round(
                spoilage_loss,
                2
            ),

        "demand":
            demand_category,

        "expected_net_value":
            net_value,

        "decision_score":
            decision_score
    }


# =========================================================
# COMPARE MARKETS
# =========================================================

def compare_options(options):

    evaluated_options = []


    for option in options:

        result = evaluate_option(

            option_name=
                option["option_name"],

            quantity=
                option["quantity"],

            price=
                option["price"],

            transport_cost=
                option["transport_cost"],

            spoilage_percentage=
                option["spoilage_percentage"],

            demand_category=
                option["demand_category"],

            handling_cost=
                option.get(
                    "handling_cost",
                    0
                )
        )


        evaluated_options.append(
            result
        )


    # Sort by expected net value

    evaluated_options.sort(

        key=lambda x:
            x["expected_net_value"],

        reverse=True
    )


    # Assign ranking

    for index, option in enumerate(

        evaluated_options,

        start=1
    ):

        option["rank"] = index


    return evaluated_options


# =========================================================
# SELL NOW VS WAIT
# =========================================================

def compare_sell_now_vs_wait(

    quantity,

    current_price,

    predicted_next_day_price,

    current_spoilage_percentage,

    next_day_spoilage_percentage,

    transport_cost,

    handling_cost=0

):

    # -----------------------------------------------------
    # SELL NOW
    # -----------------------------------------------------

    sell_now_value = calculate_expected_net_value(

        quantity=quantity,

        price=current_price,

        transport_cost=transport_cost,

        spoilage_percentage=
            current_spoilage_percentage,

        handling_cost=handling_cost
    )


    # -----------------------------------------------------
    # WAIT
    # -----------------------------------------------------

    wait_value = calculate_expected_net_value(

        quantity=quantity,

        price=predicted_next_day_price,

        transport_cost=transport_cost,

        spoilage_percentage=
            next_day_spoilage_percentage,

        handling_cost=handling_cost
    )


    difference = (
        wait_value
        - sell_now_value
    )


    # -----------------------------------------------------
    # DECISION
    # -----------------------------------------------------

    if wait_value > sell_now_value:

        recommendation = "Wait 1 Day"

        reason = (
            "The predicted next-day selling value "
            "is higher than the estimated value "
            "of selling today."
        )

    else:

        recommendation = "Sell Now"

        reason = (
            "The estimated value of selling today "
            "is higher than or equal to the predicted "
            "next-day value."
        )


    return {

        "sell_now_value":
            round(
                sell_now_value,
                2
            ),

        "wait_one_day_value":
            round(
                wait_value,
                2
            ),

        "difference":
            round(
                difference,
                2
            ),

        "recommendation":
            recommendation,

        "reason":
            reason
    }