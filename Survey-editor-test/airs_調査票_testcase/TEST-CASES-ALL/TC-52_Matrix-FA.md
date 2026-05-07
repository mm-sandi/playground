# 52 — Matrix Free-Text Fields (マトリクスFA)
**Purpose:** Verify matrix questions with free-text sub-fields.

---

## Background

Matrix questions (MTS = single-select, MTM = multi-select) can embed free-answer (`<fa>`) tags in three positions:

- **Column header (表頭) FA** — a free-text field attached to a column header choice.
- **Row item (表側) FA** — a free-text field attached to a row item.
- **Cell (表内) FA** — a free-text field that appears inside the answer cell when a respondent selects that cell.

The `<fa>` tag accepts attributes such as `size`, `required`, `no` (groups shared FAs), and `type="number"` (numeric-only input). The `required` attribute can be `true` (respondent must fill it in) or `false` (optional).

Answers entered in these fields must appear correctly in the tabulation results (フリーコメント popup) after the survey closes.

---

## Source Files

| File | Survey type |
|---|---|
| `selenium/01_マトリクスFA（オープン調査票）.html` | Open survey |
| `selenium/02_マトリクスFA（Quick調査票）.html` | Quick survey |

---

## Test Group 1 — Open Survey Matrix FA (オープン調査票)

**Source file:** `01_マトリクスFA（オープン調査票）.html`

### TC-52-01 Create an Open survey with four matrix FA question variants

**Pre-conditions:**
- Admin account `admin_4001` (user ID 4001) has access to the Open survey type.

**Steps:**
1. Log in as admin `4001`.
2. Create a new Open survey named `AnswerMatrixFAType_OPEN_<today>` (PC-only device).
3. Add **Q1 (MTS, normal display)**: 5 column headers each with a column-FA (`<fa size="15" />`); row items have a row-FA and a cross-reference cell-FA (`<fa no="1-5" size="15"/>`). Row item 1 FA is required; items 2–4 are optional.
4. Add **Q2 (MTS, reverse display)**: same structure but `display` set to reverse layout; all four row FAs are required.
5. Add **Q3 (MTM, normal display)**: 5 column headers with column-FAs; row items have row-FAs and cell-FAs; Q3 row 1 cell FAs are required; rows 2–4 optional.
6. Add **Q4 (MTM, reverse display)**: reverse layout; row FAs are required or optional per specification.
7. Finalize the questionnaire, complete all condition settings, and launch the survey (実査中).

**Expected results:**
- All four matrix questions save and preview without errors.
- Survey launches successfully.

---

### TC-52-02 Respondent A — fills in all optional and required FAs

**Pre-conditions:** Survey from TC-52-01 is running.

**Steps:**
1. Open the survey URL.
2. For Q1: select cells (1,1), (1,3), (1,4); enter text in the column-FA, row FAs, and multiple cell FAs.
3. For Q2: select cells in each row; enter text in all row and cell FAs.
4. For Q3: select cells; enter text in all row and cell FAs.
5. For Q4: select cells in all four rows; enter text in row FAs and cell FAs.
6. Fill in the profile attributes page (name, email, gender, age, zip code, prefecture, address, phone) and submit.

**Expected results:**
- Each question page advances without validation errors.
- The final "Thank you" confirmation page is not shown (browser window closed; admin view remains).

---

### TC-52-03 Respondent B — required FA validation fires on missing cell FA

**Pre-conditions:** Survey from TC-52-01 is running.

**Steps:**
1. Open the survey URL as a second respondent.
2. For Q1: select cells (1,1), (2,2), (3,4), (4,2) but do **not** fill in the required cell FA for row 1.
3. Click Next.

**Expected results:**
- Validation error displayed: "1.選択肢A／1.大変よい の入力欄は必ず回答してください。"

4. Enter text in the required cell FA and proceed.
5. Complete Q2, Q3, Q4 with assorted cell selections and FAs, then submit.

**Expected results:**
- All validation errors resolve after filling in required fields.
- Submission succeeds.

---

### TC-52-04 Respondent C — partial FA fill (only some fields entered)

**Pre-conditions:** Survey from TC-52-01 is running.

**Steps:**
1. Open the survey URL as a third respondent.
2. Selectively fill only some FAs (leave optional FAs blank) and select cells across Q1–Q4.
3. Submit the profile attributes page and finish.

**Expected results:**
- Survey accepts submission with optional FAs left blank.

---

### TC-52-05 Verify tabulation shows correct FA text per respondent

**Pre-conditions:** All three respondents have submitted; admin terminates the survey.

**Steps:**
1. Log in as admin `50070`, search for the survey by RID, and click "End" (終了).
2. Open the simple tabulation page (`showResearchOutlineAndGtSimpleTabulateByAdminAction`).
3. For Q1 column-FA, open the free-comment popup for the second column; verify respondent A's and C's entries are present.
4. For Q1 row-FA, verify A's and C's header answers appear.
5. Repeat for Q2 column headers, row FAs, and cell FAs.
6. Repeat for Q3 and Q4 row and cell FAs.

**Expected results:**
- Each popup shows the correct TOTAL count and contains the expected answer text for respondents A, B, and C as entered in TC-52-02 through TC-52-04.

---

## Test Group 2 — Quick Survey Matrix FA (Quick調査票)

**Source file:** `02_マトリクスFA（Quick調査票）.html`

### TC-52-06 Create a Quick survey with four matrix FA question variants

**Pre-conditions:**
- Admin account `admin_4001`.

**Steps:**
1. Create a new Quick survey named `表頭FA＆表内FA_<today>_01_Quick調査票` (PC-only).
2. Add **Q1 (MTS, normal display)**: column headers include both text-FA and number-FA tags; row items include row-FAs (`<fa />`) and cell-FAs with `no` grouping. Required setting is `false` on the question level.
3. Add **Q2 (MTS, reverse display)**: column headers have row-FAs; row items have cell-FAs; one cell-FA in row 1 is `required="true"`.
4. Add **Q3 (MTM, normal display)**: same FA structure as Q1 with the display in normal order.
5. Add **Q4 (MTM, reverse display)**: same FA structure as Q2.
6. Finalize, configure conditions (delivery method = panel, target industry = 901), and launch.

**Expected results:**
- Survey launches (実査中).

---

### TC-52-07 Monitor 1 (reg053) — answers all questions including optional FAs

**Pre-conditions:** Survey from TC-52-06 is running.

**Steps:**
1. Log in to the monitor site as `reg053@macromill.com` and open the survey URL.
2. On the single question page: fill in column-FA, number-FA, row-FA, and cell-FA fields for Q1–Q4 as specified; select checkboxes/radio buttons.
3. Wait for the answer-time check pause and click Finish.

**Expected results:**
- Confirmation page: "ご協力ありがとうございました。"

---

### TC-52-08 Monitor 2 (reg054) — answers with a different selection pattern

**Pre-conditions:** Survey from TC-52-06 is running.

**Steps:**
1. Log in as `reg054@macromill.com`, open the survey, and answer Q1–Q4 with a different cell-selection pattern (fewer cells selected, different FAs filled).
2. Finish the survey.

**Expected results:**
- Confirmation page displayed.

---

### TC-52-09 Monitor 3 (reg055) — required FA validation fires when cell selected without FA

**Pre-conditions:** Survey from TC-52-06 is running.

**Steps:**
1. Log in as `reg055@macromill.com`, open the survey.
2. Select cells across Q1–Q4 but leave required FAs blank.
3. Click Finish.

**Expected results:**
- Validation errors:
  - "2.Q1選択肢B／3.Q1どちらともいえない の入力欄は必ず回答してください。"
  - "1.Q2選択肢A／1.Q2大変よい の入力欄は必ず回答してください。"

4. Fill in the two required FAs and click Finish.

**Expected results:**
- Confirmation page displayed.

---

### TC-52-10 Verify Quick survey tabulation shows correct FA text

**Pre-conditions:** All three monitors have submitted; admin terminates the survey.

**Steps:**
1. Log in as admin, search by RID, and end the survey.
2. Open the simple tabulation page.
3. For each of Q1–Q4, open the free-comment popup for each column-FA and row-FA column; verify expected answer text and TOTAL counts.

**Expected results (sample checks):**
- Q1 first column-FA popup: TOTAL 2 件, contains `Q1_189` and `Q1_192`.
- Q1 column "Q1悪い" popup: TOTAL 0 (no entries because that column had no FA).
- Q1 row-FA (row 3 / どちらともいえない): TOTAL 1 件, contains `189`.
- Q2, Q3, Q4 follow the same pattern: cells with FAs show the correct monitor IDs; cells with no FAs show 0 entries; required-FA cell shows all three monitors (including `回答必須` from monitor 3).
