# Part 3.2 — Worked Narrative Report

## 1. May Ethnic Wear Growth

### Context
This analysis compares the Ethnic Wear revenue in April and May.

### Insight
**Fact:** Ethnic Wear revenue increased by **77.1% MoM** from April to May. This change is flagged because it is above the defined threshold.

### Implication
**Recommendation:** Check which resellers and regions helped increase Ethnic Wear revenue in May. This can help understand what worked well and whether the same approach can be used again.

**Hypothesis:** The increase may be because of higher reseller activity or customer demand, but this is not confirmed by the available data.

### Self-Score

- **Specificity:** Pass — It clearly mentions Ethnic Wear and the April-to-May change.
- **Audience fit:** Pass — It is written in simple language for a reseller operations report.
- **Completeness:** Pass — It includes Context, Insight, and Implication.
- **Actionability:** Pass — It gives a clear next step to check resellers and regions.

---

## 2. June Ethnic Wear Decline

### Context
This analysis compares the Ethnic Wear revenue in May and June.

### Insight
**Fact:** Ethnic Wear revenue decreased by **58.74% MoM** from May to June. This change is flagged because the decrease is above the defined threshold.

### Implication
**Recommendation:** Check the resellers and regions that had lower Ethnic Wear performance in June. This can help identify where the decline happened and what needs further checking.

**Hypothesis:** The decrease may be because of lower reseller activity or customer demand, but this is not confirmed by the available data.

### Self-Score

- **Specificity:** Pass — It clearly mentions Ethnic Wear and the May-to-June change.
- **Audience fit:** Pass — It is suitable for a simple monthly reseller operations report.
- **Completeness:** Pass — It includes Context, Insight, and Implication.
- **Actionability:** Pass — It gives a clear next step to investigate the decline.

---

# Part 3.3 — Chart-Choice Justification

## 1. Highest Total Revenue Month

**Chart type:** Column chart.

**Framework:** Univariate comparison — revenue is compared across different months.

**Why this chart:** A column chart makes it easy to compare the revenue for April, May, and June. The result should be understandable within 10 seconds. The y-axis should start at zero. A 3D chart should be avoided. Since there is only one series, a legend is not needed.

Data:
- April: 419417.43
- May: 444594.25
- June: 398055.24

---

## 2. Ethnic Wear Share of April Total

**Chart type:** 100% stacked bar chart.

**Framework:** Univariate composition — the April total revenue is divided between different categories.

**Why this chart:** A 100% stacked bar can show how much of the April total came from Ethnic Wear. The percentage can be understood quickly. The y-axis should start at zero and go to 100%. 3D should be avoided. A legend can be used because there are multiple categories.

Ethnic Wear share of April total: **24.92%**.

---

## 3. Compare Four Region Revenues

**Chart type:** Bar chart.

**Framework:** Univariate comparison — revenue is compared across four regions.

**Why this chart:** A bar chart makes it easy to compare the revenue of North, South, East, and West. The chart should be clear within 10 seconds. The value axis should start at zero. 3D should be avoided. A legend is not needed because there is only one series.

Data:
- North: 337125.46
- South: 316736.68
- East: 275098.45
- West: 333106.33
---

# Part 3.4 — Masked Top-Reseller Narrative

## Top Reseller Example

### Context
One of the top resellers identified in Part 1 is represented using an alias instead of the reseller's real name. The reseller is from the **West** region.

### Insight
**Fact:** The reseller is represented as **ALIAS-19** to protect the reseller's name.

### Implication
**Recommendation:** Use the alias when discussing this reseller in reports. The region can still be used for analysis without exposing the reseller's actual name.

### Masking Check

The final narrative does not contain the raw reseller name.

**Masking result:** Passed — `assert_no_raw_names_leak()` returned `True`.