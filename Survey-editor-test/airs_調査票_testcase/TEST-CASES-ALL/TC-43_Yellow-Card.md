# 43 — Yellow Card (イエローカード)

**Total scripts:** 1 test file (498 commands)  
**Purpose:** Verify that low-quality respondents are correctly assigned a "yellow card" penalty based on configurable thresholds, and that the penalty affects their survey participation.

---

## TC-43-01 — Yellow Card Assignment and Threshold Verification

**Scope:** Admin + Monitor  
**Platform:** Desktop

**Scenario:** An administrator configures yellow card rules (thresholds for detecting low-quality responses such as too-fast completion, straight-lining, etc.). Multiple respondent accounts are put through surveys under conditions that trigger the yellow card. The system assigns penalties and the administrator verifies the records.

**Setup:**
- Admin user (ID: admin_50128)
- Multiple monitor (respondent) test accounts
- Survey configured with yellow card detection enabled
- Threshold settings: response time threshold (-1 = any), score threshold (0.05), warning count (3 per group)

**Steps:**
1. Admin logs in and navigates to the yellow card configuration screen.
2. Admin sets detection thresholds (response time, quality score, maximum warnings before penalty).
3. Admin creates or opens a survey designed to trigger yellow card conditions.
4. Upload a CSV of test respondents.
5. Multiple respondents complete the survey under conditions that should trigger the yellow card (e.g., completing too quickly, selecting the same answer repeatedly).
6. Admin reviews the respondent quality report.
7. Admin verifies which respondents received a yellow card and which did not.

**Expected Results:**
- Respondents who meet the penalty threshold are flagged with a yellow card.
- Respondents who do not meet the threshold are not penalized.
- Yellow card records are visible in the admin report.
- Penalized respondents have their participation status updated accordingly.

---
