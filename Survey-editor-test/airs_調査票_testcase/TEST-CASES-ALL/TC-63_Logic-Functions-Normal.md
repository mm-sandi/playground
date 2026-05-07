# 63 — Logic and Function Combinations: Normal Answer Mode / ロジックと関数の組合せ（通常）

**Total scripts:** ~270 files across 7 logic categories  
**Purpose:** Verify that all combinations of conditional expression functions (any, notany, all, notall, snotall, match, count, nvl, num, countif) work correctly across all 7 logic types when respondents answer normally (non-auto, non-non-applicable mode).

**How tests are structured:**  
Each logic category has a `Research/` folder (survey creation scripts) and an `Answer/` folder (respondent answer scripts). Each condition function is tested with two answer variants — one that triggers the condition (shows/hides correctly) and one that does not.

---

## TC-63-01 — Select Condition (セレクト条件) × All Condition Functions

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** A question is shown or hidden based on a select condition (questionSelect). The condition is evaluated using each of the available condition functions. Admin creates the survey; a respondent answers it.

**Condition functions tested:**
| Function | Description |
|----------|-------------|
| `any(Qn, "values")` | True if any of the specified choices were selected |
| `notany(Qn, "values")` | True if none of the specified choices were selected |
| `all(Qn, "values")` | True if all specified choices were selected |
| `notall(Qn, "values")` | True if not all specified choices were selected |
| `snotall(Qn, "values")` | True if specified choices are all unanswered |
| `match(Qn, "values")` | True if selection exactly matches the specified set |
| `count(Qn) operator N` | True if number of selected choices meets the comparison |
| `count(Qn, "values") operator N` | True if count of specific choices meets the comparison |
| `nvl(Qn)` | True if question has no answer (null value) |
| `num(Qn) operator N` | True if FA numeric value meets the comparison |
| `countif(Qn, "values")` | True if count of specified values meets condition (single argument) |
| `countif(Qn, "values", N)` | True if count meets condition (three-argument form) |

**Steps (per function):**
1. Admin creates a survey: Q1 (source, MAC/SAR), Q2 (target, shown/hidden by condition).
2. Configure select condition on Q2 using the function above.
3. Respondent A answers Q1 in a way that satisfies the condition → Q2 is shown; respondent answers Q2.
4. Respondent B answers Q1 in a way that does NOT satisfy the condition → Q2 is hidden; survey skips Q2.

**Expected Results:**
- Q2 appears only when the condition evaluates to true
- Q2 is hidden when the condition evaluates to false
- Answer data for hidden Q2 is recorded as non-applicable

---

## TC-63-02 — Choice Select (選択肢セレクト) × All Condition Functions

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Individual choices in a target question are shown or hidden based on a choiceSelect condition. Same 12 condition functions as TC-63-01.

**Steps (per function):**
1. Admin creates a survey: Q1 (source), Q2 (target with choiceSelect on some choices).
2. Configure choiceSelect condition on specific choices of Q2 using each function.
3. Respondent A answers Q1 to trigger condition → filtered choices appear in Q2.
4. Respondent B answers Q1 to not trigger condition → all choices appear in Q2 (or target choices are hidden).

**Expected Results:**
- Correct choices are shown/hidden based on condition evaluation
- Hidden choices are recorded as "no answer" (not selected, not in ANSWER_DETAIL)

---

## TC-63-03 — Condition Expression Error Check (条件式エラーチェック) × All Functions

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The admin attempts to save invalid condition expressions using each function. The system must reject invalid inputs and display appropriate error messages.

**Errors tested (per function):**
- Missing required arguments
- Out-of-range question reference
- Invalid comparison operator
- Argument type mismatch (e.g., passing text where a number is expected)
- Referencing a future question (forward reference)

**Expected Results:**
- All invalid expressions produce clear error messages at save time
- Valid expressions save without error

---

## TC-63-04 — Row Select (表側セレクト) × All Condition Functions

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Sub-questions (rows) of a matrix question are shown or hidden based on a subQuestionSelect condition evaluated with each condition function.

**Steps (per function):**
1. Admin creates a survey: Q1 (source), Q2 (matrix target with row-select on specific rows).
2. Configure row-select condition using each function.
3. Respondent A answers Q1 to trigger condition → specific rows are hidden in Q2.
4. Respondent B answers Q1 differently → all rows are shown.

**Expected Results:**
- Hidden rows are not displayed to the respondent
- Hidden row answer data is recorded as non-applicable

---

## TC-63-05 — Column Select (表頭セレクト) × All Condition Functions

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Columns (表頭) of a matrix question are shown or hidden based on a column-select condition.

**Steps (per function):**
1. Admin creates a survey with Q1 (source) and Q2 (matrix with column-select).
2. Configure column-select condition on specific columns of Q2.
3. Respondents answer Q1 to trigger/not trigger the condition.

**Expected Results:**
- Columns appear/disappear based on condition evaluation
- Hidden column choices are not available for selection and not recorded

---

## TC-63-06 — Input Select (入力欄セレクト) × All Condition Functions

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** FA input fields (free answer boxes) in a target question are shown or hidden based on an input-select condition.

**Steps (per function):**
1. Admin creates a survey: Q1 (source), Q2 (target with FA fields selectively shown by condition).
2. Configure input-select condition on each FA field.
3. Respondent A triggers condition → FA field appears.
4. Respondent B does not trigger → FA field is hidden.

**Expected Results:**
- FA input fields show/hide based on condition
- Hidden FA input data is treated as no answer

---

## TC-63-07 — Item Select (項目セレクト) × All Condition Functions

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Rating or ranking items in a target question are shown or hidden based on an item-select condition.

**Steps (per function):**
1. Admin creates a survey: Q1 (source), Q2 (RAT or RNK target with item-select).
2. Configure item-select condition.
3. Respondents answer Q1 to trigger/not trigger the condition.

**Expected Results:**
- Correct items are shown/hidden
- Hidden items are not selectable and are recorded as non-applicable

---
