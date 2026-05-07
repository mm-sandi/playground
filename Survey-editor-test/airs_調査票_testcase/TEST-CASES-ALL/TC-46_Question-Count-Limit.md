# 46 — Question Count Limit (作成制限超過質問数)
**Purpose:** Verify behavior when a survey exceeds the maximum allowed question complexity count (matrix questions count as multiple).

---

## Background

The system tracks two counts on the survey detail page:
- **Question Count (質問カウント / numAccountQuestionSpan)** — the total billing-unit count, calculated as: actual questions + overflow units.
- **Actual Questions (質問数 / numQuestionSpan)** — the number of questions the respondent sees.
- **Overflow Units (作成制限超過 / numOverflowedQuestionSpan)** — additional units charged because large matrix questions each "consume" more than one slot.

These numbers must display consistently on the survey detail page, the condition-settings screen, and inside the question-count field on the order/SF form.

---

## Source Files

| File | Survey type |
|---|---|
| `質問カウント_作成制限超過質問数_Open.html` | Open survey |
| `質問カウント_作成制限超過質問数_Quick.html` | Quick survey |

---

## Test Group 1 — Open Survey Question Count Display

**Source file:** `質問カウント_作成制限超過質問数_Open.html`

### TC-46-01 Initial count after building a large survey

**Pre-conditions:**
- Admin account `admin_4001` has access to the Open survey type.

**Steps:**
1. Log in to the admin site as `admin_4001`.
2. Create a new Open survey.
3. Add the following questions in sequence:
   - **MTS** matrix (single-select): 90 column headers, 90 row items.
   - **MTM** matrix (multi-select): 90 column headers, 90 row items (with a sub-header row).
   - **MTT** matrix (two-sided): 90 column headers, 90 left-side items, 90 right-side items.
   - **FAS** free-answer-set question: 50 free-answer (`<fa>`) sub-items.
   - **RAT** rating question.
4. Add a profile-attribute FAS question (50 sub-items) under the attribute question section.
5. Finalize the questionnaire and navigate to "Settings complete."

**Expected results:**
- Question Count displays **29 問**.
- Actual Questions displays **6 問**.
- Overflow Units displays **23 問分**.

---

### TC-46-02 Count updates when a matrix question is edited to reduce columns

**Pre-conditions:** TC-46-01 has been run; survey is in the detail view.

**Steps:**
1. Navigate to questionnaire edit.
2. Edit the first question (MTS) and reduce the column labels to only 5 columns.
3. Save and return to "Settings complete."

**Expected results:**
- Question Count: **27 問**.
- Actual Questions: **6 問**.
- Overflow Units: **21 問分**.

---

### TC-46-03 Condition-settings screen does not show question-count section for Open surveys

**Pre-conditions:** Survey from TC-46-02.

**Steps:**
1. Click "Condition Settings."
2. Proceed to the first unset condition (order/SF settings).

**Expected results:**
- The text "●質問カウント", "質問数：", "作成制限超過：", and the note "※質問数には質問カウントを自動で設定します。" are **not present** on the condition-settings page.

---

### TC-46-04 Count persists correctly after launching the survey and reverting via version restore

**Pre-conditions:** Survey is running (実査中).

**Steps:**
1. Open the survey's questionnaire for editing.
2. Increase the first question back to 40 column headers and save.
3. Confirm the count increases (expected: 28 問 / 6 問 / 22 問分).
4. Use the version-restore feature (復元) to revert to the previous questionnaire version.

**Expected results after restore:**
- Question Count: **27 問**.
- Actual Questions: **6 問**.
- Overflow Units: **21 問分**.

---

## Test Group 2 — Quick Survey Question Count Display

**Source file:** `質問カウント_作成制限超過質問数_Quick.html`

### TC-46-05 Initial count after building a large Quick survey

**Pre-conditions:**
- Admin account `admin_4003` has access to the Quick survey type.

**Steps:**
1. Log in as `admin_4003`.
2. Create a new Quick survey (PC-only device setting).
3. Add the same sequence of questions as TC-46-01 (MTS, MTM, MTT, FAS with 50 items, RAT).
4. Finalize the questionnaire and navigate to "Settings complete."

**Expected results:**
- Question Count: **27 問** (Quick surveys have one fewer question than the equivalent Open survey in this scenario).
- Actual Questions: **5 問**.
- Overflow Units: **22 問分**.

---

### TC-46-06 Quick survey condition-settings screen shows the question-count breakdown

**Pre-conditions:** Survey from TC-46-05, in condition settings.

**Steps:**
1. On the condition-settings screen, proceed to the first unset condition.

**Expected results:**
- The label shows **27** in the question-count field (`numSfQuestionLable`).
- The breakdown text reads: **(質問数： 5 問　＋　作成制限超過： 22 問分　＝　質問カウント： 27 問)**.
- The note "※質問数には質問カウントを自動で設定します。" is **not present** (count is explicitly stated, not auto-set).

---

### TC-46-07 Count updates after editing down and re-launching the Quick survey

**Pre-conditions:** Quick survey is active (実査中).

**Steps:**
1. Edit the first question to 5 column headers and save.
2. Navigate to condition settings.

**Expected results:**
- Question Count: **25 問**.
- Actual Questions: **5 問**.
- Overflow Units: **20 問分**.
- The breakdown text reads: **(質問数： 5 問　＋　作成制限超過： 20 問分　＝　質問カウント： 25 問)**.

---

### TC-46-08 Second Quick survey — count persists after editing up and restoring

**Pre-conditions:** A second Quick survey with the same structure (TC-46-05 repeated, survey name suffix `_2`).

**Steps:**
1. After initial setup, confirm count is 27 問 / 5 問 / 22 問分.
2. Edit the first question to 40 column headers.
3. Confirm count increases to **26 問 / 5 問 / 21 問分**.
4. Use version-restore to revert.

**Expected results after restore:**
- Question Count: **25 問**.
- Actual Questions: **5 問**.
- Overflow Units: **20 問分**.
