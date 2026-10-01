import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from part2_engine.growth_engine import (
    validate_feed,
    mom_growth,
    is_flagged,
)


def load_revenue_data(csv_path):
    """Load category and revenue values from a CSV file."""


def load_revenue_data(csv_path, target_month):
    """Load category and revenue values for one month."""
    data = {}

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["month"] == target_month:
                category = row["category"]
                revenue = float(row["revenue"])
                data[category] = revenue

    return data


def draft_message(category, mom_pct):
    """Fill the Part 3 narrative template with supplied values."""
    context = (
        f"This analysis reviews the monthly revenue change for {category}."
    )

    insight = (
        f"Fact: {category} revenue changed by {mom_pct}% month-over-month. "
        f"This change is flagged for review."
    )

    implication = (
        f"Recommendation: Review the {category} performance and identify "
        f"the resellers or regions that contributed to this change."
    )

    return f"{context} {insight} {implication}"


def run(month: str, previous_month_csv: str, current_month_csv: str) -> dict:
    # 1. Validate the current feed
    validation_result = validate_feed(current_month_csv)

    if isinstance(validation_result, tuple):
        validation_status, validation_errors = validation_result
    else:
        validation_status = validation_result
        validation_errors = []

    # 2. Hard Stop if the feed is invalid
    if not validation_status:
        return {
            "run_month": month,
            "validation_status": "invalid",
            "validation_errors": validation_errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "hard_stop",
        }

    # 3. Load previous and current revenue
    previous_month = {
        "May": "April",
        "June": "May",
    }.get(month)

    previous_data = load_revenue_data(previous_month_csv, previous_month)
    current_data = load_revenue_data(current_month_csv, month)

    flagged = []
    suppressed = []
    escalated = []

    # 4. Calculate growth and flag status
    for category, current_revenue in current_data.items():

        if category not in previous_data:
            continue

        previous_revenue = previous_data[category]

        mom_pct = mom_growth(previous_revenue, current_revenue)
        flag_status = is_flagged(mom_pct)

        if flag_status == "flagged":
            flagged.append({
                "category": category,
                "mom_pct": mom_pct,
                "previous_revenue": previous_revenue,
                "current_revenue": current_revenue,
            })

        elif flag_status == "escalate_exact_boundary":
            escalated.append(category)

    # 5. Sort flagged categories by absolute MoM change
    flagged.sort(key=lambda item: abs(item["mom_pct"]), reverse=True)

    # 6. Draft only the top 3
    drafted_entries = flagged[:3]

    for item in drafted_entries:
        item["drafted"] = True
        item["message"] = draft_message(
            item["category"],
            item["mom_pct"]
        )

    # 7. Suppress remaining flagged categories
    for item in flagged[3:]:
        suppressed.append(item["category"])

    # 8. Return one structured JSON object
    return {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": drafted_entries,
        "suppressed_categories": suppressed,
        "escalated_categories": escalated,
        "action_taken": "drafted_and_held_for_approval",
    }


if __name__ == "__main__":
    import sys

    result = run(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
    )

    print(json.dumps(result, indent=2))
