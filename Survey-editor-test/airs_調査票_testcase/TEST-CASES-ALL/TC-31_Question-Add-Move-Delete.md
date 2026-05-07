# 31 — Question Add / Move / Delete (質問追加・移動・削除)

**Total scripts:** 86 files across multiple test groups  
**Purpose:** Verify that Question IDs (QIDs) and all logic references (questionSelect, choiceSelect, subQuestionSelect, etc.) remain correct and intact when questions are added, moved, or deleted within a survey.

---

## TC-31-01 — Add Questions and Comment Questions at Various Positions

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator creates a survey with a fixed initial structure (AC question, comment questions C1–C4, regular questions Q1–Q3). Questions and comment questions are then inserted at the beginning, middle, and end of the survey. After each addition, the display order and QID assignment must match the expected sequence exactly.

**Setup:**
- Admin user with survey builder access
- Initial structure: AC · C1 · Q1 · C2 · Q2 · C3 · Q3 · C4 (all SAR or MAC type)
- Question text includes the original position label (e.g., "追加前Q1") to track QID shifts

**Steps:**
1. Admin creates initial survey structure with 4 comment questions and 3 regular questions.
2. Admin adds a new question after Q1 (middle of survey) — labels it "追加後Q2".
3. Admin verifies the order is now: AC · C1 · Q1 · Q2(追加後) · C2 · Q3 · C3 · Q4 · C4.
4. Admin adds another question after Q3 and after Q5 (current last question).
5. Admin adds comment questions after C1 (middle) and after C6 (last comment).
6. Admin adds a question at the very beginning (before C1) and at the very end.
7. After all additions, admin verifies the final display order and QID labels match the expected sequence exactly.

**Expected Results:**
- Each added question appears in the correct position immediately after insertion.
- QID numbers shift correctly — all downstream questions renumber.
- Comment questions added at any position appear in the correct order.
- The final survey structure matches the expected sequence with all labels correct.

---

## TC-31-02 — Add Questions with Sub-Question Select (SubQ) Logic

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A survey uses 項目セレクト (subQuestionSelect / item-select) logic where a downstream question's sub-questions are controlled by a source question's answer. Questions are added before and after the source/target questions, and the logic references must remain intact after the add operation.

**Setup:**
- Survey with subQuestionSelect logic linking Q1 → Q2
- Both Q1 (SAP or MAC type) and Q2 (matrix type) are present

**Steps:**
1. Admin creates a survey with subQuestionSelect logic configured between Q1 and Q2.
2. Admin adds a new question before Q1.
3. Admin verifies the logic reference updates: Q1 becomes Q2, Q2 becomes Q3 — and the subQuestionSelect link still points to the correct questions.
4. Admin adds a question between Q1 and Q2.
5. Admin verifies logic is not broken.

**Expected Results:**
- Logic references update automatically after question addition.
- subQuestionSelect link remains pointing to the correct source and target questions.
- Preview shows correct behavior after the addition.

---

## TC-31-03 — Move Questions and Verify Logic Reference Integrity

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Questions are moved up or down within a survey. When a source question is moved past a target question (or vice versa), logic that references the source must remain valid. If a question is moved in a way that creates a forward-reference (source appears after target), the logic should be cleared or flagged.

**Setup:**
- Survey with multiple question types and logic rules (questionSelect, choiceSelect, etc.)
- At least one logic chain between Q1 → Q3

**Steps:**
1. Admin creates survey with logic between Q1 (source) and Q3 (target).
2. Admin moves Q3 above Q1 (creating a forward-reference).
3. Admin verifies: logic is auto-cleared or an error is shown.
4. Admin moves Q1 below Q3 (restoring correct order).
5. Admin re-adds the logic and saves.

**Expected Results:**
- Moving questions that creates an invalid forward-reference clears or flags the logic.
- Moving questions within a valid order preserves logic references.
- QID labels update correctly after each move.

---

## TC-31-04 — Delete Questions and Verify Logic Auto-Clear

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A source question referenced by multiple logic rules is deleted. All logic rules that reference the deleted question must be automatically cleared. QIDs of remaining questions must renumber correctly.

**Setup:**
- Survey with Q1 as the source for: questionSelect on Q3, choiceSelect on Q4, subQuestionSelect on Q5
- All question types: SAR, MAC, SAP, MTS

**Steps:**
1. Admin creates survey with logic from Q1 to Q3, Q4, Q5.
2. Admin verifies all logic is configured correctly.
3. Admin deletes Q1.
4. Admin verifies: Q3, Q4, Q5 (now Q2, Q3, Q4) have their logic auto-cleared.
5. Admin verifies QID renumbering is correct for all remaining questions.

**Expected Results:**
- Deleting a source question clears all dependent logic automatically.
- No orphaned logic references remain.
- Remaining questions renumber from Q1 sequentially.
- Editor does not show errors after deletion.

---

## TC-31-05 — Choice Randomization After Add / Move / Delete

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A question with choice randomization is present in the survey. Questions are added before it and after it. Randomization settings must be preserved regardless of position changes.

**Setup:**
- Survey with one SAR/MAC question with choice randomization enabled
- Additional questions added around it

**Steps:**
1. Admin creates a survey with a randomized-choice question (e.g., Q1 with rand=random).
2. Admin adds a new question before Q1.
3. Admin verifies Q1 (now Q2) still has randomization enabled.
4. Admin adds a question after Q1 and moves the original Q1 to the end.
5. Admin verifies randomization is preserved regardless of position.

**Expected Results:**
- Randomization settings are preserved after add, move, or position change.
- Preview shows randomized choices at the correct question regardless of QID.

---
