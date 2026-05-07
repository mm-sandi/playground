# 35 — Answer Behavior / 回答 (All Question Types)

**Total scripts:** ~75 files (37 Research setup + 31 automatic answer + 7 manual answer)  
**Purpose:** Verify that all question types record correct answer data (ANSWER_xxx, ANSWER_DETAIL_xxx tables), and that survey access rules, logic-driven hidden questions, and cell/survey lifecycle events behave correctly.

---

## TC-35-01 — Normal Answer: All Main Question Types (Valid Responses)

**Scope:** Respondent  
**Platform:** Desktop  
**Survey type:** Quick (for SAR first test), then Open (for all remaining questions)

**Scenario:** A survey is created with one question of each type. A respondent answers every question with a valid response. The system records the correct data in ANSWER and ANSWER_DETAIL tables.

**Question types covered:** SAR, MAC, SAP, SAS, MTS, MTM, MTT, FAL, FAS, RAT, RNK

**Steps:**
1. Create a Quick survey with a SAR question (4 choices, no FA field). Upload respondent list (MID: 275091). Respondent selects Choice 1.
2. Create an Open survey with the following questions in sequence:
   - Q1: SAR (no FA) — select Choice 3
   - Q2: SAR (with FA on Choice 4) — select Choice 4, type "SAR1" in FA
   - Q3: MAC (no FA, 4 choices) — select Choices 1 and 3
   - Q4: MAC (FA on Choice 4) — select Choices 2 and 4, type "MAC1" in FA
   - Q5: SAP — select one option
   - Q6: SAS — select one option
   - Q7: MTS (4 rows × 4 columns, no FA) — select different column for each row
   - Q8: MTS (FA on row 4) — answer all rows, type "MTS1" in FA
   - Q9: MTM (4 rows × 4 columns, no FA) — select multiple columns per row
   - Q10: MTM (FA on row 4) — select multiple columns, type "MTM1" in FA
   - Q11: MTT — same as MTS without FA
   - Q12: FAL — type "FAL1"
   - Q13: FAS (5 text fields) — type "FAL1" through "FAL5" in each field
   - Q14: RAT (4 items) — enter 1, 3, 6 (leave item 4 blank)
   - Q15: RNK (4 items, rank all 4) — assign ranks 1–4

**Expected Results:**
- ANSWER_DETAIL records are created correctly for each question number (QNO)
- For SAR/SAP/SAS: 1 record per question, VALUE = selected choice number, TEXT = NULL (or FA text if FA selected)
- For MAC: 1 record per selected choice, same QNO, different VALUE
- For MTS/MTM/MTT: 1 record per row (SNO = row number), VALUE = selected column
- For FAL: 1 record, VALUE = NULL, TEXT = typed text
- For FAS: 1 record per text field (SNO = field number), VALUE = NULL, TEXT = typed text
- For RAT: 1 record per item, VALUE = entered number (0 if left blank)
- For RNK: 1 record per rank position, VALUE = item number

---

## TC-35-02 — Normal Answer: Profile Questions (Basic Attributes, Open Survey)

**Scope:** Respondent  
**Platform:** Desktop  
**Survey type:** Open

**Scenario:** A survey includes standard respondent profile (basic attribute) fields. The respondent fills in all fields and the data is stored correctly.

**Profile fields tested:** f_name (last/first name), f_email, f_sex, f_age, f_zip, f_pref, f_addr, f_tel

**Steps:**
1. Create an Open survey with basic attribute questions enabled.
2. Open the answer screen from the survey detail view.
3. Fill in: name (田中 一郎), email, sex, age, zip code, prefecture, address, phone number.
4. Submit the response.

**Expected Results:**
- ANSWER_DETAIL records created for each profile question number (QNO 30001+)
- For f_name: 2 records (SNO=1 for last name, SNO=2 for first name), VALUE = text
- All other fields: 1 record each with correct VALUE or TEXT

---

## TC-35-03 — Normal Answer: Additional Attribute Questions (Open Survey)

**Scope:** Respondent  
**Platform:** Desktop  
**Survey type:** Open

**Scenario:** A survey uses custom additional attribute questions (f_sar, f_mac, f_sap, f_fas, f_tel, f_zip, f_prm). These are answered and verified in the DB.

**Question types tested:** f_sar (no FA), f_sar (with FA), f_mac (no FA), f_mac (with FA), f_sap, f_fas, f_tel (additional), f_zip (additional), f_prm

**Steps:**
1. Create an Open survey with additional attribute questions.
2. Answer each attribute question with a valid response.
3. Verify ANSWER_DETAIL records.

**Expected Results:**
- Same recording rules as main questions: VALUE stores choice number, TEXT stores FA input
- f_mac produces multiple records per question (one per selected choice)

---

## TC-35-04 — No-Answer (Blank) Responses: All Main Question Types

**Scope:** Respondent  
**Platform:** Desktop  
**Survey type:** Open (all questions in one survey, with a dummy question at the end to allow submission)

**Scenario:** A respondent deliberately skips all non-required questions. The system records "no answer" entries in the DB (not absent rows — records with NULL or 0 values).

**Important note:** A dummy question at the end must be answered to allow submission; otherwise, the survey cannot complete.

**Questions:** SAR through RNK (same types as TC-35-01), plus basic and additional attribute fields

**Steps:**
1. Create survey with all question types plus a dummy answered question at the end.
2. Leave all other questions blank and submit.

**Expected Results:**
- ANSWER_DETAIL records still exist for unanswered questions
- For choice questions: no record created (absence = no selection)
- For free text questions: record with VALUE = NULL, TEXT = NULL
- For RAT: VALUE = 0 for each unanswered item
- No server error; submission completes normally

---

## TC-35-05 — Logic-Hidden Choices Recorded as No Answer

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** When logic hides individual choices or matrix cells (piping, reverse-piping, choiceSelect, matrix piping), the hidden options that were never shown to the respondent must be recorded as "no answer" (not as valid selections).

**Logic types tested:**
- Piping (パイピング) — hides choices not selected in source question
- Reverse piping (逆パイピング) — hides choices that were selected in source question
- Matrix piping (マトリクス回答パイピング) — hides matrix rows/columns based on prior matrix answer
- Choice select (選択肢セレクト) — shows only specified choices

**Steps:**
1. Create a survey with source and target questions connected by each logic type.
2. Answer the source question (selecting specific choices).
3. Verify the target question shows only the logic-visible choices.
4. Answer the target question.

**Expected Results:**
- ANSWER_DETAIL records for target question do NOT contain selections for hidden choices
- Hidden choice positions are stored as "no answer" (absent or NULL), not as valid data
- Visible choices are recorded normally

---

## TC-35-06 — Logic-Hidden Questions Recorded as Non-Applicable (非該当)

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** When logic completely hides a question (questionSelect / jump / piping that makes entire question disappear), the question must be recorded as "non-applicable" (非該当) in the answer data.

**Logic types tested:**
- Question select (質問セレクト) — question only shows if condition met
- Jump (ジャンプ) — question skipped
- Piping / reverse piping that hides a full question
- Matrix piping that hides a full question
- Choice select, row select, column select, item select, input select — each can hide entire questions

**Steps:**
1. Create survey with conditional logic that hides certain questions based on source answer.
2. Answer source question in a way that triggers the hide condition.
3. Observe that target questions are not displayed.
4. Complete and submit the survey.

**Expected Results:**
- ANSWER records for hidden questions are marked as non-applicable (非該当)
- No valid answer data in ANSWER_DETAIL for skipped questions
- Question QIDs remain correctly numbered in the data

---

## TC-35-07 — Loop Answer Patterns

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A survey uses loop logic to repeat a block of questions multiple times. Various answer patterns are verified: all loops answered, early termination, and randomized loop order.

**Sub-scenarios:**
1. Answer all loop iterations with valid responses
2. Answer the start condition falsely — loop block does not display; those questions recorded as non-applicable
3. Answer with an early exit condition — loop terminates early; remaining iterations recorded as non-applicable
4. Randomize loop order — verify answer data still records correctly regardless of display order
5. Loop condition referenced from a randomized source question

**Expected Results:**
- Active loop iterations produce valid ANSWER_DETAIL records
- Non-triggered loop iterations are stored as non-applicable
- Loop randomization does not affect data integrity

---

## TC-35-08 — Question Randomization Answer Patterns

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A block of questions is set to display in random order. The respondent answers all questions, and the data must be stored by QID (not display order).

**Steps:**
1. Create a survey with a question randomization block.
2. Answer all questions in the order displayed.
3. Verify ANSWER_DETAIL QNO values match original question IDs, regardless of display order.

**Sub-scenario:** Randomize only a subset (section count limit smaller than question count). Verify excluded questions are non-applicable.

**Expected Results:**
- ANSWER_DETAIL QNO = original question number
- Questions excluded by section limit are non-applicable
- Display order has no effect on stored data

---

## TC-35-09 — Choice Randomization Answer Patterns

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A question has its choices displayed in random order. The respondent selects choices by their displayed position, but the data must record the original choice number (VALUE = original choice index, not display position).

**Steps:**
1. Create a SAR/MAC question with choice randomization enabled.
2. Answer the question by selecting specific displayed choices.
3. Verify ANSWER_DETAIL VALUE stores the original choice number.

**Expected Results:**
- VALUE in ANSWER_DETAIL = original choice index, not the display position
- Randomization does not change which choice is stored

---

## TC-35-10 — Required Questions Combined with Logic

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A question is marked as required but logic makes it non-applicable. The system must correctly handle the case where "required" and "hidden" conflict.

**Patterns tested:**
1. Required question is the piping target, piping source answered with nothing → question becomes non-applicable (not a required violation)
2. Required question is piping target, source answered with one choice → question appears and must be answered
3. Required question is reverse-piping target, source answered with all-but-one choice → question appears and must be answered
4. Required question hidden by jump → non-applicable (no required violation)

**Expected Results:**
- Non-applicable questions never trigger required validation errors
- Visible required questions still enforce required answer behavior
- Data stored appropriately in each case

---

## TC-35-11 — Close Survey Access Rules

**Scope:** Respondent  
**Platform:** Desktop  
**Survey type:** Close (登録制)

**Scenario:** Various access scenarios for a closed (registered respondent) survey — unauthorized access attempts, duplicate sessions, and survey lifecycle boundary tests.

**Sub-scenarios:**
1. Access URL without logging in → redirected to login or error page
2. Logged-in respondent who is not in the delivery list accesses URL → access denied
3. URL accessed before survey status reaches "In Progress" (実査中) → blocked
4. URL accessed after survey is "In Progress" → opens normally
5. Same respondent opens answer screen in two browser tabs; completes in one tab, tries to answer in other → second tab rejected
6. Answer screen opened 10 times (with branch between title and Q1) → tracked correctly
7. Answer screen opened 10 times (without branch between title and Q1) → tracked correctly
8. Respondent completes survey; admin terminates the cell → cell correctly closed
9. Two respondents both have answer screens open; one's cell is terminated → only that respondent is blocked
10. Cell terminates before respondent clicks "Answer" button → response is discarded
11. Survey terminates before respondent clicks "Answer" button → response is discarded
12. Survey is in "実査中修正" status; cell and survey are ended → handled correctly
13. Delivery type: Normal (通常) — answer and close cell
14. Delivery type: Quota allocation (割付) — answer and close cell
15. Delivery type: Delivery control (配信コントロール) — answer and close cell

**Expected Results:**
- Unauthorized access is blocked with appropriate error/redirect
- Duplicate session: only first completion is valid
- Lifecycle boundaries are enforced correctly
- Delivery types each produce correct cell closure behavior

---

## TC-35-12 — Open Survey Access Rules

**Scope:** Respondent  
**Platform:** Desktop  
**Survey type:** Open (公開型)

**Scenario:** Various access scenarios for an open survey — timing restrictions, redirect settings, duplicate answer prevention, and cell lifecycle.

**Sub-scenarios:**
1. Access before "In Progress" status (no "before start" URL configured) → blocked
2. Access after "Aggregation" status (no "after end" URL configured) → blocked
3. Access before "In Progress" (with custom "before start" redirect URL) → redirected to specified URL
4. Access after "Aggregation" (with custom "after end" redirect URL) → redirected to specified URL
5. Thanks screen → custom URL redirect configured → works correctly
6. Direct URL redirect (no thanks screen) → works correctly
7. Duplicate answer via f_email (basic attribute) → duplicate detected, rejected
8. Duplicate answer via additional attribute ID → check enabled → duplicate rejected
9. Duplicate answer via additional attribute ID → check disabled → second response accepted
10. Answer screen opened when cell is already closed (evaluated by additional attribute ID) → handled correctly
11. No branching on open survey answer screen → confirmed
12. Cell closed by answer data; duplicate respondent attempts to answer → new cell opens and respondent is reassigned
13. "実査中修正" status; end cell and survey → correct behavior
14. Answer screen opened when cell already closed → handled correctly
15. Answer screen opened when entire survey already closed → handled correctly

**Expected Results:**
- Timing and lifecycle restrictions are correctly enforced
- Redirect URLs function as configured
- Duplicate detection works per configured attribute
- Cell/survey closure states handled gracefully

---

## TC-35-13 — External Close Survey Access

**Scope:** Respondent  
**Platform:** Desktop  
**Survey type:** External Close (外部Close) — respondent clicks "Answer" from the respondent portal (My Page)

**Sub-scenarios:**
1. Respondent clicks "Answer" on My Page; survey is already closed at that moment → error message shown
2. Respondent clicks "Answer" on My Page; their cell is already closed → error message shown
3. Respondent clicks "Answer" on My Page; neither cell nor survey is closed → answer screen opens normally
4. Respondent clicks "Answer"; cell is closed → same as scenario 2

**Expected Results:**
- Correct error handling when survey or cell is unavailable at click time
- Normal access works when both cell and survey are active

---

## TC-35-14 — External Open Survey Answer Data Integration

**Scope:** System integration  
**Platform:** Desktop  
**Survey type:** External Open (外部Open)

**Scenario:** A respondent answers via an external K3 server, and the response data arrives at AIRs3 via servlet. At the moment of arrival, the survey is already closed.

**Steps:**
1. Configure an External Open survey linked to a K3 server.
2. Respondent answers externally.
3. Survey is closed before the servlet delivers the data.
4. Verify how the incoming response is handled.

**Expected Results:**
- Incoming data is handled correctly even if survey is closed
- No data corruption or server error

---
