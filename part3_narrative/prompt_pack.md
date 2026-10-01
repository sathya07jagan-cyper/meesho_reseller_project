
# Part 3.1 — Reusable Prompt Pack

## 1. Trigger

Generate a narrative only when the `is_flagged` result is `"flagged"`.

## 2. Input List

The following placeholders are required:

- `{category}` — Product category.
- `{prev_month}` — Previous month.
- `{month}` — Current month.
- `{previous_revenue}` — Revenue in the previous month.
- `{current_revenue}` — Revenue in the current month.
- `{mom_pct}` — Month-over-month percentage growth or decline.
- `{flag_status}` — Flagging result.

## 3. Reusable Prompt

You are a business analyst preparing a monthly reseller operations report.

Use only the information provided below:

- Category: {category}
- Previous month: {prev_month}
- Current month: {month}
- Previous revenue: {previous_revenue}
- Current revenue: {current_revenue}
- Month-over-month change: {mom_pct}%
- Flag status: {flag_status}

Write a concise narrative using these three sections:

**Context:** State the category and the months being compared.

**Insight:** State the exact percentage change and identify it as a **Fact**. Describe whether revenue increased or decreased.

**Implication:** Give one specific, actionable recommendation. If you suggest a possible cause that is not supported by the data, label it as a **Hypothesis**.

Rules:
- Generate the narrative only if the flag status is `"flagged"`.
- Do not invent facts, causes, or numbers.
- Do not state any number that is not included in the supplied inputs.
- Clearly distinguish facts from hypotheses.
- Keep the narrative clear and suitable for a business audience.

## 4. Validation Checklist

Before accepting the narrative, check:

- [ ] All numbers match the supplied inputs exactly.
- [ ] Facts and hypotheses are clearly distinguished.
- [ ] The context identifies the category and comparison period.
- [ ] The insight accurately describes the direction and percentage of change.
- [ ] The implication includes a specific, actionable recommendation.
- [ ] No unsupported causes or extra numbers are included.