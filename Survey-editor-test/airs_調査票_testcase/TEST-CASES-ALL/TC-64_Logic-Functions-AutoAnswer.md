# 64 — Logic and Function Combinations: Auto-Answer Mode / ロジックと関数の組合せ（自動回答）

**Total scripts:** ~282 files across 8 logic categories  
**Purpose:** Verify that all combinations of conditional expression functions (any, notany, all, notall, snotall, match, count, nvl, num, countif) work correctly across all 7 logic types when the survey uses **auto-answer mode** (自動回答). An additional category tests auto-answer combined with FA input.

**Difference from directory 63 (Normal):**  
In auto-answer mode, the system automatically selects answers based on pre-configured rules or system logic — the respondent does not manually interact. This tests whether the logic conditions are still evaluated correctly even when answers are filled in automatically.

---

## TC-64-01 — Select Condition (セレクト条件) × All Condition Functions [Auto-Answer]

**Scope:** Admin / System  
**Platform:** Desktop

**Scenario:** Same as TC-63-01 (question shown/hidden by select condition), but answers are provided automatically by the auto-answer mechanism rather than by a human respondent.

**Condition functions tested:** any, notany, all, notall, snotall, match, count(1 arg), count(2 args), nvl, num, countif(1 arg), countif(3 args)

**Steps (per function):**
1. Admin creates the survey with auto-answer configured on Q1.
2. Configure select condition on Q2 using the function.
3. Run auto-answer — system fills Q1 with the trigger value → Q2 appears and is auto-answered.
4. Run auto-answer with non-trigger value → Q2 is hidden; recorded as non-applicable.

**Expected Results:**
- Condition correctly evaluates auto-filled answers
- Auto-answered questions respect the show/hide logic
- Non-applicable questions are recorded correctly even in auto-answer mode

---

## TC-64-02 — Choice Select (選択肢セレクト) × All Condition Functions [Auto-Answer]

**Scope:** Admin / System  
**Platform:** Desktop

**Scenario:** Choices in a target question are shown/hidden based on condition, with auto-answer filling answers automatically.

**Expected Results:**
- Choice filtering works correctly with auto-filled source answers
- Auto-answered hidden choices are not recorded

---

## TC-64-03 — Condition Expression Error Check (条件式エラーチェック) × All Functions [Auto-Answer]

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Same as TC-63-03 — validates that invalid condition expressions are rejected at configuration time, regardless of answer mode.

**Expected Results:**
- Invalid expressions produce error messages at save time
- Valid expressions save without error

---

## TC-64-04 — Row Select (表側セレクト) × All Condition Functions [Auto-Answer]

**Scope:** Admin / System  
**Platform:** Desktop

**Scenario:** Matrix sub-questions (rows) are shown/hidden based on condition, with auto-answer providing answers for the source question.

**Expected Results:**
- Row filtering evaluates correctly with auto-filled source answers
- Hidden rows recorded as non-applicable

---

## TC-64-05 — Column Select (表頭セレクト) × All Condition Functions [Auto-Answer]

**Scope:** Admin / System  
**Platform:** Desktop

**Scenario:** Matrix columns are shown/hidden based on condition, with auto-answer mode active.

**Expected Results:**
- Column filtering works with auto-filled source answers

---

## TC-64-06 — Input Select (入力欄セレクト) × All Condition Functions [Auto-Answer]

**Scope:** Admin / System  
**Platform:** Desktop

**Scenario:** FA input fields shown/hidden by condition, auto-answer mode active.

**Expected Results:**
- FA visibility logic evaluates correctly with auto-filled source answers

---

## TC-64-07 — Item Select (項目セレクト) × All Condition Functions [Auto-Answer]

**Scope:** Admin / System  
**Platform:** Desktop

**Scenario:** Rating/ranking items shown/hidden by condition, auto-answer mode active.

**Expected Results:**
- Item visibility logic evaluates correctly with auto-filled source answers

---

## TC-64-08 — Auto-Answer Combined with FA Input (自動回答＋FA)

**Scope:** Admin / System  
**Platform:** Desktop

**Scenario:** Auto-answer mode is combined with questions that have free-answer (FA) text fields. Verify that auto-answer correctly populates both choice selections AND FA text values, and that logic depending on FA values (e.g., `num()` conditions) evaluates correctly.

**Steps:**
1. Create a survey with a question that has an FA field.
2. Configure auto-answer to fill both the choice and the FA text value.
3. Configure a condition using `num()` that depends on the FA value.
4. Run auto-answer with a value that triggers the condition → dependent question appears.
5. Run auto-answer with a value that does not trigger → dependent question is hidden.

**Expected Results:**
- Auto-answer fills FA text fields correctly
- `num()` and other FA-dependent conditions evaluate correctly on auto-filled values
- Logic-dependent questions show/hide based on auto-filled FA content

---
