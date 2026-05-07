# 41 — Conditional Expression Configuration and Evaluation / 条件式の設定・評価

**Total scripts:** ~216 files across 5 subdirectories  
**Purpose:** Verify that conditional expression functions (snotall, count, countif, num) and the condition-expression input UI work correctly — both in configuration (editor-side validation) and at answer time (runtime evaluation). These functions drive logic conditions for questionSelect, choiceSelect, screeningOut, and other features.

---

## TC-41-01 — `snotall()` Function: Configuration Validation

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The `snotall()` function evaluates whether a set of choices contains no response for ALL sub-questions or choices (i.e., "not answered for all"). Tests verify that the function can be configured, validates correctly, and shows appropriate error messages.

**Setup:**
- Survey with a MAC or MTM question (Q1) as the source
- A logic condition using `snotall(Q1, "1,2,3")` as the expression

**Steps (Preparation / 事前準備):**
1. Create the base survey with the required question types.
2. Configure a logic rule using `snotall()` as the condition expression.

**Steps (Configuration Validation / 1_設定時):**
3. Attempt to save the condition with missing required arguments → verify error message.
4. Attempt to use `snotall()` on a question type that does not support it → verify error.
5. Configure a valid `snotall()` expression → verify it saves without error.
6. Verify the saved condition expression text is displayed correctly on the logic settings screen.

**Expected Results:**
- Invalid `snotall()` configurations produce clear error messages
- Valid expressions save and display correctly
- Expression is shown in the format `snotall(Qx, "values")`

---

## TC-41-02 — `snotall()` Function: Runtime Evaluation

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** At answer time, the `snotall()` function evaluates correctly based on what the respondent has selected. The logic condition correctly triggers or does not trigger depending on whether the specified choices are all unanswered.

**Steps (Runtime / 2_動作時):**
1. Open the survey with the `snotall()` condition configured.
2. Answer Q1 in a way that does NOT satisfy the condition (some matching choices selected) → logic condition is false; dependent question/choice appears.
3. Answer Q1 in a way that satisfies the condition (none of the matching choices selected) → logic condition is true; dependent question/choice disappears.

**Expected Results:**
- `snotall()` evaluates to true only when all specified choices are unanswered
- Dependent logic (show/hide) reacts correctly in real-time

---

## TC-41-03 — `snotall()` Function: Used Within a Survey (Internal Logic)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `snotall()` function is used inside the survey's condition expressions for various logic types: select condition, choice select, column select, row select, input select, item select, internal screening-out, client screening, IF tag, and response quota (回答割付).

**Sub-scenarios (3_調査票内 / Files 01–10):**
1. Condition expression error check — invalid `snotall()` usage in each context
2. Select condition using `snotall()`
3. Choice select using `snotall()`
4. Column select (表頭セレクト) using `snotall()`
5. Row select (表側セレクト) using `snotall()`
6. Input select / item select using `snotall()`
7. Internal screening-out (SCR) using `snotall()`
8. Client SCR using `snotall()`
9. IF tag condition using `snotall()`
10. Response quota (回答割付) using `snotall()`

**Expected Results:**
- `snotall()` functions correctly as a condition in all these logic contexts
- Evaluation triggers the correct show/hide or SCR behavior at answer time

---

## TC-41-04 — `count()` Function: Counting Selected Choices

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `count()` function counts how many choices a respondent has selected from a MAC or similar question. This count is then used in a condition expression (e.g., `count(Q1) >= 2`).

**Configuration validation tests (設定):**
1. Configure `count(Q1)` with a valid MAC question → saves without error.
2. Configure `count()` with an invalid question type → error shown.
3. Configure `count()` with an out-of-range question number → error shown.
4. Configure `count()` with a question that does not exist → error shown.

**Runtime tests (回答 1–8):**
5. Respondent selects 0 choices (no answer) → count = 0; condition `count(Q1) >= 2` is false.
6. Respondent selects exactly 1 choice → count = 1; condition false.
7. Respondent selects exactly 2 choices → count = 2; condition true (threshold met).
8. Respondent selects 3 or more choices → count > threshold; condition still true.
9. Condition comparison operators: >, >=, <, <=, ==, != all evaluate correctly.
10. Combined condition: `count(Q1) >= 2 AND count(Q2) <= 3`.
11. `count()` used with choiceSelect, questionSelect, and SCR conditions.
12. Answer after editing the condition → reconfigured expression evaluates correctly.

**Expected Results:**
- count() returns the exact number of selected choices
- All comparison operators work correctly
- Combined expressions with AND/OR are evaluated correctly

---

## TC-41-05 — `countif()` Function: Counting Choices That Match a Value

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `countif()` function counts how many choices match a specific value or set of values (e.g., `countif(Q1, "1,2") >= 1` means "at least one of choices 1 or 2 was selected"). Tests verify configuration and runtime evaluation.

**Configuration validation tests:**
1. Valid `countif(Q1, "1,2")` expression → saves without error.
2. Empty value list → error.
3. Invalid choice numbers → error.
4. Out-of-range question → error.

**Runtime tests:**
5. Source question answered with matching choices → condition true.
6. Source question answered with non-matching choices only → condition false.
7. countif used with matrix question (specify sub-question + value).
8. Combined with AND/OR operators in complex expressions.
9. Used in choiceSelect, questionSelect, SCR conditions.

**Expected Results:**
- `countif()` correctly counts only the matching choices
- Comparison result correctly triggers or suppresses logic

---

## TC-41-06 — `num()` Function: Numeric Value Comparison from FA Inputs

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `num()` function reads a numeric value from a free-answer (FA) input field and compares it to a threshold. This is used in conditions such as `num(Q1) > 30`.

**Configuration validation tests:**
1. Valid `num(Q1) > 30` expression where Q1 is a numeric FA field → saves without error.
2. Using `num()` on a non-FA question type → error.
3. Invalid comparison operator → error.
4. Out-of-range question reference → error.

**Runtime tests:**
5. Respondent enters a value above the threshold → condition true.
6. Respondent enters a value below the threshold → condition false.
7. Respondent enters a value equal to the threshold → equality comparison works correctly.
8. Respondent leaves the FA blank (no answer) → `num()` returns 0 or null; condition evaluates as false.
9. Respondent enters non-numeric text (if numeric validation not enforced separately) → evaluated gracefully.

**Expected Results:**
- `num()` extracts and compares the numeric FA value correctly
- Blank input is treated as 0 or no value; condition evaluates false
- All comparison operators work correctly

---

## TC-41-07 — Condition Expression Input UI (条件式入力補助インタフェース)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The condition expression editor provides a UI for building conditions without typing raw expressions. Tests verify the UI correctly sets conditions, validates input, and generates the correct expression text.

**Setup:**
- Survey with Q1 (SAR/MAC), Q2 (SAR/MAC), and an age attribute question
- Logic settings screen where condition expression UI is accessible

**Steps:**
1. Open the condition settings UI.
2. Select a question (Q1) from the dropdown → UI loads its choices.
3. Select a choice from Q1 → expression `(select condition: Q1=1)` is generated.
4. Add a second condition row with OR operator → select Q1, choice 2 → expression becomes `Q1=1 OR Q1=2`.
5. Attempt to save with "Age" selected but no value entered → error message shown ("年齢は必ず入力してください").
6. Enter age value and save → expression generated correctly.
7. Use AND operator between two conditions → verify expression uses AND logic.
8. Use OR + AND combination → verify operator precedence is correct.
9. Verify the generated expression string matches what appears in the logic settings summary.

**Expected Results:**
- UI correctly generates condition expressions from dropdown/checkbox selections
- Required fields are validated before save
- AND/OR operators produce correct logical expressions
- Expression text is readable and saved correctly in the survey definition

---
