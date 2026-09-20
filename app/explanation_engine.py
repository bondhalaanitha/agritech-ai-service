# -----------------------------------------
# AgriShield - Recommendation Explanation
# -----------------------------------------


def generate_recommendation_explanation(
    recommendation,
    demand_category,
    spoilage_percentage
):

    reasons = []

    reasons.append(
        "Expected net value is ₹"
        + str(
            recommendation[
                "expected_net_value"
            ]
        )
    )

    reasons.append(
        "Transport cost is ₹"
        + str(
            recommendation[
                "transport_cost"
            ]
        )
    )

    reasons.append(
        "Estimated spoilage is "
        + str(
            spoilage_percentage
        )
        + "%"
    )

    reasons.append(
        "Predicted demand is "
        + demand_category
    )

    reasons.append(
        "Handling cost is ₹"
        + str(
            recommendation[
                "handling_cost"
            ]
        )
    )

    return reasons


def generate_timing_explanation(
    timing_result
):

    reasons = []

    reasons.append(
        "Selling now gives an estimated net value of ₹"
        + str(
            timing_result[
                "sell_now_value"
            ]
        )
    )

    reasons.append(
        "Waiting one day gives an estimated net value of ₹"
        + str(
            timing_result[
                "wait_one_day_value"
            ]
        )
    )

    reasons.append(
        "Estimated difference is ₹"
        + str(
            abs(
                timing_result[
                    "difference"
                ]
            )
        )
    )

    reasons.append(
        timing_result["reason"]
    )

    return reasons