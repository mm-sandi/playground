# 61 — FA Tag `quote` Attribute (FAタグのquote属性)

**Total scripts:** 2 test files (admin + monitor)  
**Purpose:** Verify that the `quote` attribute on FA (free-answer) tags correctly pipes user profile data (last name, first name) into question text, including correct handling of empty values, special characters, and quotation mark wrapping.

---

## TC-61-01 — FA Tag `quote` Attribute: Survey Creation and Response

**Scope:** Admin + Monitor  
**Platform:** Desktop

**Scenario:** An administrator creates a survey where a FAS (free-answer short) question uses FA tags with `quote` attributes to pre-fill respondent name fields from profile data (e.g., `<fa quote="lname"/>` for last name, `<fa quote="fname"/>` for first name). A respondent completes the survey and the system verifies that the pre-filled values match the respondent's profile.

**Setup:**
- Admin user (ID: admin_4001)
- Monitor test account with profile data (last name and first name on record)
- Survey named "FAタグのquote属性テスト_[today]_01"
- FAS question with text: `氏名：<fa size="10" quote="lname" /><fa size="10" quote="fname" />`
- Sample size: 1 (upload CSV with 1 monitor)

**Steps — Admin:**
1. Admin logs in and creates a new Quick survey.
2. Admin adds a FAS question with FA tags using the `quote="lname"` and `quote="fname"` attributes to display the respondent's last and first name as pre-filled fields.
3. Admin configures character limits (size=10 for each field).
4. Admin uploads respondent CSV file.
5. Admin sets delivery quantity and saves settings.
6. Admin finalizes and publishes the survey.

**Steps — Monitor (Respondent):**
7. Respondent logs in to the monitor portal.
8. Respondent opens the survey.
9. Respondent verifies the name fields are pre-filled with their profile last name and first name.
10. Respondent confirms the values and submits.

**Expected Results:**
- The FAS question displays the respondent's last name and first name in the correct FA tag positions.
- Pre-filled values match the respondent's registered profile data exactly.
- The respondent can submit without re-entering their name.
- Answer data is recorded correctly.

---
