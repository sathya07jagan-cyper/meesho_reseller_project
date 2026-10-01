import csv
from pathlib import Path

from growth_engine import mom_growth, is_flagged

base_path = Path(__file__).parent
csv_path = base_path / "fixtures" / "monthly_category_revenue.csv"
output_path = base_path / "output" / "growth_results.csv"

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

revenue_data = {}

for row in rows:
    month = row["month"].strip()
    category = row["category"].strip()
    revenue = float(row["revenue"])

    revenue_data[(month, category)] = revenue

results = []

categories = sorted({row["category"].strip() for row in rows})

for category in categories:
    april = revenue_data.get(("April", category))
    may = revenue_data.get(("May", category))
    june = revenue_data.get(("June", category))

    if april is not None and may is not None:
        growth = mom_growth(april, may)
        status = is_flagged(growth)

        results.append({
            "category": category,
            "comparison": "April to May",
            "previous_revenue": april,
            "current_revenue": may,
            "mom_pct": growth,
            "status": status,
        })

    if may is not None and june is not None:
        growth = mom_growth(may, june)
        status = is_flagged(growth)

        results.append({
            "category": category,
            "comparison": "May to June",
            "previous_revenue": may,
            "current_revenue": june,
            "mom_pct": growth,
            "status": status,
        })

with open(output_path, "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "category",
        "comparison",
        "previous_revenue",
        "current_revenue",
        "mom_pct",
        "status",
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Saved {len(results)} results to {output_path}")