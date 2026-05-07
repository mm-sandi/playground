# [DRAFT] 1. Editor UI Validations

**Status:** DRAFT
**Count:** 501 test cases

> **Scope:** Survey Editor — from survey creation through save, Save to AIRs, and publish.
> Answer-runtime cases live in `survey-answer-execution-FULL.md`. E2E pipeline cases live in `e2e-flow-FULL.md`.

**Sections:**
1. Survey-Level Configuration (SV-ED-001–015) — **15 cases**
2. Non-Matrix Question Types (QT-SAR, QT-MAC, QT-SAP, QT-FA, QT-FAL, QT-RNK-001–014, QT-RAT, QT-NOTE) — **49 cases**
3. Matrix Question Types (MT-MTS-001–011, MT-MTM-001–013, MT-MTT) — **30 cases**
4. Required Setting (REQ-ED-001–019) — **19 cases**
5. Randomization — Choice & Sub-question (RAND-ED-001–046) — **46 cases**
6. Randomization — Question / Section-Block (QRAND-ED-001–033) — **32 cases**
7. Specify Number of Choice (SPECN-ED-001–017) — **17 cases**
8. FA / FAL Input Settings (FA-ED-001–012) — **12 cases**
9. Logic: questionSelect (QSEL-ED-001–023) — **23 cases**
10. Logic: choiceSelect (CSEL-ED-001–014) — **14 cases**
11. Logic: subquestionSelect (SQSEL-ED-001–012) — **12 cases**
12. Logic: matrixInclusion (MINC-ED-001–008) — **8 cases**
13. Logic: countMatrix (CM-ED-001–020) — **20 cases**
14. Logic: screeningOut (SCR-ED-001–012) — **12 cases**
15. Logic: Prohibition & Exclusive (PRX-ED-001–018) — **18 cases**
16. Logic: Page Break (PB-ED-001–008) — **8 cases**
17. Logic Combinations (COMB-ED-001–030) — **30 cases**
18. Save Validation — General (SAV-ED-001–014) — **14 cases**
19. Publish Validation (PUB-ED-001–011) — **11 cases**
20. Save to AIRs (AIRS-001–015) — **15 cases**
21. Answer Reference — Editor Configuration (AREF-ED-001–033) — **33 cases**
22. Image Rendering — Editor Configuration (IMG-ED-001–036) — **36 cases**
23. AND / OR Multi-Condition Logic (LCOMB-ED-001–024) — **24 cases**

**Columns:** Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA

---

## 1. Survey-Level Configuration (SV-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| SV-ED-001 | Create survey — empty title blocked | Open Editor. Start new survey. Leave title blank. | Attempt to save. | Editor blocks save. Error: "Survey title is required." Survey not persisted. | NT | |
| SV-ED-002 | Create survey — title provided, saves | Open Editor. Enter title "Test Survey". Add one SAR question. | Click Save. | Survey saved to DB. Confirmation shown. Survey ID assigned. No errors. | NT | |
| SV-ED-003 | Add and remove pages | Open saved survey. | Add page 2. Confirm page 2 in sidebar. Remove page 2. | Page added and removed without error. Page count reflects changes. Survey saves after each operation. | NT | |
| SV-ED-004 | Duplicate survey — all settings preserved | Open survey with Q1 (SAR, required=ON, rand=random) and Q2 (MAC, specN=exact:2). | Use Duplicate Survey action. | New survey created. Q1 and Q2 duplicated with all settings intact. New survey ID assigned. | NT | |
| SV-ED-005 | Save survey with no questions — succeeds | Create survey with title. Add no questions. | Click Save. | Survey saves with empty question list. No error. | NT | |
| SV-ED-006 | Draft question — save not blocked | Add a question and leave it in Draft state. | Click Save. | Survey saves. Draft question preserved in draft state. No blocking error. | NT | |
| SV-ED-007 | Delete question — logic on dependent questions auto-cleared | Add Q1 (SAR, 5 choices). Add Q2 (SAR) with questionSelect referencing Q1. Delete Q1. | Click Save. | Survey saves without Q1. Q2 remains. Logic on Q2 that referenced Q1 is automatically cleared before save (no orphaned reference, no editor error). | NT | |
| SV-ED-008 | Reorder questions — saves new order | Add Q1, Q2, Q3 to page 1. Drag Q3 above Q1. | Click Save. | Survey saves with order Q3, Q1, Q2. Reopening confirms new order. | NT | |
| SV-ED-009 | Survey language setting — saves | Create survey. Set language to Japanese. Add one SAR question. | Click Save. | Survey saves. Language=Japanese persisted. Reopen confirms language setting. | NT | |
| SV-ED-010 | Move question between pages — saves correct position | Create 2-page survey. Add Q1 on page 1, Q2 on page 2. Drag Q2 to page 1. | Click Save. | Survey saves. Both questions on page 1. Page 2 empty (or removed). No orphaned page references. | NT | |
| SV-ED-011 | Survey title at maximum length — saves | Create survey. Enter title at maximum allowed character count (e.g., 255 characters). | Click Save. | Survey saves. Max-length title stored without truncation or error. *(Cross-ref: SAV-ED-012 tests the same boundary in the Save Validation section as a targeted edge case; SV-ED-011 validates it in the survey-creation workflow context.)* | NT | |
| SV-ED-012 | Back button defaults to hidden on new survey creation | Create a new survey. Navigate to survey settings / conditions page. | Observe back-button setting before any change. | Back button setting reads "表示しない" (hidden) by default. Admin has not explicitly set it. | NT | |
| SV-ED-013 | Back button = Show — saves and persists after reopen | Create survey. Set back button = "表示する" (show). Add one question. | Click Save. Reopen survey settings. | Saves. Back button setting persists as "表示する" after reopening. | NT | |
| SV-ED-014 | Screening-out point amount configuration — saves | Create survey. Open survey conditions / delivery settings page. Set the screening-out point award to a specific point value (e.g., 5 points). | Click Save. | Saves. Screening-out point amount persisted. When a respondent is screened out at runtime, the configured point value is awarded. | NT | |
| SV-ED-015 | Screening-out points differ by panel type — saves | Create survey. Configure screening-out point settings: General panel = 5 points, Specific panel = 10 points. | Click Save. Reopen settings. | Saves. Per-panel-type point values persisted independently. Reopening confirms both values stored correctly. | NT | |

---

## 2. Non-Matrix Question Type Configuration (QT-ED)

Tests that each non-matrix question type saves correctly with **1 choice** (boundary) and **5 choices** (normal).

### SAR — Single Answer Radio

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QT-SAR-01 | SAR with 1 choice — saves | Add SAR question with text. Add 1 choice "Option A". | Click Save. | Survey saves. 1-choice SAR persisted without error. | NT | |
| QT-SAR-02 | SAR with 5 choices — saves | Add SAR question with text. Add 5 choices (A–E). | Click Save. | Survey saves. All 5 choice texts stored correctly. | NT | |
| QT-SAR-03 | SAR empty question text — blocked | Add SAR. Leave question text blank. Add 3 choices. | Click Save. | Editor blocks. Error: question text required. | NT | |
| QT-SAR-04 | SAR blank choice text — blocked | Add SAR with text. Add 3 choices; leave choice 2 blank. | Click Save. | Editor blocks. All choice texts must be non-empty. | NT | |
| QT-SAR-05 | SAR duplicate choice texts — blocked or warned | Add SAR with text. Add 3 choices; set choices 1 and 3 to identical text "Option A". | Click Save. | Editor blocks or warns: duplicate choice text. Choices must be distinguishable. | NT | |
| QT-SAR-06 | SAR with large choice count (20 choices) — saves | Add SAR with text. Add 20 choices. | Click Save. | Survey saves. All 20 choices persisted. No performance error in editor. | NT | |

### MAC — Multiple Answer Checkbox

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QT-MAC-01 | MAC with 1 choice — saves | Add MAC with text. Add 1 choice. | Click Save. | Survey saves. MAC with 1 choice stored. | NT | |
| QT-MAC-02 | MAC with 5 choices — saves | Add MAC with text. Add 5 choices (A–E). | Click Save. | Survey saves. All 5 choices preserved. | NT | |
| QT-MAC-03 | MAC empty question text — blocked | Add MAC. Leave text blank. Add 3 choices. | Click Save. | Editor blocks. Question text required. | NT | |
| QT-MAC-04 | MAC specN=Exact:3 with 5 choices — saves | Add MAC with 5 choices. Set Specify Number = Exact 3. | Click Save. | Survey saves. specN=exact:3 persisted. | NT | |
| QT-MAC-05 | MAC duplicate choice texts — blocked or warned | Add MAC with 5 choices. Set choices 2 and 4 to identical text "Same". | Click Save. | Editor blocks or warns: duplicate choice text. | NT | |
| QT-MAC-06 | MAC choice with "Other" free-text textbox — saves | Add MAC with 5 choices. Enable "Other" textbox on choice 5. | Click Save. | Survey saves. Choice 5 has Other textbox flag persisted. | NT | |

### SAP — Dropdown / Scale

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QT-SAP-01 | SAP with 1 option — saves | Add SAP with text. Add 1 option. | Click Save. | Survey saves. 1-option SAP stored. | NT | |
| QT-SAP-02 | SAP with 5 options — saves | Add SAP with text. Add 5 options (1–5). | Click Save. | Survey saves. All 5 options preserved. | NT | |
| QT-SAP-03 | SAP empty question text — blocked | Add SAP. Leave text blank. Add 3 options. | Click Save. | Editor blocks. Question text required. | NT | |
| QT-SAP-04 | SAP blank option text — blocked | Add SAP with 5 options; leave option 3 blank. | Click Save. | Editor blocks. All option texts must be non-empty. | NT | |
| QT-SAP-05 | SAP scale endpoint labels — saves | Add SAP in scale mode with 5 points. Set left label "Strongly Disagree", right label "Strongly Agree". | Click Save. | Survey saves. Scale labels persisted. | NT | |
| QT-SAP-06 | SAP as dropdown — saves | Add SAP in dropdown mode with 5 options (labeled 1–5). | Click Save. | Survey saves. Dropdown mode and all options persisted. | NT | |

### FA — Free Answer (single-line)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QT-FA-01 | FA type=Text, maxLength=100 — saves | Add FA. Set type=Text, maxLength=100. | Click Save. | Survey saves. type and maxLength persisted. | NT | |
| QT-FA-02 | FA type=Date — saves | Add FA. Set type=Date. | Click Save. | Survey saves. type=Date stored. | NT | |
| QT-FA-03 | FA type=Number, min=0, max=100 — saves | Add FA. Set type=Number, min=0, max=100. | Click Save. | Survey saves. FA Number settings persisted. | NT | |
| QT-FA-04 | FA maxLength=0 — blocked | Add FA type=Text. Set maxLength=0. | Click Save. | Editor blocks. maxLength must be ≥ 1. | NT | |
| QT-FA-05 | FA Number min > max — blocked | Add FA type=Number. Set min=50, max=10. | Click Save. | Editor blocks. Error: min must not exceed max. | NT | |
| QT-FA-06 | FA placeholder text — saves | Add FA type=Text. Enter placeholder text "Please type here". | Click Save. | Survey saves. Placeholder text persisted. Appears in answer page input field. | NT | |

### FAL — Free Answer List (multi-line)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QT-FAL-01 | FAL size=3 lines — saves | Add FAL. Set size=3. | Click Save. | Survey saves. size=3 persisted. | NT | |
| QT-FAL-02 | FAL size=1 — boundary saves | Add FAL. Set size=1. | Click Save. | Survey saves. size=1 is valid minimum. | NT | |
| QT-FAL-03 | FAL size=0 — blocked | Add FAL. Set size=0. | Click Save. | Editor blocks. size must be ≥ 1. | NT | |
| QT-FAL-04 | FAL required=ON — saves | Add FAL. Set size=3. Set Required=ON. | Click Save. | Survey saves. FAL required=ON persisted. | NT | |

### RNK — Ranking

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QT-RNK-01 | RNK with 1 item — saves | Add RNK with text. Add 1 ranking item. | Click Save. | Survey saves. 1-item RNK stored. | NT | |
| QT-RNK-02 | RNK with 5 items — saves | Add RNK with text. Add 5 items (A–E). | Click Save. | Survey saves. All 5 items preserved. | NT | |
| QT-RNK-03 | RNK blank item text — blocked | Add RNK with 3 items; leave item 2 blank. | Click Save. | Editor blocks. All item texts must be non-empty. | NT | |
| QT-RNK-04 | RNK fixedLast item — saves | Add RNK 5 items. Mark item 5 as Fixed (fixedLast). | Click Save. | Survey saves. fixedLast flag on item 5 persisted. | NT | |
| QT-RNK-05 | RNK partial ranking allowed flag — saves | Add RNK 5 items. Enable "partial ranking" (allow respondent to rank fewer than all items). | Click Save. | Survey saves. Partial ranking flag persisted. | NT | |
| QT-RNK-06 | RNK required-count = N (rank at least N items required) | Add RNK 5 items. Set required-count = 3 (respondent must rank at least 3 items). | Click Save. | Survey saves. required-count=3 persisted. Preview shows "Required: rank up to 3rd place." | NT | |
| QT-RNK-07 | RNK required-count = total item count (all must be ranked) | Add RNK 5 items. Set required-count = 5 (all items must be ranked). | Click Save. | Survey saves. required-count=5 persisted. All 5 items are required to be ranked. | NT | |
| QT-RNK-08 | RNK required-count = 0 — blocked | Add RNK 5 items. Set required-count = 0. | Click Save. | Editor blocks. required-count must be ≥ 1. | NT | |
| QT-RNK-09 | RNK required-count > item count — blocked | Add RNK 5 items. Set required-count = 6 (exceeds 5 items). | Click Save. | Editor blocks. required-count cannot exceed total item count. | NT | |
| QT-RNK-10 | RNK display unit = 位 (rank-position suffix) — preview shows "N位：" | Add RNK 5 items. Set display unit = 位 (rank-position mode). | Click Save. Preview survey. | Saves. Preview renders rank slots as "1位：", "2位：", … "5位：". | NT | |
| QT-RNK-11 | RNK display unit = 番目 (ordinal suffix) — preview shows "N番目：" | Add RNK 5 items. Set display unit = 番目 (ordinal mode). | Click Save. Preview survey. | Saves. Preview renders rank slots as "1番目：", "2番目：", … "5番目：". | NT | |
| QT-RNK-12 | RNK required-count indicator in preview (N位まで必須) | Add RNK 5 items. Display unit = 位. Set required-count = 3 (first 3 required). | Click Save. Preview survey. | Saves. Preview shows "【 3位まで必須 】" indicator. Slots 1–3 are mandatory; slots 4–5 are optional. | NT | |
| QT-RNK-13 | RNK display format = dropdown (select-box style) — saves | Add RNK 5 items. Set display format = dropdown (select-box per rank slot). | Click Save. Preview survey. | Saves. display format = dropdown persisted. Preview renders each rank slot as a `<select>` dropdown containing item names. | NT | |
| QT-RNK-14 | RNK display format = radio-button grid — saves | Add RNK 5 items. Set display format = radio-button grid (respondent selects rank in a grid layout). | Click Save. Preview survey. | Saves. display format = radio-button grid persisted. Preview renders items as rows with radio buttons for each rank position. | NT | |

### RAT — Rating / Constant Sum

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QT-RAT-01 | RAT with 1 item — saves | Add RAT with text. Add 1 item. Configure scale. | Click Save. | Survey saves. 1-item RAT stored. | NT | |
| QT-RAT-02 | RAT with 5 items — saves | Add RAT with text. Add 5 items (A–E). Configure scale 1–5. | Click Save. | Survey saves. 5-item RAT with scale persisted. | NT | |
| QT-RAT-03 | RAT blank item text — blocked | Add RAT 3 items; leave item 1 blank. | Click Save. | Editor blocks. All item texts must be non-empty. | NT | |
| QT-RAT-04 | RAT scale endpoint labels — saves | Add RAT 5 items. Set left label "Disagree", right label "Agree". | Click Save. | Survey saves. Scale labels persisted. | NT | |
| QT-RAT-05 | RAT as constant-sum, total=100 — saves | Add RAT in constant-sum mode. Set required total = 100. Add 5 items. | Click Save. | Survey saves. constant-sum mode and total=100 persisted. | NT | |

### Note — Static Display Text

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QT-NOTE-01 | Note with text — saves | Add Note. Enter display text. | Click Save. | Survey saves. Note text persisted. No required toggle (N/A). | NT | |
| QT-NOTE-02 | Note empty text — blocked | Add Note. Leave text blank. | Click Save. | Editor blocks. Note text must not be empty. | NT | |

---

## 3. Matrix Question Type Configuration (MT-ED)

Tests matrix types with **3 sub-questions (SQs)** × **1 choice** and **3 SQs** × **5 choices**.

### MTS — Matrix Single Answer (Radio per row)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| MT-MTS-01 | MTS: 3 SQs × 1 choice — saves | Add MTS. Add 3 SQs (R1–R3). Add 1 column choice (C1). | Click Save. | Survey saves. MTS 3×1 persisted. | NT | |
| MT-MTS-02 | MTS: 3 SQs × 5 choices — saves | Add MTS. Add 3 SQs (R1–R3). Add 5 column choices (C1–C5). | Click Save. | Survey saves. MTS 3×5 stored. All SQ and choice texts preserved. | NT | |
| MT-MTS-03 | MTS: empty SQ text — blocked | Add MTS 3 SQs × 3 choices. Leave SQ2 text blank. | Click Save. | Editor blocks. All sub-question texts must be non-empty. | NT | |
| MT-MTS-04 | MTS: empty column text — blocked | Add MTS 3 SQs × 3 choices. Leave column 2 text blank. | Click Save. | Editor blocks. All column texts must be non-empty. | NT | |
| MT-MTS-05 | MTS: Disable Choice — specific cell disabled | Add MTS 3 SQs × 5 choices. Disable SQ1 × C3 in Disable Choices panel. | Click Save. | Survey saves. Disabled cell (SQ1, C3) persisted. | NT | |
| MT-MTS-06 | MTS: Required = All | Add MTS 3 SQs × 5 choices. Set Required = All. | Click Save. | Survey saves. Required=All persisted. | NT | |
| MT-MTS-07 | MTS: Required = Custom — SQ1 only | Add MTS 3 SQs × 5 choices. Set Required = Custom. Mark SQ1 required. | Click Save. | Survey saves. Required=Custom with SQ1 required. SQ2, SQ3 optional. | NT | |
| MT-MTS-08 | MTS: rand=random on rows AND columns — saves | Add MTS 3 SQs × 5 choices. Set row rand = Random AND column rand = Random. | Click Save. | Survey saves. Both row and column rand=random persisted. | NT | |
| MT-MTS-09 | MTS: all cells disabled — editor warns | Add MTS 3 SQs × 3 choices. Disable all 9 cells (SQ1–SQ3 × C1–C3). | Click Save. | Editor shows warning: all cells disabled, matrix has no selectable answers. Does not hard-block save. | NT | |
| MT-MTS-10 | MTS: column-header FA tag (`<fa size="15"/>` in column text) — saves | Add MTS 3 SQs × 5 choices. In column C1 text field, enter text containing `<fa size="15"/>`. | Click Save. | Saves. Column-header FA tag preserved in C1 text. Preview renders a text-input field next to C1 header. | NT | |
| MT-MTS-11 | MTS: cell FA tag (`<fa no="1-5" required="true" size="15"/>`) — saves | Add MTS 3 SQs × 5 choices. In SQ1 row text, enter `<fa no="1-5" required="true" size="15"/>` to define a cell FA shared across columns 1–5 for SQ1. | Click Save. | Saves. Cell FA tag preserved in SQ1 row text. At answer time, when the respondent selects any cell in SQ1, a required text-input field appears inside that cell; the respondent must fill it before the page can advance. SQ2 and SQ3 are unaffected. | NT | |

### MTM — Matrix Multiple Answer (Checkbox per row)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| MT-MTM-01 | MTM: 3 SQs × 1 choice — saves | Add MTM. Add 3 SQs and 1 column choice. | Click Save. | Survey saves. MTM 3×1 persisted. | NT | |
| MT-MTM-02 | MTM: 3 SQs × 5 choices — saves | Add MTM. Add 3 SQs and 5 column choices. | Click Save. | Survey saves. MTM 3×5 stored. | NT | |
| MT-MTM-03 | MTM: specN Exact=2 on SQ1 (3×5) — saves | Add MTM 3 SQs × 5 choices. Set SQ1 specN = Exact 2. | Click Save. | Survey saves. SQ1 specN=exact:2 persisted. SQ2, SQ3 unaffected. | NT | |
| MT-MTM-04 | MTM: specN Exact=2 on SQ1 (3×1) — blocked | Add MTM 3 SQs × 1 choice. Set SQ1 specN = Exact 2. | Click Save. | Editor blocks. Exact:2 > 1 available choice. Error shown. | NT | |
| MT-MTM-05 | MTM: Switch to Radio on SQ2 | Add MTM 3 SQs × 5 choices. Enable Switch to Radio on SQ2. | Click Save. | Survey saves. SQ2 set as radio (single-select). SQ1, SQ3 remain checkbox. | NT | |
| MT-MTM-06 | MTM: prohibition SQ1 → SQ2 | Add MTM 3 SQs × 5 choices. Add prohibition: if SQ1=C1 then SQ2 cannot select C1. | Click Save. | Survey saves. Prohibition rule persisted. | NT | |
| MT-MTM-07 | MTM: Required = Custom — SQ2 and SQ3 | Add MTM 3 SQs × 5 choices. Set Required=Custom. Mark SQ2 and SQ3 required. | Click Save. | Survey saves. SQ2 and SQ3 required flag persisted. | NT | |
| MT-MTM-08 | MTM: matrixInclusion from another matrix | Add Q1 (MTM, 3 SQs × 5 choices). Add Q2 (MTM, 3 SQs × 5 choices). Configure matrixInclusion on Q2 to include SQ1 and SQ3 from Q1. | Click Save. | Survey saves. matrixInclusion rule stored on Q2. | NT | |
| MT-MTM-09 | MTM: SQ1 specN=Exact:2 with 2 disabled choices (3×5, 3 active) — saves | Add MTM 3 SQs × 5 choices. Disable C4 and C5 in SQ1. Set SQ1 specN=Exact:2. | Click Save. | Survey saves. Per spec: disabled choices reduce effective pool but specN override rules apply at runtime. Editor does not block. | NT | |
| MT-MTM-10 | MTM: row rand=random — SQ3 fixed at last position | Add MTM 3 SQs × 5 choices. Set row rand=random. Mark SQ3 as fixed. | Click Save. | Survey saves. Row rand=random with SQ3 fixed flag persisted. SQ1 and SQ2 shuffle; SQ3 stays at authored position. | NT | |
| MT-MTM-11 | MTM: row FA tag (`<fa/>`) in sub-question text — saves | Add MTM 3 SQs × 5 choices. In SQ2 text, append `<fa/>`. | Click Save. | Saves. Row FA tag preserved in SQ2 text. Preview shows a text-input field beside SQ2's row header. | NT | |
| MT-MTM-12 | MTM: cell FA with `required="true"` attribute — saves | Add MTM 3 SQs × 5 choices. In SQ1 text, add `<fa required="true" size="15"/>`. | Click Save. | Saves. Required cell FA persisted. At answer time, if a cell in SQ1 is checked, the FA input becomes mandatory before the page can advance. | NT | |
| MT-MTM-13 | MTM: column-header FA with `type="number"` (numeric-only input) — saves | Add MTM 3 SQs × 5 choices. In column C1 text, enter `<fa type="number" size="10"/>`. | Click Save. | Saves. Numeric-only FA tag preserved in C1 column header. Preview renders a number-input field next to the C1 header; non-numeric input is rejected at answer time. | NT | |

### MTT — Matrix Bipolar

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| MT-MTT-01 | MTT: 3 SQs × 1 choice — saves | Add MTT. Add 3 SQs and 1 column. Configure left/right labels. | Click Save. | Survey saves. MTT 3×1 persisted. | NT | |
| MT-MTT-02 | MTT: 3 SQs × 5 choices — saves | Add MTT. Add 3 SQs and 5 columns. Configure left/right labels. | Click Save. | Survey saves. MTT 3×5 with labels stored. | NT | |
| MT-MTT-03 | MTT: missing bipolar labels — blocked | Add MTT 3 SQs × 5 choices. Leave left label blank. | Click Save. | Editor blocks. Both bipolar endpoint labels required. | NT | |
| MT-MTT-04 | MTT: Required = All | Add MTT 3 SQs × 5 choices. Set Required = All. | Click Save. | Survey saves. Required=All persisted. | NT | |
| MT-MTT-05 | MTT: Required = Custom — SQ1 and SQ3 | Add MTT 3 SQs × 5 choices. Set Required=Custom. Mark SQ1 and SQ3 required. | Click Save. | Survey saves. SQ1 and SQ3 required flags persisted. SQ2 optional. | NT | |
| MT-MTT-06 | MTT: rand=random on columns — saves | Add MTT 3 SQs × 5 choices. Set column rand=Random. | Click Save. | Survey saves. Column rand=random persisted. | NT | |

---

## 4. Required Setting — Editor Validation (REQ-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| REQ-ED-001 | Required=ON on SAR (1 choice) — saves | Add SAR 1 choice. Set Required=ON. | Click Save. | Saves. required=ON persisted. | NT | |
| REQ-ED-002 | Required=ON on SAR (5 choices) — saves | Add SAR 5 choices. Set Required=ON. | Click Save. | Saves. required=ON persisted. | NT | |
| REQ-ED-003 | Required=ON on MAC (5 choices) — saves | Add MAC 5 choices. Set Required=ON. | Click Save. | Saves. required=ON persisted. | NT | |
| REQ-ED-004 | Required=ON on SAP (5 choices) — saves | Add SAP 5 choices. Set Required=ON. | Click Save. | Saves. required=ON persisted. | NT | |
| REQ-ED-005 | Required=ON on FA — saves | Add FA type=Text. Set Required=ON. | Click Save. | Saves. required=ON persisted. | NT | |
| REQ-ED-006 | Required=ON on RNK (5 items) — saves | Add RNK 5 items. Set Required=ON. | Click Save. | Saves. required=ON persisted. | NT | |
| REQ-ED-007 | Required=ON on RAT (5 items) — saves | Add RAT 5 items. Set Required=ON. | Click Save. | Saves. required=ON persisted. | NT | |
| REQ-ED-008 | Required toggle disabled for Note | Add Note. Open settings panel. | Observe Required field. | Required toggle absent or grayed out. Cannot enable required on Note type. | NT | |
| REQ-ED-009 | Toggle ON→OFF→ON, save, reopen — final ON | Add SAR 3 choices. Toggle required ON, then OFF, then ON. | Save. Reopen survey. | Required=ON persists after reopen. Toggle stored correctly. | NT | |
| REQ-ED-010 | MTS Required = All — saves | Add MTS 3 SQs × 5 choices. Set Required = All. | Click Save. | Saves. Required=All stored for all SQs. | NT | |
| REQ-ED-011 | MTS Required = Custom — SQ1 only | Add MTS 3 SQs × 5 choices. Set Required = Custom. Mark SQ1. | Click Save. | Saves. Required=Custom with SQ1 flag. SQ2, SQ3 optional. | NT | |
| REQ-ED-012 | MTM Required = Custom — all 3 SQs marked | Add MTM 3 SQs × 5 choices. Set Required=Custom. Mark all 3. | Click Save. | Saves. All 3 SQs required. Functionally equivalent to All Required. | NT | |
| REQ-ED-013 | Required=ON + all choices hidden by choiceSelect — editor warns | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set Required=ON on Q2. Add choiceSelect: hide all 5 choices of Q2 when Q1=C1. | Click Save. | Editor shows save-time warning: required question may have no visible choices under this condition. Does not hard-block save. | NT | |
| REQ-ED-014 | Duplicate question — required flag preserved | Add SAR 3 choices Required=ON. Duplicate the question. | Inspect copy. | Duplicate has Required=ON. All settings faithfully copied. | NT | |
| REQ-ED-015 | Required=ON on FAL — saves | Add FAL. Set size=3. Set Required=ON. | Click Save. | Saves. FAL required=ON persisted. | NT | |
| REQ-ED-016 | Required=ON on MTT (5 choices) — saves | Add MTT 3 SQs × 5 choices. Set Required=All. | Click Save. | Saves. MTT Required=All persisted for all SQs. | NT | |
| REQ-ED-017 | MTS Required: switch All→Custom→OFF→All — final state persists | Add MTS 3 SQs × 5 choices. Set Required=All. Change to Custom (mark SQ1). Change to OFF. Change back to All. | Save. Reopen. | Required=All persisted as final setting. Reopen confirms All mode. | NT | |
| REQ-ED-018 | MTM Required=Custom — 0 rows marked | Add MTM 3 SQs × 5 choices. Set Required=Custom. Mark no rows. | Click Save. | Editor shows warning: Custom mode with no rows marked is equivalent to OFF. Saves without error. | NT | |
| REQ-ED-019 | MAC Required=ON with all choices exclusive — editor accepts | Add MAC 5 choices. Mark all 5 as Exclusive. Set Required=ON. | Click Save. | Saves. Per spec: exclusive choices are valid selections; required still enforceable. | NT | |

---

## 5. Randomization — Choice & Sub-question (RAND-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| RAND-ED-001 | SAR rand=random (5 choices) — saves | Add SAR 5 choices. Set Randomization = Random. | Click Save. | Saves. rand=random persisted. | NT | |
| RAND-ED-002 | SAR rand=flip (5 choices) — saves | Add SAR 5 choices. Set Randomization = Flip. | Click Save. | Saves. rand=flip persisted. | NT | |
| RAND-ED-003 | SAR rand=random — all choices fixed (effective no-op) | Add SAR 5 choices. Set rand=random. Mark all 5 choices as fixed (randomize=false). | Click Save. | Saves. rand=random persisted with all choices pinned. Editor may show info: no choices will be shuffled. | NT | |
| RAND-ED-004 | SAR rand=random — choice 5 fixed, rest shuffle | Add SAR 5 choices. Set rand=random. Mark only choice 5 as fixed (pinned to last position). | Click Save. | Saves. rand=random persisted. Choice 5 fixed flag persisted. Choices 1–4 will shuffle; choice 5 stays at authored position. | NT | |
| RAND-ED-005 | SAR rand=random (1 choice) — valid no-op | Add SAR 1 choice. Set rand=random. | Click Save. | Saves. Editor accepts rand on 1-choice question (runtime no-op). | NT | |
| RAND-ED-006 | MAC rand=random (5 choices) — saves | Add MAC 5 choices. Set rand=random. | Click Save. | Saves. rand=random persisted. | NT | |
| RAND-ED-007 | MAC rand=random — choices 4 and 5 fixed | Add MAC 5 choices. Set rand=random. Mark choices 4 and 5 as fixed (randomize=false). | Click Save. | Saves. rand=random persisted. Choices 4 and 5 fixed flags persisted. Choices 1–3 shuffle; choices 4–5 stay at authored positions. | NT | |
| RAND-ED-008 | MTS rand=random on rows (3 SQs × 5 choices) — saves | Add MTS 3 SQs × 5 choices. Set row rand = Random. | Click Save. | Saves. rand=random on rows persisted. | NT | |
| RAND-ED-009 | MTS rand=random on columns (3 SQs × 5 choices) — saves | Add MTS 3 SQs × 5 choices. Set column rand = Random. | Click Save. | Saves. rand=random on columns persisted. | NT | |
| RAND-ED-010 | MTS rand=flip on rows (3 SQs × 1 choice) — saves | Add MTS 3 SQs × 1 choice. Set row rand = Flip. | Click Save. | Saves. rand=flip on rows persisted even with 1 column. | NT | |
| RAND-ED-011 | MTM rand=random rows (3 SQs × 5 choices) — saves | Add MTM 3 SQs × 5 choices. Set row rand = Random. | Click Save. | Saves. rand=random on rows persisted. | NT | |
| RAND-ED-012 | MTT rand=flip rows (3 SQs × 5 choices) — saves | Add MTT 3 SQs × 5 choices. Set row rand = Flip. | Click Save. | Saves. rand=flip on rows persisted. | NT | |
| RAND-ED-013 | RNK rand=random (5 items) — saves | Add RNK 5 items. Set rand=random. | Click Save. | Saves. rand=random persisted. | NT | |
| RAND-ED-014 | RAT rand=flip (5 items) — saves | Add RAT 5 items. Set rand=flip. | Click Save. | Saves. rand=flip persisted. | NT | |
| RAND-ED-015 | FA rand — editor disables option | Add FA. | Attempt to set rand on FA. | Randomization control absent or disabled for FA. Cannot set rand on FA. | NT | |
| RAND-ED-016 | Note rand — editor disables option | Add Note. | Attempt to set rand on Note. | Randomization control absent or disabled for Note. | NT | |
| RAND-ED-017 | SAP rand=random (5 choices) — saves | Add SAP 5 choices. Set rand=random. | Click Save. | Saves. rand=random persisted for SAP. | NT | |
| RAND-ED-018 | SAP rand=flip (5 choices) — saves | Add SAP 5 choices. Set rand=flip. | Click Save. | Saves. rand=flip persisted for SAP. | NT | |
| RAND-ED-019 | MAC rand=flip (5 choices) — saves | Add MAC 5 choices. Set rand=flip. | Click Save. | Saves. rand=flip persisted for MAC. | NT | |
| RAND-ED-020 | RNK rand=random — 1 of 3 items randomizable (items 2 and 3 fixed) | Add RNK 3 items. Set rand=random. Mark items 2 and 3 as fixed. Only item 1 participates in shuffle. | Click Save. | Saves. rand=random persisted. Items 2 and 3 fixed flags persisted. Editor accepts even though only 1 item shuffles. | NT | |
| RAND-ED-021 | MAC with choice groups, group rand=random — saves | Add MAC 5 choices. Create 2 choice groups using separator. Set group rand=random. | Click Save. | Saves. Choice groups and group rand=random persisted. Groups shuffle independently of per-choice rand. | NT | |
| RAND-ED-022 | MAC with choice groups, group rand=flip — saves | Add MAC 5 choices in 2 groups. Set group rand=flip. | Click Save. | Saves. Group rand=flip persisted. | NT | |
| RAND-ED-023 | MAC mixed grouped and ungrouped choices — blocked | Add MAC 5 choices. Move 3 into a group; leave 2 ungrouped. | Click Save. | Editor blocks. All choices must be grouped or all ungrouped; mixing is invalid. | NT | |
| RAND-ED-024 | MTS with SQ groups, SQ-group rand=random — saves | Add MTS 3 SQs × 5 choices. Create 2 SQ groups. Set SQ-group rand=random. | Click Save. | Saves. SQ groups and SQ-group rand=random persisted. | NT | |
| RAND-ED-025 | MTM with SQ groups, SQ-group rand=flip — saves | Add MTM 3 SQs × 5 choices in 2 SQ groups. Set SQ-group rand=flip. | Click Save. | Saves. SQ-group rand=flip persisted. | NT | |
| RAND-ED-026 | MTM rand=flip on columns (3 SQs × 5 choices) — saves | Add MTM 3 SQs × 5 choices. Set column rand=flip. | Click Save. | Saves. Column rand=flip persisted. Same column order (flipped) displayed across all rows. | NT | |
| RAND-ED-027 | MTT rand=random on columns (3 SQs × 5 choices) — saves | Add MTT 3 SQs × 5 choices. Set column rand=random. | Click Save. | Saves. Column rand=random persisted for MTT. | NT | |
| RAND-ED-028 | RAT rand=random on sub-questions (items) — saves | Add RAT 5 items. Set sub-question rand=random. | Click Save. | Saves. Sub-question rand=random persisted on RAT. | NT | |
| RAND-ED-029 | RAT rand=flip on sub-questions — saves | Add RAT 5 items. Set sub-question rand=flip. | Click Save. | Saves. Sub-question rand=flip persisted on RAT. | NT | |
| RAND-ED-030 | MTS: all column choices fixed, column rand=random — saves (no-op) | Add MTS 3 SQs × 5 choices. Set column rand=random. Mark all 5 columns as fixed. | Click Save. | Saves. All columns fixed; rand=random is a no-op at runtime. Editor does not block. | NT | |
| RAND-ED-031 | MTM: all SQs fixed, SQ rand=random — saves (no-op) | Add MTM 3 SQs × 5 choices. Set SQ rand=random. Mark all 3 SQs as fixed. | Click Save. | Saves. All SQs fixed; SQ rand=random is a no-op at runtime. Editor does not block. | NT | |
| RAND-ED-032 | SAR rand=random — middle choice (C3 of 5) fixed | Add SAR 5 choices. Set rand=random. Mark only choice 3 as fixed. | Click Save. | Saves. Choice 3 fixed at its authored position. Choices 1, 2, 4, 5 shuffle around it. | NT | |
| RAND-ED-033 | MAC rand=random all choices fixed — effective OFF | Add MAC 5 choices. Set rand=random. Mark all 5 choices as fixed. | Click Save. | Saves. With all choices pinned, rand is effectively OFF at runtime. Editor persists the config without blocking. | NT | |
| RAND-ED-034 | MTS column rand=random with C5 fixed — saves | Add MTS 3 SQs × 5 choices. Set column rand=random. Mark column C5 as fixed. | Click Save. | Saves. C5 stays at authored position. Columns C1–C4 shuffle. Consistent across all rows. | NT | |
| RAND-ED-035 | MTT: SQ rand=random + column rand=flip simultaneously — saves | Add MTT 3 SQs × 5 choices. Set SQ rand=random AND column rand=flip. | Click Save. | Saves. Both independent randomization controls persisted. Sub-question order randomized; column order flipped per respondent. | NT | |
| RAND-ED-036 | RNK rand=flip (5 items) — saves | Add RNK 5 items. Set rand=flip. | Click Save. | Saves. RNK rand=flip persisted. Items displayed in reverse order for half of respondents. | NT | |
| RAND-ED-037 | SAR rand=random → turn off (set to OFF) — saves | Add SAR 5 choices with rand=random. Remove randomization (set to OFF). | Click Save. | Saves. rand=OFF persisted. Reopening confirms no randomization. | NT | |
| RAND-ED-038 | MTS: SQ-group rand + SQ individual rand simultaneously — saves | Add MTS 3 SQs in 2 SQ groups. Set SQ-group rand=random AND SQ individual rand=random. | Click Save. | Saves. Both SQ-group and SQ individual rand controls are independent and coexist. | NT | |
| RAND-ED-039 | MTM row rand=flip (3 SQs × 5 choices) — saves | Add MTM 3 SQs × 5 choices. Set row rand=flip. | Click Save. | Saves. Row rand=flip persisted for MTM. | NT | |
| RAND-ED-040 | MTS column rand=flip (3 SQs × 5 choices) — saves | Add MTS 3 SQs × 5 choices. Set column rand=flip. | Click Save. | Saves. Column rand=flip persisted for MTS. | NT | |
| RAND-ED-041 | FAL rand — editor disables option | Add FAL. | Attempt to set rand on FAL. | Randomization control absent or disabled for FAL. Cannot set rand on FAL. | NT | |
| RAND-ED-042 | Duplicate question — rand settings and fixed flags preserved | Add SAR 5 choices. Set rand=random. Mark choice 5 as fixed. Save. Duplicate the question. | Inspect copy. | Duplicate has rand=random and choice 5 fixed flag preserved. All per-choice fixed flags copied faithfully. | NT | |
| RAND-ED-043 | SAR rand=flip — choice 3 fixed (middle position) | Add SAR 5 choices. Set rand=flip. Mark choice 3 as fixed. | Click Save. | Saves. rand=flip persisted. Choice 3 stays at authored position; remaining choices flip order around it. | NT | |
| RAND-ED-044 | MTM column rand=random (3 SQs × 5 choices) — saves | Add MTM 3 SQs × 5 choices. Set column rand=random. | Click Save. | Saves. Column rand=random persisted for MTM. Column order randomized consistently across all rows. | NT | |
| RAND-ED-045 | RAT: sub-question group rand=random — saves | Add RAT 5 items arranged in 2 SQ groups. Set SQ-group rand=random. | Click Save. | Saves. Sub-question group rand=random persisted on RAT. | NT | |
| RAND-ED-046 | MTS: SQ2 fixed in row rand, SQ1 and SQ3 shuffle — saves | Add MTS 3 SQs × 5 choices. Set row rand=random. Mark SQ2 as fixed. | Click Save. | Saves. SQ2 fixed at its authored position. SQ1 and SQ3 shuffle around it. | NT | |

---

## 6. Randomization — Question / Section-Block (QRAND-ED)

> Question randomization reorders entire questions (grouped into **Sections**) within a **Block**. Only `RANDOM` shuffle mode is available at this level. The Section/Block UI is accessed via a dedicated tab in the Editor, separate from the per-question settings panel.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QRAND-ED-001 | Create block with 2 randomizable sections — saves | Create survey with Q1–Q4. Group Q1–Q2 in Section 1 and Q3–Q4 in Section 2. Create a block containing both sections. Mark both sections as randomizable. | Click Save. | Saves. Block with 2 randomizable sections persisted. | NT | |
| QRAND-ED-002 | Block with only 1 randomizable section — blocked | Create survey Q1–Q4. Create block with Section 1 (Q1, Q2). Mark 1 section as randomizable. No second section. | Attempt to confirm block. | Editor blocks. Minimum 2 randomizable sections required per block. Error shown. | NT | |
| QRAND-ED-003 | Fixed section in block (1 fixed + 2 randomizable) — saves | Create block with 3 sections: Section 1 marked fixed, Sections 2 and 3 randomizable. | Click Save. | Saves. Fixed section retains authored position. Sections 2 and 3 shuffle. | NT | |
| QRAND-ED-004 | "Max sections displayed" = 1 (block has 3 randomizable sections) — saves | Create block with 3 randomizable sections. Set max sections displayed = 1. | Click Save. | Saves. Only 1 randomly-chosen section shown to each respondent. | NT | |
| QRAND-ED-005 | "Max sections displayed" = 0 — blocked | Create block with 3 sections. Set max sections displayed = 0. | Attempt to save. | Editor blocks. Max sections displayed must be ≥ 1. | NT | |
| QRAND-ED-006 | "Max sections displayed" > total section count — blocked | Create block with 3 sections. Set max sections displayed = 4. | Attempt to save. | Editor blocks. Max sections displayed cannot exceed total section count. | NT | |
| QRAND-ED-007 | "Max sections displayed" < (fixed section count + 1) — blocked | Create block with 3 sections: 2 fixed + 1 randomizable. Set max sections displayed = 2. (Fixed count=2, so min valid = 3.) | Attempt to save. | Editor blocks. Max sections displayed must be ≥ fixed sections + 1. Error shown. | NT | |
| QRAND-ED-008 | Delete section would leave block with <2 randomizable — delete disabled | Create block with exactly 2 randomizable sections. | Attempt to delete one section. | Delete button disabled. Editor prevents reducing randomizable section count below 2. | NT | |
| QRAND-ED-009 | Questions outside all sections — maintain authored position | Survey with Q1 (outside any section), Q2–Q3 in Section 1, Q4–Q5 in Section 2, Q6 (outside). Create block with Sections 1 and 2. | Click Save. | Saves. Q1 and Q6 display at their authored positions relative to the block. | NT | |
| QRAND-ED-010 | Move/copy/delete disabled for questions inside a section | Create block with Section 1 containing Q1 and Q2. | Observe question-card controls on Q1. | Move-up, move-down, copy, and delete buttons on Q1 and Q2 are disabled while inside the section. | NT | |
| QRAND-ED-011 | "Max sections displayed" = total section count — saves (show all) | Create block with 3 randomizable sections. Set max sections displayed = 3. | Click Save. | Saves. All sections shown to every respondent in random order. | NT | |
| QRAND-ED-012 | Block with all sections fixed (0 randomizable) — blocked | Create block with 3 sections. Mark all 3 as fixed. | Attempt to save. | Editor blocks. At least 2 sections must be randomizable within a block. | NT | |
| QRAND-ED-013 | 3-section block: 2 randomizable + 1 fixed at authored-last position — saves | Create block with Section 1 (randomizable), Section 2 (randomizable), Section 3 (fixed, placed last). | Click Save. | Saves. Section 3 always displayed last. Sections 1 and 2 shuffle. | NT | |
| QRAND-ED-014 | questionSelect from question in Section A to question in Section B (same block) — blocked | Create block with Section A (Q1) and Section B (Q2). Set questionSelect on Q2 referencing Q1. | Attempt to save. | Editor blocks. Logic between questions in different sections of the same block is not permitted. | NT | |
| QRAND-ED-015 | questionSelect from question in Block 1 to question in Block 2 — allowed | Create 2 separate blocks. Q1 in Block 1, Q2 in Block 2. Set questionSelect on Q2 referencing Q1. | Click Save. | Saves. Cross-block logic is permitted because block-level order is never randomized. | NT | |
| QRAND-ED-016 | questionSelect from question outside section to question inside section — allowed | Q1 outside any section. Q2 inside Section A (in a block). Set questionSelect on Q2 referencing Q1. | Click Save. | Saves. Logic from a fixed-position question to a sectioned question is permitted. | NT | |

> **Note — QRAND-ED-017 intentionally absent.** A case with that ID was added during an earlier pass but subsequently removed as a duplicate of QRAND-ED-007 (both tested "block with all sections fixed is blocked"). The numbering gap is intentional; no case should be renumbered to fill it.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QRAND-ED-018 | Copy-paste logic from question in Section A to question in Section B — blocked | Create block with Section A (Q1) and Section B (Q2). Attempt to copy the questionSelect logic from Q1 and paste it on Q2 (different section, same block). | Attempt copy-paste. | Editor blocks copy-paste of logic across different sections within the same block. | NT | |
| QRAND-ED-019 | Question inside section with choice rand=random — coexists | Create block with Section 1 containing Q1 (SAR, 5 choices). Set rand=random on Q1's choices. | Click Save. | Saves. Choice-level randomization and question-level section membership coexist. Both settings persisted independently. | NT | |
| QRAND-ED-020 | Delete section from block with 3 randomizable sections — succeeds | Create block with 3 randomizable sections. Delete Section 2. | Observe editor. | Section 2 deleted. Block now has 2 randomizable sections. Delete is permitted because ≥ 2 randomizable sections remain. | NT | |

### Section + Logic Restrictions (QRAND-ED-021–030)

> Per spec (page 1582366789): the cross-section restriction within the same block applies to **all selection logic types**, not only questionSelect. Logic is blocked between questions in different sections of the same block regardless of logic type.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QRAND-ED-021 | choiceSelect cross-section same block — blocked | Create block with Section A (Q1: SAR, 5 choices) and Section B (Q2: SAR, 5 choices). Attempt to set choiceSelect on Q2: hide Q2.C3 when Q1=C1. Q1 and Q2 are in different sections of the same block. | Attempt to configure logic. | Editor blocks. Per spec: all selection logic types (including choiceSelect) are not configurable between questions in different sections of the same block. | NT | |
| QRAND-ED-022 | subquestionSelect cross-section same block — blocked | Create block with Section A (Q1: SAR, 5 choices) and Section B (Q2: MTS, 3 SQs × 5 choices). Attempt subquestionSelect on Q2: hide Q2.SQ1 when Q1=C1. | Attempt to configure logic. | Editor blocks. subquestionSelect cannot be set between different sections of the same block. | NT | |
| QRAND-ED-023 | countMatrix cross-section same block — blocked | Create block with Section A (Q1: MTM, 3 SQs × 5 choices) and Section B (Q2: SAR). Attempt to set countMatrix condition: show Q2 if countMatrix(Q1)>=2 (Q1 in Section A, Q2 in Section B). | Attempt to configure logic. | Editor blocks. countMatrix condition source and target cannot span different sections of the same block. | NT | |
| QRAND-ED-024 | matrixInclusion cross-section same block — blocked | Create block with Section A (Q1: MTS, 3 SQs × 5 choices) and Section B (Q2: MTM, 3 SQs × 5 choices). Attempt matrixInclusion on Q2 from Q1. | Attempt to configure logic. | Editor blocks. matrixInclusion cannot reference a source question in a different section of the same block. | NT | |
| QRAND-ED-025 | Adding section/block AFTER logic is already configured — error | Create survey. Add Q1 (SAR, 5 choices) and Q2 (SAR) on same page. Set questionSelect: show Q2 if Q1=C1. Save. Now attempt to place Q1 in Section A and Q2 in Section B of a new block. | Attempt section assignment. | Editor displays error. The existing cross-question logic conflicts with placing Q1 and Q2 in different sections of the same block. User must remove the logic before this section assignment is permitted. | NT | |
| QRAND-ED-026 | Logic source inside section → target question after block — allowed | Create block with Section A containing Q1 (SAR, 5 choices). Place Q2 (SAR) after the block (outside any section, positioned after the block in survey order). Set questionSelect on Q2: show if Q1=C1. | Click Save. | Saves. Source Q1 is inside a section; target Q2 is always positioned after the block. Relative order is guaranteed (block always precedes post-block questions). Editor allows the logic. | NT | |
| QRAND-ED-027 | Logic within same section without page break — blocked | Create block with Section A containing Q1 (SAR, 5 choices) and Q2 (SAR) as consecutive items (no page break between them). Attempt to set questionSelect on Q2: show if Q1=C1. | Attempt to configure logic. | Editor blocks. Even within the same section, a page break must exist between source and target questions before selection logic can be set. The mandatory page break rule applies globally, including within sections. | NT | |
| QRAND-ED-028 | Required=ON on question inside section with max-sections-displayed limit — saves | Create block with 3 sections: Section 1 contains Q1 (SAR, required=ON). Set max sections displayed = 1. | Click Save. | Saves. Editor places no restriction on required=ON inside a section that may not be displayed to some respondents. Runtime required-check bypass (when section is not shown) is handled at answer time. | NT | |
| QRAND-ED-029 | screeningOut on question inside section — saves | Create block with Section A containing Q1 (SAR, 5 choices). Mark Q1.C3 as screen-out. | Click Save. | Saves. screeningOut on a question inside a randomized section is permitted. No section-specific restriction exists in the spec. | NT | |
| QRAND-ED-030 | Manual logic input cross-section same block — blocked | Create block with Section A (Q1: SAR, 5 choices) and Section B (Q2: SAR). Attempt to manually type/enter a logic expression in Q2's manual logic field that references Q1 as source. | Attempt to confirm manual logic. | Editor blocks. Per spec: the cross-section restriction applies equally to manual logic input and UI-based logic configuration. | NT | |

### Section Item Ordering & Additional Cases (QRAND-ED-031–033)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QRAND-ED-031 | Logic within same section WITH page break — allowed | Create block with Section A containing Q1 (SAR, 5 choices), a page break, then Q2 (SAR) as consecutive items. Set questionSelect on Q2: show if Q1=C1. | Click Save. | Saves. The mandatory page break rule is satisfied even within the same section. Logic between Q1 and Q2 within the same section is permitted when a page break separates them. | NT | |
| QRAND-ED-032 | Block page break — saves | Create survey with Q1 (SAR) before a block and Q2 (SAR) as the first question inside the block's Section A. Set a block page break (page break placed before the block start, distinct from item-level pbBefore). | Click Save. | Saves. Block page break persisted. Block page break is a separate setting from item-level page breaks and is valid for separating pre-block content from the block. | NT | |
| QRAND-ED-033 | Non-consecutive section items (skip a question in the middle) — blocked | Create survey Q1, Q2, Q3 (all SAR). Attempt to create Section A that includes Q1 and Q3 but NOT Q2 (leaving Q2 outside the section, skipping it in the middle of the section range). | Attempt section assignment. | Editor blocks. Per spec: items set in sections must be consecutive — skipping questions in the middle is not permitted. Q1 and Q3 can only be in the same section if Q2 is also included. | NT | |

---

## 7. Specify Number of Choice — Editor Validation (SPECN-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| SPECN-ED-001 | MAC specN = NONE (5 choices) — saves | Add MAC 5 choices. Set Specify Number = None. | Click Save. | Saves. specN=none persisted. | NT | |
| SPECN-ED-002 | MAC specN = Exact:1 (5 choices) — saves | Add MAC 5 choices. Set specN = Exact 1. | Click Save. | Saves. specN=exact:1 persisted. | NT | |
| SPECN-ED-003 | MAC specN = Exact:5 = choiceCount — saves | Add MAC 5 choices. Set specN = Exact 5. | Click Save. | Saves. specN=exact:5 at choiceCount boundary is valid. | NT | |
| SPECN-ED-004 | MAC specN = Exact:6 > 5 choices — blocked | Add MAC 5 choices. Set specN = Exact 6. | Click Save. | Editor blocks. Error: specN exceeds available choices. | NT | |
| SPECN-ED-005 | MAC specN = Max:3 (5 choices) — saves | Add MAC 5 choices. Set specN = Max 3. | Click Save. | Saves. specN=max:3 persisted. | NT | |
| SPECN-ED-006 | MAC specN = Max:5 = choiceCount — saves | Add MAC 5 choices. Set specN = Max 5. | Click Save. | Saves. Max:5 is valid boundary. | NT | |
| SPECN-ED-007 | MAC specN = Max:6 > 5 choices — blocked | Add MAC 5 choices. Set specN = Max 6. | Click Save. | Editor blocks. Max exceeds available choices. | NT | |
| SPECN-ED-008 | MAC specN = Exact:1 (1 choice) — saves | Add MAC 1 choice. Set specN = Exact 1. | Click Save. | Saves. specN=exact:1 with 1 choice is valid. | NT | |
| SPECN-ED-009 | MAC specN = Exact:2 (1 choice) — blocked | Add MAC 1 choice. Set specN = Exact 2. | Click Save. | Editor blocks. Exact:2 > 1 available choice. | NT | |
| SPECN-ED-010 | MTM SQ1 specN = Exact:2 (3 SQs × 5 choices) — saves | Add MTM 3 SQs × 5 choices. Set SQ1 specN = Exact:2. | Click Save. | Saves. SQ1 specN=exact:2 persisted. SQ2, SQ3 unaffected. | NT | |
| SPECN-ED-011 | MTM SQ1 specN = Exact:6 > 5 choices — blocked | Add MTM 3 SQs × 5 choices. Set SQ1 specN = Exact:6. | Click Save. | Editor blocks. Exact:6 exceeds 5 available columns. | NT | |
| SPECN-ED-012 | MTM: SQ1=Max:3, SQ2=Max:2, SQ3=none (3×5) — all save | Add MTM 3 SQs × 5 choices. Set SQ1=Max:3, SQ2=Max:2, SQ3=none. | Click Save. | Saves. Per-SQ specN settings persisted independently. | NT | |
| SPECN-ED-013 | MTM SQ1 specN = Exact:2 (3 SQs × 1 choice) — blocked | Add MTM 3 SQs × 1 choice. Set SQ1 specN = Exact:2. | Click Save. | Editor blocks. Exact:2 > 1 available column. | NT | |
| SPECN-ED-014 | MAC: add choice after specN set — re-validates | Add MAC 5 choices. Set specN=Exact:5. Add 6th choice. | Observe editor. | specN=Exact:5 still valid (now below choiceCount). No error. Saves with 6 choices and specN=Exact:5. | NT | |
| SPECN-ED-015 | MAC: remove choice causing specN violation — blocked | Add MAC 5 choices. Set specN=Exact:4. Remove choice 5, then choice 4 (3 remain). | Click Save. | Editor blocks when specN=Exact:4 > 3 remaining choices. Error shown. | NT | |
| SPECN-ED-016 | MAC specN = Max:0 — blocked | Add MAC 5 choices. Set specN = Max 0. | Click Save. | Editor blocks. Max:0 means no choices can be selected; invalid constraint. | NT | |
| SPECN-ED-017 | MTM SQ1: specN=Exact:3 with 2 disabled choices (5 cols, 3 active) — editor accepts | Add MTM 3 SQs × 5 choices. Disable C4 and C5 in SQ1. Set SQ1 specN=Exact:3. Total cols=5 ≥ 3. | Click Save. | Saves. Editor validates against total column count, not active count. Per spec: disabled choices may trigger runtime override. | NT | |

---

## 8. FA / FAL Input Settings — Editor Validation (FA-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| FA-ED-001 | FA type=Text, maxLength=1 — minimum saves | Add FA. Set type=Text, maxLength=1. | Click Save. | Saves. maxLength=1 is valid minimum. | NT | |
| FA-ED-002 | FA type=Text, maxLength=200 — saves | Add FA. Set type=Text, maxLength=200. | Click Save. | Saves. maxLength=200 persisted. | NT | |
| FA-ED-003 | FA type=Text, maxLength=0 — blocked | Add FA. Set type=Text, maxLength=0. | Click Save. | Editor blocks. maxLength must be ≥ 1. | NT | |
| FA-ED-004 | FA type=Number, min=0, max=100 — saves | Add FA. Set type=Number, min=0, max=100. | Click Save. | Saves. min/max persisted. | NT | |
| FA-ED-005 | FA type=Number, min=50, max=10 — blocked | Add FA. Set type=Number, min=50, max=10. | Click Save. | Editor blocks. min must be ≤ max. | NT | |
| FA-ED-006 | FA type=Number, min=max=5 — saves | Add FA. Set type=Number, min=5, max=5. | Click Save. | Saves. Single allowed value (min=max) is valid. | NT | |
| FA-ED-007 | FA type=Date — saves | Add FA. Set type=Date. | Click Save. | Saves. type=Date persisted. | NT | |
| FA-ED-008 | FAL size=5 lines — saves | Add FAL. Set size=5. | Click Save. | Saves. size=5 persisted. | NT | |
| FA-ED-009 | FAL size=1 — boundary saves | Add FAL. Set size=1. | Click Save. | Saves. size=1 is valid minimum. | NT | |
| FA-ED-010 | FAL size=0 — blocked | Add FAL. Set size=0. | Click Save. | Editor blocks. size must be ≥ 1. | NT | |
| FA-ED-011 | FA type switch Text→Number — settings reset | Add FA. Set type=Text, maxLength=50. Switch type to Number. | Observe editor. | Text-specific settings (maxLength) cleared or hidden. Number settings (min/max) appear. Saves with type=Number. | NT | |
| FA-ED-012 | FA type=Number with decimal allowed — saves | Add FA. Set type=Number, allow decimals flag ON, min=0.5, max=9.5. | Click Save. | Saves. Decimal settings persisted. | NT | |

---

## 9. Logic: questionSelect — Editor Configuration (QSEL-ED)

questionSelect shows or hides an entire question based on a preceding question's answer.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| QSEL-ED-001 | questionSelect: show Q2 if Q1=C1 (SAR→SAR, 5 choices) | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set questionSelect: show Q2 if Q1=C1. | Click Save. | Saves. questionSelect condition persisted. | NT | |
| QSEL-ED-002 | questionSelect: operator=any — any of [C1, C2] selected | Add Q1 (MAC, 5 choices). Add Q2 (SAR). Set questionSelect: show Q2 if Q1 any of [C1, C2]. | Click Save. | Saves. operator=any condition stored. | NT | |
| QSEL-ED-003 | questionSelect: operator=notAll — not all of [C1, C2] | Add Q1 (MAC, 5 choices). Add Q2 (SAR). Set questionSelect: show Q2 if Q1 notAll [C1, C2]. | Click Save. | Saves. operator=notAll condition stored. | NT | |
| QSEL-ED-004 | questionSelect: operator=all — all of [C1, C2] selected | Add Q1 (MAC, 5 choices). Add Q2 (SAR). Set questionSelect: show Q2 if Q1 all [C1, C2]. | Click Save. | Saves. operator=all condition stored. | NT | |
| QSEL-ED-005 | questionSelect: source question deleted — condition auto-cleared | Add Q1 (SAR, 5 choices). Add Q2 with questionSelect referencing Q1. Delete Q1. | Observe editor. | questionSelect condition on Q2 is automatically cleared. Q2 displayed unconditionally. No broken state, no orphaned condition. | NT | |
| QSEL-ED-006 | questionSelect: Q2 required=ON, hidden by default — no save block | Add Q1 (SAR, 5 choices). Add Q2 (MAC, required=ON). Set questionSelect: show Q2 only if Q1=C1 (default: Q2 hidden). | Click Save. | Saves. No error for required question hidden by logic. Required bypassed at runtime when Q2 not shown. | NT | |
| QSEL-ED-007 | questionSelect: forward reference (Q2 references Q3) — blocked | Add Q1, Q2, Q3. Add questionSelect on Q2 referencing Q3. | Click Save. | Editor blocks. questionSelect can only reference earlier questions. Error shown. | NT | |
| QSEL-ED-008 | questionSelect: 1-choice source (SAR, 1 choice) — saves | Add Q1 (SAR, 1 choice). Add Q2. Set questionSelect if Q1=C1. | Click Save. | Saves. Condition on single available choice is valid. | NT | |
| QSEL-ED-009 | questionSelect: 5-choice source (MAC), operator=any 3 of 5 | Add Q1 (MAC, 5 choices). Add Q2. Set questionSelect any of [C1,C3,C5]. | Click Save. | Saves. 3-choice any condition persisted. | NT | |
| QSEL-ED-010 | questionSelect: matrix source (MTS, SQ1=C1, 3 SQs × 5 choices) | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2. Set questionSelect: show Q2 if Q1.SQ1=C1. | Click Save. | Saves. Matrix sub-question condition reference stored. | NT | |
| QSEL-ED-011 | questionSelect: AND condition (Q1=C1 AND Q1=C2) — blocked or accepted per type | Add Q1 (SAR, 5 choices). Add Q2. Set questionSelect: show Q2 if Q1=C1 AND Q1=C2. | Click Save. | SAR cannot satisfy both simultaneously. Editor blocks (contradictory for SAR) or shows a warning. | NT | |
| QSEL-ED-012 | questionSelect: AND condition across two sources (Q1=C1 AND Q2=C1) | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Add Q3. Set questionSelect: show Q3 if Q1=C1 AND Q2=C1. | Click Save. | Saves. Multi-source AND condition persisted. | NT | |
| QSEL-ED-013 | questionSelect: condition on last question in survey | Add Q1 (SAR, 5 choices) as last question. Add Q2 after. Set questionSelect: show Q2 if Q1=C1. | Click Save. | Saves. Condition referencing immediately preceding question is valid. | NT | |
| QSEL-ED-014 | questionSelect: cross-page reference (Q on page 1 drives visibility of Q on page 2) | Create 2-page survey. Add Q1 (SAR, 5 choices) on page 1. Add Q2 on page 2. Set questionSelect: show Q2 if Q1=C1. | Click Save. | Saves. Cross-page questionSelect condition persisted. | NT | |
| QSEL-ED-015 | questionSelect: FA source (Q1=FA, respondent typed value drives visibility) | Add Q1 (FA, type=Text). Add Q2 (SAR). Set questionSelect based on Q1 answer text condition. | Click Save. | Saves if FA-based condition is supported. Error shown if FA cannot be a questionSelect source. | NT | |
| QSEL-ED-016 | questionSelect: source question type changed to incompatible type → condition auto-cleared | Add Q1 (MAC, 5 choices). Add Q2 (SAR) with questionSelect: show Q2 if Q1 any[C1,C2]. Change Q1 type from MAC to FA (no choices). | Observe editor after type change. | The questionSelect condition on Q2 is automatically cleared. No broken state. Q2 shown unconditionally. Editor may show inline info message: "Logic referencing Q1 was cleared due to question type change." | NT | |
| QSEL-ED-017 | questionSelect: source question moved after target (forward reference) → condition blocked | Add Q1 (SAR, 5 choices). Add Q2 with questionSelect: show Q2 if Q1=C1 (valid: Q1 before Q2). Move Q1 to a position after Q2 in the survey. | Observe editor after move. | Editor detects invalid forward reference. Condition on Q2 flagged or auto-cleared. Error: "Source question must appear before the target question." | NT | |
| QSEL-ED-018 | questionSelect using snotall() function — saves | Add Q1 (MAC, 5 choices). Add Q2 (SAR). Open condition builder for Q2. Select operator = snotall, source = Q1, choices = [C1, C2]. | Click Save. | Saves. snotall condition (show Q2 when not all of C1, C2 are selected) persisted. | NT | |
| QSEL-ED-019 | questionSelect using count() function (1-arg: total selected count) — saves | Add Q1 (MAC, 5 choices). Add Q2 (SAR). Set questionSelect: show Q2 if count(Q1) >= 3. | Click Save. | Saves. count() 1-argument condition stored. Condition evaluates based on number of choices selected in Q1. | NT | |
| QSEL-ED-020 | questionSelect using count() range condition (>=min AND <=max) — saves | Add Q1 (MAC, 5 choices). Add Q2 (SAR). Set questionSelect: show Q2 if count(Q1) >= 2 AND count(Q1) <= 4. | Click Save. | Saves. count() range condition (two threshold inequalities combined with AND) stored. Show Q2 when exactly 2–4 choices selected in Q1. | NT | |
| QSEL-ED-021 | questionSelect using countif() function — saves | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (SAR). Set questionSelect: show Q2 if countif(Q1, "C1") >= 2 (at least 2 sub-questions selected C1). | Click Save. | Saves. countif() condition stored. | NT | |
| QSEL-ED-022 | questionSelect using num() function on FA source — saves | Add Q1 (FA, type=Number). Add Q2 (SAR). Set questionSelect: show Q2 if num(Q1) >= 10. | Click Save. | Saves. num() condition converts FA text to numeric for comparison. Condition persisted. | NT | |
| QSEL-ED-023 | questionSelect using nvl() function (null / empty-value check) — saves | Add Q1 (SAR, 5 choices). Add Q2 (SAR). Set questionSelect: show Q2 if nvl(Q1) evaluates true (Q1 holds no answer value — either unanswered or non-applicable). | Click Save. | Saves. nvl() null-check condition persisted. nvl() evaluates true whenever Q1's value is null or empty; applies to both choice questions (nothing selected) and FA questions (blank text). | NT | |

> **Note — advanced condition functions apply to all logic types:** The operators tested in QSEL-ED-018–023 (snotall, count, count-range, countif, num, nvl) are valid in choiceSelect and subquestionSelect conditions as well as questionSelect. Cases QSEL-ED-018–023 use questionSelect as a representative vehicle; teams testing choiceSelect or subquestionSelect with these operators should use the same operator descriptions with the appropriate target type.

---

## 10. Logic: choiceSelect — Editor Configuration (CSEL-ED)

choiceSelect shows or hides specific choices on a question based on another question's answer.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| CSEL-ED-001 | choiceSelect: hide Q2.C3 when Q1=C1 (5 choices each) | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set choiceSelect: hide Q2.C3 when Q1=C1. | Click Save. | Saves. choiceSelect hide rule persisted. | NT | |
| CSEL-ED-002 | choiceSelect: show Q2.C3 only when Q1=C1 | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set choiceSelect show mode: Q2.C3 visible only when Q1=C1. | Click Save. | Saves. choiceSelect show rule persisted. | NT | |
| CSEL-ED-003 | choiceSelect: operator=any (MAC source, 5 choices) | Add Q1 (MAC, 5 choices). Add Q2 (SAR, 5 choices). Set choiceSelect: show Q2.C1 if Q1 any of [C1, C2]. | Click Save. | Saves. any operator in choiceSelect stored. | NT | |
| CSEL-ED-004 | choiceSelect: operator=notAll | Add Q1 (MAC, 5 choices). Add Q2 (MAC, 5 choices). Set choiceSelect: show Q2.C3 if Q1 notAll [C1, C2]. | Click Save. | Saves. notAll operator stored. | NT | |
| CSEL-ED-005 | choiceSelect: 1-choice source — saves | Add Q1 (SAR, 1 choice). Add Q2 (SAR, 5 choices). Set choiceSelect: show Q2.C1 if Q1=C1. | Click Save. | Saves. Condition on single source choice is valid. | NT | |
| CSEL-ED-006 | choiceSelect: hide all choices — editor warns | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set choiceSelect: hide all 5 choices of Q2 when Q1=C1. | Click Save. | Saves. Optional warning: "All choices may be hidden when Q1=C1." Not hard-blocked. | NT | |
| CSEL-ED-007 | choiceSelect: source choice deleted — condition auto-cleared | Add Q1 (SAR, 5 choices). Add Q2 with choiceSelect referencing Q1.C3. Delete C3 from Q1. | Observe editor. | choiceSelect condition referencing deleted C3 is automatically cleared. No broken state, no orphaned reference. | NT | |
| CSEL-ED-008 | choiceSelect: matrix source (MTS SQ1=C2, 3 SQs × 5 choices) | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (SAR, 5 choices). Set choiceSelect: hide Q2.C1 when Q1.SQ1=C2. | Click Save. | Saves. choiceSelect with matrix sub-question source persisted. | NT | |
| CSEL-ED-009 | choiceSelect: RNK source — show Q2 choice if RNK item ranked first | Add Q1 (RNK, 5 items). Add Q2 (SAR, 5 choices). Set choiceSelect: show Q2.C1 if Q1 item 1 ranked first. | Click Save. | Saves if RNK choiceSelect source supported. Error shown if not supported. | NT | |
| CSEL-ED-010 | choiceSelect: multiple rules on same target choice | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set two choiceSelect rules both targeting Q2.C3: rule A hides when Q1=C1, rule B hides when Q1=C2. | Click Save. | Saves. Multiple rules on same choice coexist. | NT | |
| CSEL-ED-011 | choiceSelect: MTM cell-level (hide Q2.C1 in SQ1 only, not SQ2) | Add Q1 (SAR, 5 choices). Add Q2 (MTM, 3 SQs × 5 choices). Set choiceSelect: hide Q2.SQ1.C1 when Q1=C1. | Click Save. | Saves. Cell-level choiceSelect on MTM persisted. SQ2 and SQ3 unaffected. | NT | |
| CSEL-ED-012 | choiceSelect: operator=all (MAC source, all of [C1, C2, C3] selected) | Add Q1 (MAC, 5 choices). Add Q2 (SAR, 5 choices). Set choiceSelect: show Q2.C1 if Q1 all of [C1, C2, C3]. | Click Save. | Saves. `all` operator in choiceSelect stored. Condition activates only when all three choices are selected simultaneously. | NT | |
| CSEL-ED-013 | choiceSelect: source question deleted → condition auto-cleared | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices) with choiceSelect: hide Q2.C3 when Q1=C1. Delete Q1. | Observe editor. | choiceSelect condition on Q2 referencing deleted Q1 is automatically cleared. No broken state. All choices of Q2 visible unconditionally. | NT | |
| CSEL-ED-014 | choiceSelect: source question type changed to incompatible type → condition auto-cleared | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices) with choiceSelect: hide Q2.C1 when Q1=C1. Change Q1 type to FA (no choices). | Observe editor after type change. | choiceSelect condition on Q2 automatically cleared. No broken state. Editor may show info: "Logic referencing Q1 was cleared due to type change." | NT | |

---

## 11. Logic: subquestionSelect — Editor Configuration (SQSEL-ED)

subquestionSelect shows or hides specific sub-questions in a matrix based on another question's answer.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| SQSEL-ED-001 | subquestionSelect: hide MTS SQ2 when Q1=C1 (5 choices) | Add Q1 (SAR, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices). Set subquestionSelect: hide Q2.SQ2 when Q1=C1. | Click Save. | Saves. subquestionSelect condition on SQ2 persisted. | NT | |
| SQSEL-ED-002 | subquestionSelect: show MTM SQ3 only when Q1=C3 | Add Q1 (SAR, 5 choices). Add Q2 (MTM, 3 SQs × 5 choices). Set subquestionSelect: show Q2.SQ3 only when Q1=C3. | Click Save. | Saves. Show-mode subquestionSelect persisted. | NT | |
| SQSEL-ED-003 | subquestionSelect: operator=any (MAC source, 5 choices) | Add Q1 (MAC, 5 choices). Add Q2 (MTS, 3 SQs). Set subquestionSelect: show SQ1 if Q1 any of [C1, C2]. | Click Save. | Saves. any operator persisted. | NT | |
| SQSEL-ED-004 | subquestionSelect: source SQ deleted — condition auto-cleared | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (MTS, 3 SQs). Set subquestionSelect using Q1.SQ2. Delete Q1.SQ2. | Observe editor. | subquestionSelect condition referencing deleted Q1.SQ2 is automatically cleared. No broken state, no orphaned reference. | NT | |
| SQSEL-ED-005 | subquestionSelect: all SQs hidden — editor warns | Add Q1 (SAR, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices). Configure subquestionSelect hiding all 3 SQs when Q1=C1. | Click Save. | Saves. Optional warning: all sub-questions may be hidden. | NT | |
| SQSEL-ED-006 | subquestionSelect: 1-choice source condition | Add Q1 (SAR, 1 choice). Add Q2 (MTS, 3 SQs × 3 choices). Set subquestionSelect: hide SQ1 when Q1=C1. | Click Save. | Saves. Condition on 1-choice source valid. | NT | |
| SQSEL-ED-007 | subquestionSelect: MTT target — hide SQ2 | Add Q1 (SAR, 5 choices). Add Q2 (MTT, 3 SQs × 5 choices). Set subquestionSelect: hide Q2.SQ2 when Q1=C1. | Click Save. | Saves. subquestionSelect on MTT target persisted. | NT | |
| SQSEL-ED-008 | subquestionSelect: operator=notAll | Add Q1 (MAC, 5 choices). Add Q2 (MTS, 3 SQs). Set subquestionSelect: show SQ1 if Q1 notAll [C1, C2]. | Click Save. | Saves. notAll operator on subquestionSelect persisted. | NT | |
| SQSEL-ED-009 | subquestionSelect: AND condition (SQ visible only if Q1=C1 AND Q2=C2) | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Add Q3 (MTS, 3 SQs). Set subquestionSelect: show Q3.SQ1 if Q1=C1 AND Q2=C2. | Click Save. | Saves. Multi-source AND condition on subquestionSelect persisted. | NT | |
| SQSEL-ED-010 | subquestionSelect: operator=all (MAC source, all of [C1, C2] selected) | Add Q1 (MAC, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices). Set subquestionSelect: show Q2.SQ1 if Q1 all of [C1, C2]. | Click Save. | Saves. `all` operator in subquestionSelect stored. Condition activates only when both C1 and C2 are selected in Q1. | NT | |
| SQSEL-ED-011 | subquestionSelect: source question deleted → condition auto-cleared | Add Q1 (SAR, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices) with subquestionSelect: hide Q2.SQ1 when Q1=C1. Delete Q1. | Observe editor. | subquestionSelect condition on Q2 referencing deleted Q1 is automatically cleared. No broken state. All SQs of Q2 visible unconditionally. | NT | |
| SQSEL-ED-012 | subquestionSelect: source question type changed to incompatible type → condition auto-cleared | Add Q1 (SAR, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices) with subquestionSelect: hide SQ1 when Q1=C1. Change Q1 type to Note (no choices). | Observe editor after type change. | subquestionSelect condition on Q2 automatically cleared. No broken state. | NT | |

---

## 12. Logic: matrixInclusion — Editor Configuration (MINC-ED)

matrixInclusion dynamically includes sub-questions in MTM based on a source matrix's answers.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| MINC-ED-001 | matrixInclusion: Q2 includes SQs from Q1 (3 SQs × 5 choices each) | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (MTM, 3 SQs × 5 choices). Configure matrixInclusion on Q2 from Q1. | Click Save. | Saves. matrixInclusion rule persisted. | NT | |
| MINC-ED-002 | matrixInclusion: source is non-matrix — blocked | Add Q1 (SAR, 5 choices). Add Q2 (MTM, 3 SQs). Attempt matrixInclusion from Q1. | Click Save. | Editor blocks. matrixInclusion source must be a matrix type. | NT | |
| MINC-ED-003 | matrixInclusion: source question deleted — condition auto-cleared | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (MTM, 3 SQs × 5 choices) with matrixInclusion from Q1. Delete Q1. | Observe editor. | matrixInclusion condition on Q2 automatically cleared. Q2 displayed with all SQs unconditionally. No crash, no broken state. | NT | |
| MINC-ED-004 | matrixInclusion: source and target SQ counts differ | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (MTM, 5 SQs × 5 choices). Configure matrixInclusion. | Click Save. | Saves. Editor handles SQ count mismatch gracefully. | NT | |
| MINC-ED-005 | matrixInclusion: 0 SQs included (all filtered out) — editor warns | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (MTM, 3 SQs). Configure matrixInclusion with inclusion condition that matches 0 SQs at design time. | Click Save. | Editor shows warning: matrixInclusion may result in 0 visible SQs. Does not hard-block save. | NT | |
| MINC-ED-006 | matrixInclusion: MTM as source | Add Q1 (MTM, 3 SQs × 5 choices). Add Q2 (MTM, 3 SQs × 5 choices). Configure matrixInclusion on Q2 from Q1. | Click Save. | Saves. MTM source for matrixInclusion accepted. | NT | |
| MINC-ED-007 | matrixInclusion: partial SQ inclusion (include only SQ2 from 3-SQ source) | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (MTM, 3 SQs × 5 choices). Configure matrixInclusion to include only Q1.SQ2. | Click Save. | Saves. Partial inclusion rule persisted. At runtime, only SQ matching Q1.SQ2 will appear in Q2. | NT | |
| MINC-ED-008 | matrixInclusion: MTT as source | Add Q1 (MTT, 3 SQs × 5 choices). Add Q2 (MTM, 3 SQs × 5 choices). Configure matrixInclusion on Q2 from Q1 (MTT source). | Click Save. | Saves if MTT is a valid matrixInclusion source. Error shown if MTT is blocked as source (only MTS and MTM supported). Expected behavior to be confirmed against spec. | NT | |

---

## 13. Logic: countMatrix — Editor Config Validation (CM-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| CM-ED-001 | Compound condition: lower bound > upper bound — blocked | Add Q1 (MTS, 3 SQs × 5 choices). Configure countif >= 3 AND <= 2. | Confirm condition. | Editor rejects. Error: "Please set a value within the valid range." Condition not saved. | NT | |
| CM-ED-002 | Compound condition: equality outside range — blocked | Add Q1 (MTS). Configure countif == 5 AND <= 3. | Confirm condition. | Editor rejects. No value satisfies both. | NT | |
| CM-ED-003 | Redundant constraint — blocked or warned | Add Q1 (MTS). Configure countif == 3 AND <= 4. | Confirm condition. | Editor blocks or warns: <=4 adds no restriction when ==3 already holds. Exact behavior (hard-block vs. warning) to be confirmed against spec. | NT | |
| CM-ED-004 | Negative threshold — blocked | Add Q1 (MTS). Configure countif >= -1. | Confirm condition. | Editor rejects. Negative threshold invalid. | NT | |
| CM-ED-005 | Threshold > max possible count (MTS, 3 SQs × 1 choice): countif >= 4 — blocked | Add Q1 (MTS, 3 SQs × 1 choice). Configure countif >= 4. Max possible = 3 × 1 = 3. | Confirm condition. | Editor rejects. Threshold 4 exceeds achievable max of 3. | NT | |
| CM-ED-006 | Threshold = max possible count (MTS, 3 SQs × 5 choices): countif >= 3 — accepted | Add Q1 (MTS, 3 SQs × 5 choices). Configure countif >= 3. | Confirm condition. | Editor accepts. Threshold 3 equals max achievable (1/SQ × 3 SQs). | NT | |
| CM-ED-007 | Threshold > max possible (MTS, 3 SQs × 5 choices): countif >= 4 — blocked | Add Q1 (MTS, 3 SQs × 5 choices). Configure countif >= 4. Max for MTS = 1/SQ = 3. | Confirm condition. | Editor rejects. Threshold 4 exceeds max of 3. | NT | |
| CM-ED-008 | specN reduced below CM threshold — blocked | Add Q1 (MTM, 3 SQs × 5 choices). Configure countif >= 6. Reduce specN=Max:1. | Apply specN change and save. | Editor blocks. New ceiling (3 × 1 = 3) < threshold 6. Error shown. | NT | |
| CM-ED-009 | Switch to Radio on SQ reduces ceiling below CM threshold | Add Q1 (MTM, 3 SQs × 5 choices). Configure countif >= 6. Enable Switch to Radio on SQ1. | Apply and save. | Editor shows error if new ceiling < threshold 6. CM condition must be reconciled. | NT | |
| CM-ED-010 | Source question deleted — countMatrix condition auto-cleared | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (SAR). Configure countMatrix on Q1 (>=2) as condition for showing Q2. Delete Q1. | Observe editor. | countMatrix condition on Q2 automatically cleared. Q2 shown unconditionally. No crash, no broken state. | NT | |
| CM-ED-011 | countMatrix with MTM source (3 SQs × 5 choices) — accepted | Add Q1 (MTM, 3 SQs × 5 choices). Configure countif >= 2. | Confirm condition. | Editor accepts. MTM valid as countMatrix source. | NT | |
| CM-ED-012 | countMatrix operator == 0 — valid | Add Q1 (MTS, 3 SQs × 5 choices). Configure countif == 0. | Confirm condition. | Editor accepts. Zero threshold is valid. | NT | |
| CM-ED-013 | countMatrix: partial SQ range — count only specific SQs | Add Q1 (MTS, 3 SQs × 5 choices). Configure countif on SQ1 and SQ2 only (not SQ3) >= 2. | Confirm condition. | Saves if partial-SQ range is supported. Error shown if all SQs must be included. | NT | |
| CM-ED-014 | countMatrix: partial choice range — count only specific choices | Add Q1 (MTM, 3 SQs × 5 choices). Configure countif counting only C1 and C3 selections >= 3. | Confirm condition. | Saves if partial-choice range is supported. Error shown if not supported. | NT | |
| CM-ED-015 | countMatrix: valid compound >=2 AND <=4 | Add Q1 (MTM, 3 SQs × 5 choices). Configure countif >= 2 AND <= 4. | Confirm condition. | Editor accepts. Range 2–4 is satisfiable within max of 15 (3 SQs × 5). | NT | |
| CM-ED-016 | countMatrix operator != (not equal) | Add Q1 (MTS, 3 SQs × 5 choices). Configure countif != 2. | Confirm condition. | Editor accepts if != operator supported. Error shown if not. | NT | |
| CM-ED-017 | countMatrix operator <= (less-than-or-equal) | Add Q1 (MTS, 3 SQs × 5 choices). Configure countif <= 2. | Confirm condition. | Editor accepts if <= operator supported. Condition saved. | NT | |
| CM-ED-018 | countMatrix: full range (>=0 AND <=max) — editor warns redundant | Add Q1 (MTM, 3 SQs × 5 choices). Configure countif >= 0 AND <= 15. Max = 15. | Confirm condition. | Editor warns: condition always true (covers full range). Saves if no hard-block. | NT | |
| CM-ED-019 | countMatrix with MTT source (3 SQs × 5 choices) — accepted | Add Q1 (MTT, 3 SQs × 5 choices). Configure countif >= 2. | Confirm condition. | Editor accepts if MTT is valid as countMatrix source. Per behavior: MTT rows are single-answer like MTS, max count = 3. Blocked if MTT not supported as source. | NT | |
| CM-ED-020 | countMatrix: source question type changed from matrix to non-matrix → condition auto-cleared | Add Q1 (MTS, 3 SQs × 5 choices). Configure countMatrix(Q1)>=2 as condition for Q2 (SAR). Change Q1 type from MTS to SAR. | Observe editor. | countMatrix condition on Q2 automatically cleared. No broken state. countMatrix source must be a matrix type; changing Q1 to SAR invalidates the condition. | NT | |

---

## 14. Logic: screeningOut — Editor Configuration (SCR-ED)

screeningOut routes the respondent out of the survey when a marked choice is selected.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| SCR-ED-001 | screeningOut on SAR choice (5 choices) — saves | Add Q1 (SAR, 5 choices). Mark choice 5 as screen-out. | Click Save. | Saves. screeningOut flag on choice 5 persisted. | NT | |
| SCR-ED-002 | screeningOut on SAR 1 choice — saves | Add Q1 (SAR, 1 choice). Mark the single choice as screen-out. | Click Save. | Saves. screeningOut on only choice is valid. | NT | |
| SCR-ED-003 | screeningOut on MAC choice (5 choices) — saves | Add Q1 (MAC, 5 choices). Mark choice 3 as screen-out. | Click Save. | Saves. screeningOut on MAC choice 3 persisted. | NT | |
| SCR-ED-004 | screeningOut on SAP choice (5 choices) — saves | Add Q1 (SAP, 5 choices). Mark choice 2 as screen-out. | Click Save. | Saves. screeningOut on SAP choice persisted. | NT | |
| SCR-ED-005 | screeningOut on multiple choices — saves | Add Q1 (SAR, 5 choices). Mark choices 4 and 5 as screen-out. | Click Save. | Saves. Multiple screen-out choices persisted. | NT | |
| SCR-ED-006 | screeningOut on matrix cell (MTS, 3 SQs × 5 choices, SQ1 × C5) | Add Q1 (MTS, 3 SQs × 5 choices). Mark SQ1 × C5 as screen-out. | Click Save. | Saves. screeningOut on specific matrix cell persisted. | NT | |
| SCR-ED-007 | screeningOut on first question — saves | Create survey. Add Q1 (SAR, 5 choices). Mark choice 1 screen-out. Add Q2. | Click Save. | Saves. Screen-out on first question is valid. | NT | |
| SCR-ED-008 | screeningOut: source choice deleted — condition removed | Add Q1 (SAR, 5 choices). Mark C3 screen-out. Delete C3. | Observe editor. | screeningOut on deleted C3 removed. No broken state. | NT | |
| SCR-ED-009 | screeningOut on RNK item — saves | Add Q1 (RNK, 5 items). Mark item 3 as screen-out. | Click Save. | Saves if screeningOut on RNK items is supported. Error or disabled if not. | NT | |
| SCR-ED-010 | screeningOut: all choices screened — editor warns | Add Q1 (SAR, 5 choices). Mark all 5 choices as screen-out. | Click Save. | Editor shows warning: all choices route to screen-out, question always terminates. Does not hard-block save. | NT | |
| SCR-ED-011 | screeningOut on MTM cell (3 SQs × 5 choices, SQ2 × C3) | Add Q1 (MTM, 3 SQs × 5 choices). Mark SQ2 × C3 as screen-out. | Click Save. | Saves. screeningOut on MTM cell persisted. | NT | |
| SCR-ED-012 | screeningOut: question type changed to type without choices → screen-out auto-cleared | Add Q1 (SAR, 5 choices). Mark choice 3 as screen-out. Change Q1 type from SAR to FA (no choices). | Observe editor after type change. | All screeningOut settings on Q1 automatically cleared. No broken state. Editor may show info message about clearing. | NT | |

---

## 15. Logic: Prohibition and Exclusive — Editor Configuration (PRX-ED)

> **Numbering note:** IDs in this section are non-sequential by design. Prohibition sub-section uses PRX-ED-001–005 and PRX-ED-011–013; Exclusive sub-section uses PRX-ED-006–010 and PRX-ED-014–018. The interleaved numbering is an artifact of how cases were added across review passes; no IDs have been renumbered to preserve cross-reference stability.

### Prohibition (cross-SQ constraint in matrix)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| PRX-ED-001 | MTS prohibition: SQ1 C1 → SQ2 cannot select C1 (3 SQs × 5 choices) | Add MTS Q1 (3 SQs × 5 choices). Add prohibition: SQ1=C1 → SQ2 cannot select C1. | Click Save. | Saves. Prohibition rule persisted. | NT | |
| PRX-ED-002 | MTM prohibition: SQ1 C1 → SQ2 cannot select C1 (3 SQs × 5 choices) | Add MTM Q1 (3 SQs × 5 choices). Add prohibition rule. | Click Save. | Saves. MTM prohibition rule persisted. | NT | |
| PRX-ED-003 | Prohibition on 1-choice matrix (MTS, 3 SQs × 1 choice) | Add MTS Q1 (3 SQs × 1 choice). Add prohibition: SQ1=C1 → SQ2 cannot select C1. | Click Save. | Saves. Prohibition valid on 1-choice matrix. | NT | |
| PRX-ED-004 | Prohibition: referenced SQ removed — rule cleaned up | Add MTS Q1 (3 SQs × 5 choices). Add prohibition on SQ2. Delete SQ2. | Observe editor. | Prohibition referencing SQ2 removed. No broken state. | NT | |
| PRX-ED-005 | Prohibition circular reference — blocked | Add MTS Q1 (3 SQs × 5 choices). Attempt: SQ1→SQ2 prohibited AND SQ2→SQ1 prohibited on same choice. | Click Save. | Editor blocks circular prohibition. Error shown. | NT | |
| PRX-ED-011 | MTS prohibition: non-adjacent SQs (SQ1 → SQ3, skip SQ2) | Add MTS Q1 (3 SQs × 5 choices). Add prohibition: SQ1=C1 → SQ3 cannot select C1. | Click Save. | Saves. Non-adjacent SQ prohibition persisted. | NT | |
| PRX-ED-012 | MTT prohibition: SQ1 → SQ2 | Add MTT Q1 (3 SQs × 5 choices). Add prohibition: SQ1=C1 → SQ2 cannot select C1. | Click Save. | Saves if MTT supports prohibition. Error shown if not supported. | NT | |
| PRX-ED-013 | Prohibition: column-level scope (forbid choice column across all SQs) | Add MTM Q1 (3 SQs × 5 choices). Add column-level prohibition: if any SQ selects C5, no other SQ can select C5. | Click Save. | Saves if column-level prohibition is supported. Editor persists the rule. | NT | |

### Exclusive

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| PRX-ED-006 | MAC exclusive choice (5 choices) — saves | Add MAC 5 choices. Mark choice 5 as Exclusive. | Click Save. | Saves. Exclusive flag on choice 5 persisted. | NT | |
| PRX-ED-007 | MAC exclusive choice (1 choice) — saves | Add MAC 1 choice. Mark as Exclusive. | Click Save. | Saves. Exclusive on single choice is valid. | NT | |
| PRX-ED-008 | MTM exclusive per-SQ — SQ1.C5 (3 SQs × 5 choices) | Add MTM 3 SQs × 5 choices. Mark C5 in SQ1 as Exclusive. | Click Save. | Saves. Exclusive flag on SQ1.C5 persisted. SQ2, SQ3 unaffected. | NT | |
| PRX-ED-009 | RNK exclusive item (5 items) — saves | Add RNK 5 items. Mark item 5 as Exclusive. | Click Save. | Saves. Exclusive flag on ranking item 5 persisted. | NT | |
| PRX-ED-010 | MAC multiple exclusive choices — blocked or warned | Add MAC 5 choices. Mark both choice 4 and choice 5 as Exclusive. | Click Save. | Editor blocks or warns. Only one exclusive choice allowed per question. | NT | |
| PRX-ED-014 | MAC exclusive on first choice — saves | Add MAC 5 choices. Mark choice 1 as Exclusive. | Click Save. | Saves. Exclusive on first choice is valid. | NT | |
| PRX-ED-015 | SAP exclusive choice — editor disables or blocks | Add SAP 5 choices. Attempt to mark a choice as Exclusive. | Observe editor. | Exclusive flag unavailable or blocked on SAP (dropdown/scale). Error or control absent. | NT | |
| PRX-ED-016 | MTM prohibition: same-SQ (SQ1.C1 → SQ1 cannot also select C2) | Add MTM 3 SQs × 5 choices. Add prohibition: SQ1=C1 → SQ1 cannot select C2 (within same row). | Click Save. | Saves. Same-row prohibition is valid for MTM (checkbox rows can hold multiple selections; the rule prevents C1 and C2 from being co-selected in SQ1). Note: for MTS (radio rows), this would be a no-op since radio inherently prevents selecting two choices. | NT | |
| PRX-ED-017 | Prohibition: question type changed from matrix to non-matrix → rules auto-cleared | Add MTM 3 SQs × 5 choices (Q1). Add prohibition: SQ1=C1 → SQ2 cannot select C1. Change Q1 type from MTM to SAR. | Observe editor after type change. | All prohibition rules on Q1 automatically cleared. No broken state. Editor may show info: "Prohibition settings cleared due to question type change." | NT | |
| PRX-ED-018 | Exclusive: question type changed to non-MAC → exclusive flag auto-cleared | Add MAC 5 choices (Q1). Mark choice 5 as Exclusive. Change Q1 type from MAC to SAR. | Observe editor after type change. | Exclusive flag on Q1's choice is automatically cleared (SAR has no exclusive concept). No broken state. | NT | |

---

## 16. Logic: Page Break — Editor Configuration (PB-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| PB-ED-001 | pbBefore on Q2 — saves | Add Q1, Q2, Q3 to page 1. Set pbBefore=true on Q2. | Click Save. | Saves. pbBefore persisted on Q2. | NT | |
| PB-ED-002 | pbAfter on Q1 — saves | Add Q1, Q2. Set pbAfter=true on Q1. | Click Save. | Saves. pbAfter on Q1 persisted. | NT | |
| PB-ED-003 | pbBefore on first question — saves | Add Q1–Q3. Set pbBefore on Q1. | Click Save. | Saves. pbBefore on first question valid (no-op at runtime or first page). | NT | |
| PB-ED-004 | Page break removed — saves updated state | Add Q1, Q2 with pbBefore on Q2. Remove pbBefore from Q2. | Click Save. | Saves. No page break persisted. Single-page behavior restored. | NT | |
| PB-ED-005 | Multiple page breaks — saves | Add Q1–Q5. Set pbBefore on Q2 and Q4. | Click Save. | Saves. Two page breaks persisted. Survey has 3 logical pages. | NT | |
| PB-ED-006 | Page break + required=ON on same question — saves | Add Q1 (SAR, 5 choices). Add Q2 (SAR, required=ON, pbBefore=true). | Click Save. | Saves. Required + page break combination is valid. | NT | |
| PB-ED-007 | Page break on matrix question (pbBefore on MTS) — saves | Add Q1 (SAR, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices) with pbBefore=true. | Click Save. | Saves. Matrix question with page break persisted. | NT | |
| PB-ED-008 | screeningOut question followed by page break — saves | Add Q1 (SAR, 5 choices) with choice 5 marked screen-out. Set pbBefore=true on Q2 immediately after. | Click Save. | Saves. screeningOut + page break coexist without error. | NT | |

---

## 17. Logic Combinations — Editor Validation (COMB-ED)

Tests that multiple logic settings coexist and save correctly.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| COMB-ED-001 | questionSelect + choiceSelect on same downstream question — saves | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set questionSelect: show Q2 if Q1=C1; set choiceSelect: hide Q2.C3 if Q1=C2. | Click Save. | Saves. Both rules coexist on Q2. | NT | |
| COMB-ED-002 | Required + randomization (SAR, 5 choices) — saves | Add SAR 5 choices. Set Required=ON. Set rand=random. | Click Save. | Saves. Both settings persisted. | NT | |
| COMB-ED-003 | Required + specN (MAC, 5 choices) — saves | Add MAC 5 choices. Set Required=ON. Set specN=Exact:3. | Click Save. | Saves. Required + specN coexist. | NT | |
| COMB-ED-004 | screeningOut + questionSelect on next question — saves | Add Q1 (SAR, 5 choices). Mark Q1.C5 screen-out. Add Q2 with questionSelect referencing Q1. | Click Save. | Saves. screeningOut and questionSelect coexist. | NT | |
| COMB-ED-005 | MTM: specN + prohibition + required — saves (3 SQs × 5 choices) | Add MTM 3 SQs × 5 choices. Set SQ1 specN=Exact:2. Add prohibition SQ1→SQ2. Set Required=Custom (SQ1, SQ2). | Click Save. | Saves. Three settings coexist. | NT | |
| COMB-ED-006 | MTS: subquestionSelect + prohibition — saves | Add Q1 (SAR, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices). Set subquestionSelect: hide Q2.SQ3 if Q1=C1. Add prohibition on Q2 (SQ1→SQ2). | Click Save. | Saves. Both rules on Q2 coexist. | NT | |
| COMB-ED-007 | countMatrix + questionSelect (count condition drives Q2 visibility) | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (SAR). Set questionSelect on Q2: show if countMatrix(Q1) >= 2. | Click Save. | Saves. countMatrix as questionSelect condition persisted. | NT | |
| COMB-ED-008 | rand + choiceSelect — saves | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices) with rand=random and choiceSelect (hide C3 if Q1=C1). | Click Save. | Saves. rand + choiceSelect coexist. | NT | |
| COMB-ED-009 | screeningOut + rand (SAR, 5 choices) — saves | Add Q1 (SAR, 5 choices). Set rand=random. Mark C5 screen-out. | Click Save. | Saves. Screen-out on randomized choice is valid. | NT | |
| COMB-ED-010 | Required=All + matrixInclusion (MTM, 3 SQs × 5 choices) — saves | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (MTM, 3 SQs × 5 choices). Set Required=All on Q2. Configure matrixInclusion from Q1. | Click Save. | Saves. Required=All + matrixInclusion coexist. | NT | |
| COMB-ED-011 | pageBreak + questionSelect on same question — saves | Add Q1 (SAR). Add Q2 with pbBefore=true and questionSelect condition. | Click Save. | Saves. Page break + questionSelect coexist on Q2. | NT | |
| COMB-ED-012 | MTM: Switch to Radio + specN=Exact:2 on same SQ — blocked | Add MTM 3 SQs × 5 choices. Enable Switch to Radio on SQ1. Set SQ1 specN=Exact:2. | Click Save. | Editor blocks. Switch to Radio limits SQ1 to 1 selection; specN=Exact:2 is impossible. | NT | |
| COMB-ED-013 | MAC: exclusive + specN — editor accepts (exclusive overrides specN per spec) | Add MAC 5 choices. Mark choice 5 exclusive. Set specN=Exact:2. | Click Save. | Saves. Per spec: exclusive overrides specN. No conflict at editor level. | NT | |
| COMB-ED-014 | questionSelect any operator + screeningOut on source | Add Q1 (MAC, 5 choices). Mark Q1.C5 screen-out. Add Q2. Set questionSelect: show Q2 if Q1 any of [C1, C3]. | Click Save. | Saves. any operator + screen-out on source coexist. | NT | |
| COMB-ED-015 | MTM: rand=random + prohibition + Required=All (3 SQs × 5 choices) | Add MTM 3 SQs × 5 choices. Set rand=random on cols. Add prohibition SQ1→SQ2. Set Required=All. | Click Save. | Saves. Three settings coexist. | NT | |
| COMB-ED-016 | Required=Custom (SQ1) + subquestionSelect hiding SQ1 — saves with warning | Add Q1 (SAR, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices). Set Required=Custom, mark SQ1. Set subquestionSelect: hide Q2.SQ1 when Q1=C1. | Click Save. | Saves. Optional warning: required SQ may be hidden. At runtime required check bypassed for hidden SQ. | NT | |
| COMB-ED-017 | choiceSelect + screeningOut on same target choice — saves | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set choiceSelect: show Q2.C3 only when Q1=C1. Also mark Q2.C3 as screen-out. | Click Save. | Saves. choiceSelect visibility + screeningOut on same choice coexist. | NT | |
| COMB-ED-018 | matrixInclusion + subquestionSelect on same target matrix — saves | Add Q1 (MTS, 3 SQs × 5 choices). Add Q2 (SAR, 5 choices). Add Q3 (MTM, 3 SQs). Set matrixInclusion on Q3 from Q1. Also set subquestionSelect: hide Q3.SQ2 when Q2=C1. | Click Save. | Saves. matrixInclusion and subquestionSelect coexist on Q3. | NT | |
| COMB-ED-019 | rand=random + questionSelect — saves | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Set rand=random on Q2. Also set questionSelect: show Q2 if Q1=C1. | Click Save. | Saves. rand=random + questionSelect coexist. | NT | |
| COMB-ED-020 | 4-way combination: Required + rand + specN + choiceSelect — saves | Add Q1 (SAR, 5 choices). Add Q2 (MAC, 5 choices). Set Required=ON on Q2. Set rand=random on Q2 choices. Set specN=Max:3 on Q2. Add choiceSelect on Q2: hide Q2.C5 when Q1=C1. | Click Save. | Saves. All four settings (Required, rand, specN, choiceSelect) coexist on Q2 without conflict. | NT | |
| COMB-ED-021 | Question-rand section + choiceSelect on question within section — saves | Create block with Section 1 (Q1, SAR 5 choices) and Section 2 (Q2, SAR 5 choices). Set choiceSelect on Q1: hide C3 when a question outside the block = C1. | Click Save. | Saves. Question-level randomization and choice-level logic on a sectioned question coexist. | NT | |
| COMB-ED-022 | Prohibition + Inclusion check on same MTM question — saves | Add MTM Q1 (3 SQs × 5 choices). Add prohibition: SQ1=C1 → SQ2 cannot select C1. Add inclusion: SQ1 must include at least 1 choice from SQ3. | Click Save. | Saves. Prohibition and inclusion rules coexist on Q1 without conflict. | NT | |
| COMB-ED-023 | Two prohibition rules on same MTM question — saves | Add MTM Q1 (3 SQs × 5 choices). Add prohibition rule A: SQ1=C1 → SQ2 cannot select C1. Add prohibition rule B: SQ2=C2 → SQ3 cannot select C2. | Click Save. | Saves. Both prohibition rules persisted on Q1. | NT | |
| COMB-ED-024 | Exclusive + Prohibition on same MTM question — saves | Add MTM Q1 (3 SQs × 5 choices). Mark SQ1.C5 as Exclusive. Add prohibition: SQ1=C1 → SQ2 cannot select C1. | Click Save. | Saves. Exclusive flag and prohibition rule coexist on Q1. | NT | |
| COMB-ED-025 | Exclusive + Inclusion check on same MTM question — saves | Add MTM Q1 (3 SQs × 5 choices). Mark SQ1.C5 as Exclusive. Add inclusion: SQ2 must include at least 1 choice from SQ3. | Click Save. | Saves. Exclusive flag and inclusion check coexist on Q1. | NT | |
| COMB-ED-026 | AR piping chain where piping target also has fieldSelect condition — saves | Add Q1 (MAC, 5 choices). Add Q2 (FAS, 5 input fields) with AR piping from Q1 (all choices). Set fieldSelect on Q2: input field 2 visible only if Q1 selected C2. | Click Save. | Saves. AR piping and fieldSelect coexist on Q2. | NT | |
| COMB-ED-027 | matrixInclusion + questionSelect on same target matrix — saves | Add Q1 (SAR, 5 choices). Add Q2 (MTS, 3 SQs × 5 choices). Add Q3 (MTM, 3 SQs × 5 choices). Set matrixInclusion on Q3 from Q2. Set questionSelect: show Q3 only if Q1=C1. | Click Save. | Saves. matrixInclusion and questionSelect coexist on Q3. | NT | |
| COMB-ED-028 | Insert question before source — all logic references auto-update to new QIDs | Add Q1 (SAR, 5 choices), Q2 (SAR) with questionSelect referencing Q1. Insert a new question at the very beginning (becomes new Q1; original Q1 → Q2, original Q2 → Q3). | Observe editor after insertion. Save. | Logic reference on original Q2 (now Q3) automatically updates to point to original Q1 (now Q2). Survey saves without orphaned references. No manual re-linking required. | NT | |
| COMB-ED-029 | Choice randomization settings preserved after question add and move | Add Q1 (SAR, 5 choices, rand=random, choice 5 fixed). Add Q2 (SAR). Insert new question before Q1 (Q1 shifts to Q2 position). Then move original Q1 to the end. | Click Save. Reopen. | rand=random and fixed-choice-5 flag are preserved on the original SAR question regardless of its new QID or position in survey. | NT | |
| COMB-ED-030 | Delete source question with multiple dependent logic types — all cleared | Add Q1 (SAR, 5 choices). Add Q2 with questionSelect referencing Q1. Add Q3 (MTM) with subquestionSelect referencing Q1. Add Q4 (SAR) with choiceSelect referencing Q1. Delete Q1. | Click Save. | All three logic rules (questionSelect on Q2, subquestionSelect on Q3, choiceSelect on Q4) are automatically cleared. No orphaned references remain. Survey saves cleanly. | NT | |

---

## 18. Save Validation — General (SAV-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| SAV-ED-001 | All questions valid — save succeeds | Survey with Q1 (SAR, 5 choices), Q2 (MAC, 5 choices), Q3 (MTS, 3 SQs × 5 choices). All fields filled. | Click Save. | All questions saved. Survey persisted. No errors. | NT | |
| SAV-ED-002 | One invalid question blocks entire save | Survey with Q1 (SAR, valid) and Q2 (SAR, empty question text). | Click Save. | Editor blocks. Error on Q2. Neither question saved until Q2 is fixed. | NT | |
| SAV-ED-003 | Question order persists after save | Add Q1, Q2, Q3. Reorder to Q2, Q3, Q1. | Click Save. Reopen. | Survey reopens with order Q2, Q3, Q1. | NT | |
| SAV-ED-004 | Unsaved changes indicator shown | Save survey. Add a choice. | Observe UI. | "Unsaved changes" indicator visible. Indicator clears after Save. | NT | |
| SAV-ED-005 | Navigate away with unsaved changes — confirmation prompt | Make a change without saving. | Click browser back / navigate away. | Editor shows "Unsaved changes — leave?" dialog. Survey not lost. | NT | |
| SAV-ED-006 | Remove logic condition — not persisted | Add Q1, Q2 with questionSelect on Q2. Remove the questionSelect. | Click Save. | Saves. No logic on Q2 in DB. Q2 shown unconditionally. | NT | |
| SAV-ED-007 | Save with all QTs present — validates all | Survey with one of each QT (SAR, MAC, SAP, FA, FAL, RNK, RAT, MTS, MTM, MTT, Note), all valid. | Click Save. | All QTs saved. No per-QT error. | NT | |
| SAV-ED-008 | Multiple rapid saves — no duplication | Click Save multiple times in quick succession. | Check DB. | Survey saved once. No duplicate entries. No data corruption. | NT | |
| SAV-ED-009 | Survey with special characters in title — saves | Create survey. Enter title with special chars: "Test & Survey <v2>: Q&A". | Click Save. | Survey saves. Special characters stored and displayed correctly. | NT | |
| SAV-ED-010 | Very long question text — saves | Add SAR. Enter question text at maximum allowed length (e.g., 500 characters). | Click Save. | Survey saves. Long text persisted without truncation. | NT | |
| SAV-ED-011 | Network error mid-save — graceful failure | Save survey. Simulate network disconnection during save. | Click Save. | Error shown: "Save failed — check network connection." Survey not partially saved. On reconnect, retry works. | NT | |
| SAV-ED-012 | Survey title at exact maximum length — saves | Enter survey title of exactly N characters (system max, e.g., 255). | Click Save. | Saves. Max-length title persisted. | NT | |
| SAV-ED-013 | Survey question count limit — large matrix causes overflow count | Create survey. Add MTS with 30 SQs × 30 choices. Check editor's question count indicator. | Observe editor. | Editor displays a calculated "effective question count" exceeding the raw question count (per spec: large matrix questions contribute additional count based on SQ/choice dimensions). If limit is exceeded, editor blocks save with error. | NT | |
| SAV-ED-014 | Delete question with active logic on it — logic referencing it cleared before save | Add Q1 (SAR, 5 choices). Add Q2 (SAR) with questionSelect referencing Q1. Add Q3 with choiceSelect referencing Q2. Delete Q2. | Click Save. | Survey saves. Logic on Q3 that referenced Q2 is auto-cleared (no dangling reference). Survey saved without Q2. | NT | |

---

## 19. Publish Validation (PUB-ED)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| PUB-ED-001 | Publish valid survey — succeeds | Create and save survey with at least one valid question. | Click Publish. | Survey status → Published. No errors. | NT | |
| PUB-ED-002 | Publish empty survey — blocked | Create and save survey with no questions. | Click Publish. | Editor blocks. Error: "Survey must have at least one question." | NT | |
| PUB-ED-003 | Publish with validation errors — blocked | Survey with Q2 having empty question text. | Click Publish. | Editor blocks. Same validation rules as Save. | NT | |
| PUB-ED-004 | Publish — survey enters read-only / restricted mode | Create and save valid survey. | Click Publish. | Survey published. Editor enters view-only or restricted-edit mode. Further changes require un-publish or new version. | NT | |
| PUB-ED-005 | Publish with logic configured — succeeds | Survey with Q1 (SAR) driving questionSelect on Q2 and choiceSelect on Q2 choices. All valid. | Click Publish. | Survey publishes. Logic preserved in published state. | NT | |
| PUB-ED-006 | Re-publish after edit — survey updated | Publish survey. Edit Q1 text. Re-save. | Click Publish again. | Survey republishes. Updated version live. No data loss. | NT | |
| PUB-ED-007 | Publish survey with screeningOut — succeeds | Survey with Q1 (SAR) marking C5 as screen-out. Q2 present. | Click Publish. | Survey publishes. screeningOut flag preserved in published state. | NT | |
| PUB-ED-008 | Preview before publish — survey renders in preview | Create and save valid survey with Q1 (SAR, 5 choices) and Q2 (MAC, 5 choices). | Click Preview. | Preview mode opens. Q1 and Q2 render correctly. Required indicators match settings. Logic not bypassed in preview. | NT | |
| PUB-ED-009 | Un-publish published survey — returns to draft | Publish survey. | Click Un-publish (or equivalent). | Survey status → Draft (or Unpublished). Editor re-enables editing. | NT | |
| PUB-ED-010 | Publish single-question survey — succeeds | Create and save survey with exactly 1 question (SAR, 5 choices). | Click Publish. | Survey publishes. One-question survey is valid. | NT | |
| PUB-ED-011 | Export / download published survey definition — succeeds | Publish survey. | Use Export / Download survey definition action. | Survey definition file (JSON or XML) downloaded without error. File is non-empty and contains correct question data. | NT | |

---

## 20. Save to AIRs (AIRS-001 – AIRS-015)

> **Context:** "Save to AIRs" converts the saved MaUS JSON survey to AIRs XML and pushes to the legacy AIRs system. One-way: existing AIRs surveys cannot be overwritten. Credentials dialog (AIRs username + password) precedes the push. On success, the AIRs ID is displayed in the Editor.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AIRS-001 | Happy path — valid survey saved to AIRs | Create survey with at least one SAR question. Save to DB. | Click "Save to AIRs". Enter valid credentials. Confirm. | Success message. AIRs ID displayed. Survey record updated. | NT | |
| AIRS-002 | Invalid credentials — error shown | Save valid survey to DB. | Click "Save to AIRs". Enter wrong credentials. Confirm. | Authentication error shown. Survey not pushed. No AIRs ID. Retry allowed. | NT | |
| AIRS-003 | Unsaved changes — blocked or auto-saved first | Open survey with unsaved changes. | Click "Save to AIRs". | Either: auto-saves then shows credential dialog; OR blocks with "Please save first." No data loss. | NT | |
| AIRS-004 | Survey with validation errors — blocked | Survey with deliberate error (blank question text). | Attempt "Save to AIRs". | Blocked. Validation errors shown. Credential dialog does not appear. | NT | |
| AIRS-005 | Re-save to AIRs — one-way constraint | Survey already has AIRs ID. Edit and save to DB. | Click "Save to AIRs" again. | Button disabled or warning shown. Original AIRs survey not modified. AIRs ID unchanged. | NT | |
| AIRS-006 | Empty survey (no questions) — blocked | Survey with no questions. Save to DB. | Click "Save to AIRs". | Blocked. Error: "Survey has no questions." | NT | |
| AIRS-007 | Multiple QTs (SAR, MAC, FA, MTS, MTM) — all convert | Survey with SAR, MAC, FA, MTS, MTM. Save to DB. | Click "Save to AIRs". Valid credentials. | All QTs converted to AIRs XML. No conversion error. AIRs ID returned. | NT | |
| AIRS-008 | Logic configured (questionSelect + choiceSelect) — persists in AIRs XML | Survey with Q1→Q2 questionSelect and choiceSelect. Save to DB. | Click "Save to AIRs". Valid credentials. | Logic definitions in AIRs XML. No error. AIRs ID returned. | NT | |
| AIRS-009 | AIRs system unavailable — graceful error | Save valid survey. Simulate AIRs unavailability. | Click "Save to AIRs". Valid credentials. | Error: "Failed to reach AIRs. Try again later." No AIRs ID. Editor unchanged. | NT | |
| AIRS-010 | Cancel credential dialog — no push | Save valid survey. | Click "Save to AIRs". Click Cancel in credential dialog. | Dialog closes. No push. No AIRs ID. Survey unchanged. | NT | |
| AIRS-011 | RNK question — converts to AIRs XML | Survey with RNK (5 items). Save to DB. | Click "Save to AIRs". Valid credentials. | RNK converted to AIRs XML ranking type. No error. AIRs ID returned. | NT | |
| AIRS-012 | RAT question — converts to AIRs XML | Survey with RAT (5 items, scale 1–5). Save to DB. | Click "Save to AIRs". Valid credentials. | RAT converted to AIRs XML rating type. Scale labels preserved. No error. AIRs ID returned. | NT | |
| AIRS-013 | MTT question — converts to AIRs XML | Survey with MTT (3 SQs × 5 choices, bipolar labels). Save to DB. | Click "Save to AIRs". Valid credentials. | MTT converted to AIRs XML bipolar matrix type. Labels preserved. AIRs ID returned. | NT | |
| AIRS-014 | countMatrix logic — converts to AIRs XML | Survey with Q1 (MTS, 3 SQs × 5 choices) and countMatrix condition on Q2. Save to DB. | Click "Save to AIRs". Valid credentials. | countMatrix logic represented in AIRs XML. No conversion error. AIRs ID returned. | NT | |
| AIRS-015 | FAL question — converts to AIRs XML | Survey with FAL (size=3). Save to DB. | Click "Save to AIRs". Valid credentials. | FAL converted to AIRs XML free-text multiline type. size setting preserved. AIRs ID returned. | NT | |

---

## 21. Answer Reference — Editor Configuration (AREF-ED)

> **Answer Reference** lets a question display the respondent's prior answer inline. It is inserted via the "Insert Answer" toolbar button in the rich-text editor. Typing `{{` manually is OUT OF SCOPE. A page break is mandatory between source and target questions.

### Basic Insertion by Source Type

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AREF-ED-001 | AR from SAR source `{{Q1}}` into question text — saves | 2-page survey. Q1 (SAR, 5 choices) on page 1. Q2 (SAR) on page 2. Page break between them. | In Q2 question text, click "Insert Answer" → select Q1 → `{{Q1}}` format. Click Save. | Saves. AR chip `{{Q1}}` persisted in Q2 question text. | NT | |
| AREF-ED-002 | AR from MAC source (multi-select) `{{Q1}}` — saves | Q1 (MAC, 5 choices) on page 1. Q2 on page 2. | Insert `{{Q1}}` in Q2 question text. Click Save. | Saves. At runtime multiple selected choices will be joined with half-width comma. | NT | |
| AREF-ED-003 | AR from SAP source `{{Q1}}` — saves | Q1 (SAP, 5 options) on page 1. Q2 on page 2. | Insert `{{Q1}}` in Q2 question text. Click Save. | Saves. AR chip persisted. | NT | |
| AREF-ED-004 | AR from FAL source `{{Q1FA}}` — saves | Q1 (FAL) on page 1. Q2 on page 2. | Insert `{{Q1FA}}` in Q2 question text. Click Save. | Saves. AR chip `{{Q1FA}}` persisted. Warning shown: source FA may be blank. | NT | |
| AREF-ED-005 | AR from MTS sub-question `{{Q1S1}}` — saves | Q1 (MTS, 3 SQs × 5 choices) on page 1. Q2 on page 2. | Insert `{{Q1S1}}` (column selected in SQ1 of Q1) in Q2 text. Click Save. | Saves. AR chip `{{Q1S1}}` persisted. | NT | |
| AREF-ED-006 | AR from MTM sub-question `{{Q1S1}}` — saves | Q1 (MTM, 3 SQs × 5 choices) on page 1. Q2 on page 2. | Insert `{{Q1S1}}` in Q2 text. Click Save. | Saves. AR chip `{{Q1S1}}` persisted. | NT | |
| AREF-ED-007 | AR from RNK `{{Q1S1}}` — saves | Q1 (RNK, 5 items) on page 1. Q2 on page 2. | Insert `{{Q1S1}}` in Q2 text. Click Save. | Saves. AR chip persisted. | NT | |
| AREF-ED-008 | AR from FA Textbox on choice `{{Q1_1FA}}` — saves with warning | Q1 (SAR, 5 choices) with FA textbox on choice 1 on page 1. Q2 on page 2. | Insert `{{Q1_1FA}}` in Q2 text. Click Save. | Saves. Warning displayed: "Source FA textbox is optional; value may be blank." AR chip persisted. | NT | |
| AREF-ED-009 | AR numeric variant `{{Q1_1N}}` — saves with warning | Q1 (SAR, 5 choices) with numeric FA on choice 1 on page 1. Q2 on page 2. | Insert `{{Q1_1N}}` in Q2 text. Click Save. | Saves. AR chip `{{Q1_1N}}` persisted. Optional-source warning shown. | NT | |

### Target Locations

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AREF-ED-010 | AR in choice text — saves | Q1 (SAR, 5 choices) page 1. Q2 (SAR, 5 choices) page 2. | Insert `{{Q1}}` in Q2 choice 3 text. Click Save. | Saves. AR chip in choice text persisted. | NT | |
| AREF-ED-011 | AR in matrix sub-question text — saves | Q1 (SAR) page 1. Q2 (MTS, 3 SQs × 5 choices) page 2. | Insert `{{Q1}}` in Q2.SQ2 text. Click Save. | Saves. AR chip in SQ text persisted. | NT | |
| AREF-ED-012 | AR in left/right text of FA Textbox — saves | Q1 (SAR) page 1. Q2 (FA) page 2. FA question configured with left-text and right-text label fields (e.g., "Price: ___ yen"). | Insert `{{Q1}}` in Q2 left-text field. Click Save. | Saves. AR chip in left-text of FA question persisted. | NT | |
| AREF-ED-013 | AR in RAT response item text — saves | Q1 (SAR) page 1. Q2 (RAT, 5 items) page 2. | Insert `{{Q1}}` in Q2 response item 1 text. Click Save. | Saves. AR chip in response item text persisted. | NT | |

### Prohibited Locations

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AREF-ED-014 | AR in Note question text — blocked | Q1 (SAR) page 1. Q2 (Note) page 2. | Attempt to insert `{{Q1}}` in Note text via "Insert Answer" button. | "Insert Answer" toolbar button absent or disabled in Note text editor. AR cannot be inserted in Note. | NT | |
| AREF-ED-015 | AR in question comment (top field) — blocked | Q1 (SAR) page 1. Q2 (SAR) page 2. | Attempt to insert AR in Q2's top comment field. | "Insert Answer" button absent or disabled in the comment field. AR cannot be inserted in comments. | NT | |
| AREF-ED-016 | AR in sub-question comment — blocked | Q1 (SAR) page 1. Q2 (MTS, 3 SQs) page 2. | Attempt to insert AR in Q2.SQ1 comment field. | AR insertion blocked in sub-question comment. | NT | |

### Page Break and Ordering Constraints

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AREF-ED-017 | No page break between source and target — auto page break inserted | Q1 (SAR) and Q2 (SAR) on same page. | Insert `{{Q1}}` in Q2 text. | Editor automatically inserts a page break between Q1 and Q2. Confirmation or info message shown. AR chip saved. | NT | |
| AREF-ED-018 | Forward reference (target question before source) — error | Q1 (SAR) page 1. Q2 (SAR) page 2. Insert AR on Q2 referencing Q1. Move Q2 above Q1 (Q2 now page 1, Q1 page 2). | Observe editor after move. | Error displayed on Q2: source question Q1 must be on a prior page. AR chip remains but is marked invalid until fixed. | NT | |
| AREF-ED-019 | Source question deleted after AR inserted — error displayed | Q1 (SAR) page 1. Q2 (SAR) page 2 with `{{Q1}}` AR. | Delete Q1. | Error displayed on Q2: referenced source no longer exists. Confirmation modal shown before deletion warning of the impact. | NT | |
| AREF-ED-020 | Source question moved to same page as target — error | Q1 page 1. Q2 page 2 with `{{Q1}}` AR. Move Q1 to page 2. | Observe editor. | Error displayed. Page break no longer separates source and target. AR chip marked invalid. | NT | |
| AREF-ED-021 | Page break deleted after AR inserted — error | Q1 page 1. Q2 page 2 with `{{Q1}}` AR. Delete the page break between them (merging to 1 page). | Observe editor. | Error displayed. AR requires source and target to be on different pages. | NT | |

### Chip Interaction

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AREF-ED-022 | Click AR chip to change source — dropdown reopens | Q2 with existing `{{Q1}}` AR chip. A third question Q3 also exists on a prior page. | Click the `{{Q1}}` chip in Q2's text. | Dropdown reopens. User can select Q3 as new source. Chip updates to `{{Q3}}`. | NT | |
| AREF-ED-023 | Delete AR chip via Backspace — chip removed | Q2 with `{{Q1}}` AR chip in text. | Place cursor immediately after chip. Press Backspace. | Chip deleted. No residual data in question text. | NT | |
| AREF-ED-024 | Multiple AR chips in same question text — saves | Q1, Q3 on page 1. Q2 on page 2 with both `{{Q1}}` and `{{Q3}}` chips in text. | Click Save. | Saves. Both AR chips persisted. | NT | |

### Section Randomization Interactions

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AREF-ED-025 | AR inserted then source and target placed in same randomized section — error | Create block with Section A. Insert `{{Q1}}` AR on Q2. Place Q1 and Q2 both into Section A (randomized). | Observe editor. | Error displayed. Source and target of an AR cannot both be in the same randomized section. | NT | |
| AREF-ED-026 | Source in different section (same block, randomized) — warning | Q1 in Section A (randomized). Q2 in Section B (randomized), same block. `{{Q1}}` AR on Q2. | Click Save. | Warning: source question may be skipped due to section display limits. Does not hard-block save. | NT | |

### Warnings

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AREF-ED-027 | Source FA optional → AR may be blank — warning | Q1 (SAR) with optional FA textbox on choice 1. Q2 references `{{Q1_1FA}}`. | Click Save. | Warning: "Source FA textbox is optional; referenced content may be blank for some respondents." Save permitted. | NT | |
| AREF-ED-028 | Source in block with max-sections-displayed limit — warning | Q1 in Section A of a block with max sections displayed = 1 (only 1 of 3 sections shown). Q2 outside block references `{{Q1}}`. | Click Save. | Warning: source question Q1 may not be shown to all respondents. Save permitted. | NT | |

### Combinations

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| AREF-ED-029 | AR + required=ON on target question — saves | Q1 (SAR) page 1. Q2 (SAR, required=ON) page 2 with `{{Q1}}` in text. | Click Save. | Saves. AR and required coexist on Q2. | NT | |
| AREF-ED-030 | AR + choiceSelect on target question — saves | Q1 page 1. Q2 page 2 with AR from Q1 AND choiceSelect (hides C3 of Q2 based on Q1 answer). | Click Save. | Saves. AR chip and choiceSelect rule coexist on Q2. | NT | |
| AREF-ED-031 | AR in choice text + rand=random on same question — saves | Q1 page 1. Q2 (SAR, 5 choices, rand=random) page 2. AR chip in Q2 choice 3 text. | Click Save. | Saves. AR in choice text and choice randomization coexist. | NT | |
| AREF-ED-032 | AR source question type changed to incompatible type → chip invalidated | Q1 (SAR, 5 choices) page 1. Q2 page 2 with `{{Q1}}` AR chip. Change Q1 type from SAR to Note (no answer output). | Observe editor after type change. | AR chip `{{Q1}}` in Q2 is marked invalid or automatically removed. Error shown: "Referenced source Q1 no longer produces answer output." | NT | |
| AREF-ED-033 | AR source question moved to same page as target after type-change re-routing — error | Q1 page 1. Q2 page 2 with `{{Q1}}` AR. Move Q1 to page 2 (same page as Q2). | Observe editor. | Error on Q2: AR requires source and target on different pages. Chip marked invalid. (Extends AREF-ED-020 to confirm consistent error messaging.) | NT | |

---

## 22. Image Rendering — Editor Configuration (IMG-ED)

> Images are URL-based (HTTPS only). Three display modes: **Inline** (embedded in text), **Thumbnail** (small preview that opens a modal; "click required" variant blocks page progression until opened), **Button** (opens full image in new tab — design still under review as of spec date). Alt text is optional except for images in choices (required).

### Inline Images — Basic Insertion by Location

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-001 | Inline image in SAR question text — saves | Add SAR 5 choices. In question text, insert image with valid HTTPS URL. | Click Save. | Saves. Image URL, mode=inline, persisted in question text. | NT | |
| IMG-ED-002 | Inline image in SAR choice text — saves | Add SAR 5 choices. Insert image in choice 3 text. Set alt text. | Click Save. | Saves. Inline image in choice 3 persisted. | NT | |
| IMG-ED-003 | Inline image in MAC choice text — saves | Add MAC 5 choices. Insert image in choice 1 text. Set alt text. | Click Save. | Saves. Inline image in MAC choice persisted. | NT | |
| IMG-ED-004 | Inline image in MTS sub-question text — saves | Add MTS 3 SQs × 5 choices. Insert image in SQ2 text. | Click Save. | Saves. Inline image in SQ2 text persisted. | NT | |
| IMG-ED-005 | Inline image in MTS column text — saves | Add MTS 3 SQs × 5 choices. Insert image in column C3 text. Set alt text. | Click Save. | Saves. Inline image in column C3 text persisted. | NT | |
| IMG-ED-006 | Inline image in Note question — saves | Add Note. Insert image in Note text. | Click Save. | Saves. Inline image in Note persisted. | NT | |
| IMG-ED-007 | Inline image in survey introduction text — saves | Open survey settings. Insert image in introduction/intro text. | Click Save. | Saves. Inline image in survey intro persisted. | NT | |
| IMG-ED-008 | Inline image in RAT response item text — saves | Add RAT 5 items. Insert image in response item 2 text. | Click Save. | Saves. Inline image in RAT item persisted. | NT | |
| IMG-ED-009 | Inline image in RNK ranking item text — saves | Add RNK 5 items. Insert image in item 1 text. | Click Save. | Saves. Inline image in RNK item persisted. | NT | |
| IMG-ED-010 | Multiple inline images on same line — saves | Add SAR 5 choices. Insert 2 images side-by-side in question text. | Click Save. | Saves. Both image URLs persisted. Each has its own settings. | NT | |

### Thumbnail Display Mode

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-011 | Thumbnail mode in lower question comment — saves | Add SAR 5 choices. In the lower comment field, insert image, set mode=Thumbnail. Provide thumbnail URL and full-image URL. | Click Save. | Saves. Thumbnail mode persisted with both URLs in lower comment. | NT | |
| IMG-ED-012 | Thumbnail click-required toggle ON — saves | Add SAR. Insert thumbnail in lower comment. Set "Click required" = ON. | Click Save. | Saves. Click-required flag persisted. At answer time, respondent must open modal before proceeding. | NT | |
| IMG-ED-013 | Thumbnail click-required + click-optional on same question — saves | Add SAR. Insert 2 thumbnails in lower comment: one click-required, one click-optional. | Click Save. | Saves. Both flags persisted independently. Click-required shows "・＊" indicator; click-optional shows "・". | NT | |
| IMG-ED-014 | Thumbnail in Note question — saves | Add Note. Insert thumbnail in Note text or lower comment. Provide both URLs. | Click Save. | Saves. Thumbnail mode in Note persisted. | NT | |

### Button Display Mode

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-015 | Button mode in lower question comment — saves | Add SAR. In lower comment, insert image, set mode=Button. Provide full-image URL. | Click Save. | Saves. Button mode persisted. *(Note: Survey Answer UX for Button mode is under design review; runtime rendering may vary.)* | NT | |
| IMG-ED-035 | Button mode — no thumbnail URL field shown (only full-image URL required) | Add SAR. In lower comment, insert image, set mode=Button. Observe form fields shown for Button mode. Provide full-image URL only. | Click Save. | Button mode shows only the full-image URL field (no separate thumbnail URL field). Saves. Only the full-image URL is required for Button mode. | NT | |
| IMG-ED-036 | Button mode — missing full-image URL — blocked on save | Add SAR. In lower comment, select mode=Button. Leave full-image URL blank. | Click Save. | Editor blocks. Error: full-image URL is required when Button mode is selected. | NT | |

### Placement Restrictions

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-016 | Image in SAP choice text — blocked | Add SAP 5 choices. Attempt to insert image in choice text. | Attempt insert. | Image insertion blocked in SAP choice text. Insert image control absent or returns error. | NT | |
| IMG-ED-017 | Thumbnail/Button in question text (not lower comment) — blocked | Add SAR. Attempt to insert Thumbnail mode image in the main question text field. | Attempt insert. | Thumbnail and Button modes are restricted to lower comment and Note. Error shown or mode options absent. | NT | |
| IMG-ED-018 | Image in sub-question group label — blocked | Add MTS with SQ groups. Attempt to insert image in SQ group label. | Attempt insert. | Image insertion blocked in SQ group labels. Insert control absent. | NT | |
| IMG-ED-019 | Image in choice group label — blocked | Add MAC with choice groups. Attempt to insert image in choice group label. | Attempt insert. | Image insertion blocked in choice group labels. Insert control absent. | NT | |

### URL Validation

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-020 | HTTP (non-HTTPS) URL — blocked on save | Add SAR. Insert image with URL starting with `http://`. | Click Save. | Editor blocks. Inline error: HTTPS required. HTTP is rejected to prevent mixed-content. | NT | |
| IMG-ED-021 | Invalid URL syntax (e.g., empty, malformed) — blocked | Add SAR. Enter invalid URL (e.g., `not-a-url`) for image. | Click Save. | Editor blocks. Inline error: invalid URL format. | NT | |
| IMG-ED-022 | Unsupported file type in URL (non-image, e.g., `.pdf`) — blocked | Add SAR. Enter URL pointing to a PDF file. | Click Save. | Editor blocks. Inline error: unsupported image format. | NT | |
| IMG-ED-023 | Unreachable URL (CORS / 404) — warning only, save permitted | Add SAR. Enter valid HTTPS URL that is unreachable or CORS-denied. | Click Save. | Editor shows warning: image could not be previewed; URL may be inaccessible. Save is permitted. | NT | |

### Alt Text and Thumbnail URL Validation

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-024 | Alt text missing for choice image — blocked on save | Add SAR 5 choices. Insert inline image in choice 2. Leave alt text blank. | Click Save. | Editor blocks. Error: alt text is required for images in choices. | NT | |
| IMG-ED-025 | Alt text missing for question text image — saves (optional) | Add SAR. Insert inline image in question text. Leave alt text blank. | Click Save. | Saves. Alt text is optional for images not in choice text. | NT | |
| IMG-ED-026 | Thumbnail URL missing when Thumbnail mode selected — blocked on save | Add SAR. In lower comment, select mode=Thumbnail. Provide only full-image URL; leave thumbnail URL blank. | Click Save. | Editor blocks. Error: thumbnail URL is required when Thumbnail mode is enabled. | NT | |

### Display Size Settings

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-027 | Set image width = 300px (manual) — saves | Add SAR 5 choices. Insert inline image in choice text. Set width = 300. Set alt text. | Click Save. | Saves. Width=300 persisted. | NT | |
| IMG-ED-028 | Set image dimensions = auto — saves | Add SAR. Insert inline image in question text. Set width = auto, height = auto. | Click Save. | Saves. Auto dimensions persisted. Image renders at natural size (capped at 184px long edge at answer time). | NT | |

### Answer Reference Interaction

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-029 | Choice with inline image used as AR source — image suppressed in AR output | Q1 (SAR, 5 choices) page 1 — choice 3 has inline image + text. Q2 page 2 with `{{Q1}}` AR. | Click Save. | Saves. When AR resolves at runtime, only choice text is shown; the inline image from choice 3 is NOT included in the AR output. | NT | |

### Combinations with Other Settings

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| IMG-ED-030 | Image in choice + screeningOut on same choice — saves | Add SAR 5 choices. Insert inline image in choice 5 text (with alt text). Mark choice 5 as screen-out. | Click Save. | Saves. Image and screeningOut coexist on choice 5. | NT | |
| IMG-ED-031 | Image in choice + choiceSelect (hide that choice) — saves | Add Q1 (SAR, 5 choices). Add Q2 (SAR, 5 choices). Insert inline image in Q2.C3 text. Set choiceSelect: hide Q2.C3 when Q1=C1. | Click Save. | Saves. Image and choiceSelect coexist on Q2.C3. | NT | |
| IMG-ED-032 | Image in matrix column text + column rand=random — saves | Add MTS 3 SQs × 5 choices. Insert inline image in column C4 text. Set column rand=random. | Click Save. | Saves. Image in column text and column randomization coexist. C4 (with image) shuffles with other columns. | NT | |
| IMG-ED-033 | Thumbnail click-required + question required=ON — saves | Add SAR 5 choices. Set required=ON. Insert thumbnail in lower comment with click-required=ON. | Click Save. | Saves. Respondent must open the thumbnail modal AND answer the question before proceeding. | NT | |
| IMG-ED-034 | Inline image in question text + questionSelect (question hidden) — saves | Add Q1 (SAR, 5 choices). Add Q2 (SAR, inline image in question text). Set questionSelect: show Q2 only if Q1=C1. | Click Save. | Saves. Image in question text and questionSelect coexist. If Q2 is hidden, image is not rendered. | NT | |

---

## 23. AND / OR Multi-Condition Logic (LCOMB-ED)

> Tests 2-condition combinations using AND / OR connectives across questionSelect, choiceSelect, subquestionSelect, and countMatrix. Each case has exactly 2 condition rows joined by one connective.

### 23a. questionSelect — AND / OR (LCOMB-ED-001–009)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| LCOMB-ED-001 | questionSelect OR: (Q1=C1) OR (Q2=C2) | Survey with Q1 (SAR, 3 choices), Q2 (SAR, 3 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1=C1) OR (Q2=C2). | Click Save. | Saves without error. Two-condition OR on exact operators accepted. | NT | |
| LCOMB-ED-002 | questionSelect OR: (Q1 any[C1,C2]) OR (Q2=C3) | Survey with Q1 (MAC, 4 choices), Q2 (SAR, 3 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 any[C1,C2]) OR (Q2=C3). | Click Save. | Saves without error. `any` operator in condition row 1 combined with OR connective and exact in row 2 is accepted. | NT | |
| LCOMB-ED-003 | questionSelect OR: (Q1 notAll[C1,C2]) OR (Q2=C3) | Survey with Q1 (MAC, 4 choices), Q2 (SAR, 3 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 notAll[C1,C2]) OR (Q2=C3). | Click Save. | Saves without error. `notAll` operator in condition row 1 combined with OR connective accepted. | NT | |
| LCOMB-ED-004 | questionSelect AND: (Q1 any[C1,C2]) AND (Q2=C3) | Survey with Q1 (MAC, 4 choices), Q2 (SAR, 3 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 any[C1,C2]) AND (Q2=C3). | Click Save. | Saves without error. `any` AND exact 2-condition combination accepted. | NT | |
| LCOMB-ED-005 | questionSelect AND: (Q1 any[C1,C2]) AND (Q2 any[C3,C4]) | Survey with Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 any[C1,C2]) AND (Q2 any[C3,C4]). | Click Save. | Saves without error. Both condition rows use `any`; AND connective accepted. | NT | |
| LCOMB-ED-006 | questionSelect AND: (Q1 any[C1,C2]) AND (Q2 notAll[C3,C4]) | Survey with Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 any[C1,C2]) AND (Q2 notAll[C3,C4]). | Click Save. | Saves without error. `any` AND `notAll` 2-condition combination accepted. | NT | |
| LCOMB-ED-007 | questionSelect AND: (Q1 notAll[C1,C2]) AND (Q2 notAll[C3,C4]) | Survey with Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 notAll[C1,C2]) AND (Q2 notAll[C3,C4]). | Click Save. | Saves without error. Both condition rows use `notAll` with AND connective; accepted. | NT | |
| LCOMB-ED-008 | questionSelect OR: (Q1 any[C1,C2]) OR (Q2 notAll[C3,C4]) | Survey with Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 any[C1,C2]) OR (Q2 notAll[C3,C4]). | Click Save. | Saves without error. `any` OR `notAll` 2-condition combination accepted. | NT | |
| LCOMB-ED-009 | questionSelect OR: (Q1 any[C1,C2]) OR (Q2 any[C3,C4]) | Survey with Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 any[C1,C2]) OR (Q2 any[C3,C4]). | Click Save. | Saves without error. Both rows use `any` with OR connective; accepted. | NT | |

### 23b. choiceSelect — AND / OR (LCOMB-ED-010–013)

> Survey order in these cases: Q1 (source 1) → Q2 (source 2) → Q3 (target with choices). Both sources precede the target.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| LCOMB-ED-010 | choiceSelect OR: hide choice if (Q1=C1) OR (Q2=C2) | Survey in order: Q1 (SAR, 3 choices), Q2 (SAR, 3 choices), Q3 (MAC, 5 choices). Set choiceSelect on Q3.C3: hide if (Q1=C1) OR (Q2=C2). | Click Save. | Saves without error. Two-source OR choiceSelect accepted. | NT | |
| LCOMB-ED-011 | choiceSelect AND: hide choice if (Q1 any[C1,C2]) AND (Q2=C3) | Survey in order: Q1 (MAC, 4 choices), Q2 (SAR, 3 choices), Q3 (MAC, 5 choices). Set choiceSelect on Q3.C3: hide if (Q1 any[C1,C2]) AND (Q2=C3). | Click Save. | Saves without error. `any` AND exact 2-condition choiceSelect accepted. | NT | |
| LCOMB-ED-012 | choiceSelect OR: hide choice if (Q1 notAll[C1,C2]) OR (Q2=C3) | Survey in order: Q1 (MAC, 4 choices), Q2 (SAR, 3 choices), Q3 (MAC, 5 choices). Set choiceSelect on Q3.C3: hide if (Q1 notAll[C1,C2]) OR (Q2=C3). | Click Save. | Saves without error. `notAll` OR exact 2-condition choiceSelect accepted. | NT | |
| LCOMB-ED-013 | choiceSelect AND: hide choice if (Q1 any[C1,C2]) AND (Q2 notAll[C3,C4]) | Survey in order: Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (MAC, 5 choices). Set choiceSelect on Q3.C3: hide if (Q1 any[C1,C2]) AND (Q2 notAll[C3,C4]). | Click Save. | Saves without error. `any` AND `notAll` 2-condition choiceSelect accepted. | NT | |

### 23c. subquestionSelect — AND / OR (LCOMB-ED-014–016)

> Survey order in these cases: Q1 (source 1) → Q2 (source 2) → Q3 (matrix target). Both sources precede the target matrix.

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| LCOMB-ED-014 | subquestionSelect OR: show SQ if (Q1=C1) OR (Q2=C2) | Survey in order: Q1 (SAR, 3 choices), Q2 (SAR, 3 choices), Q3 (MTS, 3 SQs, 4 choices). Set subquestionSelect on Q3.SQ1: show if (Q1=C1) OR (Q2=C2). | Click Save. | Saves without error. Two-source OR subquestionSelect accepted. | NT | |
| LCOMB-ED-015 | subquestionSelect OR: show SQ if (Q1 any[C1,C2]) OR (Q2=C3) | Survey in order: Q1 (MAC, 4 choices), Q2 (SAR, 3 choices), Q3 (MTS, 3 SQs, 4 choices). Set subquestionSelect on Q3.SQ2: show if (Q1 any[C1,C2]) OR (Q2=C3). | Click Save. | Saves without error. `any` OR exact 2-condition subquestionSelect accepted. | NT | |
| LCOMB-ED-016 | subquestionSelect AND: show SQ if (Q1 notAll[C1,C2]) AND (Q2 any[C3,C4]) | Survey in order: Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (MTS, 3 SQs, 4 choices). Set subquestionSelect on Q3.SQ3: show if (Q1 notAll[C1,C2]) AND (Q2 any[C3,C4]). | Click Save. | Saves without error. `notAll` AND `any` 2-condition subquestionSelect accepted. | NT | |
| LCOMB-ED-022 | subquestionSelect AND: (Q1 any[C1,C2]) AND (Q2 any[C3,C4]) | Survey in order: Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (MTS, 3 SQs, 4 choices). Set subquestionSelect on Q3.SQ1: show if (Q1 any[C1,C2]) AND (Q2 any[C3,C4]). | Click Save. | Saves without error. Both condition rows use `any` with AND connective; subquestionSelect 2-condition combination accepted. | NT | |
| LCOMB-ED-023 | subquestionSelect AND: (Q1 any[C1,C2]) AND (Q2 notAll[C3,C4]) | Survey in order: Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (MTS, 3 SQs, 4 choices). Set subquestionSelect on Q3.SQ2: show if (Q1 any[C1,C2]) AND (Q2 notAll[C3,C4]). | Click Save. | Saves without error. `any` AND `notAll` 2-condition subquestionSelect accepted. | NT | |

### 23d. Additional choiceSelect pattern (LCOMB-ED-024)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| LCOMB-ED-024 | choiceSelect OR: hide choice if (Q1 any[C1,C2]) OR (Q2 any[C3,C4]) | Survey in order: Q1 (MAC, 4 choices), Q2 (MAC, 4 choices), Q3 (MAC, 5 choices). Set choiceSelect on Q3.C3: hide if (Q1 any[C1,C2]) OR (Q2 any[C3,C4]). | Click Save. | Saves without error. Both condition rows use `any` with OR connective; 2-condition choiceSelect accepted. | NT | |

### 23e. countMatrix — AND / OR with other logic (LCOMB-ED-017–021)

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| LCOMB-ED-017 | countMatrix OR: two thresholds on same matrix (≥3 OR ≤1) | Survey with Q1 (MTM, 3 SQs, 5 choices), Q2 (SAR). Set questionSelect on Q2: show if countMatrix(Q1)>=3 OR countMatrix(Q1)<=1. | Click Save. | Per spec: countMatrix compound conditions use AND only (e.g., >=2 AND <=4). OR between two countMatrix conditions on the same source is not supported. Editor blocks: cannot combine two countMatrix rows on the same source with OR. Use AND to express a range. | NT | |
| LCOMB-ED-018 | questionSelect AND: (Q1=C1) AND (countMatrix(Q2)>=2) | Survey in order: Q1 (SAR, 3 choices), Q2 (MTM, 3 SQs, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1=C1) AND countMatrix(Q2)>=2. | Click Save. | Saves without error. Selection condition AND countMatrix threshold 2-condition combination accepted. | NT | |
| LCOMB-ED-019 | questionSelect OR: (Q1=C1) OR (countMatrix(Q2)>=2) | Survey in order: Q1 (SAR, 3 choices), Q2 (MTM, 3 SQs, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1=C1) OR countMatrix(Q2)>=2. | Click Save. | Saves without error. Selection condition OR countMatrix threshold 2-condition combination accepted. | NT | |
| LCOMB-ED-020 | questionSelect AND: (Q1 any[C1,C2]) AND (countMatrix(Q2)>=2) | Survey in order: Q1 (MAC, 4 choices), Q2 (MTM, 3 SQs, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 any[C1,C2]) AND countMatrix(Q2)>=2. | Click Save. | Saves without error. `any` AND countMatrix 2-condition combination accepted. | NT | |
| LCOMB-ED-021 | questionSelect OR: (Q1 notAll[C1,C2]) OR (countMatrix(Q2)>=2) | Survey in order: Q1 (MAC, 4 choices), Q2 (MTM, 3 SQs, 4 choices), Q3 (SAR). Set questionSelect on Q3: show if (Q1 notAll[C1,C2]) OR countMatrix(Q2)>=2. | Click Save. | Saves without error. `notAll` OR countMatrix 2-condition combination accepted. | NT | |

---

## Change Log

| Date | Change | Case IDs |
|---|---|---|
| 2026-05-07 | Overall 3-pass review. **Pass 1 (accuracy):** Fixed AREF-ED-012 — setup corrected from Q2 (FAL) to Q2 (FA) with left/right text fields (FAL has no left/right label fields; FA does); title updated to "FA Textbox" to remove ambiguous "FAS" abbreviation. Added intentional-gap note after QRAND-ED-016 explaining QRAND-ED-017 was removed as duplicate. Added cross-reference note on SV-ED-011 pointing to SAV-ED-012 to clarify they cover the same boundary from different contexts. Added PRX-ED section numbering note explaining the non-sequential ID structure. **Pass 2 (gap fill):** Added IMG-ED-035 (Button mode shows only full-image URL field) and IMG-ED-036 (Button mode missing URL blocked) to improve thin Button mode coverage. Added LCOMB-ED-022 (subquestionSelect AND: both `any`) and LCOMB-ED-023 (subquestionSelect AND: `any+notAll`) to close subquestionSelect combination gaps. Added LCOMB-ED-024 (choiceSelect OR: both `any`) to close choiceSelect combination gap. Updated LCOMB subsection labels to 23a–23e. **Pass 3 (structure):** Updated TOC ranges (IMG-ED-001–036, LCOMB-ED-001–024), updated count (496 → 501). Total: 496 → 501. | AREF-ED-012 fix; IMG-ED-035–036; LCOMB-ED-022–024 |
| 2026-05-07 | 3-pass review: Pass 1 (accuracy) — fixed QSEL-ED-020 title ("2-arg" → range condition), expanded MT-MTS-11 expected result to specify per-cell required FA behavior, broadened QSEL-ED-023 nvl() description to cover FA blank as well as choice null. Pass 2 (gap fill) — added: QT-RNK-13–14 (RNK display formats: dropdown, radio-button grid); SV-ED-014–015 (screening-out point amount config + per-panel-type differentiation); MT-MTM-13 (matrix FA with type="number" numeric input). Pass 3 (quality) — updated TOC ranges (SV-ED-001–015, QT-RNK-001–014, MT-MTM-001–013), updated count (489 → 496), added cross-reference note after QSEL-ED-023 clarifying advanced functions apply to all logic types. Total: 489 → 496. | QT-RNK-13–14, SV-ED-014–015, MT-MTM-13; QSEL-ED-020/023 corrections |
| 2026-05-07 | Gap review against AIRs TEST-CASES.md files (31_質問追加_移動_削除, 38_ロジック解除, 41_条件式の設定・評価, 43_イエローカード, 44_順位回答質問単位変更チェック, 47_回答「戻る」ボタン, 50_順位回答（回答形式）, 52_マトリクスFA). Gaps identified and filled: (1) RNK display unit labels (位/番目) and required-count indicator in preview → QT-RNK-10–12; (2) Back button default hidden + toggle saves → SV-ED-012–013; (3) Matrix FA tags (<fa>) for MTS/MTM column, row, and cell positions → MT-MTS-10–11, MT-MTM-11–12; (4) Advanced condition expression functions in editor (snotall, count range, countif, num, nvl) → QSEL-ED-018–023; (5) Question insert auto-updates logic refs, randomization preserved after add/move, multi-type logic cascade on delete → COMB-ED-028–030. Total: 471 → 489. | QT-RNK-10–12, SV-ED-012–013, MT-MTS-10–11, MT-MTM-11–12, QSEL-ED-018–023, COMB-ED-028–030 |
| 2026-05-02 | Re-read AIRs 29_ロジック組合せ_追加分 (previously failed with mojibake; re-read with correct encoding utf-8/cp932). New gap found: 6 logic-combination cases not previously covered from AIRs combination tests. Added: COMB-ED-022 (prohibition+inclusion on same matrix), COMB-ED-023 (two prohibition rules on same matrix), COMB-ED-024 (exclusive+prohibition on same matrix), COMB-ED-025 (exclusive+inclusion on same matrix), COMB-ED-026 (AR piping target also has fieldSelect), COMB-ED-027 (matrixInclusion+questionSelect on same target). COMB TOC updated 001–021 → 001–027. Total: 464 → 471. | COMB-ED-022–027 |
| 2026-05-02 | 3-pass review against AIRs legacy regression test cases (38_ロジック解除, 31_質問追加_移動_削除, 46_作成制限超過質問数, 44_順位回答質問単位変更チェック). Key findings: (1) "Logic auto-cleared when source question type changes" — entire category missing; added QSEL-ED-016, CSEL-ED-014, SQSEL-ED-012, SCR-ED-012, PRX-ED-017, PRX-ED-018, CM-ED-020, AREF-ED-032; (2) Source-question-deleted cases strengthened/added: CSEL-ED-013, SQSEL-ED-011, CM-ED-010 (tightened); (3) Forward-reference after move: QSEL-ED-017; (4) RNK required-count settings: QT-RNK-06–09; (5) Question complexity count limit: SAV-ED-013; (6) Multi-logic delete cascade: SAV-ED-014; (7) AR moved-to-same-page: AREF-ED-033. Pass 2 fixes: tightened QSEL-ED-005, CSEL-ED-007, SQSEL-ED-004, MINC-ED-003, SV-ED-007 expected results from "removed or flagged" to definitive "auto-cleared". Total: 446 → 464. | QSEL-ED-016–017, CSEL-ED-013–014, SQSEL-ED-011–012, SCR-ED-012, PRX-ED-017–018, CM-ED-020, AREF-ED-032–033, QT-RNK-06–09, SAV-ED-013–014 |
| 2026-05-02 | 3-pass review of latest QRAND-ED-021–030 additions and full file. Fixes: QSEL-ED-006 setup missing Q1 definition (added Q1 SAR); PB-ED-006 setup missing Q1 definition (added Q1 SAR); COMB-ED-007 terminology "countif" → "countMatrix" for consistency. New cases: QRAND-ED-031 (same-section logic WITH page break → allowed, positive counterpart to QRAND-ED-027); QRAND-ED-032 (block page break distinct from item page break → saves); QRAND-ED-033 (non-consecutive section items → blocked, per spec). TOC range updated 001–030 → 001–033. Total: 443 → 446. | QRAND-ED-031–033 |
| 2026-05-02 | Question randomization + selection logic spec review (page 1582366789). Key spec finding: cross-section restriction within same block applies to ALL selection logic types, not only questionSelect. Added 10 new QRAND-ED cases: QRAND-ED-021–024 (choiceSelect/subquestionSelect/countMatrix/matrixInclusion each blocked cross-section); QRAND-ED-025 (sections+logic configured in wrong order → error); QRAND-ED-026 (source inside section → target after block → allowed); QRAND-ED-027 (logic within same section still requires page break → blocked); QRAND-ED-028 (required=ON inside section with display limit → saves); QRAND-ED-029 (screeningOut inside section → saves); QRAND-ED-030 (manual logic input cross-section → blocked). Also fixed TOC range (was 001–019, QRAND-ED-020 existed but was unlisted). Total: 433 → 443. | QRAND-ED-021–030 |
| 2026-05-02 | 3-pass full review (pass 1: section numbering — fixed duplicate §7 FA-ED header and corrected §8–20 off-by-one in body vs TOC; pass 2: removed duplicate QRAND-ED-017 (same as QRAND-007), fixed COMB-ED-020 undefined Q0 reference, fixed LCOMB-ED-010–016 and 018–021 forward-reference bug in source question ordering, corrected PRX-ED-016 expected result for MTM same-row prohibition, clarified LCOMB-ED-017 countMatrix OR behavior, softened CM-ED-003 hard-block claim; pass 3: added CSEL-ED-012 `all` operator, SQSEL-ED-010 `all` operator, MINC-ED-008 MTT source, CM-ED-019 MTT source). Net: 430 → 433. | CSEL-ED-012, SQSEL-ED-010, MINC-ED-008, CM-ED-019; removed QRAND-ED-017 |
| 2026-05-02 | AND/OR multi-condition logic review — added Section 23 (LCOMB-ED-001–021, 21 cases) covering: questionSelect with OR and AND using exact/any/notAll operators (9 cases); choiceSelect OR/AND with any/notAll (4 cases); subquestionSelect OR/AND with any/notAll (3 cases); countMatrix mixed with selection logic via AND/OR (5 cases). Total: 409 → 430. | LCOMB-ED-001–021 |
| 2026-05-02 | Answer Reference + Image Rendering specs read from Confluence. Added Section 21 (AREF-ED-001–031, 31 cases) and Section 22 (IMG-ED-001–034, 34 cases) covering: AR by source QT, target locations, prohibited locations, page-break constraints, auto page-break, chip interaction, section-rand interactions, warnings, combinations; image inline/thumbnail/button modes, placement restrictions, URL/alt-text validation, size settings, AR+image interaction, combinations. Total: 344 → 409. | AREF-ED-001–031, IMG-ED-001–034 |
| 2026-05-02 | Randomization 3-pass spec review — corrected 5 cases (removed non-existent `absolute` mode; clarified `fixedLast` as per-item fixed flag, not a mode); split RAND-ED into choice/sub-question (RAND-ED-001–046) and question/section-block (QRAND-ED-001–020) sections; added 47 new randomization cases covering: choice groups, SQ groups, missing QT×mode combos, question-rand blocks/sections, section constraints, logic interactions. Total: 297 → 344. | RAND-ED-001–046, QRAND-ED-001–020, COMB-ED-019–021 |
| 2026-05-02 | 3-pass gap review — added 82 cases across all sections. New cases: SV-ED-009–011, QT-SAR-05–06, QT-MAC-05–06, QT-SAP-05–06, QT-FA-06, QT-FAL-04, QT-RNK-05, QT-RAT-05, MT-MTS-08–09, MT-MTM-09–10, MT-MTT-05–06, REQ-ED-015–019, RAND-ED-017–020, SPECN-ED-016–017, FA-ED-011–012, QSEL-ED-011–015, CSEL-ED-009–011, SQSEL-ED-007–009, MINC-ED-005–007, CM-ED-013–018, SCR-ED-009–011, PRX-ED-011–016, PB-ED-007–008, COMB-ED-016–020, SAV-ED-009–012, PUB-ED-007–011, AIRS-011–015. Total: 215 → 297. | See IDs |
| 2026-05-02 | Full rewrite — expanded editor coverage per updated scope. Added sections: SV-ED (8), QT-ED (30), MT-ED (19), REQ-ED (14), RAND-ED (16), SPECN-ED (15), FA-ED (10), QSEL-ED (10), CSEL-ED (8), SQSEL-ED (6), MINC-ED (4), CM-ED extended to 12, SCR-ED (8), PRX-ED (10), PB-ED (6), COMB-ED (15), SAV-ED (8), PUB-ED (6), AIRS (10). Coverage: all QTs × 1 choice / 5 choices / 3 SQs; all logic types and combinations. | All |
| 2026-05-01 | Reorganized per three-file rule. E2E/answer-runtime cases removed. | AIRS-001–010, V-REQ-007, CM-ED-001–008 |

---

## Out of Scope

> Features not yet developed. Cases will be activated when features ship.

### Loop Block

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| E2E-005 | Loop block — validation recovery in iteration 2 | Loop block over Q10–Q12; maxIterations=3 | Complete iter 1; in iter 2, submit invalid answer to Q10; correct and resubmit | Error returned for Q10 in iter 2; corrected; iter 3 proceeds. | NT | |

### Quota

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| E2E-008 | Quota-based routing — quota boundary | Segment A quota=50; 49 already in | Respondents 50 and 51 qualify for A | Respondent 50 → A. Respondent 51 → quota full, alternate path. | NT | |

### User-Attribute Pre-Fill

| Test ID | Scenario Title | Setup | Action | Expected Outcome | Tested | Related JIRA |
|---|---|---|---|---|---|---|
| E2E-010 | User attribute pre-fill — visible on survey start | Q1 pre-filled from user["name"]="Tanaka" | Open survey | Q1 shows "Tanaka"; value recorded. | NT | |
