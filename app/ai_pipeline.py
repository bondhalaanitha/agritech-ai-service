# -----------------------------------------
# AgriShield - Selling Decision AI Pipeline
# -----------------------------------------

from price_prediction import predict_price

from demand_prediction import (
    predict_demand,
    get_demand_category
)

from spoilage_prediction import (
    calculate_spoilage_risk
)

from decision_engine import (
    compare_options,
    compare_sell_now_vs_wait
)

from explanation_engine import (
    generate_recommendation_explanation,
    generate_timing_explanation
)


def run_ai_pipeline(
    temperature,
    rainfall,
    supply,
    current_price,
    crop_age,
    shelf_life,
    quality,
    selling_options
):

    print("\n")
    print("==========================================")
    print("       AGRISHIELD SELLING DECISION")
    print("==========================================")


    # =========================================
    # 1. DEMAND PREDICTION
    # =========================================

    predicted_demand = predict_demand(
        temperature=temperature,
        rainfall=rainfall,
        supply=supply,
        current_price=current_price
    )

    demand_category = get_demand_category(
        predicted_demand
    )

    print("\nDemand Prediction")
    print("-------------------------")

    print(
        "Predicted demand:",
        predicted_demand
    )

    print(
        "Demand category:",
        demand_category
    )


    # =========================================
    # 2. PRICE PREDICTION
    # =========================================

    predicted_price = predict_price(
        temperature=temperature,
        rainfall=rainfall,
        supply=supply,
        demand=predicted_demand,
        current_price=current_price
    )

    print("\nPrice Prediction")
    print("-------------------------")

    print(
        "Current price: ₹",
        current_price
    )

    print(
        "Predicted next-day price: ₹",
        predicted_price
    )


    # =========================================
    # 3. CURRENT SPOILAGE RISK
    # =========================================

    spoilage_result = calculate_spoilage_risk(
        crop_age=crop_age,
        shelf_life=shelf_life,
        temperature=temperature,
        quality=quality
    )

    # IMPORTANT:
    # Use one variable name consistently.

    current_spoilage = spoilage_result[
        "risk_percentage"
    ]

    spoilage_category = spoilage_result[
        "risk_category"
    ]


    print("\nSpoilage Risk")
    print("-------------------------")

    print(
        "Risk:",
        current_spoilage,
        "%"
    )

    print(
        "Category:",
        spoilage_category
    )


    # =========================================
    # 4. NEXT-DAY SPOILAGE RISK
    # =========================================

    next_day_crop_age = crop_age + 1

    next_day_spoilage_result = (
        calculate_spoilage_risk(
            crop_age=next_day_crop_age,
            shelf_life=shelf_life,
            temperature=temperature,
            quality=quality
        )
    )

    next_day_spoilage = (
        next_day_spoilage_result[
            "risk_percentage"
        ]
    )


    # =========================================
    # 5. SELL NOW VS WAIT
    # =========================================

    if len(selling_options) > 0:

        quantity_for_timing = selling_options[0][
            "quantity"
        ]

        transport_for_timing = selling_options[0][
            "transport_cost"
        ]

        handling_for_timing = (
            selling_options[0].get(
                "handling_cost",
                0
            )
        )

    else:

        quantity_for_timing = 0
        transport_for_timing = 0
        handling_for_timing = 0


    timing_result = compare_sell_now_vs_wait(

        quantity=quantity_for_timing,

        current_price=current_price,

        predicted_next_day_price=predicted_price,

        current_spoilage_percentage=current_spoilage,

        next_day_spoilage_percentage=next_day_spoilage,

        transport_cost=transport_for_timing,

        handling_cost=handling_for_timing
    )


    print("\nSell Now vs Wait 1 Day")
    print("-------------------------")

    print(
        "Sell now value: ₹",
        timing_result[
            "sell_now_value"
        ]
    )

    print(
        "Wait 1 day value: ₹",
        timing_result[
            "wait_one_day_value"
        ]
    )

    print(
        "Difference: ₹",
        abs(
            timing_result[
                "difference"
            ]
        )
    )

    print(
        "Timing recommendation:",
        timing_result[
            "recommendation"
        ]
    )


    # =========================================
    # 6. UPDATE SELLING OPTIONS
    # =========================================

    updated_options = []

    for option in selling_options:

        updated_option = option.copy()

        updated_option[
            "spoilage_percentage"
        ] = current_spoilage

        updated_option[
            "demand_category"
        ] = demand_category

        updated_options.append(
            updated_option
        )


    # =========================================
    # 7. COMPARE SELLING OPTIONS
    # =========================================

    decision_results = compare_options(
        updated_options
    )


    print("\nSelling Decision")
    print("-------------------------")

    for result in decision_results:

        print(
            result["rank"],
            ".",
            result["option"],
            "| Price: ₹",
            result["price_per_kg"],
            "| Expected Net Value: ₹",
            result["expected_net_value"]
        )


    # =========================================
    # 8. RECOMMENDED OPTION
    # =========================================

    recommendation = decision_results[0]


    # =========================================
    # 9. EXPLANATION
    # =========================================

    explanation = (
        generate_recommendation_explanation(

            recommendation=recommendation,

            demand_category=demand_category,

            spoilage_percentage=current_spoilage
        )
    )


    timing_explanation = (
        generate_timing_explanation(
            timing_result
        )
    )


    # =========================================
    # 10. FINAL RECOMMENDATION
    # =========================================

    print("\n")
    print("==========================================")
    print("          FINAL RECOMMENDATION")
    print("==========================================")

    print(
        "Recommended option:",
        recommendation[
            "option"
        ]
    )

    print(
        "Expected Net Value: ₹",
        recommendation[
            "expected_net_value"
        ]
    )

    print(
        "Decision Score:",
        recommendation[
            "decision_score"
        ]
    )


    print("\nWhy this option?")

    for reason in explanation:

        print(
            "•",
            reason
        )


    print("\nTiming Recommendation")

    print(
        "•",
        timing_result[
            "recommendation"
        ]
    )

    for reason in timing_explanation:

        print(
            "•",
            reason
        )


    print("==========================================")


    # =========================================
    # 11. RETURN COMPLETE RESULT
    # =========================================

    return {

        "predicted_next_day_price":
            predicted_price,

        "predicted_demand":
            predicted_demand,

        "demand_category":
            demand_category,

        "spoilage_percentage":
            current_spoilage,

        "next_day_spoilage_percentage":
            next_day_spoilage,

        "spoilage_category":
            spoilage_category,

        "spoilage_breakdown":
            spoilage_result,

        "next_day_spoilage_breakdown":
            next_day_spoilage_result,

        "selling_options":
            decision_results,

        "recommendation":
            recommendation,

        "explanation":
            explanation,

        "timing_decision":
            timing_result,

        "timing_explanation":
            timing_explanation
    }