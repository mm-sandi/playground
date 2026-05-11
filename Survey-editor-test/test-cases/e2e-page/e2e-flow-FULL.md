# \[DRAFT\] 4. E2E Flow (Editor → Answer)

**Status:** DRAFT        
**Count:** ~255 active cases + 3 out-of-scope stubs — Pipeline (E2E-001–E2E-013, 10 active + 3 OOS), Comprehensive (E2E-NEW-001–E2E-NEW-013, 13), C1-E2E-001–045 (45), C5-E2E-001–080 (80), C-2LOGIC-001–072 (72), E2E-GAP-001–012 (12)

---

## Pipeline Cases (E2E-001 – E2E-013)

| Test ID | Scenario Title | Setup Steps | Answer Steps | Expected Outcome | Tested |
| --- | --- | --- | --- | --- | --- |
| E2E-001 | Routing skips questions; answers recorded correctly | Create 5-question survey; Q1 (RadioButton) choice "B" routes to Q4 (skipping Q2, Q3) | Select B on Q1; answer Q4 and Q5 | Answered questions: Q1, Q4, Q5 recorded in final submission. Q2 and Q3 absent. Survey completes. | NT |
| E2E-002 | Screening flow — respondent disqualified mid-survey | 3-question survey; Q2 is a screening question with disqualifying choice | Select disqualifying choice on Q2 | Survey routes to screeningOut after Q2; Q3 not presented; final submission reflects screeningOut status; session ends | NT |
| E2E-003 | Screening flow — downstream session termination and BE integration | Same setup as E2E-002 | Same as E2E-002 | After executor returns screeningOut, no further questions presented; survey session ends in screeningOut state. Panel removal is a downstream BE concern out of FE executor scope. | NT |
| E2E-004 | ConstantSum validation — invalid then valid submission | ConstantSumQuestion; totalValue = 100 | Submit \[40, 40, 30\] (sum = 110); then submit \[40, 40, 20\] (sum = 100) | First submission → ConstantSumError (ValidationErrorType = 5); question not advanced; error displayed. Second submission → passes; survey advances. Accepted answer recorded as \[40, 40, 20\]. | NT |
| E2E-006 | Multi-page survey — answer persistence on back-navigation | 3-page survey; questions on all pages | Answer page 1; navigate to page 2; navigate back to page 1 | Page 1 answers persist on back-navigation; page 2 loads correctly on forward navigation; no data loss | NT |
| E2E-007 | Choice randomization — fixed-last item always last | Question group; 4 items (A, B, C, D); D marked fixed-last; randomizeType = "fixed-last"; run 10 times with different seeds | Complete survey 10 times | In all 10 runs, D always appears at last position. Positions of A, B, C differ across runs. D never appears in positions 1–3 in any run. | NT |
| E2E-009 | checkAlert — non-blocking warning, progression not blocked | TextQuestion with softWarn threshold; answer within maxLength but exceeds softWarn | Submit answer triggering checkAlert but not violating hard validation | Executor response includes non-blocking `alerts` field (distinct from `errors`). Warning displayed in UI. Respondent can advance — NOT blocked. No ValidationError returned. | NT |
| E2E-011 | Exclusive Checkbox — deselect all, UI prevents progression | CheckboxQuestion marked required; respondent selects 2 choices then deselects all | Select A, B; then deselect both; attempt to advance | UI reflects zero-selection state; executor returns RequiredError (ValidationErrorType = 4); error displayed; respondent cannot advance until at least one choice selected | NT |
| E2E-012 | Multi-type survey completion — smoke test | Survey with one of each type: RadioButton, Checkbox, Text, ConstantSum, Ranking, Matrix | Answer all questions with valid inputs | All questions advance without ValidationErrors; final submission contains all answer types in correct format; survey completion state reached; no executor errors | NT |
| E2E-013 | RankingQuestion — RankingError (type 6) and RankingCountError (type 7) end-to-end | RankingQuestion; 5 items; requiredRankCount = 3 | (a) Submit with duplicate rank positions; (b) Correct but rank only 1 item; (c) Rank exactly 3 items with unique positions | (a) → ValidationErrorType = 6 (RankingError); blocked. (b) → ValidationErrorType = 7 (RankingCountError); blocked. (c) → Passes; survey advances; 3 ranked items recorded in correct order in modifiedMausInfo. | NT |

---

## Comprehensive E2E Cases (E2E-NEW-001 – E2E-NEW-013)

**Columns:** Test ID | Question Type | Description | Pre-conditions | Steps to Perform | Expectations | Actual Result | Tested Survey ID | Tested

| Test ID | Question Type | Description | Pre-conditions | Steps to Perform | Expectations | Actual Result | Tested Survey ID | Tested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E2E-NEW-001 | Radio (SAR) | Horizontal 5-column layout created in Editor renders correctly in Answer. | New survey. | Editor: add Radio, 5 choices, direction=Horizontal, columns=5. 2. Publish. 3. Open Answer. | All 5 choices appear in a single row in Answer. |  |  | NT |
| E2E-NEW-002 | Checkbox (MAC) | Exclusive + Specify=Exact 3 enforced end-to-end. | New survey. | Editor: Checkbox, 5 choices, choice 5=Exclusive, Specify=Exact 3. 2. Publish. 3. Answer: (a) select 3 non-exclusive → Next; (b) select exclusive only → Next; (c) select 2 non-exclusive → Next. | (a) Valid. (b) Valid. (c) Error: "This question requires selecting 3 choices." |  |  | NT |
| E2E-NEW-003 | Matrix Radio (MTS) | Disable Choices configuration in Editor prevents those choices from being selected in Answer. | New survey. | Editor: MTS, choice 2 disabled for SQ1 via Disable Choices dialog. 2. Publish. 3. Answer: attempt to select choice 2 in SQ1. | Choice 2 in SQ1 is not selectable (disabled/grayed). Other SQs unaffected. |  |  | NT |
| E2E-NEW-004 | Matrix Checkbox (MTM) | Matrix Inclusion configured in Editor produces correct dynamic reveal in Answer. | New survey. | Editor: MTM, Matrix Inclusion SQ1→SQ2 for choices 1–3. 2. Publish. 3. Answer: load (observe SQ2); select choices 1+2 in SQ1 (observe SQ2); deselect (observe SQ2). | Initial SQ2: only choices 4–5 visible. After SQ1 selection: choices 1, 2, 4, 5 visible. After deselection: choices 1, 2 removed from SQ2. |  |  | NT |
| E2E-NEW-005 | Matrix Checkbox (MTM) | Prohibition of Simultaneous Matrix Check configured in Editor enforces bidirectional hiding in Answer. | New survey. | Editor: MTM, Prohibition SQ1↔SQ2. 2. Publish. 3. Answer: select choice 1 in SQ1; observe SQ2; select choice 2 in SQ2; observe SQ1. | Choice 1 hidden in SQ2 after SQ1 selection. Choice 2 hidden in SQ1 after SQ2 selection. |  |  | NT |
| E2E-NEW-006 | Ranking (RNK) | Flip randomization configured in Editor appears as normal or fully-reversed order in Answer. | New survey. | Editor: Ranking 5 choices, randomization=Flip. 2. Publish. 3. Load Answer in 5+ sessions. | Each session shows either the original order or fully reversed; no other orderings occur. |  |  | NT |
| E2E-NEW-007 | Constant Sum (RAT) | Out-of-10 unit with 5 items enforces total=10 in Answer. | New survey. | Editor: RAT 5 items, unit=Out of 10. 2. Publish. 3. Answer: enter values summing to 9 → Next; enter values summing to 10 → Next. | First attempt: error "Enter values so that the total is 10." Second attempt: valid; proceeds. |  |  | NT |
| E2E-NEW-008 | Screening Out | Yellow flag screening-out configured in Editor results in screeningOutFlg=2 saved in response data. | New survey. | Editor: Screening Out rule with yellow flag ON triggered by Q1=choice A. 2. Publish. 3. Answer Q1=choice A. 4. Inspect saved response data. | Respondent redirected to Thank You page (same as normal screen-out); response record has `screeningOutFlg = 2` (yellow flag screen-out — distinguishable from `screeningOutFlg = 1` which is standard screen-out without yellow flag, and `screeningOutFlg = 0` which is not screened out). No further questions presented. |  |  | NT |
| E2E-NEW-009 | Text Box (FA) | Number type with min=0 and max=24 configured in Editor validates range in real-time in Answer. | New survey. | Editor: FA type=Number, min=0, max=24. 2. Publish. 3. Answer: enter -1; then enter 25; then enter 12. | -1: real-time error "requires a value of 0 or higher". 25: real-time error "requires a value of 24 or lower". 12: valid, no error. |  |  | NT |
| E2E-NEW-010 | Note | Note inserted between Q1 and Q2 in Editor is displayed without a number in Answer; question numbering is correct. | New survey. | Editor: add Q1, then insert a Note (N1), then add Q2. 2. Publish. 3. Open Answer. | Answer shows Q1, then Note content (no number label), then Q2. Q1 labeled Q1, Q2 labeled Q2. Note not numbered in Answer. |  |  | NT |
| E2E-NEW-011 | Question Selection | Question Selection logic configured in Editor correctly shows/hides Q2 in Answer based on Q1 answer. | New survey. | Editor: Q1 Radio, Q2 Radio, Selection logic: show Q2 only if Q1=choice A. 2. Publish. 3. Answer Q1=choice B → observe Q2. 4. Answer Q1=choice A → observe Q2. | Q2 hidden when Q1=B; Q2 shown when Q1=A. |  |  | NT |
| E2E-NEW-012 | Sub-question Selection | Sub-question Selection logic configured in Editor shows/hides a specific SQ in Answer. | New survey. | Editor: Matrix Radio, SQ2 with selection logic gated on a previous question's answer. 2. Publish. 3. Answer the gating question with qualifying value. 4. Answer with non-qualifying value. | SQ2 visible on qualifying answer; SQ2 hidden on non-qualifying answer. |  |  | NT |
| E2E-NEW-013 | Any (auto-select) | Choice selection narrowing to 1 displayed choice triggers auto-select and hides the required question in Answer. | New survey with choice selection reducing a Radio question to 1 visible choice. | Editor: Q1 Checkbox + Q2 Radio with choice selection (choices of Q2 gated on Q1 answers), such that selecting choice A in Q1 leaves only 1 choice in Q2. Q2 required=Yes. 2. Publish. 3. Answer Q1=choice A only. 4. Observe Q2. | Q2 not displayed; its single remaining choice is auto-selected; answer recorded silently. Survey proceeds to Q3. |  |  | NT |

---

## 3. Choice-Count × Logic Combination Cases

End-to-end scenarios exercising the Editor → Answer pipeline at the **1 displayed choice** (C1-) and **5 choices created** (C5-) boundaries, with one logic and two logics applied simultaneously. Focus: configuration in Editor propagates to the Answer runtime (auto-select, hiding, validation, randomization, screen-out).

### 3.1 One-Choice Cases (C1-E2E-001 – C1-E2E-045)

| ID | Choices | Question Type | Logic 1 | Logic 2 | Description | Pre-conditions | Steps | Expected Result | Tested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1-E2E-001 | 1 | Radio (SAR) | Choice Selection | — | Editor configures Choice Selection that narrows Q2 to 1 choice; required → Q2 auto-selected in Answer. | Editor: Q1 Checkbox; Q2 Radio required=Yes with Choice Selection gating by Q1. | Editor create+publish. 2. Answer Q1 such that only 1 choice remains in Q2. 3. Observe Q2. | Q2 not shown; single choice auto-selected; survey advances to Q3. | NT |
| C1-E2E-002 | 1 | Radio (SAR) | Choice Selection | Screening Out | Narrowed single choice is also a screen-out trigger. | Editor: Q2 required=Yes; Choice Selection narrows to 1; that choice flagged screen-out. | Editor publish. 2. Answer Q1 → Q2 auto-trigger. | Auto-select fires; screen-out exits survey to Thank You. | NT |
| C1-E2E-003 | 1 | Radio (SAR) | Question Selection | Choice Selection | Q2 gated visible by Q Selection; choices narrowed to 1 by Choice Selection. | Editor: both logics on Q2 required. | Editor publish. 2. Gating Q answered qualifying. 3. Observe Q2. | Q2 auto-selected, hidden; survey advances. | NT |
| C1-E2E-004 | 1 | Radio (SAR) | Choice Selection | — | Optional Q2 narrowed to 1 → shown (no auto-select). | Editor: Q2 required=No; Choice Selection narrows to 1. | Publish. 2. Answer Q1. 3. Observe Q2. | Q2 displayed; no auto-select. | NT |
| C1-E2E-005 | 1 | Radio (SAR) | Choice Selection | — | Textbox on the single remaining choice → no auto-select. | Editor: Q2 required=Yes; remaining choice has textbox. | Publish. 2. Trigger. | Q2 displayed; respondent fills textbox. | NT |
| C1-E2E-006 | 1 | Checkbox (MAC) | Choice Selection | — | Required Checkbox Specify=Unspecified narrowed to 1 → auto-select. | Editor: Q2 Checkbox required=Yes, Specify=Unspecified, Choice Selection narrows to 1. | Publish. 2. Trigger. | Auto-selected; hidden. | NT |
| C1-E2E-007 | 1 | Checkbox (MAC) | Choice Selection | Exclusive | Single remaining choice = Exclusive + Specify=Exact 1 → no auto-select. | Editor: Q2 required=Yes, Specify=Exact 1; narrowed choice is Exclusive. | Publish. 2. Trigger. | Q2 displayed. | NT |
| C1-E2E-008 | 1 | Checkbox (MAC) | Choice Selection | Screening Out | Auto-select + screen-out on remaining choice. | Editor: Required Checkbox narrowed to 1 screen-out choice. | Publish. 2. Trigger. | Exit. | NT |
| C1-E2E-009 | 1 | Checkbox (MAC) | Choice Selection | Question Selection | Q visible + narrowed to 1 → auto-select. | Editor: Q2 required; both logics. | Publish. 2. Trigger. | Auto-select; hidden. | NT |
| C1-E2E-010 | 1 | Checkbox (MAC) | Choice Randomization | Choice Selection | Randomization moot with 1 displayed; auto-select still fires. | Editor: Q2 required; both logics. | Publish. 2. Trigger. | Auto-selected. | NT |
| C1-E2E-011 | 1 | Dropdown (SAP) | Choice Selection | — | Required Dropdown narrowed to 1 → auto-select. | Editor: Dropdown required=Yes; Choice Selection gating. | Publish. 2. Trigger. | Auto-selected; hidden. | NT |
| C1-E2E-012 | 1 | Dropdown (SAP) | Choice Selection | Screening Out | Narrowed choice triggers screen-out. | Editor: required Dropdown; screen-out on remaining choice. | Publish. 2. Trigger. | Exit. | NT |
| C1-E2E-013 | 1 | Text Box (FA) | Question Selection | — | FA hidden via Q Selection (no "1 choice" notion). | Editor: required FA gated off. | Publish. 2. Trigger non-qualifying. | FA not rendered; no required error. | NT |
| C1-E2E-014 | 1 | Text Box (FA) | Question Selection | Screening Out | Gating answer screens out; FA never shown. | Editor: FA gated; gating choice screens out. | Publish. 2. Trigger. | Exit. | NT |
| C1-E2E-015 | 1 | Text Area (FAL) | Question Selection | — | FAL hidden via Q Selection. | Editor: required FAL gated off. | Publish. 2. Trigger. | Not rendered. | NT |
| C1-E2E-016 | 1 | Text Area (FAL) | Question Selection | Screening Out | Gating screens out. | Editor: FAL gated; screen-out on gating. | Publish. 2. Trigger. | Exit. | NT |
| C1-E2E-017 | 1 | Matrix Radio (MTS) | Choice Selection | — | All SQs narrowed to 1 choice → entire matrix hidden. | Editor: MTS required=All; Choice Selection narrows all SQs. | Publish. 2. Trigger. | Matrix hidden; answers recorded. | NT |
| C1-E2E-018 | 1 | Matrix Radio (MTS) | Choice Selection | — | Only SQ1 narrowed to 1 → SQ1 row hidden. | Editor: MTS; narrowing affects SQ1 only. | Publish. 2. Trigger. | SQ1 row hidden; others shown. | NT |
| C1-E2E-019 | 1 | Matrix Radio (MTS) | Sub-question Selection | — | SQ1 hidden via SQ Selection; SQ2 still multi-choice. | Editor: MTS; SQ1 gated off. | Publish. 2. Trigger. | SQ1 not shown. | NT |
| C1-E2E-020 | 1 | Matrix Radio (MTS) | Choice Selection | Sub-question Selection | Combined: some SQs hidden, remaining SQs narrowed to 1. | Editor: MTS; both logics. | Publish. 2. Trigger. | Hidden SQs omitted; narrowed SQs auto-selected. | NT |
| C1-E2E-021 | 1 | Matrix Radio (MTS) | Prohibition | Choice Selection | Prohibition + Choice Selection narrow SQ2 to 1. | Editor: MTS Prohibition SQ1↔SQ2 + Choice Selection. | Publish. 2. Select in SQ1 to narrow SQ2. | SQ2 auto-selected; row hidden. | NT |
| C1-E2E-022 | 1 | Matrix Radio (MTS) | Choice Selection | Sub-question Randomization | SQ rows random; 1-choice auto-select still fires by SQ ID. | Editor: MTS; Choice Selection + SQ Random. | Publish. 2. Trigger. | Auto-select on targeted SQ regardless of display order. | NT |
| C1-E2E-023 | 1 | Matrix Checkbox (MTM) | Choice Selection | — | All SQs narrowed; Specify=Unspecified → whole matrix hidden. | Editor: MTM required=All, Specify=Unspecified. | Publish. 2. Trigger. | Matrix hidden. | NT |
| C1-E2E-024 | 1 | Matrix Checkbox (MTM) | Choice Selection | Exclusive | Narrowed SQ1 to 1 Exclusive choice → no auto-select. | Editor: MTM SQ1 Specify=Exact 1 + Exclusive on narrowed choice. | Publish. 2. Trigger. | SQ1 displayed. | NT |
| C1-E2E-025 | 1 | Matrix Checkbox (MTM) | Matrix Inclusion | Choice Selection | Inclusion + selection converge to 1 scoped choice; SQ2 required + 1 → auto-select. | Editor: MTM Inclusion SQ1→SQ2; SQ2 required, Specify=Unspecified. | Publish. 2. Select 1 in SQ1. | SQ2 auto-selected if 1 revealed. | NT |
| C1-E2E-026 | 1 | Matrix Checkbox (MTM) | Prohibition | Choice Selection | Prohibition empties SQ2 to 1; SQ2 required + 1 → auto-select. | Editor: MTM Prohibition + Choice Selection. | Publish. 2. Select in SQ1 to narrow SQ2. | SQ2 auto-selected. | NT |
| C1-E2E-027 | 1 | Matrix Checkbox (MTM) | Matrix Inclusion | Sub-question Selection | SQ2 hidden via SQ Selection; inclusion effectively no-op. | Editor: MTM Inclusion + SQ2 gated off. | Publish. 2. Trigger. | SQ2 not rendered. | NT |
| C1-E2E-028 | 1 | Matrix Checkbox (MTM) | Choice Selection | Screening Out | Narrowed choice triggers screen-out. | Editor: MTM SQ1 required; narrowed choice screens out. | Publish. 2. Trigger. | Exit. | NT |
| C1-E2E-029 | 1 | Bipolar Matrix (MTT) | Choice Selection | — | All SQs narrowed to 1 → MTT hidden. | Editor: MTT required=All; narrowing. | Publish. 2. Trigger. | Matrix hidden. | NT |
| C1-E2E-030 | 1 | Bipolar Matrix (MTT) | Sub-question Selection | Choice Selection | Some rows hidden; others narrowed. | Editor: MTT both logics. | Publish. 2. Trigger. | Rows hidden or auto-selected accordingly. | NT |
| C1-E2E-031 | 1 | Bipolar Matrix (MTT) | Question Selection | Choice Selection | Whole MTT gated; if shown, SQs narrowed → auto-select rows. | Editor: MTT both logics. | Publish. 2. Trigger qualifying. | MTT shown; all auto-selected; hidden. | NT |
| C1-E2E-032 | 1 | Ranking (RNK) | Choice Selection | — | Required=All narrowed to 1 → rank 1 auto-assigned. | Editor: Ranking required=All; Choice Selection. | Publish. 2. Trigger. | Auto-rank; hidden. | NT |
| C1-E2E-033 | 1 | Ranking (RNK) | Exclusive | Choice Selection | Narrowed to 1 Exclusive choice — auto-rank behavior under review. | Editor: Ranking required=All; narrowed choice = Exclusive; Response Count=3. | Publish. 2. Trigger Choice Selection so only exclusive choice remains. | Per auto-select spec: 1 displayed choice → auto-rank fires (rank1=exclusive choiceId; ranks 2–3 also filled with exclusive choiceId); question hidden. The spec lists no Exclusive exception for RNK auto-select (unlike MAC). Needs verification — if exclusive blocks auto-rank, question is displayed for manual input. | NT |
| C1-E2E-034 | 1 | Ranking (RNK) | Choice Selection | Screening Out | Narrowed ranked choice screens out. | Editor: Ranking required=All; narrowed = screen-out. | Publish. 2. Trigger. | Exit. | NT |
| C1-E2E-035 | 1 | Ranking (RNK) | Choice Randomization | Choice Selection | 1 choice → randomization moot. | Editor: Ranking; both logics. | Publish. 2. Trigger. | Auto-ranked. | NT |
| C1-E2E-036 | 1 | Constant Sum (RAT) | Choice Selection | — | Required RAT narrowed to 1 → auto-filled with totalValue. | Editor: RAT required=Yes; Choice Selection. | Publish. 2. Trigger. | Single remaining item auto-filled with the question's totalValue (100 for Percent mode; 10 for Out-of-10 mode); question hidden; survey advances silently. | NT |
| C1-E2E-037 | 1 | Constant Sum (RAT) | Choice Selection | Choice Randomization | Randomization moot; auto-fill fires. | Editor: RAT both logics. | Publish. 2. Trigger. | Auto-filled. | NT |
| C1-E2E-038 | 1 | Constant Sum (RAT) | Choice Selection | Question Selection | Q visible only if gated; if visible + narrowed to 1 → auto-fill. | Editor: RAT both logics. | Publish. 2. Trigger qualifying. | Auto-filled when visible. | NT |
| C1-E2E-039 | 1 | Note | Question Selection | — | Note hidden when Q Selection not qualifying. | Editor: Note gated. | Publish. 2. Trigger non-qualifying. | Not rendered. | NT |
| C1-E2E-040 | 1 | Any | Choice Selection | Question Selection | If Q hidden by Q Selection, Choice Selection effect moot. | Editor: any Q; both logics. | Publish. 2. Trigger non-qualifying on Q Selection. | Q not rendered. | NT |
| C1-E2E-041 | 1 | Radio (SAR) | Choice Selection | Choice Randomization | Randomization on 1 choice moot; auto-select fires. | Editor: Radio required; both logics. | Publish. 2. Trigger. | Auto-selected. | NT |
| C1-E2E-042 | 1 | Matrix Radio (MTS) | Choice Selection | Question Selection | Q visible → all SQs narrowed to 1 → matrix hidden. | Editor: MTS both logics. | Publish. 2. Trigger qualifying. | Matrix shown then hidden; answers recorded. | NT |
| C1-E2E-043 | 1 | Matrix Checkbox (MTM) | Matrix Inclusion | Exclusive | Revealed single choice in SQ2 = Exclusive → no auto-select in SQ2. | Editor: MTM Inclusion; revealed choice Exclusive; SQ2 Specify=Exact 1. | Publish. 2. Select in SQ1. | SQ2 displayed; no auto-select. | NT |
| C1-E2E-044 | 1 | Ranking (RNK) | Choice Selection | Question Selection | Q visible + narrowed to 1 → auto-rank. | Editor: Ranking required=All; both logics. | Publish. 2. Trigger qualifying. | Auto-rank; hidden. | NT |
| C1-E2E-045 | 1 | Constant Sum (RAT) | Choice Selection | Screening Out | Narrowed item triggers screen-out — not applicable (RAT items don't screen-out); expect editor-level rejection or no-op. | Editor: RAT; attempt to configure screen-out on item. | Editor publish. | Editor rejects screen-out on RAT items; if allowed, behavior: exit on save submission. | NT |

### 3.2 Five-Choice Cases (C5-E2E-001 – C5-E2E-080)

| ID | Choices | Question Type | Logic 1 | Logic 2 | Description | Pre-conditions | Steps | Expected Result | Tested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C5-E2E-001 | 5 | Radio (SAR) | None | — | Editor vertical layout; Answer renders 5 choices vertically. | Editor: Radio 5 choices, vertical. | Publish. 2. Answer load. | 5 choices vertical. | NT |
| C5-E2E-002 | 5 | Radio (SAR) | None | — | Horizontal 5-column layout in Editor renders correctly. | Editor: Radio 5 choices, horizontal 5-col. | Publish. 2. Answer load. | Single row of 5. | NT |
| C5-E2E-003 | 5 | Radio (SAR) | Choice Randomization | — | Random mode configured in Editor varies order in Answer. | Editor: Radio Random. | Publish. 2. 3 sessions. | Order differs. | NT |
| C5-E2E-004 | 5 | Radio (SAR) | Choice Randomization | — | Flip mode: normal or reversed only. | Editor: Radio Flip. | Publish. 2. Many sessions. | Normal/reversed. | NT |
| C5-E2E-005 | 5 | Radio (SAR) | Choice Selection | — | Editor gating narrows to 3 in Answer. | Editor: Q1 Checkbox + Q2 Radio Choice Selection. | Publish. 2. Answer Q1 to narrow Q2. | Q2 shows 3 choices. | NT |
| C5-E2E-006 | 5 | Radio (SAR) | Question Selection | — | Q2 shown only when Q1 qualifies. | Editor: Q2 Q Selection. | Publish. 2. Q1 non-qualifying; then qualifying. | Q2 hidden then shown. | NT |
| C5-E2E-007 | 5 | Radio (SAR) | Screening Out | — | Choice 4 screen-out. | Editor: Radio choice 4 screen-out. | Publish. 2. Select 4. | Exit. | NT |
| C5-E2E-008 | 5 | Radio (SAR) | Choice Randomization | Screening Out | Random order; screen-out tied to choice ID. | Editor: Radio Random + choice 4 screen-out. | Publish. 2. Many sessions; select the screen-out choice by ID. | Consistent exit. | NT |
| C5-E2E-009 | 5 | Radio (SAR) | Choice Selection | Question Selection | Q shown + narrowed choices. | Editor: Radio both logics. | Publish. 2. Trigger qualifying. | Visible + narrowed. | NT |
| C5-E2E-010 | 5 | Checkbox (MAC) | None | — | Specify=Exact 3; select 3 → valid. | Editor: Checkbox 5 choices Specify=Exact 3. | Publish. 2. Select 3. Next. | Advance. | NT |
| C5-E2E-011 | 5 | Checkbox (MAC) | None | — | Specify=Exact 3; select 2 → count error. | Same. | Publish. 2. Select 2. Next. | Error. | NT |
| C5-E2E-012 | 5 | Checkbox (MAC) | Exclusive | — | Choice 5 Exclusive. | Editor: Checkbox; choice 5 Exclusive. | Publish. 2. Select 1+2, then 5. | Only 5 remains. | NT |
| C5-E2E-013 | 5 | Checkbox (MAC) | Exclusive | — | Specify=Exact 3 + Exclusive: exclusive-only valid. | Editor: Checkbox Specify=Exact 3 + choice 5 Exclusive. | Publish. 2. Select 5. Next. | Valid. | NT |
| C5-E2E-014 | 5 | Checkbox (MAC) | Choice Randomization | Exclusive | Exclusive fixed; others randomized. | Editor: Checkbox Random + Exclusive. | Publish. 2. Many sessions. | Choice 5 at fixed position. | NT |
| C5-E2E-015 | 5 | Checkbox (MAC) | Choice Selection | — | Narrows to 3. | Editor: Checkbox Choice Selection. | Publish. 2. Trigger. | 3 choices. | NT |
| C5-E2E-016 | 5 | Checkbox (MAC) | Screening Out | — | Choice 5 screen-out. | Editor: Checkbox; choice 5 screen-out. | Publish. 2. Select 5. Next. | Exit. | NT |
| C5-E2E-017 | 5 | Checkbox (MAC) | Screening Out | Exclusive | Choice 5 = Exclusive + screen-out. | Editor: Both on choice 5. | Publish. 2. Select 1+2, then 5. | Cleared; exit. | NT |
| C5-E2E-018 | 5 | Checkbox (MAC) | Question Selection | Choice Selection | Both logics. | Editor: Checkbox both logics. | Publish. 2. Trigger. | Visible + narrowed. | NT |
| C5-E2E-019 | 5 | Checkbox (MAC) | Choice Randomization | Choice Selection | Narrowed set randomized. | Editor: Checkbox both logics. | Publish. 2. Trigger. | Narrowed + random. | NT |
| C5-E2E-020 | 5 | Dropdown (SAP) | None | — | Required Dropdown; skip → required error. | Editor: Dropdown required. | Publish. 2. Skip. Next. | Required error. | NT |
| C5-E2E-021 | 5 | Dropdown (SAP) | Choice Randomization | — | Random order. | Editor: Dropdown Random. | Publish. 2. 3 sessions. | Varies. | NT |
| C5-E2E-022 | 5 | Dropdown (SAP) | Choice Selection | — | Narrows dropdown options. | Editor: Dropdown Choice Selection. | Publish. 2. Trigger. | 3 options. | NT |
| C5-E2E-023 | 5 | Dropdown (SAP) | Screening Out | Choice Randomization | Screen-out tied to ID across random orders. | Editor: Dropdown Random + screen-out. | Publish. 2. Many sessions; select screen-out ID. | Consistent exit. | NT |
| C5-E2E-024 | 5 | Text Box (FA) | None | — | Editor min/max numeric constraints enforced in Answer. | Editor: FA Number type, min=0, max=24. | Publish. 2. Enter -1; 25; 12. | Real-time errors / OK. | NT |
| C5-E2E-025 | 5 | Text Box (FA) | Question Selection | — | FA gated off. | Editor: FA gated. | Publish. 2. Trigger non-qualifying. | Not rendered. | NT |
| C5-E2E-026 | 5 | Text Area (FAL) | None | — | Maxlength enforced. | Editor: FAL maxlength=100. | Publish. 2. Enter 101 chars. | Real-time error. | NT |
| C5-E2E-027 | 5 | Text Area (FAL) | Question Selection | Screening Out | Gating answer screens out; FAL never shown. | Editor: FAL gated; gating screens out. | Publish. 2. Trigger. | Exit. | NT |
| C5-E2E-028 | 5 | Matrix Radio (MTS) | None | — | Required=All; skip SQ → per-SQ error. | Editor: MTS required=All. | Publish. 2. Skip 1 SQ. Next. | Per-SQ error. | NT |
| C5-E2E-029 | 5 | Matrix Radio (MTS) | None | — | Required=Customize; optional SQ can be blank. | Editor: MTS Customize. | Publish. 2. Answer required only. Next. | Valid. | NT |
| C5-E2E-030 | 5 | Matrix Radio (MTS) | None | — | Disable Choices removes a cell from selectability. | Editor: MTS; disable SQ1 choice 2. | Publish. 2. Attempt to select SQ1 choice 2. | Disabled. | NT |
| C5-E2E-031 | 5 | Matrix Radio (MTS) | Choice Randomization | — | Columns randomized. | Editor: MTS Random. | Publish. 2. 3 sessions. | Varies. | NT |
| C5-E2E-032 | 5 | Matrix Radio (MTS) | Sub-question Randomization | — | Rows randomized. | Editor: MTS SQ Random. | Publish. 2. 3 sessions. | Varies. | NT |
| C5-E2E-033 | 5 | Matrix Radio (MTS) | Sub-question Selection | — | SQ2 hidden based on gating. | Editor: MTS SQ Selection. | Publish. 2. Trigger non-qualifying. | SQ2 hidden. | NT |
| C5-E2E-034 | 5 | Matrix Radio (MTS) | Prohibition | — | Prohibition SQ1↔SQ2 hides choices. | Editor: MTS Prohibition. | Publish. 2. Select in SQ1; observe SQ2. | Selected choice hidden in SQ2. | NT |
| C5-E2E-035 | 5 | Matrix Radio (MTS) | Screening Out | — | Choice in SQ1 triggers screen-out. | Editor: MTS; SQ1 choice 4 screen-out. | Publish. 2. Select SQ1=4. Next. | Exit. | NT |
| C5-E2E-036 | 5 | Matrix Radio (MTS) | Choice Randomization | Sub-question Randomization | Rows + columns random independently. | Editor: both random. | Publish. 2. 3 sessions. | Both vary. | NT |
| C5-E2E-037 | 5 | Matrix Radio (MTS) | Prohibition | Sub-question Randomization | Prohibition by SQ/choice ID; row order doesn't break behavior. | Editor: MTS Prohibition + SQ Random. | Publish. 2. Multiple sessions. | Prohibition correct. | NT |
| C5-E2E-038 | 5 | Matrix Radio (MTS) | Choice Selection | Sub-question Selection | Both narrow. | Editor: MTS both logics. | Publish. 2. Trigger. | Narrowed rows + columns. | NT |
| C5-E2E-039 | 5 | Matrix Radio (MTS) | Question Selection | Choice Randomization | Visible only if gated; if visible, columns random. | Editor: MTS both logics. | Publish. 2. Trigger qualifying. | Visible + random. | NT |
| C5-E2E-040 | 5 | Matrix Checkbox (MTM) | None | — | Per-SQ Specify=Exact 2; select 1 → per-SQ count error. | Editor: MTM SQ1 Specify=Exact 2. | Publish. 2. Select 1 in SQ1. Next. | Per-SQ count error. | NT |
| C5-E2E-041 | 5 | Matrix Checkbox (MTM) | None | — | Switch to Radio on SQ1 → SQ1 renders as radio. | Editor: MTM SQ1 switch-to-radio. | Publish. 2. Observe SQ1. | Renders as radio row. | NT |
| C5-E2E-042 | 5 | Matrix Checkbox (MTM) | Matrix Inclusion | — | Inclusion SQ1→SQ2 reveals dynamically. | Editor: MTM Inclusion SQ1→SQ2 choices 1–3. | Publish. 2. Select SQ1=1,2. | SQ2 shows 1,2,4,5. | NT |
| C5-E2E-043 | 5 | Matrix Checkbox (MTM) | Matrix Inclusion | — | Deselect removes from SQ2. | Same. | Publish. 2. Deselect choice 1. | SQ2 drops choice 1. | NT |
| C5-E2E-044 | 5 | Matrix Checkbox (MTM) | Prohibition | — | SQ1↔SQ2 bidirectional. | Editor: MTM Prohibition. | Publish. 2. Select in SQ1; then SQ2. | Bidirectional hide. | NT |
| C5-E2E-045 | 5 | Matrix Checkbox (MTM) | Exclusive | — | Choice 5 Exclusive on SQ1. | Editor: MTM SQ1 choice 5 Exclusive. | Publish. 2. Select 1+2+5 in SQ1. | Only 5 remains in SQ1. | NT |
| C5-E2E-046 | 5 | Matrix Checkbox (MTM) | Choice Randomization | — | Columns random. | Editor: MTM Random. | Publish. 2. 3 sessions. | Varies. | NT |
| C5-E2E-047 | 5 | Matrix Checkbox (MTM) | Sub-question Randomization | — | Rows random. | Editor: MTM SQ Random. | Publish. 2. 3 sessions. | Varies. | NT |
| C5-E2E-048 | 5 | Matrix Checkbox (MTM) | Screening Out | — | Choice 5 in SQ1 screens out. | Editor: MTM SQ1 choice 5 screen-out. | Publish. 2. Select SQ1=5. Next. | Exit. | NT |
| C5-E2E-049 | 5 | Matrix Checkbox (MTM) | Matrix Inclusion | Prohibition | Inclusion + Prohibition on non-overlapping SQ pairs coexist. | Editor: MTM Inclusion SQ1→SQ2; Prohibition SQ2↔SQ3. | Publish. 2. Select in SQ1 and SQ2. | Both behaviors observed. | NT |
| C5-E2E-050 | 5 | Matrix Checkbox (MTM) | Matrix Inclusion | Exclusive | Revealed Exclusive choice behaves exclusive in SQ2. | Editor: MTM Inclusion; revealed choice Exclusive in SQ2. | Publish. 2. Select it in SQ2. | Others cleared. | NT |
| C5-E2E-051 | 5 | Matrix Checkbox (MTM) | Prohibition | Choice Randomization | Prohibition by ID; random columns still hide correctly. | Editor: MTM Prohibition + Random. | Publish. 2. Many sessions. | Correct ID hidden. | NT |
| C5-E2E-052 | 5 | Matrix Checkbox (MTM) | Exclusive | Sub-question Randomization | Exclusive per-SQ preserved regardless of row order. | Editor: MTM Exclusive + SQ Random. | Publish. 2. Many sessions. | Behavior preserved. | NT |
| C5-E2E-053 | 5 | Matrix Checkbox (MTM) | Choice Selection | Prohibition | Both narrow SQ2 choices. | Editor: MTM Choice Selection + Prohibition. | Publish. 2. Trigger. | Narrowed + hidden further. | NT |
| C5-E2E-054 | 5 | Matrix Checkbox (MTM) | Screening Out | Matrix Inclusion | Revealed choice triggers screen-out. | Editor: MTM Inclusion; revealed choice has screen-out. | Publish. 2. Select it in SQ2. | Exit. | NT |
| C5-E2E-055 | 5 | Matrix Checkbox (MTM) | Question Selection | Matrix Inclusion | Q hidden → inclusion moot. | Editor: MTM gated + Inclusion. | Publish. 2. Trigger non-qualifying. | Matrix not rendered. | NT |
| C5-E2E-056 | 5 | Bipolar Matrix (MTT) | None | — | Required=All skip SQ → per-SQ error. | Editor: MTT required=All. | Publish. 2. Skip SQ. Next. | Per-SQ error. | NT |
| C5-E2E-057 | 5 | Bipolar Matrix (MTT) | None | — | Required=Customize optional SQ blank valid. | Editor: MTT Customize. | Publish. 2. Answer required only. Next. | Valid. | NT |
| C5-E2E-058 | 5 | Bipolar Matrix (MTT) | Choice Randomization | — | Columns random. | Editor: MTT Random. | Publish. 2. 3 sessions. | Varies. | NT |
| C5-E2E-059 | 5 | Bipolar Matrix (MTT) | Sub-question Randomization | — | Rows random. | Editor: MTT SQ Random. | Publish. 2. 3 sessions. | Varies. | NT |
| C5-E2E-060 | 5 | Bipolar Matrix (MTT) | Choice Selection | — | Narrow columns. | Editor: MTT Choice Selection. | Publish. 2. Trigger. | Narrowed. | NT |
| C5-E2E-061 | 5 | Bipolar Matrix (MTT) | Sub-question Selection | — | Hide SQ. | Editor: MTT SQ Selection. | Publish. 2. Trigger. | SQ hidden. | NT |
| C5-E2E-062 | 5 | Bipolar Matrix (MTT) | Screening Out | — | Choice screen-out. | Editor: MTT; screen-out on choice. | Publish. 2. Select it. Next. | Exit. | NT |
| C5-E2E-063 | 5 | Bipolar Matrix (MTT) | Choice Randomization | Sub-question Randomization | Both axes random. | Editor: MTT both random. | Publish. 2. 3 sessions. | Both vary. | NT |
| C5-E2E-064 | 5 | Bipolar Matrix (MTT) | Question Selection | Sub-question Selection | Q gated + some SQs hidden. | Editor: MTT both logics. | Publish. 2. Trigger. | Conditional visibility. | NT |
| C5-E2E-065 | 5 | Ranking (RNK) | None | — | Required=All rc=5; rank 4 → count error. | Editor: Ranking required=All rc=5. | Publish. 2. Rank 4. Next. | Error. | NT |
| C5-E2E-066 | 5 | Ranking (RNK) | None | — | Non-consecutive rank → consecutive error. | Editor: Ranking. | Publish. 2. Rank 1 and 3. Next. | Error. | NT |
| C5-E2E-067 | 5 | Ranking (RNK) | None | — | Required=Min 3 consecutive → valid. | Editor: Ranking Min 3. | Publish. 2. Rank 1,2,3. Next. | Valid. | NT |
| C5-E2E-068 | 5 | Ranking (RNK) | Exclusive | — | Exclusive ranking item clears others. | Editor: Ranking choice 5 Exclusive. | Publish. 2. Rank others, then 5. | Others cleared. | NT |
| C5-E2E-069 | 5 | Ranking (RNK) | Choice Randomization | — | Items random. | Editor: Ranking Random. | Publish. 2. 3 sessions. | Varies. | NT |
| C5-E2E-070 | 5 | Ranking (RNK) | Choice Randomization | Exclusive | Exclusive position fixed. | Editor: Ranking both. | Publish. 2. Many sessions. | Exclusive fixed; others random. | NT |
| C5-E2E-071 | 5 | Ranking (RNK) | Choice Selection | — | Narrows to 3; rc auto-capped. | Editor: Ranking Choice Selection rc=5. | Publish. 2. Trigger. | rc effective=3. | NT |
| C5-E2E-072 | 5 | Ranking (RNK) | Screening Out | — | Ranked screen-out choice exits. | Editor: Ranking screen-out. | Publish. 2. Rank that choice. Next. | Exit. | NT |
| C5-E2E-073 | 5 | Ranking (RNK) | Question Selection | Choice Randomization | Q gated; random when visible. | Editor: Ranking both logics. | Publish. 2. Trigger qualifying. | Visible + random. | NT |
| C5-E2E-074 | 5 | Constant Sum (RAT) | None | — | Percent sum=100 valid. | Editor: RAT Percent. | Publish. 2. 20×5. Next. | Valid. | NT |
| C5-E2E-075 | 5 | Constant Sum (RAT) | None | — | Out-of-10; sum=10 valid. | Editor: RAT Out-of-10. | Publish. 2. 2×5. Next. | Valid. | NT |
| C5-E2E-076 | 5 | Constant Sum (RAT) | None | — | Percent sum <100 → below-total error on Next. | Editor: RAT Percent. | Publish. 2. Sum=99. Next. | Error. | NT |
| C5-E2E-077 | 5 | Constant Sum (RAT) | None | — | Percent sum >100 → auto-correct non-blocking. | Editor: RAT Percent. | Publish. 2. Sum=101. | Auto-correct. | NT |
| C5-E2E-078 | 5 | Constant Sum (RAT) | Choice Randomization | — | Items random; bar follows displayed order. | Editor: RAT Random. | Publish. 2. Load. | Bar matches order. | NT |
| C5-E2E-079 | 5 | Constant Sum (RAT) | Choice Selection | — | Narrow to 3; total still enforced. | Editor: RAT Choice Selection. | Publish. 2. Trigger; sum narrowed. | Valid. | NT |
| C5-E2E-080 | 5 | Note | Question Selection | — | Note conditional display. | Editor: Note gated. | Publish. 2. Trigger qualifying/non. | Visible/hidden accordingly. | NT |

---

## P3 Pattern — Two-Logic Combination Cases (C-2LOGIC)

These cases validate interactions between two or more logic/configuration features applied simultaneously, confirming no interference and correct combined results.

| Test ID | Logic Combination | QT | Scenario | Setup | Expected Result | NT |
| --- | --- | --- | --- | --- | --- | --- |
| C-2LOGIC-001 | rand + exclusive | MAC | Exclusive randomized with others | MAC q1 rand=random; choice-5 exclusive 5 choices | choice-5 in random position; selecting it deselects choices 1-4 |  |
| C-2LOGIC-002 | rand + exclusive | MAC | fixedLast + exclusive at bottom | MAC q1 rand=fixedLast; choice-5 exclusive AND fixed | choice-5 always last; 1-4 randomized above; exclusive deselect unchanged |  |
| C-2LOGIC-003 | rand + exclusive | MAC | Flip + exclusive | MAC q1 rand=flip; exclusive=choice-3; select choice-3 | Flip changes display order on next load; exclusive logic unchanged |  |
| C-2LOGIC-004 | questionSelect + choiceSelect | SAR | Question shown, choice filtered | SAR q2 shown by questionSelect(q1=A); choiceSelect hides choice-3 when q1=A; q1=A | q2 shown AND choice-3 hidden simultaneously; respondent selects from 1,2,4 |  |
| C-2LOGIC-005 | questionSelect + choiceSelect | SAR | Question hidden — choiceSelect irrelevant | SAR q2 hidden by questionSelect(q1=B); q1=B | q2 hidden; choiceSelect has no effect; neither rendered |  |
| C-2LOGIC-006 | questionSelect + choiceSelect | MAC | MAC shown, exclusive choice hidden | MAC q2 questionSelect shows q1=A; choiceSelect hides exclusive choice-5 when q1=A; q1=A | q2 shown; exclusive choice-5 hidden; respondent multi-selects from 1-4 without exclusive |  |
| C-2LOGIC-007 | questionSelect + choiceSelect | MTS | Matrix shown, column filtered | MTS q2 questionSelect shows q1=A; choiceSelect hides col-3 when q1=A; q1=A | q2 shown; col-3 hidden across all rows |  |
| C-2LOGIC-008 | questionSelect + choiceSelect | RAT | RAT shown, item filtered | RAT q2 questionSelect shows q1=Agree; choiceSelect hides item-2 when q1=Agree | q2 shown; item-2 row hidden; respondent rates items 1,3,4 |  |
| C-2LOGIC-009 | matrixInclusion + prohibition | MTM | Included rows, prohibited col-combo | MTM q1; matrixInclusion keeps rows 1,2,3; prohibition prevents col-1 in all 3 | 3 rows visible; selecting col-1 in all 3 blocked; max 2 rows can have col-1 | Note: matrixInclusion is MTM-only; was incorrectly listed as MTS. |
| C-2LOGIC-010 | matrixInclusion + prohibition | MTM | matrixInclusion removes row covered by prohibition | MTM q1; prohibition references row-4; matrixInclusion excludes row-4 | row-4 hidden; prohibition for row-4 irrelevant; other rows unaffected |  |
| C-2LOGIC-011 | matrixInclusion + prohibition | MTM | MTM subset + cross-row prohibition | MTM q1; matrixInclusion keeps rows 1,3,5; prohibition prevents col-2 in >2 rows | 3 rows shown; prohibition applies to visible rows only |  |
| C-2LOGIC-012 | questionSelect + required | SAR | Required hidden → submit allowed | SAR q2 required; questionSelect hides q2; condition not met | q2 hidden; required skipped; submit succeeds without q2 |  |
| C-2LOGIC-013 | questionSelect + required | SAR | Required shown → must answer | SAR q2 required; questionSelect shows q2; condition met | q2 visible and required; submit blocked if unanswered |  |
| C-2LOGIC-014 | questionSelect + required | MAC | Required MAC shown then hidden | MAC q2 required; shown q1=A; respondent answers q2; then q1→B | q2 hidden; q2 answer cleared from submission; submit succeeds |  |
| C-2LOGIC-015 | questionSelect + required | MTS | Required MTS hidden | MTS q2 all SQs required; questionSelect hides q2; condition not met | entire MTS hidden; all SQ required checks skipped; submit allowed |  |
| C-2LOGIC-016 | questionSelect + required | FA | Required FA follow-up hidden | FA q2 required; questionSelect shows q2 when q1=Other; q1=A | FA hidden; required not enforced; submit succeeds |  |
| C-2LOGIC-017 | choiceSelect + specN | MAC | Exact specN, some choices hidden — satisfiable | MAC q1 specN=exact:2; choiceSelect hides 2 of 5 → 3 visible | 3 visible; must select exactly 2; submit blocked until exactly 2 |  |
| C-2LOGIC-018 | choiceSelect + specN | MAC | Exact specN, hidden makes impossible | MAC q1 specN=exact:4; choiceSelect hides 3 of 5 → 2 visible | only 2 selectable but exact:4 required; submit blocked with specN error |  |
| C-2LOGIC-019 | choiceSelect + specN | MAC | Max specN, choices below max | MAC q1 specN=max:3; choiceSelect hides 4 of 5 → 1 visible | 1 visible; select 0 or 1 (within max:3); submit allowed |  |
| C-2LOGIC-020 | choiceSelect + specN | MTM | MTM row specN + column hidden | MTM q1 row-1 specN=exact:3; choiceSelect hides col-3 → 4 cols remain | row-1 must select exactly 3 from 4 visible cols; possible; no error |  |
| C-2LOGIC-021 | choiceSelect + specN | MTM | MTM row specN + hidden cols impossible | MTM q1 row-1 specN=exact:3; choiceSelect hides 3 cols → 2 remain | only 2 cols visible; exact:3 impossible; submit blocked |  |
| C-2LOGIC-022 | rand + matrixInclusion | MTM | Included rows randomized | MTM q1; matrixInclusion keeps 3 of 5 rows; rand=random | 3 included rows in random order; excluded rows never shown | Note: matrixInclusion is MTM-only; was incorrectly listed as MTS. |
| C-2LOGIC-023 | rand + matrixInclusion | MTM | fixedLast row + matrixInclusion | MTM q1; matrixInclusion keeps rows 1,2,3,5; rand=fixedLast; row-5 fixed | row-5 always last; rows 1,2,3 randomized; row-4 excluded | Note: matrixInclusion is MTM-only; was incorrectly listed as MTS. |
| C-2LOGIC-024 | rand + matrixInclusion | MTM | MTM included rows + random cols | MTM q1; matrixInclusion keeps rows 1,3; rand=random on cols | rows 1,3 shown; col order randomized; specN/prohibition use col IDs |  |
| C-2LOGIC-025 | exclusive + specN | MAC | Exclusive selected clears specN selections | MAC q1 specN=exact:2; excl=choice-5; select 1+2 then 5 | selecting 5 clears 1,2; now 1 selected; specN=exact:2 not met; submit blocked |  |
| C-2LOGIC-026 | exclusive + specN | MAC | Non-exclusive re-selected after exclusive | MAC q1 specN=exact:2; excl=choice-5; select 5 then 1 then 2 | selecting 1 deselects exclusive 5; then 2; exactly 2 selected; submit allowed |  |
| C-2LOGIC-027 | exclusive + specN | MAC | Max specN, exclusive within limit | MAC q1 specN=max:3; excl=choice-5; select choice-5 | 1 selection ≤ max:3; submit allowed |  |
| C-2LOGIC-028 | rand + questionSelect | SAR | Hidden question — randomization moot | SAR q2 rand=random; questionSelect hides q2 | q2 not rendered; no random order computed for hidden question |  |
| C-2LOGIC-029 | rand + questionSelect | MAC | MAC shown by questionSelect; rand applied | MAC q2 rand=random; questionSelect shows q2 when q1=A; q1=A | q2 shown with randomized choice order |  |
| C-2LOGIC-030 | rand + questionSelect | MTS | MTS shown, rows randomized | MTS q2 rand=random; questionSelect shows q2 when q1=A; q1=A | q2 matrix shown; SQ row order randomized |  |
| C-2LOGIC-031 | matrixInclusion + specN | MTM | Excluded row had specN — irrelevant | MTM q1; row-2 specN=exact:2; matrixInclusion excludes row-2 | row-2 hidden; specN for row-2 not enforced |  |
| C-2LOGIC-032 | matrixInclusion + specN | MTM | Included rows all have specN overrides | MTM q1; rows 1,2,3 included; row-1 exact:1, row-2 max:2, row-3 exact:2 | All 3 enforce their specN; submit requires all rows to satisfy |  |
| C-2LOGIC-033 | prohibition + required | MTS | Required + prohibition: empty SQ from prohibition → no validation error | MTS q1 all rows required; prohibition causes a SQ to have 0 available choices | Per spec: empty SQ resulting from prohibition is NOT a validation error — survey always advances on Next regardless of required=ON; the prohibition-forced empty state waives required for that SQ |  |
| C-2LOGIC-034 | prohibition + required | MTM | Required per-row + col prohibition | MTM q1 each row req ≥1; prohibition prevents col-3 in >1 row | every row has ≥1 selection; col-3 in at most 1 row |  |
| C-2LOGIC-035 | questionSelect + choiceSelect + required | MAC | All three: shown, filtered, required | MAC q2 required; questionSelect shows q1=A; choiceSelect hides choice-3 q1=A; q1=A | q2 shown; choice-3 hidden; required enforced with visible choices only |  |
| C-2LOGIC-036 | questionSelect + choiceSelect + required | MAC | Question hidden — required+choiceSelect skipped | MAC q2 required; questionSelect hides q1=B; q1=B | q2 hidden; required not enforced; choiceSelect not evaluated; submit succeeds |  |
| C-2LOGIC-037 | rand + exclusive + choiceSelect | MAC | 3-way: random + exclusive + choiceSelect | MAC q1 rand=random excl=ch5; choiceSelect hides ch3 q0=A; q0=A | ch3 hidden; ch5 exclusive; remaining (1,2,4,5) randomized; exclusive deselect unchanged |  |
| C-2LOGIC-038 | pbBefore + questionSelect | SAR | Page break before hidden question | SAR q2 pbBefore=true; questionSelect hides q2; condition not met | q2 hidden → page break before q2 not rendered; no blank page; flows to q3 |  |
| C-2LOGIC-039 | pbAfter + questionSelect | SAR | Page break after hidden question | SAR q2 pbAfter=true; questionSelect hides q2; condition not met | q2 hidden → pbAfter not rendered; no orphan break between q1 and q3 |  |
| C-2LOGIC-040 | pbBefore + questionSelect | MAC | Page break before MAC conditionally shown | MAC q3 pbBefore=true; questionSelect shows q3 when q1=A and q2=B; conditions met | q3 shown with page break before it; break renders correctly |  |
| C-2LOGIC-041 | matrixInclusion + choiceSelect | MTS | Row subset + column subset | MTS q1 5×5; matrixInclusion keeps rows 1,2,3; choiceSelect hides cols 4,5 q0=A; q0=A | rows 1,2,3 shown; cols 4,5 hidden; effective matrix 3×3 |  |
| C-2LOGIC-042 | matrixInclusion + choiceSelect | MTM | MTM row subset + col subset | MTM q1; matrixInclusion keeps rows 2,4; choiceSelect hides col-1; q0=A | rows 2,4 shown; col-1 hidden; specN and prohibition recalculated |  |
| C-2LOGIC-043 | specN global + specN row override | MTM | Row override takes precedence over global | MTM q1 global specN=max:3; row-1 override exact:2 | row-1 must select exactly 2; other rows use max:3 |  |
| C-2LOGIC-044 | specN global + specN row override | MTM | Row override exact > global max | MTM q1 global specN=max:1; row-2 override exact:3 | row-2 selects exactly 3 (override); other rows limited to max:1 |  |
| C-2LOGIC-045 | rand + prohibition | MTM | Column randomized; prohibition by col ID | MTM q1 rand=random cols; prohibition prevents col-ID-3 in >1 row | col display order randomized; prohibition tracks by ID not position |  |
| C-2LOGIC-046 | rand + prohibition | MTS | Row order randomized; prohibition enforced | MTS q1 rand=random rows; prohibition prevents col-2 in all rows | rows in random order; prohibition by IDs; selecting col-2 in all rows blocked |  |

---

### C-2LOGIC Additional Cases (C-2LOGIC-047–072)

| Test ID | Logic Combination | QT | Scenario | Setup | Expected Result | NT |
| --- | --- | --- | --- | --- | --- | --- |
| C-2LOGIC-047 | rand + required | SAR | Random order + required: answer mandatory regardless of position | SAR q1 rand=random required=ON; 5 choices | Choices randomized; required enforced; submit blocked if no selection regardless of which choice is where |  |
| C-2LOGIC-048 | rand + required | MTS | Flip row order + required=all: all rows required in any order | MTS q1 rand=flip required=all; 4 rows | Half see original order; half reversed; all 4 rows required in both orderings; per-row error if skipped |  |
| C-2LOGIC-049 | rand + required | MTM | Random cols + required=custom: marked rows enforced by SQ ID | MTM q1 rand=random cols required=custom; SQs 1,3 marked required | Col order randomized; SQs 1,3 required by ID regardless of display position |  |
| C-2LOGIC-050 | choiceSelect + required | SAR | Required SAR: hidden choices, 2 remain; still required | SAR q1 required=ON 5 choices; choiceSelect hides 3 → 2 visible | 2 choices visible; required still enforced; respondent must pick one; submit blocked if none picked |  |
| C-2LOGIC-051 | choiceSelect + required | RNK | Required=All RNK: hidden items reduce required count | RNK q1 required=all 5 items; choiceSelect hides item-4 → 4 remain | 4 items shown; required=all means rank all 4 visible; ranking 3 of 4 blocked |  |
| C-2LOGIC-052 | choiceSelect + required | RAT | Required RAT: hidden item reduces total constraint | RAT q1 required=ON percent total=100 5 items; choiceSelect hides item-5 → 4 visible | 4 items shown; sum of 4 must equal 100; item-5 excluded; submit blocked until sum=100 |  |
| C-2LOGIC-053 | questionSelect + rand | MAC | Question shown by condition; choices then randomized | MAC q2 rand=random; questionSelect shows q2 when q1=A; q1=A | q2 visible with randomized choices; both logics apply independently on question visibility |  |
| C-2LOGIC-054 | questionSelect + rand | MTS | MTS shown by condition; row order then flipped | MTS q2 rand=flip; questionSelect shows q2 when q1=A; q1=A | q2 matrix shown; row order flipped per respondent segment; SQ required by ID |  |
| C-2LOGIC-055 | specN + exclusive | MAC | Max:3 + exclusive: exclusive satisfies within max | MAC q1 specN=max:3; exclusive=choice-5; select choice-5 | 1 selection ≤ max:3; exclusive alone valid; submit allowed |  |
| C-2LOGIC-056 | specN + exclusive | MAC | Exact:3 + exclusive: exclusive alone does NOT satisfy exact | MAC q1 specN=exact:3; exclusive=choice-5; select choice-5 only | Per spec: exclusive → specN ignored for this question; selecting exclusive alone is valid; submit allowed |  |
| C-2LOGIC-057 | specN + exclusive | MTM | Per-row exact:2 + row exclusive: exclusive overrides | MTM q1 SQ-1 specN=exact:2; SQ-1 col-5 exclusive; select col-5 in SQ-1 | Per spec: exclusive override → specN ignored for SQ-1; col-5 alone satisfies SQ-1 |  |
| C-2LOGIC-058 | specN + disabled | MAC | Exact:3 + 1 disabled choice: specN ignored | MAC q1 specN=exact:3; choice-3 disabled; 4 selectable; respondent selects 2 | Per spec: disabled choice preventing valid count → specN ignored; 2 selections accepted |  |
| C-2LOGIC-059 | specN + disabled | MAC | Exact:3 + 0 disabled: specN fully enforced | MAC q1 specN=exact:3; no disabled choices; 5 choices; respondent selects 2 | specN enforced; 2 < exact:3; submit blocked |  |
| C-2LOGIC-060 | specN + disabled | MTM | Per-row exact:2 + disabled col: specN ignored for that row | MTM q1 SQ-1 specN=exact:2; SQ-1 col-1 disabled; 4 selectable; SQ-1 selects 1 | Per spec: disabled → specN ignored for SQ-1; 1 selection valid |  |
| C-2LOGIC-061 | matrixInclusion + required | MTM | Inclusion reveals choices; required SQ must select from revealed + baseline | MTM q1; SQ-2 required specN=unspecified; inclusion SQ1→SQ2; SQ1 selects choice-1 (revealed in SQ2) | SQ-2 has baseline + choice-1 visible; respondent selects ≥1; required satisfied |  |
| C-2LOGIC-062 | matrixInclusion + required | MTM | Inclusion reveals 0 additional; required SQ has baseline choices | MTM q1; SQ-2 required; inclusion SQ1→SQ2; SQ1 selects nothing | SQ-2 has baseline choices only; required still enforced on baseline; submit blocked if nothing selected |  |
| C-2LOGIC-063 | prohibition + specN | MTM | Prohibition reduces available cols below specN exact | MTM q1 specN=exact:3; prohibition SQ1↔SQ2; SQ1 selects choices 1,2,3 → hides 1,2,3 from SQ2 | SQ2 has only 2 cols (4,5) remaining; exact:3 impossible; per spec: impossible count → specN ignored; submit succeeds |  |
| C-2LOGIC-064 | prohibition + specN | MTM | Prohibition reduces to exactly specN: just satisfiable | MTM q1 specN=exact:2; prohibition SQ1↔SQ2; SQ1 selects choices 1,2,3 → SQ2 has 2 cols left | SQ2 can select exactly 2 from remaining 2 cols; exact:2 satisfiable; submit allowed |  |
| C-2LOGIC-065 | rand + specN | MAC | Random order + specN=exact:2: count enforced regardless of order | MAC q1 rand=random specN=exact:2; 5 choices | Choices randomized; respondent must select exactly 2; order irrelevant to count enforcement |  |
| C-2LOGIC-066 | rand + specN | MTM | Random cols + per-row exact:2: count by col ID not position | MTM q1 rand=random cols SQ-1 specN=exact:2; respondent selects 2 cols by ID | specN=exact:2 satisfied; order of cols in display irrelevant; validation by col ID count |  |
| C-2LOGIC-067 | questionSelect + specN | MAC | MAC hidden by questionSelect: specN not enforced | MAC q2 specN=exact:2; questionSelect hides q2; condition not met | q2 hidden; specN not enforced; submit without q2 answer succeeds |  |
| C-2LOGIC-068 | questionSelect + specN | MTM | MTM shown; per-row specN enforced | MTM q2 specN=exact:2; questionSelect shows q2 when q1=A; q1=A | q2 shown; each row must select exactly 2; submit blocked until all rows satisfy specN |  |
| C-2LOGIC-069 | choiceSelect + exclusive | MAC | Exclusive choice hidden by choiceSelect | MAC q1 exclusive=choice-5; choiceSelect hides choice-5; condition met | choice-5 not displayed; exclusive behavior dormant; respondent multi-selects from 1-4 freely |  |
| C-2LOGIC-070 | choiceSelect + exclusive | MAC | Non-exclusive choices hidden, exclusive remains visible | MAC q1 exclusive=choice-5; choiceSelect hides choices 1-4; choice-5 remains | only exclusive choice-5 visible; selecting it (exclusive) is the only option; deselect logic irrelevant with 1 choice |  |
| C-2LOGIC-071 | rand + choiceSelect | SAR | Random + choiceSelect hides choice after randomization | SAR q1 rand=random; choiceSelect hides choice-ID-3 when condition met | choice-ID-3 removed from displayed randomized set; remaining 4 choices in adjusted order |  |
| C-2LOGIC-072 | rand + choiceSelect | MAC | fixedLast + choiceSelect hides non-fixed choice | MAC q1 rand=fixedLast; choice-5 fixed last; choiceSelect hides choice-2 | choice-2 hidden; choice-5 still last; remaining 3 non-fixed choices randomized above |  |

## Edge-Case and Gap-Fill E2E Cases (E2E-GAP-001 – E2E-GAP-012)

These cases address coverage gaps identified in the second comprehensive review (2026-05-11). They cover scenarios not addressed in the original pipeline or combination tables.

**Columns:** Test ID | Question Type | Scenario | Pre-conditions | Steps | Expected Outcome | Tested

| Test ID | QT | Scenario | Pre-conditions | Steps | Expected Outcome | Tested |
|---|---|---|---|---|---|---|
| E2E-GAP-001 | FAL (Text Area) | FAL required=Yes end-to-end — skipping blocks, answering succeeds | Create survey: Q1 (FAL, 3 rows, required=Yes). Publish. | Open Answer. (a) Leave all rows empty; click Next. (b) Fill all 3 rows; click Next. | (a) Required error: at least one/all rows must be filled; survey does NOT advance. (b) All rows filled; required satisfied; survey advances; multi-line content preserved in submission. | NT |
| E2E-GAP-002 | FAL (Text Area) | FAL required=Custom+Minimum N rows end-to-end | Create survey: Q1 (FAL, 5 rows, required=Custom+Minimum, minimum=3). Publish. | Open Answer. (a) Fill 2 rows only; click Next. (b) Fill 3 rows; click Next. | (a) Only 2 filled < minimum 3; required error; survey blocked. (b) 3 filled ≥ minimum; required satisfied; survey advances. | NT |
| E2E-GAP-003 | FAL (Text Area) | FAL per-row type validation (number row) — realTime error end-to-end | Create survey: Q1 (FAL, row-1 type=Number). Publish. | Open Answer. (a) Type "abc" in row-1. (b) Type "42" in row-1; click Next. | (a) realTime validation error fires immediately on invalid input; field highlighted; not necessary to click Next. (b) Numeric value accepted; no error; survey advances. | NT |
| E2E-GAP-004 | RAT | Optional RAT — all items left empty → survey advances without total error | Create survey: Q1 (RAT, percent-total=100, 5 items, required=OFF). Publish. | Open Answer. Leave all 5 items at 0. Click Next. | All items empty; per spec: optional RAT with all items empty is saved as "unanswered"; no ConstantSumError; survey advances. | NT |
| E2E-GAP-005 | RAT | Optional RAT — at least one item has value → total enforcement triggered | Create survey: Q1 (RAT, percent-total=100, 5 items, required=OFF). Publish. | Open Answer. Enter 30% for item-1 only; leave items 2–5 at 0. Click Next. | 30% ≠ 100%; total enforcement triggered; ConstantSumError (ValidationErrorType=5); survey does NOT advance; respondent must adjust total to 100%. | NT |
| E2E-GAP-006 | RNK | RNK exclusive choice at rank N — prior ranks preserved; subsequent rank slots filled with exclusive choiceId in saved data | Create survey: Q1 (Ranking, 5 choices, choice-5=Exclusive, required=All, Response Count=5). Publish. | Open Answer. Rank choice-1→rank1, choice-2→rank2. Then assign choice-5→rank3. Observe ranks 1–5. Click Next. | Per spec: rank1=choice-1 and rank2=choice-2 are preserved (ranks BEFORE exclusive are unchanged); rank3=choice-5 (exclusive selected); ranks 4 and 5 automatically filled with choice-5's choiceId (exclusive choiceId propagates to all subsequent rank slots up to Response Count). UI disables rank-4 and rank-5 input. Required=All satisfied; survey advances. Saved data: S1=choice1, S2=choice2, S3=choice5, S4=choice5, S5=choice5. | NT |
| E2E-GAP-007 | Any (screeningOut) | Yellow-flag screen-out — explicit screeningOutFlg=2 verification | Create survey: Q1 (SAR), Screening Out rule on choice-A with yellow flag = ON. Publish. | Open Answer. Select choice-A. Click Next. Inspect response record in API/DB. | Survey terminates after Q1; respondent sees Thank You page; API response shows `screeningOutFlg = 2` (yellow flag, distinguishable from standard `screeningOutFlg = 1`). Standard screen-out without yellow flag would show `screeningOutFlg = 1`. | NT |
| E2E-GAP-008 | Any (page break) | Back navigation skips page whose all questions are hidden by questionSelect | Create survey: Q1 (SAR, page-1), Q2 (SAR, questionSelect shows Q2 only when Q1=A, pbBefore=true, page-2), Q3 (SAR, page-3). Publish. | Open Answer. Answer Q1=B (Q2 hidden). Navigate to page-3 (Q3). Click Back. Observe which page is shown. | Back navigation from page-3 skips page-2 (all questions hidden) and returns directly to page-1; no blank/empty page shown; Q1 answers still populated. | NT |
| E2E-GAP-009 | MTT (Bipolar Matrix) | Confirm prohibition NOT applicable to MTT — Editor-level prevention | Create survey: Q1 (MTT, 5 choices, 3 SQs). Attempt to configure prohibition (Prohibit Simultaneous Matrix Check) on Q1 in Editor. | In Editor: navigate to Q1's logic settings; attempt to configure Prohibition. Publish (if allowed). Open Answer. | Editor disables/hides the Prohibition option for MTT question types; prohibition cannot be configured on MTT. If somehow persisted, Answer runtime ignores prohibition for MTT. This case verifies no prohibition behavior fires on Bipolar Matrix. | NT |
| E2E-GAP-010 | MTS (Matrix Radio) | MTS prohibition — deselect in SQ1 restores choice in SQ2; re-select hides new choice | Create survey: Q1 (MTS, 5 choices, 3 SQs, Prohibition SQ1↔SQ2). Publish. | Open Answer. (a) Select choice-3 in SQ1; observe SQ2. (b) Deselect choice-3 in SQ1 (select choice-1 instead); observe SQ2. | (a) choice-3 hidden in SQ2 after SQ1 selects it. (b) choice-3 restored in SQ2; choice-1 now hidden in SQ2 (newly selected choice in SQ1 is now prohibited in SQ2). Dynamic real-time update; no page reload needed. | NT |
| E2E-GAP-011 | MAC | Auto-select exception: sole remaining displayed choice is Exclusive → question shown, no auto-select, even if required | Create survey: Q1 (MAC, 5 choices, choice-5=Exclusive, Specify=Exact 1, required=Yes; Choice Selection narrows to 1, and that 1 remaining choice IS choice-5). Publish. | Open Answer. Trigger Choice Selection so only choice-5 remains. Observe Q2. | Auto-select is NOT triggered: per spec, when the sole remaining displayed choice has Exclusive flag, auto-select is blocked; Q is shown to respondent; respondent must manually select choice-5. | NT |
| E2E-GAP-012 | MTS (Matrix Radio) | MTS prohibition — SQ emptied by prohibition → no required validation error; survey advances | Create survey: Q1 (MTS, 3 choices, 2 SQs, required=All, Prohibition SQ1↔SQ2: SQ1 selects all 3 choices → SQ2 has 0 available). Publish. | Open Answer. Select all 3 choices in SQ1. Click Next. | SQ2 has 0 choices remaining due to prohibition; per spec: empty SQ resulting from prohibition is NOT a validation error; survey advances on Next even though SQ2 has required=All and no selection. | NT |

---

## Change Log

| Date | Change | Case IDs |
|---|---|---|
| 2026-05-11 | 3-pass review against Confluence spec + rosemary-frontend. Pass 1: 6 accuracy corrections (C-2LOGIC-009/022/023 QT MTS→MTM for matrixInclusion, C1-E2E-036 RAT auto-fill clarified to totalValue, E2E-NEW-008 screeningOutFlg=2 explicit, C-2LOGIC-033 prohibition empty-SQ corrected). Pass 2: +12 gap-fill cases. Removed duplicate C-2LOGIC-047–072 section. Count header updated. | E2E-GAP-001–012 |
| 2026-04-27 | Added P3 expansion: 26 additional two-logic combination cases | C-2LOGIC-047–072 |
| 2026-04-27 | Added P3 base two-logic combination cases | C-2LOGIC-001–046 |

---

## Out of Scope

> These cases cover features not yet developed: **loop block** (repeating question block), **quota** routing/branching, and **user-attribute pre-fill**. They will be activated when the features ship.

### Loop Block Cases

| E2E-005 | Loop block — validation recovery in iteration 2 | Loop block over Q10–Q12; maxIterations = 3 | Complete iter 1 normally; in iter 2, submit invalid answer to Q10 (exceeds maxLength); correct and resubmit | InputLength ValidationError returned for Q10 in iter 2; respondent corrects; iter 2 completes; iter 3 proceeds normally. | NT |

### Quota Cases

| E2E-008 | Quota-based routing — quota boundary | Segment A quota = 50; 49 respondents already in segment A | Respondent 50 qualifies for A; Respondent 51 also qualifies for A | Respondent 50 → routed into segment A. Respondent 51 → quota full; routed to alternate path. Both routing decisions recorded correctly. | NT |

### User-Attribute Pre-Fill Cases

| E2E-010 | User attribute pre-fill — pre-filled answer visible on survey start | Survey with Q1 pre-filled from user\["name"\]; user\["name"\] = "Tanaka" | Open survey | Q1 displays "Tanaka" on load; modifiedMausInfo contains pre-filled value; respondent can proceed with pre-filled answer recorded | NT |

