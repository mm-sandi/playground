# 47 — Back Button Answer State (回答「戻る」ボタン)

**Total scripts:** 4 test files  
**Purpose:** Verify that when a respondent clicks "Back" during a multi-page survey, their previously entered answers are preserved and redisplayed correctly on the previous page.

---

## TC-47-01 — Back Button: Survey Default Setting (Hidden)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator verifies that when a new survey is created, the back button setting defaults to "hidden" (not displayed to respondents). The survey detail screen confirms this default.

**Setup:**
- Admin user (ID: admin_4001)
- New survey named "回答｢戻る｣ボタン_01_[today]"

**Steps:**
1. Admin logs in and creates a new survey.
2. Admin verifies the back button setting defaults to "表示しない" (hidden / do not show).
3. Admin adds one question and saves.
4. Admin finalizes the survey and checks the survey detail page.

**Expected Results:**
- Back button setting is "表示しない" (hidden) by default.
- The setting is visible in the survey detail.

---

## TC-47-02 — Back Button Visible: Client Creates Survey

**Scope:** Monitor (Client)  
**Platform:** Desktop

**Scenario:** A client user (not admin) creates a survey and enables the back button. The survey's condition settings page confirms the back button is set to "表示しない" by default, and the client verifies they can change it.

**Setup:**
- Client user (ID: CR4UKPQX)
- Survey named "回答｢戻る｣ボタン_02_[today]"
- Survey with 100 sample target

**Steps:**
1. Client logs in to the client portal (My Research Page).
2. Client creates a new survey and verifies back button defaults to "表示しない".
3. Client adds a question, saves, and finalizes.
4. Client orders the survey with 100 sample target.
5. Client verifies the survey order confirmation shows "表示しない" for back button.

**Expected Results:**
- Client survey creation shows back button default as "hidden".
- Survey order confirmation reflects the back button setting.

---

## TC-47-03 — Back Button with RAT (Ratio) Question

**Scope:** Monitor (Client)  
**Platform:** Desktop

**Scenario:** A client creates a survey with a RAT (rating/constant-sum) question where totals must equal 100. The back button is enabled. Respondent navigates forward, then clicks back — the entered ratio values must be preserved exactly.

**Setup:**
- Client user (ID: CR4UKPQX)
- Survey with RAT question requiring total = 100
- Back button enabled

**Steps:**
1. Client creates a survey with RAT question (total = 100) and enables back button.
2. Respondent starts the survey and enters values summing to 100 on the RAT question.
3. Respondent proceeds to next page.
4. Respondent clicks "Back" to return to the RAT question page.
5. Respondent verifies the previously entered values are still shown.

**Expected Results:**
- RAT values are preserved after clicking Back.
- Total sum remains at 100.
- No validation error appears on return.

---

## TC-47-04 — Back Button: Admin Creates Survey with Back Enabled

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator explicitly enables the back button on a survey and verifies the setting persists after saving. This confirms the toggle works and saves correctly.

**Setup:**
- Admin user (ID: R837W244, password: password1)
- Survey named "回答｢戻る｣ボタン_04_[today]"

**Steps:**
1. Admin logs in and creates a new survey.
2. Admin explicitly sets the back button to "表示する" (show).
3. Admin adds a question, saves, and finalizes.
4. Admin reopens the survey settings and verifies the back button is still set to "表示する".

**Expected Results:**
- Back button setting is saved correctly as "表示する".
- Setting persists after reopening the survey.

---
