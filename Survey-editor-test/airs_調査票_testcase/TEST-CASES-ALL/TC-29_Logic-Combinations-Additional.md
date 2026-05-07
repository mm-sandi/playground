# 29 — Logic Combinations: Additional Cases / ロジック組合せ_追加分

**Total scripts:** ~508 files across 6 logic combination categories  
**Purpose:** Additional logic combination tests added after directory 27. This directory focuses on matrix-specific piping/reverse-piping variants and sub-question (副質問) piping — logic types not fully covered in the original directory 27 test suite.

---

## TC-29-01 — Select Condition: Profile/Attribute Question Support (セレクト条件_属性対応分)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** A select condition uses an attribute question (profile question, f_sar/f_mac/etc.) as the source instead of a regular survey question. This tests that the condition expression can reference attribute questions.

**Setup:**
- Survey with an attribute question (f_sar or f_mac) and a regular question Q1 with a select condition based on the attribute answer.

**Steps:**
1. Admin creates a survey with attribute question as the select condition source.
2. Respondent answers the attribute question with the triggering value → Q1 is shown.
3. Respondent answers with a non-triggering value → Q1 is hidden.

**Expected Results:**
- Select conditions correctly evaluate attribute question answers
- Non-applicable Q1 is recorded correctly when attribute condition is not met

---

## TC-29-02 — Matrix Piping (マトリクスパイピング)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The answer from a matrix question (MTS or MTM) is piped into another question. Specifically, the column headers (表頭) or row-column combinations from the source matrix are used as choices in a target question.

**Combination patterns (111 HTML files):**
- MTS row answer piped to SAR/MAC choices: choices selected in Q1's matrix become choices in Q2
- MTM multi-select matrix answer piped to MAC: each selected cell in Q1 becomes a choice in Q2
- Matrix piping + row select: piped matrix content is also further filtered by row select
- Matrix piping + question select: target question with piped matrix content is conditionally shown
- Matrix piping + page break: source and target on different pages

**Steps (per pattern):**
1. Admin creates a survey with matrix piping from Q1 (MTS/MTM) to Q2 (SAR/MAC or another matrix).
2. Respondent answers Q1 (selecting specific cells in the matrix).
3. Verify Q2 shows choices corresponding to Q1's selected cells.
4. Respondent answers Q2 using the piped choices.

**Expected Results:**
- Q2's choices correctly reflect the selected cells/answers from the source matrix
- Answer data for Q2 references original matrix cell identifiers

---

## TC-29-03 — Matrix Reverse Piping (マトリクス逆パイピング)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The reverse of matrix piping — Q2 shows the matrix cells/answers NOT selected in Q1.

**Combination patterns (108 HTML files):**
- MTS reverse piping: Q2 contains only the choices NOT selected in Q1's matrix
- MTM reverse piping: for each row, Q2 shows the columns NOT selected in Q1's corresponding row
- Matrix reverse piping + row select
- Matrix reverse piping + question select
- Matrix reverse piping + choice randomization

**Steps (per pattern):**
1. Admin creates a survey with matrix reverse piping configured.
2. Respondent selects specific cells in Q1's matrix.
3. Verify Q2 shows exactly the cells NOT selected in Q1.

**Expected Results:**
- Q2's choices = Q1's total cells minus Q1's selected cells (per row for MTM)
- Combined logic (row select, etc.) further filters the reverse-piped content correctly

---

## TC-29-04 — Additional Logic Combination Tests (ロジックの組み合わせテスト_追加分)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Additional test cases covering combinations not present in directories 25 or 27. These are edge cases and multi-level logic chains.

**Coverage (42 HTML files):**
- Three-level logic chain: Q1 → Q2 (select) → Q3 (piping from Q2)
- Simultaneous piping + reverse piping: Q2 piped from Q1 AND Q3 reverse-piped from Q1
- Piping into a question that also has a question select condition
- Reverse piping + item select combination
- Multiple select conditions on the same target question (AND/OR)
- Row select + column select on the same matrix question simultaneously

**Steps:**
1. Admin creates a survey with the specified multi-level or combined logic.
2. Respondent answers in ways that trigger and do not trigger each condition.
3. Verify behavior matches specifications for each combination.

**Expected Results:**
- Multi-level logic chains evaluate in correct order
- Multiple logic types on the same question apply all constraints simultaneously
- Answer data is correctly recorded for all combinations

---

## TC-29-05 — Sub-Question Piping (副質問パイピング)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Sub-questions (副質問 — rows in a matrix question) from Q1 are piped into another question as either sub-questions or choices. This is different from matrix piping (TC-29-02) in that it pipes the row labels themselves, not the selected cell values.

**Combination patterns (129 HTML files):**
- SAR/MAC sub-question piping: the labels of Q1's sub-questions appear as choices in Q2
- MTS sub-question piping: Q1's row labels appear as Q2's row labels
- MTM sub-question piping: Q1's row labels appear in Q2 as rows
- Sub-question piping + question select: piped rows further filtered by condition
- Sub-question piping + row select: some piped rows additionally hidden by row-select
- Sub-question piping + randomization: Q1's rows are randomized; piping uses original order

**Steps (per pattern):**
1. Admin creates a survey with sub-question piping from Q1 to Q2.
2. Respondent answers Q1.
3. Verify Q2's sub-questions (rows) display the same labels as Q1's sub-questions.
4. Respondent answers Q2 using the piped sub-questions.

**Expected Results:**
- Q2's sub-questions (row labels) correctly match Q1's sub-question labels
- Original sub-question order is preserved regardless of randomization
- Answer data uses Q2's own sub-question IDs for storage

---

## TC-29-06 — Sub-Question Reverse Piping (副質問逆パイピング)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Sub-question reverse piping shows in Q2 the sub-questions (rows) NOT answered (or not selected) in Q1.

**Combination patterns (117 HTML files):**
- MTS sub-question reverse piping: Q2's rows = Q1's rows that had no answer
- MTM sub-question reverse piping: Q2's rows = Q1's rows where no column was selected
- Sub-question reverse piping + row select: additional filtering on top of reverse-piped rows
- Sub-question reverse piping + question select
- Sub-question reverse piping + randomization

**Steps (per pattern):**
1. Admin creates a survey with sub-question reverse piping from Q1 to Q2.
2. Respondent answers some (but not all) sub-questions in Q1.
3. Verify Q2 shows only the sub-questions that were NOT answered in Q1.

**Expected Results:**
- Q2's rows = Q1's unanswered sub-question rows
- If all Q1 sub-questions were answered, Q2 has no rows and is treated as non-applicable
- Combined logic applies correctly on top of reverse-piped content

---
