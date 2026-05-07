# 39 — Free-Text Invalid Input Check (FA不正回答チェック)

**Total scripts:** 4 test files  
**Purpose:** Verify that prohibited words and invalid input formats entered in free-text (FA) fields are detected and rejected.

---

## TC-39-01 — Register Prohibited Words (Admin Setup)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator registers a list of prohibited words that must be blocked when respondents enter them in free-text answer fields. The test verifies that the word registration UI works correctly and the words are saved.

**Setup:**
- Admin user with system configuration access
- Prohibited word list to register (e.g., "!!!!!Selenium!!!!!", "!!!!!Selenium2!!!!!", "!!!!!Selenium3!!!!!")

**Steps:**
1. Admin logs in to the admin portal.
2. Admin navigates to the prohibited-word registration screen.
3. Admin enters multiple prohibited words one by one and saves each.
4. Admin verifies the words appear in the registered word list.

**Expected Results:**
- All prohibited words are saved successfully.
- The word list displays all registered words.

---

## TC-39-02 — FA Invalid Input Check: Quick Survey

**Scope:** Admin + Monitor  
**Platform:** Desktop

**Scenario:** A Quick survey (panel-targeted) is created with FA (free-text) questions that have validation rules — code-only input, number-only input, and character limits. A respondent attempts to submit prohibited words and invalid formats; the system must reject them.

**Setup:**
- Admin user (ID 50068)
- Survey named "FA不正回答チェック質問設定(Quick)"
- FA questions configured with: code-type input, number-type input, size limits (min=1, max=50)
- Prohibited words registered in TC-39-01

**Steps:**
1. Admin creates a Quick survey with FA questions using `<fa type="code"/>` and `<fa type="number"/>` tags.
2. Admin sets character limits (minimum 1, maximum 50) on FA fields.
3. Respondent logs in and opens the survey.
4. Respondent attempts to enter a prohibited word in an FA field.
5. Respondent attempts to enter letters in a number-type FA field.
6. Respondent attempts to submit with 0 characters in a required FA field.
7. Respondent correctly fills all fields and submits.

**Expected Results:**
- Prohibited word entry is rejected with an error indicator (●).
- Non-numeric input in a number-type field is rejected.
- Empty required FA field blocks submission.
- Valid input submits successfully.

---

## TC-39-03 — FA Invalid Input Check: Screening Survey

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Same as TC-39-02 but using a Screening survey type. Verifies that FA validation and prohibited-word checking apply consistently regardless of survey type.

**Setup:**
- Admin user (ID 50068)
- Screening survey named "FA不正回答チェック質問設定(Scr)"
- FA questions with validation rules and character limits

**Steps:**
1. Admin creates a Screening survey with validated FA questions.
2. Admin configures prohibited-word check and format restrictions.
3. Admin enters test input including a prohibited word ("aaaa" as test value) and valid input.
4. Admin verifies validation responses.

**Expected Results:**
- FA validation rules apply correctly in Screening surveys.
- Prohibited content is flagged appropriately.

---

## TC-39-04 — FA Invalid Input Check: OPEN and External Surveys (Hidden Check)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Verifies that FA invalid-input checking is active but visually hidden on OPEN (public) and externally-linked surveys, where the prohibited-word block still applies server-side even though no visual indicator may appear to respondents.

**Setup:**
- Admin user (ID 50065)
- OPEN survey named "FA不正回答チェック(OPEN)"
- FA questions with input validation

**Steps:**
1. Admin creates an OPEN survey with FA questions.
2. Admin configures prohibited-word check.
3. Admin verifies the survey configuration is saved correctly.
4. Test input including both half-width and full-width characters is entered.

**Expected Results:**
- FA validation is active on OPEN surveys.
- Full-width and half-width characters are handled correctly.
- Prohibited-word check applies even without visual indicator.

---
