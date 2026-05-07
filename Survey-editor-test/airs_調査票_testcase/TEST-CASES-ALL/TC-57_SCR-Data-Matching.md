# 57 — Screening Data Matching (SCRデータマッチング)

**Total scripts:** 5 test files (in `セレニウム/` subfolder)  
**Purpose:** Verify that screening criteria (profile attributes such as gender, age, region) correctly match between the admin system and respondent panel records, ensuring the right respondents see the right questions.

---

## TC-57-01 — SCR Data Match: Basic Recruitment-Type Survey (No.01)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator creates a recruitment-type (募集型リク) screening survey and verifies that respondent attribute data matches the configured screening conditions. The survey's target URL is validated against the panel system.

**Setup:**
- Admin user (credentials: adminId, adminPass)
- Survey named "SCRデータマッチングテスト_No.01_[today]"
- Survey type: 募集型リク (recruitment type)
- Target URL: panel system URL with respondent/member/client parameters

**Steps:**
1. Admin logs in and creates a new recruitment-type screening survey.
2. Admin configures the target URL with the required parameters (rid, mid, cid, pane).
3. Admin sets the scroll/completion URL.
4. Admin saves the survey configuration.
5. Admin verifies the screening data matches the panel records.

**Expected Results:**
- Screening survey is created with correct type setting.
- Target and completion URLs are saved correctly.
- Respondent attribute data from the panel matches the screening conditions.

---

## TC-57-02 — SCR Data Match: Alternative URL Format (No.02)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Same as TC-57-01 but with a different URL format (xxxx vs xxx path). Verifies the system handles both URL variations for the panel integration.

**Setup:**
- Survey named "SCRデータマッチングテスト_No.02_[today]"
- Different target URL path (xxxx format)

**Steps:**
1. Admin creates a second screening survey with the alternate URL format.
2. Admin saves and verifies configuration.

**Expected Results:**
- System accepts the alternate URL format.
- Data matching works correctly regardless of URL variant.

---

## TC-57-03 — SCR Data Match: Open RID (No.03)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Tests data matching when the respondent ID (RID) is obtained dynamically from the open survey flow. The system stores the RID from the URL and uses it to verify attribute matching.

**Setup:**
- Survey named "SCRデータマッチングテスト_No.03_[today]"
- RID is extracted from survey URL dynamically

**Steps:**
1. Admin creates screening survey that captures the RID from the URL.
2. Admin uses the stored RID to verify respondent attributes match.
3. Admin completes the survey flow.

**Expected Results:**
- RID is correctly captured from the URL.
- Respondent attributes are verified against the captured RID.

---

## TC-57-04 — SCR Data Match: Scenario No.04

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Additional screening data matching scenario covering another combination of attribute conditions and URL configurations.

**Setup:**
- Survey named "SCRデータマッチングテスト_No.04_[today]"

**Steps:**
1. Admin creates and configures a screening survey per the No.04 specification.
2. Admin verifies data matching under this configuration.

**Expected Results:**
- Data matching succeeds for No.04 configuration.

---

## TC-57-05 — SCR Data Match: Scenario No.05

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Final screening data matching scenario, covering edge cases in attribute matching.

**Setup:**
- Survey named "SCRデータマッチングテスト_No.05_[today]"

**Steps:**
1. Admin creates and configures the No.05 screening scenario.
2. Admin verifies data matching.

**Expected Results:**
- Data matching succeeds for No.05 configuration.

---
