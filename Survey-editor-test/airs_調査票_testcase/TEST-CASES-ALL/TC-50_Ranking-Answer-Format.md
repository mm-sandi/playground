# 50 — Ranking Display Formats (順位回答（回答形式）)

**Total scripts:** 7 test files (in `selenium/` subfolder)  
**Purpose:** Verify that the ranking question (RNK) supports multiple display formats and product-type variants, and that answer validation and preview work correctly for each.

---

## TC-50-01 — Ranking Display Format Variants in Preview

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator creates ranking questions using each available display format (e.g., dropdown list, radio buttons, drag-and-drop) and previews each. The preview must render each format correctly and distinctly.

**Setup:**
- Admin user (ID: admin_4001)
- Ranking questions configured with each display format option

**Steps:**
1. Admin creates a ranking question.
2. Admin selects each display format one by one and previews.
3. Admin verifies each format renders differently in the preview.

**Expected Results:**
- All display formats render in preview without errors.
- Each format looks visually distinct.

---

## TC-50-02 — Ranking Product-Type Preview Display

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Ranking questions can be configured with a "product type" (商品種別) that changes how items are displayed (e.g., with images or special layouts). This test verifies the product-type setting affects the preview correctly across Quick, Screening, and Open survey types.

**Setup:**
- Admin user
- Surveys of types: Quick, Screening, Open
- Ranking question with product-type setting enabled

**Steps:**
1. Admin creates ranking questions with product-type setting in Quick, Screening, and Open surveys.
2. Admin previews each.
3. Admin verifies the product-type layout is applied correctly.

**Expected Results:**
- Product-type layout is applied consistently across all survey types.

---

## TC-50-03 — Ranking with Page Break (Branch Preview)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A ranking question is placed on one page and a follow-up question references the ranking result (via branching/piping). Preview verifies the branch condition works.

**Setup:**
- Admin user
- Multi-page survey with ranking on page 1 and branch condition on page 2

**Steps:**
1. Admin creates survey with ranking question on page 1.
2. Admin adds page break and a follow-up question with condition based on ranking answer.
3. Admin previews the flow.

**Expected Results:**
- Branch condition based on ranking answer evaluates correctly in preview.

---

## TC-50-04 — Ranking Required-Count Setting Confirmation

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Verifies that the ranking question's required-rank-count setting (all required, first N required) is saved and displayed correctly in preview.

**Setup:**
- Admin user
- Ranking questions with various required-count settings

**Steps:**
1. Admin configures ranking question with "all required" setting.
2. Admin previews — verifies required indicator shown.
3. Admin changes to "first N required" and previews.
4. Admin verifies correct indicator text.

**Expected Results:**
- Required-count indicators display correctly for all modes.

---

## TC-50-05 — Ranking Answer Flow: Survey Creation + Monitor Response

**Scope:** Admin + Monitor  
**Platform:** Desktop

**Scenario:** End-to-end test: admin creates a survey with a ranking question, respondent completes it, and answer data is verified.

**Setup:**
- Admin user (ID: admin_4001)
- Monitor test account
- Survey with ranking question, multiple display formats

**Steps:**
1. Admin creates survey with ranking question.
2. Respondent logs in, opens survey, and ranks the items.
3. Respondent submits.
4. Admin verifies answer data is recorded correctly.

**Expected Results:**
- Respondent can rank items in the configured format.
- Submitted rankings are saved correctly.

---

## TC-50-06 — Ranking Display Format Description Text

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Verifies that the description text for each ranking display format (shown to respondents as instructions) displays correctly in the survey.

**Setup:**
- Admin user
- Ranking questions with format description text enabled

**Steps:**
1. Admin enables format description text on a ranking question.
2. Admin previews.
3. Admin verifies description text appears above the ranking input.

**Expected Results:**
- Format description text is visible and correct in preview.

---

## TC-50-07 — Ranking Question Edit Confirmation

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Verifies that after a ranking question is saved, reopening the question editor shows all previously configured settings (format, required count, items) without any loss.

**Setup:**
- Admin user
- Ranking question already saved with specific settings

**Steps:**
1. Admin opens an existing ranking question for editing.
2. Admin verifies all settings (format, required count, items) are retained.
3. Admin makes a minor change and saves again.
4. Admin reopens and verifies the change was saved.

**Expected Results:**
- All ranking question settings persist after save and reopen.

---
