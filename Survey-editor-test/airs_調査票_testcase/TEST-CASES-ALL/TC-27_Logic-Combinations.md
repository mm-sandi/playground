# 27 — Logic Combinations / ロジック組合せ

**Total scripts:** ~729 files across 9 logic combination categories  
**Purpose:** Verify that logic features work correctly when combined with each other — e.g., question select + question randomization, piping + choice randomization, row select + screen branching. This tests logic interactions, not just individual logic types.

---

## TC-27-01 — Piping Combined with Other Logic (パイピング)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Choice piping (パイピング) is combined with other logic features. The choices piped into Q2 must be correct even when the piping source question is also affected by other logic.

**Combination patterns (96 HTML files):**
- Piping + question select: Q1 is conditionally hidden; piping into Q2 still evaluates correctly
- Piping + choice randomization: Q1's choices are randomized; piping copies in original order
- Piping + choice group randomization: groups are piped correctly
- Piping + page break: piping source and target are on different pages
- Piping + loop: source question is inside a loop; each loop iteration's answer is piped
- Piping + screen branching: verify branch decision and piping both apply correctly

**Steps (per pattern):**
1. Admin creates a survey with piping + the second logic feature configured.
2. Respondent answers Q1 (selecting specific choices).
3. Verify Q2 shows exactly the piped choices, reflecting all applied logic correctly.
4. Verify answer data records original choice numbers.

**Expected Results:**
- Piped choices are correct regardless of other active logic on the source question
- Logic interactions do not produce unexpected behavior
- Answer data records original choice IDs

---

## TC-27-02 — Matrix Row Piping Combined with Other Logic (マトリクス表側パイピング)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Matrix row piping (表側パイピング) is combined with other logic features. Q1's answer items become the sub-questions (rows) of a matrix Q2.

**Combination patterns (69 HTML files):**
- Row piping + question select: Q1 conditionally hidden; row piping impact
- Row piping + choice randomization: Q1 items randomized; piped rows use original order
- Row piping + row select: some piped rows further hidden by row-select
- Row piping + page break

**Steps (per pattern):**
1. Admin creates a survey with row piping + the second logic.
2. Respondent answers Q1.
3. Verify the matrix Q2 shows piped rows matching Q1's answers.

**Expected Results:**
- Piped rows correctly reflect Q1's answer items
- Combined logic (e.g., row-select after piping) applies correctly

---

## TC-27-03 — Row Select Combined with Other Logic (表側セレクト)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Row select (subQuestionSelect) is combined with other logic features. Sub-question visibility in a matrix is controlled by Q1, while other logic also applies.

**Combination patterns (149 HTML files — largest category):**
- Row select + question select: target question itself is conditionally shown
- Row select + piping: rows are both piped and selectively shown
- Row select + screen branching: row select condition is on a different page
- Row select + choice randomization: Q1 choices are randomized; row-select condition evaluates on original choice numbers
- Row select + row randomization
- Row select + item select

**Steps (per pattern):**
1. Admin creates a survey with row select + second logic configured.
2. Respondent A answers Q1 to trigger row select condition → some rows hidden.
3. Respondent B does not trigger → all rows shown.

**Expected Results:**
- Row visibility correctly combines with the second logic feature
- Non-applicable rows are recorded correctly in all combinations

---

## TC-27-04 — Question Select Combined with Other Logic (質問セレクト)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Question select (questionSelect) is combined with other features, particularly question randomization and screen branching.

**Combination patterns (126 HTML files):**
- Question select + question randomization (外からセレクト: from outside the randomization block): randomization block reorders questions but question select condition still evaluates correctly
- Question select + question randomization (ランダマイズセクション内: source and target both inside the block)
- Question select + page break (with branch line between source and target)
- Question select + page break (without branch line between source and target)
- Question select + loop: select condition based on loop question
- Multiple question selects: Q1→Q3 and Q1→Q5 simultaneously

**Steps (per pattern 2_1_1 as example):**
1. Admin creates: Q1 (MAC), Q2–Q5 in a randomization block, Q2 has select condition `any(Q1,"2")`.
2. Configure page break between Q1 and Q2 (with or without branch line).
3. Respondent answers Q1 with choice 2 + 3 → Q2 is shown; respondent answers Q2, Q3, Q4, Q5.
4. Second respondent answers Q1 with choices 1 + 3 (not 2) → Q2 is hidden; Q3, Q4, Q5 still shown.

**Expected Results:**
- Question select evaluates correctly regardless of randomization order
- Page break presence/absence does not affect condition evaluation
- Non-applicable Q2 is correctly recorded when condition is false

---

## TC-27-05 — Question Randomization Combined with Other Logic (質問ランダマイズ)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Question randomization is combined with select conditions, piping, and other logic. The randomized display order must not affect logic evaluation or answer data.

**Combination patterns (129 HTML files):**
- Question randomization + question select: select condition from outside the randomization block
- Question randomization + choice piping: source of piping is inside a randomization block
- Question randomization + row select: row select source is inside a randomization block
- Question randomization + choice randomization
- Question randomization + multiple page breaks

**Expected Results:**
- Logic conditions evaluate on original QIDs regardless of randomized display order
- Piping and select conditions work correctly with randomized question order
- Answer data always uses original QNO

---

## TC-27-06 — Reverse Piping Combined with Other Logic (逆パイピング)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Reverse piping (逆パイピング) — Q2's choices are the choices NOT selected in Q1 — is combined with other logic features.

**Combination patterns (85 HTML files):**
- Reverse piping + question select: source question for reverse piping is conditionally hidden
- Reverse piping + choice randomization: Q1 randomized; reverse piped choices use original numbering
- Reverse piping + page break
- Reverse piping + loop

**Expected Results:**
- Reverse piped choices correctly show only non-selected choices from Q1
- Combinations do not disrupt the reverse piping calculation

---

## TC-27-07 — Choice Group Randomization Combined with Other Logic (選択肢グループランダマイズ)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Choice group randomization is combined with piping, question select, and other logic.

**Combination patterns (29 HTML files):**
- Choice group randomization + question select: group order randomized; condition evaluates on original choice numbers
- Choice group randomization + piping: groups piped to another question maintain group structure

**Expected Results:**
- Group randomization order does not affect condition evaluation
- Piped groups maintain their group structure and original numbering

---

## TC-27-08 — Choice Randomization Combined with Other Logic (選択肢ランダマイズ)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Choice randomization is combined with piping, select conditions, and other logic features.

**Combination patterns (24 HTML files):**
- Choice randomization + piping: piped choices are ordered by original index, not display position
- Choice randomization + condition: condition uses original choice numbers; randomized display does not affect evaluation
- Choice randomization + row piping

**Expected Results:**
- Logic always evaluates on original choice indices, not display positions
- Piped choices maintain original order regardless of randomization

---

## TC-27-09 — Item Select Combined with Other Logic (項目セレクト)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Item select (for RAT/RNK questions) is combined with other logic features such as question select and piping.

**Combination patterns (22 HTML files):**
- Item select + question select: item visibility depends on another question's condition
- Item select + piping: items that are piped are also selectively shown/hidden

**Expected Results:**
- Item visibility correctly combines with other logic
- Non-applicable items recorded correctly

---
