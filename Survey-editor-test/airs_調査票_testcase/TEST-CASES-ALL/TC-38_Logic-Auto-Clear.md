# 38 — Logic Auto-Clear (ロジック解除)

**Total scripts:** 1 main test file (in `selenium/` subfolder)  
**Purpose:** Verify that when a source question is modified (type change, deletion), logic rules referencing it are automatically cleared to prevent orphaned/broken logic.

---

## TC-38-01 — Logic Auto-Clear When Source Question Is Modified

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator builds a survey with logic rules (question-select, choice-select, sub-question-select, etc.) referencing a source question. The admin then changes the source question's type or deletes it entirely. The system must automatically clear all dependent logic to avoid invalid references.

**Setup:**
- Admin user with survey builder access
- Survey with multiple question types, each having logic rules pointing to one source question

**Steps:**
1. Admin creates a survey with a source question (e.g., SAR) and adds logic rules on downstream questions that reference it (questionSelect, choiceSelect, subQuestionSelect, matrixInclusion, countMatrix, screeningOut, prohibition, exclusive).
2. Admin changes the source question's question type (e.g., SAR → MAC).
3. Admin verifies each downstream logic rule.
4. Admin deletes the source question.
5. Admin verifies each downstream logic rule again.

**Expected Results:**
- When source question type changes: all logic rules referencing it are automatically cleared (set back to "not configured").
- When source question is deleted: all logic rules referencing it are automatically cleared.
- No orphaned logic references remain after either modification.
- Editor does not show errors or broken references after auto-clear.

---
