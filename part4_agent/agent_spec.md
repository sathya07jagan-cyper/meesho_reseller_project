# Part 4 — Agentic Workflow Specification

## 4.1 Agent Specification

### Goal

The goal of this monitoring agent is to identify categories where monthly revenue changes by more than the 8% threshold and prepare a message for human approval before it can be sent.

### Tools

The agent uses the following tools and functions from Parts 2 and 3:

- `validate_feed` — checks whether the revenue feed is valid.
- `mom_growth` — calculates the month-over-month revenue change.
- `is_flagged` — checks whether the change crosses the 8% threshold.
- Part 3 prompt-pack template — creates the draft message for a flagged category.

The Part 2 functions are reused without changing their logic.

### Memory / State

The agent needs to remember the previous month's revenue for each category. This is required so that the current month's revenue can be compared with the previous month to calculate MoM growth.

### Planner

The agent follows these steps:

1. Load the monthly revenue feed and run `validate_feed`.
2. If the feed is invalid, stop the run and show the validation errors.
3. If the feed is valid, calculate `mom_growth` for every category using the previous month's revenue.
4. Run `is_flagged` for every category.
5. Sort flagged categories by the absolute MoM percentage from highest to lowest.
6. Draft messages for only the top 3 flagged categories using the Part 3 prompt template.
7. Put any remaining flagged categories into `suppressed_categories` with the status "suppressed, review manually".
7b. Put any category with `escalate_exact_boundary` into `escalated_categories`. No message is drafted for this category.
8. Return one structured JSON object for the run.

### Feedback Loop

The agent does not send messages automatically. It only creates drafts and holds them for human approval.

The human can review the drafted message before any message is considered ready to send.

---

## Guardrails

### Input Guardrail

`validate_feed` must pass before any MoM calculation or flagging is performed.

If validation fails, the agent performs a **Hard Stop** and shows the validation errors.

### Action Guardrail

The agent never automatically sends a message.

It only creates a draft and holds it for human approval.

### Output Guardrail

Every number in a drafted message must come from the values already provided by Part 1 or Part 2.

The agent must not invent revenue values, percentages, or other numbers.

---

## Success and Error Stopping Conditions

### Success

A successful run produces the required draft messages for flagged categories.

If no category crosses the threshold, the run can correctly produce zero drafts.

Every number in a drafted message must be traceable to the Part 1 or Part 2 data.

### Error

If `validate_feed` returns `False`, the run is a **Hard Stop**.

The validation errors must be shown in the output.

No MoM calculation, flagging, or message drafting is performed on invalid data.

---

## Given-When-Then Agent Specifications

### Given-When-Then

1. **Growth flag — positive change**
   - **Given:** April → May Ethnic Wear revenue is 104520.77 to 185107.61.
   - **When:** `mom_growth` and `is_flagged` are evaluated.
   - **Then:** `mom_growth` returns `77.1` and `is_flagged` returns `"flagged"`.

2. **Growth flag — small change**
   - **Given:** May → June Beauty & Personal Care revenue is 35542.11 to 37559.07.
   - **When:** `mom_growth` and `is_flagged` are evaluated.
   - **Then:** `mom_growth` returns `5.67` and `is_flagged` returns `"not_flagged"`.

3. **Exact boundary**
   - **Given:** Previous revenue is `100000` and current revenue is `108000`.
   - **When:** `mom_growth` and `is_flagged` are evaluated.
   - **Then:** `mom_growth` returns exactly `8.0` and `is_flagged` returns `"escalate_exact_boundary"`.

4. **Invalid feed**
   - **Given:** The corrupted feed fixture contains a negative revenue, a missing category, and a missing revenue.
   - **When:** `validate_feed` runs.
   - **Then:** It returns `False` with exactly these three errors, in this order:
     1. `line 3: negative revenue (-4200.0) for category=Western Wear`
     2. `line 4: missing category (month=July)`
     3. `line 6: missing revenue (category=Home & Kitchen)`
   - **Agent action:** Hard Stop; no flagged or suppressed categories are produced.