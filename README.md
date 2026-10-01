# Meesho Reseller Operations Capstone

This project implements a simple reseller-operations monitoring pipeline using SQL, Python, deterministic narrative templates, and a mock agent runner.

The project uses only local files and code. No API keys, paid services, network calls, or email sending are required.

## Project Flow

The project is divided into four parts:

1. **Part 1 — SQL**

   * Analyzes reseller and order data using SQLite.
   * Calculates monthly category revenue and order counts.
   * Identifies important changes in reseller operations.

2. **Part 2 — Python Engine**

   * Reads the SQL output.
   * Applies deterministic business rules.
   * Flags significant changes and inactive resellers.

3. **Part 3 — Narrative Templates**

   * Converts the Python results into simple business-readable messages.
   * Uses fixed templates instead of generating unsupported facts.

4. **Part 4 — Agent Runner**

   * Runs the complete workflow.
   * Combines the outputs from the earlier parts.
   * Produces a final monitoring report.

## Dataset

The project uses a locally generated mock dataset.

The dataset contains:

* 24 resellers
* 900 orders
* Multiple product categories
* Multiple regions
* Monthly order and revenue information
* One zero-order reseller for testing inactive-reseller detection

The dataset can be regenerated using the provided Python generator.

## Categories

The project covers these categories:

* Ethnic Wear
* Western Wear
* Kids Wear
* Home & Kitchen
* Beauty & Personal Care

## Repository Structure

```text
meesho_reseller_project
│
├── data
├── part1_sql
├── part2_engine
├── part3_narrative
├── part4_agent
└── README.md
```

## How to Run

### Step 1 — Generate the Dataset

Run the dataset generator from the project folder.

The generator creates the local reseller and order data required for the project.

### Step 2 — Run Part 1 SQL

Run the SQL queries in the `part1_sql` folder using the SQLite database.

The SQL analysis produces monthly category revenue and order-count results.

### Step 3 — Run Part 2 Python Engine

Run the Python engine in the `part2_engine` folder.

The engine applies predefined rules to identify significant changes and inactive resellers.

### Step 4 — Run Part 3 Narrative

Run the deterministic narrative templates in the `part3_narrative` folder.

The results are converted into readable monitoring statements.

### Step 5 — Run Part 4 Agent Runner

Run the agent runner in the `part4_agent` folder.

It combines the outputs into the final reseller-operations monitoring workflow.

## Important Design Principles

### No Invented Figures

The system uses only figures available in the generated dataset and SQL/Python outputs.

It does not invent revenue, order counts, percentages, or business events.

### Deterministic Logic

The monitoring rules are predefined so that the same input produces the same result.

### Offline Execution

The project is designed to run locally without external API calls or paid services.

### Safe Agent Behaviour

The mock agent runner does not send emails or perform external actions.

It only produces the required monitoring output.

## Example SQL Result

The monthly category analysis contains columns such as:

* `month`
* `category`
* `revenue`
* `n_orders`

These values are generated from the local dataset.

## Evaluation Considerations

The project can be evaluated using:

* Accuracy of classifications
* Correct identification of significant changes
* Correct identification of inactive resellers
* Avoidance of false positives and false negatives
* Reliable and repeatable outputs
* No unapproved external actions

## Reproducibility

A new user should be able to clone the repository, regenerate the dataset, and run Parts 1–4 locally by following the instructions above.

No API keys, screenshots, media files, or paid services are required.
## Submission

Push one **public GitHub repository** containing:

```text
data/generate_dataset.py
data/resellers.csv
data/orders.csv
data/meesho_reseller.db
part1_sql/queries.sql
part1_sql/output/*.csv
part2_engine/growth_engine.py
part2_engine/test_growth_engine.py
part2_engine/fixtures/*.csv
part3_narrative/prompt_pack.md
part3_narrative/narrative_report.md
part3_narrative/masking.py
part4_agent/agent_spec.md
part4_agent/mock_agent_runner.py
README.md
```

The `README.md` explains how to regenerate the dataset and run every Part in order.

The complete pipeline runs with **zero API keys** and does not require paid services or external network calls.

### Workflow Mapping

* **Part 1 → Part 2:** Compute the real numbers using SQL first, then hand the results to the Python engine for rule-based analysis.
* **Part 2 → Part 3:** Convert the computed results into controlled, business-readable narrative output.
* **Part 3 → Part 4:** Pass the validated narrative information into the mock agent runner.
* **Part 4:** Mirrors an **Intake → Summary → Report Draft → Validate** reporting flow.

Only the public GitHub repository link should be submitted for grading.
