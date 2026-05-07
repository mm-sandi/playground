# 65 — Logic and Function Combinations: Non-Applicable Source / ロジックと関数の組合せ（非該当）

**Total scripts:** ~201 files across 7 logic categories  
**Purpose:** Verify that all combinations of conditional expression functions work correctly across all 7 logic types when the **source question itself is non-applicable** (非該当 — hidden by prior logic). When the source question is non-applicable, the system must correctly handle how its dependent conditions evaluate — typically, conditions that depend on a non-applicable source should also treat the target as non-applicable.

**Key difference from directories 63 and 64:**  
The source question (Q1) has been hidden by a prior logic rule before Q2's condition is evaluated. This tests the edge case: "what happens when a condition's source question was never shown to the respondent?"

---

## TC-65-01 — Select Condition (セレクト条件) × All Condition Functions [Non-Applicable Source]

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Q2 has a select condition depending on Q1. Q1 is hidden (non-applicable) due to a prior logic rule. The system must evaluate Q2's condition with Q1 in a non-applicable state.

**Condition functions tested:** any, notany, all, notall, snotall, match, count(1 arg), count(2 args), nvl, num, countif(1 arg), countif(3 args)

**Steps (per function):**
1. Admin creates survey: Q0 (choice question), Q1 (shown only if Q0=specific choice), Q2 (shown based on condition on Q1).
2. Respondent answers Q0 in a way that hides Q1 (Q1 becomes non-applicable).
3. System evaluates Q2's condition — Q1 is non-applicable.

**Expected Behavior:**
- When source (Q1) is non-applicable:
  - Conditions like `any()`, `all()` evaluate as false (no answer = no match)
  - `notany()`, `notall()` may evaluate as true (no answer = "not any selected")
  - `snotall()` evaluates as true (all are "not answered")
  - `nvl()` evaluates as true (null/no answer)
  - `num()` evaluates as 0 (no FA value)
  - `count()` returns 0
- Q2's visibility reflects the correct evaluation
- All non-applicable questions are recorded as 非該当 in ANSWER_DETAIL

**Expected Results:**
- System does not error when evaluating conditions whose source is non-applicable
- Condition evaluates deterministically and consistently with the specification
- Answer data records non-applicable correctly for both Q1 and Q2 (when Q2 is also hidden)

---

## TC-65-02 — Choice Select (選択肢セレクト) × All Condition Functions [Non-Applicable Source]

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Choice filtering on Q2 depends on Q1, which is non-applicable. Choice visibility must be correctly determined.

**Expected Results:**
- Choice filtering evaluates correctly when source is non-applicable
- Hidden choices recorded as "no answer"

---

## TC-65-03 — Condition Expression Error Check (条件式エラーチェック) × All Functions [Non-Applicable Source]

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Invalid condition expressions are rejected at configuration time. This test confirms that error checking works correctly regardless of the non-applicable scenario (errors are always caught at configuration, not at run time).

**Expected Results:**
- Invalid expressions produce error messages at save time
- Valid expressions save without error

---

## TC-65-04 — Row Select (表側セレクト) × All Condition Functions [Non-Applicable Source]

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Matrix row visibility depends on Q1 (source), which is non-applicable. Row visibility must be determined correctly.

**Expected Results:**
- Row visibility correctly handles non-applicable source
- Non-applicable rows recorded correctly

---

## TC-65-05 — Column Select (表頭セレクト) × All Condition Functions [Non-Applicable Source]

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Matrix column visibility depends on Q1 (non-applicable). Column visibility must be correctly determined.

**Expected Results:**
- Column visibility correctly handles non-applicable source

---

## TC-65-06 — Input Select (入力欄セレクト) × All Condition Functions [Non-Applicable Source]

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** FA input field visibility depends on Q1 (non-applicable).

**Expected Results:**
- FA input visibility correctly handles non-applicable source
- Hidden FA input treated as no answer

---

## TC-65-07 — Item Select (項目セレクト) × All Condition Functions [Non-Applicable Source]

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Rating/ranking item visibility depends on Q1 (non-applicable).

**Expected Results:**
- Item visibility correctly handles non-applicable source
- Non-applicable items recorded as 非該当

---
