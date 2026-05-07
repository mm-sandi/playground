# 37 — Screening Out / スクリーニングアウト

**Total scripts:** Files in `selenium/Research/` and `selenium/Answer/` subdirs  
**Purpose:** Verify that the Screening Out (SCR) feature correctly terminates a respondent's participation when their answers match configured disqualification conditions. Tests cover configuration validation, single/multiple cell setups, AND/OR logic combinations, yellow card assignments, and point award rules.

---

## TC-37-01 — Screening Out Configuration Input Validation

**Scope:** Admin  
**Platform:** Desktop  
**Survey types:** Quick, Screening

**Scenario:** An administrator configures Screening Out conditions and point awards. Input fields must reject invalid values and accept valid ones.

**Setup:**
- Quick survey with Q1 (SAR) and a Screening Out condition: any(Q1,"1") — no yellow card
- Screening survey with a similar setup

**Steps (Quick):**
1. Create a Quick survey with one SAR question.
2. Click the Screening Out link on the survey editor. Set end condition: any(Q1,"1"), no yellow card.
3. Complete the survey setup (survey detail screen should show SCR points = 0).
4. Go to Basic Information Settings screen. Verify initial values:
   - Macromill SCR points field: 0
   - Y! Normal/Light SCR points field: 1
5. Test invalid input in SCR points fields:
   - Empty (required error)
   - Half-width letters (error)
   - Full-width letters (error)
   - Full-width Japanese (error)
   - Half-width Japanese (error)
   - Half-width symbols (error)
   - Full-width symbols (error)
   - Negative number (error)
   - Value over 1000, e.g. 1001 (error)
6. Enter full-width numbers → verify settings saved and redirected to survey detail.
7. Re-enter half-width numbers → verify settings saved correctly.
8. Go to Settings Confirmation screen and verify SCR points are displayed in the summary.
9. Configure 2 cells in delivery settings (each with delivery count = 1, target sample = 1).

**Steps (Screening):** Same validation flow using a Screening-type survey.

**Expected Results:**
- All invalid inputs produce error messages
- Valid numeric inputs (full-width or half-width) save correctly
- SCR points appear on the survey detail and settings confirmation screens

---

## TC-37-02 — Screening Out Button Behavior

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Verify button behavior on the SCR settings screen when the survey has one cell vs. multiple cells.

**Sub-scenarios:**
1. Single cell: Verify that the SCR configuration screen shows the correct buttons and the navigation works correctly
2. Multiple cells: Verify that cell-specific SCR condition buttons and shared condition buttons both display correctly

**Expected Results:**
- Single-cell surveys show appropriate button set
- Multi-cell surveys show both shared and per-cell SCR configuration options

---

## TC-37-03 — Single Cell: Respondent Triggered by SCR Condition

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A survey with a single cell has one Screening Out condition. A respondent answers in a way that matches the disqualification condition.

**Sub-scenarios:**
1. **Screened out (no yellow card):** Respondent selects the disqualifying answer. Survey terminates immediately. Respondent sees the SCR-out screen. SCR points are awarded.
2. **Not screened out:** Respondent selects a non-disqualifying answer. Survey continues normally to completion.
3. **Screened out with yellow card:** Same as #1 but yellow card flag is also assigned.
4. **Not screened out with yellow card condition configured:** Condition not matched — no yellow card assigned, survey completes normally.

**Expected Results:**
- SCR condition match → survey terminates, respondent sees SCR screen, data flagged as screened-out
- SCR condition not matched → survey completes normally
- Yellow card assigned only when configured AND condition is matched

---

## TC-37-04 — Multiple Cells: Shared and Per-Cell SCR Conditions

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A survey has multiple cells, with Screening Out conditions set on either the shared level or the individual cell level.

**Sub-scenarios:**
1. Common (shared) condition triggers SCR — respondent in any cell is screened out
2. Cell 1 condition triggers SCR — only respondents in Cell 1 are screened out
3. Neither common nor cell condition triggers — respondent completes normally
4. Both common AND cell conditions apply and both trigger — respondent is screened out (first matching condition wins)

**Expected Results:**
- Shared conditions apply regardless of cell assignment
- Cell-specific conditions only affect respondents in that cell
- First applicable SCR condition in the list terminates the session

---

## TC-37-05 — Two Cells: Shared and Cell-Specific SCR (with Yellow Card)

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A survey has 2 cells. SCR conditions are set at either the common level or cell-1-only level, with and without yellow card.

**Sub-scenarios:**
1. Common condition only, yellow card: respondent screened out AND yellow card assigned
2. Common condition only, yellow card: respondent not screened out → no yellow card
3. Common condition only, no yellow card: screened out normally
4. Common condition only, no yellow card: not screened out → completes normally
5. Cell 1 condition only, yellow card: Cell 1 respondent screened out with yellow card
6. Cell 1 condition only, yellow card: Cell 1 respondent not matched → no yellow card
7. Cell 1 condition only, no yellow card: Cell 1 screened out
8. Cell 1 condition only, no yellow card: Cell 1 not matched → completes normally

**Expected Results:**
- Cell assignment determines which conditions apply
- Yellow card only assigned when condition is configured AND matched

---

## TC-37-06 — Multiple Conditions per Cell: AND/OR Logic

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A single cell has multiple SCR conditions joined with AND or OR logic. The system must evaluate the combined expression correctly.

**Sub-scenarios:**
1. AND condition: both conditions matched → screened out
2. AND + OR conditions: partial match (only AND side) → verify SCR triggered or not
3. OR + OR conditions: either condition matched → screened out
4. OR + OR + AND conditions: complex combination — verify evaluation order and result

**Expected Results:**
- AND logic: all conditions must match
- OR logic: any one condition matching is sufficient
- Complex expressions are evaluated according to standard boolean precedence

---

## TC-37-07 — Multiple Applicable SCR Conditions: Point Priority

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A respondent's answers match more than one Screening Out condition. The system must award points from the first (highest) matching condition in the list.

**Sub-scenarios:**
1. Multiple conditions in shared (common) settings — points from the topmost matching condition
2. Multiple conditions in per-cell settings — points from the topmost matching cell-level condition
3. Both common and cell-level conditions match — determine which takes precedence
4. Multiple SCR conditions match but only the lower one has yellow card → yellow card is NOT assigned (top condition has no yellow card)

**Expected Results:**
- Point amount comes from the first matching condition in display order
- Yellow card setting of the first matched condition takes precedence
- Lower conditions that also match are ignored for points/yellow card

---

## TC-37-08 — Answer Data Not Stored for SCR-Out Respondent Without Screen Branch

**Scope:** Respondent / System  
**Platform:** Desktop

**Scenario:** When a respondent is screened out and the survey has no branch between the title screen and Q1, their answer data must not be written to the raw data table (RAWDATA).

**Steps:**
1. Create a survey with no branching between title and Q1.
2. Configure SCR condition on Q1.
3. Respondent answers Q1 matching the SCR condition and is screened out.
4. Verify RAWDATA does not contain the screened-out respondent's answer.

**Expected Results:**
- Screened-out response is NOT written to RAWDATA
- ANSWER table may have a screened-out status record, but no RAWDATA entry

---

## TC-37-09 — Parameter-Based Screening Out (Screening Survey Type)

**Scope:** Respondent  
**Platform:** Desktop  
**Survey type:** Screening

**Scenario:** Screening-type surveys can use respondent parameters passed via URL to trigger SCR conditions. Tests verify correct SCR triggering based on these external parameters.

**Sub-scenarios:**
1. Common condition with URL parameter → respondent screened out
2. Cell-specific condition with URL parameter → respondent in that cell screened out
3. Cell-specific condition, but the parameter question is absent in the URL → condition cannot be evaluated → respondent NOT screened out

**Expected Results:**
- URL parameters correctly flow into SCR condition evaluation
- Missing parameter = condition unevaluable = no SCR triggered

---

## TC-37-10 — SCR Points Vary by Panel Type

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The Screening Out point award differs based on the respondent's panel type (Macromill panel vs. Y! Normal/Light panel). Both Quick and Screening survey types are tested.

**Sub-scenarios:**
1. Quick survey: Macromill-panel respondent screened out → receives Macromill-configured SCR points; Y! respondent receives Y!-configured SCR points
2. Screening survey: Same point differentiation by panel type

**Expected Results:**
- SCR point amount matches the respondent's panel type
- Points are correctly stored in the respondent's account after SCR

---
