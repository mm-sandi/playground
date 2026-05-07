# 25 — Logic × Question Type Combinations / ロジック質問タイプ組合せ

**Total scripts:** ~1,092 files across 15 logic categories  
**Purpose:** Verify that each logic feature works correctly with ALL supported question types as both source and target. A source question provides the condition; a target question is shown, hidden, or modified based on that condition. This is the most comprehensive logic test suite.

**Test structure:**  
Each logic category has `Research/` (survey creation) and `Answer/` (respondent answer) folders. Research scripts create 5–26 surveys, each testing a different source-type or target-type combination. Answer scripts run the respondent path for each survey.

---

## TC-25-01 — Select Condition (セレクト条件 / questionSelect) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** A question (Q2) is shown or hidden based on the respondent's answer to Q1 (the source). All valid source question types are tested as Q1, and all valid target question types as Q2.

**Source question types:** SAR, MAC, SAP, SAS, FAL, FAS, RAT, RNK, MTS, MTM, MTT  
**Target question types:** SAR, MAC, SAP, SAS, FAL, FAS, RAT, RNK, MTS, MTM, MTT (each with source variations)

**Test patterns (5 survey variants):**
1. SAR source → multiple target types
2. MAC source → multiple target types
3. MTS/MTM source → matrix-specific targets
4. FAL/FAS source (text-based conditions)
5. RAT/RNK source → numeric or ranked conditions

**Steps (per variant):**
1. Admin creates a survey with Q1 (source type), Q2 (target type), and a select condition linking them.
2. Respondent A answers Q1 in a way that satisfies the condition → Q2 is displayed; respondent answers Q2.
3. Respondent B answers Q1 differently → Q2 is hidden; recorded as non-applicable.

**Expected Results:**
- Q2 correctly appears/disappears based on Q1's answer across all question type combinations
- Non-applicable data is recorded correctly for hidden Q2

---

## TC-25-02 — Piping (パイピング) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** A choice or answer text from Q1 is "piped" (copied) into Q2's choice list or question text. Tests all combinations of source and target question types.

**Piping types:**
- Choice piping: choices selected in Q1 appear as choices in Q2
- Text piping: Q1's answer text appears inline in Q2's question text (using `<answer>` tag)

**Test patterns (26 Research files → 26 surveys):**
- SAR → SAR, SAR → MAC, SAR → MTS, SAR → MTM, MAC → SAR, MAC → MAC, etc.
- Each combination tests: piping from source, answer in a way that selects certain choices, verify Q2 shows only the piped choices

**Steps (per combination):**
1. Admin creates a survey with piping configured between Q1 and Q2.
2. Respondent selects choices in Q1.
3. Verify Q2 shows exactly the choices selected in Q1 (piped in).
4. Respondent answers Q2 with the available (piped) choices.

**Expected Results:**
- Q2 displays exactly and only the choices piped from Q1
- Answer data for Q2 uses original choice numbers from Q1
- FA text piped from Q1 appears correctly in Q2's question text

---

## TC-25-03 — Input Select (入力欄セレクト) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** FA input fields (free answer boxes) in Q2 are shown or hidden based on Q1's answer. Combinations of question types for Q1 and Q2 are tested.

**Steps:**
1. Admin creates survey with input select condition linking Q1's answer to Q2's FA fields.
2. Respondent A triggers condition → specific FA fields appear in Q2.
3. Respondent B does not trigger → FA fields are hidden.

**Expected Results:**
- FA fields show/hide correctly based on condition evaluation
- Hidden FA values are not recorded

---

## TC-25-04 — Inclusion Check (包含チェック / matrixInclusion) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The inclusion check requires that choices selected in Q2 must be a subset of (or include) choices selected in Q1. Tests across all applicable question type combinations.

**Steps:**
1. Admin creates a survey with Q1 (source) and Q2 (with inclusion check against Q1).
2. Respondent selects choices in Q1.
3. Respondent answers Q2:
   - Selects only choices within Q1's selection → passes validation.
   - Selects a choice NOT in Q1's selection → inclusion check error shown.

**Expected Results:**
- Inclusion violation shows a validation error
- Valid selections within the inclusion constraint are accepted

---

## TC-25-05 — Simultaneous Selection Prohibition (同時禁止チェック) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Two specific choices in the same question (or across questions) cannot both be selected at the same time. The prohibition check enforces this.

**Steps:**
1. Admin creates a survey with simultaneous selection prohibition configured between two choices.
2. Respondent selects both prohibited choices simultaneously → error shown.
3. Respondent selects only one of the prohibited choices → no error.

**Expected Results:**
- Simultaneous selection of prohibited choice pairs triggers a validation error
- Selection of only one prohibited choice is accepted

---

## TC-25-06 — Exclusive Contradiction Check (排他矛盾チェック) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** A choice marked as "exclusive" cannot be selected together with any other choice in the same question. Tests all applicable question types.

**Steps:**
1. Admin creates a MAC question with one choice marked as exclusive.
2. Respondent selects the exclusive choice alone → no error.
3. Respondent selects the exclusive choice AND another choice → error shown.
4. Respondent deselects the exclusive choice → can select multiple non-exclusive choices normally.

**Expected Results:**
- Exclusive choice selected alone is valid
- Exclusive choice selected with any other choice triggers an error

---

## TC-25-07 — Screen Branch (画面分岐) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** A page break with a conditional branch divides the survey. Based on Q1's answer, the respondent is directed to a specific page or section. Tests all question types as the branching source.

**Steps:**
1. Admin creates a survey with a page break and conditional branch based on Q1.
2. Respondent A answers Q1 matching branch condition A → navigates to Section A.
3. Respondent B answers Q1 matching branch condition B → navigates to Section B.

**Expected Results:**
- Respondents are directed to the correct section based on their Q1 answer
- Questions in the non-selected branch are recorded as non-applicable

---

## TC-25-08 — Row Select (表側セレクト) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Sub-questions (rows) in a matrix question Q2 are shown or hidden based on Q1's answer. Tests all valid source types as Q1.

**Steps:**
1. Admin creates a survey with row-select (subQuestionSelect) logic from Q1 to Q2's rows.
2. Respondent A triggers condition → specific rows are hidden in Q2.
3. Respondent B does not trigger → all rows are shown.

**Expected Results:**
- Correct rows appear/disappear based on condition
- Non-applicable rows recorded correctly

---

## TC-25-09 — Row Piping (表側パイピング) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Sub-questions (rows) of a matrix question Q2 are replaced with the answer items from Q1. This is "row piping" — the rows in Q2 reflect what Q1 contained.

**Test patterns (26+ Research files):**
- Various source types (SAR, MAC, FAL, RNK, etc.) piped into matrix rows of MTS, MTM, MTT targets

**Steps:**
1. Admin creates a survey with row piping configured.
2. Respondent answers Q1.
3. Verify Q2's rows contain the piped answers from Q1 (as row labels).

**Expected Results:**
- Q2's rows reflect the answers/choices from Q1
- Piped row data is displayed correctly in the matrix

---

## TC-25-10 — Question Randomization (質問ランダマイズ) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** A block of questions is displayed in random order. The randomization works with all question types.

**Steps:**
1. Admin creates a survey with a question randomization block covering multiple question types.
2. Respondent answers the survey — questions appear in random order.
3. Verify that answer data uses original question numbers (QNO), not display order.

**Expected Results:**
- Questions appear in different orders across different respondents
- Answer data always records original QNO regardless of display order

---

## TC-25-11 — Reverse Piping (逆パイピング) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Reverse piping shows in Q2 only the choices that were NOT selected in Q1. This is the inverse of regular piping.

**Also tested:** Changes to the reverse piping behavior (逆パイピング動作一部変更) — a variation where the reverse piping logic has been partially updated.

**Test patterns (multiple Research files):**
- SAR, MAC, MTS, MTM source types → various targets

**Steps:**
1. Admin creates survey with reverse piping from Q1 to Q2.
2. Respondent selects some choices in Q1.
3. Verify Q2 shows exactly the choices NOT selected in Q1.
4. Respondent answers Q2 using the remaining choices.

**Expected Results:**
- Q2's choices = Q1's total choices minus Q1's selected choices
- Behavior after the partial change update is consistent with the updated spec

---

## TC-25-12 — Choice Group Randomization (選択肢グループランダマイズ) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Choices are grouped into sets that randomize as units. The order of groups is random, but choices within each group maintain their relative order.

**Steps:**
1. Admin configures choice groups and enables group randomization.
2. Respondent sees groups in random order.
3. Verify that within each group, choice order is preserved.
4. Verify answer data uses original choice numbers.

**Expected Results:**
- Groups appear in different orders across respondents
- Within-group choice order is always preserved
- Answer data records original choice numbers

---

## TC-25-13 — Choice Randomization (選択肢ランダマイズ) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Individual choices within a question are displayed in random order. Tests all question types that support choice randomization.

**Steps:**
1. Admin enables choice randomization on a question.
2. Respondent sees choices in random order.
3. Answer data records the original (editor) choice number, not the display position.

**Expected Results:**
- Choices appear in random order to respondents
- Answer VALUE always stores original choice index

---

## TC-25-14 — Item Select (項目セレクト) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Items (rating items, ranking items) in RAT or RNK question Q2 are shown or hidden based on Q1's answer.

**Steps:**
1. Admin creates a survey with item-select condition from Q1 to Q2's items.
2. Respondent A triggers condition → specific items are hidden.
3. Respondent B does not trigger → all items shown.

**Expected Results:**
- Items appear/disappear correctly
- Hidden items recorded as non-applicable

---

## TC-25-15 — Ranking Answer Check (順位回答チェック / RNK Validation) × All Question Types

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The ranking question (RNK) has validation rules: required count, duplicate rank prevention. Tests verify these validations work when RNK is used as source or target in logic combinations.

**Patterns tested:**
1. RNK with all items ranked — valid submission
2. RNK with fewer items ranked than required → error
3. RNK as source for a select condition — verify condition evaluates on ranked values
4. RNK target with piped items — rank validation still applies to piped items

**Expected Results:**
- RNK validation is enforced correctly even in complex logic scenarios
- Rank data used correctly as source for conditions

---
