# 02 — Regression Test Essentials / リグレッションテスト時必須

**Total scripts:** ~192 files  
**Purpose:** Comprehensive regression test suite covering all major survey features. These tests must pass at every release to confirm nothing is broken. Desktop and smartphone variants are included for most scenarios.

---

## TC-02-01 — Overseas Survey (海外調査): Delivery Type Variations

**Scope:** Admin  
**Platform:** Desktop + Smartphone

**Scenario:** An overseas survey is created with each of the three delivery types. Admin configures the survey and verifies the setup is correct.

**Sub-scenarios:**
1. Normal delivery (通常) — standard single-cell delivery
2. Quota allocation delivery (割付) — multiple cells with quota settings
3. Delivery control (配信Ctrl) — custom distribution control rules

**Expected Results:**
- Each delivery type can be configured and saved without error
- Survey detail screen shows the correct delivery type settings

---

## TC-02-02 — Panel Supply Survey (パネル提供用調査): Delivery Types and Points

**Scope:** Admin  
**Platform:** Desktop + Smartphone

**Scenario:** A panel supply survey (for third-party panel delivery) is configured and verified across all delivery types, plus point award configuration.

**Sub-scenarios:**
1. Normal delivery (通常)
2. Quota allocation (割付)
3. Delivery control (配信Ctrl)
4. Point award confirmation — verify that awarded points are configured and displayed correctly on the survey detail screen

**Expected Results:**
- Panel supply surveys can be created with all delivery types
- Point award amounts display correctly after configuration

---

## TC-02-03 — Open Survey: URL Parameters and Thanks Screen Customization

**Scope:** Admin  
**Platform:** Desktop + Smartphone

**Scenario:** An Open-type survey uses URL parameters passed from the external panel system to pre-fill respondent data. Thanks screen shows inserted answers.

**Sub-scenarios:**
1. Single parameter — one parameter passed via URL is stored and displayed correctly
2. Multiple parameters — several parameters in URL are all stored correctly
3. Thanks screen answer insertion — selected answer text appears on the thanks page

**Expected Results:**
- URL parameters are captured and stored with the response record
- Thanks screen dynamically displays the respondent's selected answer text

---

## TC-02-04 — Survey Reuse and Question Copy

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An existing survey is reused (流用) or individual questions are copied between surveys.

**Sub-scenarios:**
1. Custom survey reuse (調査票流用_カスタム) — create a new survey from an existing custom-type survey
2. Question copy (質問コピー) — copy one or more questions from one survey to another

**Expected Results:**
- Reused survey correctly inherits questions, logic, and settings from the source
- Copied questions maintain their original configuration (type, choices, logic references)

---

## TC-02-05 — Screening Out: Client and Internal Configurations

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Screening Out (SCR) is configured from both the client side and the internal (admin) side, for Quick and Open survey types.

**Sub-scenarios:**
1. Client SCR — Quick survey: client sets an SCR condition; respondent is screened out when matched
2. Client SCR — Open survey: same as above but Open type
3. Internal SCR — Quick survey: admin sets SCR condition; behavior verified
4. Client SCR — Screening survey type

**Expected Results:**
- SCR condition triggers correctly regardless of who configured it (client or internal)
- Screened-out respondent sees the SCR page and does not complete the survey

---

## TC-02-06 — Sub-Question Select Batch Configuration

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The "sub-question select batch setting" (副質問セレクト一括設定) allows configuring multiple subQuestionSelect logic rules at once across choices, sub-questions, or matrix questions.

**Sub-scenarios:**
1. Batch configuration for choices (選択肢) — apply subQuestionSelect to multiple choice-based references at once
2. Batch configuration for sub-questions (副質問) — configure multiple sub-question references at once
3. Batch configuration for matrix questions (マトリクス) — apply across matrix rows/columns at once

**Expected Results:**
- Batch configuration saves all selected rules without individual confirmation steps
- All configured rules are applied and visible in the logic settings

---

## TC-02-07 — Count Limit Checks / 制限数チェック

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Various maximum count limits are verified — cells, questions, choices, and AC (auto-code) questions.

**Sub-scenarios:**
1. Quota allocation limit — Quick survey: maximum number of cells cannot be exceeded
2. Quota allocation limit — Open survey: same for Open type
3. Question count limit — maximum number of questions per survey is enforced
4. Choice count limit — maximum number of choices per question is enforced
5. AC question count limit — specific limit for auto-code question types

**Expected Results:**
- Adding beyond the limit produces an appropriate error or prevents the action
- Counts at the limit are accepted without error

---

## TC-02-08 — Permission / Visibility by Role

**Scope:** Admin / Client  
**Platform:** Desktop

**Scenario:** Different user roles (RD, SRD, customized, standard client) see different UI elements and input fields. Verify that each role's view matches its permission level.

**Sub-scenarios:**
1. RD / SRD roles — verify which input fields and actions are visible/editable
2. Customized role — verify custom permission set is respected
3. Custom (カスタム) role — verify UI elements specific to this role
4. Client role — verify limited view appropriate for client users

**Expected Results:**
- Each role sees only the fields and actions they are permitted to access
- Unauthorized actions are not visible or are grayed out

---

## TC-02-09 — Category Configuration (カテゴリ設定)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A survey category is registered and assigned to a survey.

**Steps:**
1. Open the category management screen.
2. Register a new category name.
3. Assign the category to a survey.
4. Verify the category appears on the survey detail screen.

**Expected Results:**
- Category is created and saved without error
- Survey detail screen shows the correct assigned category

---

## TC-02-10 — Question Type Addition: CCR (コンベンショナル回答方式 / CCR Type)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A new CCR-type question is added to a survey. This question type is used for conventional response format (pre-coded answer entry).

**Steps:**
1. Create a survey with a CCR-type question.
2. Configure choices and required settings.
3. Save and preview.

**Expected Results:**
- CCR question is created and saved without error
- Preview displays the question in the correct conventional response format

---

## TC-02-11 — Preview: Condition Expression Compression

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** When a survey has complex conditional logic, the preview screen displays a compressed (abbreviated) version of the condition expressions for readability.

**Steps:**
1. Create a survey with multiple complex logic conditions.
2. Open the preview screen.
3. Verify that long condition expressions are compressed/abbreviated in the preview.

**Expected Results:**
- Long condition expressions are shortened in the preview display
- The compression does not affect actual logic evaluation

---

## TC-02-12 — Original Tags Combined with Logic

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Custom tags (answer, copy, if, etc.) are used in combination with logic features (questionSelect, choiceSelect, etc.) to verify they work together without conflict.

**Steps:**
1. Create a survey with an `<answer>` tag in a question that also has a questionSelect condition.
2. Create another with a `<copy>` tag and choiceSelect logic.
3. Answer the survey in ways that trigger and suppress each logic condition.

**Expected Results:**
- Tags render correctly even when logic is active
- Logic behavior is not affected by the presence of tags

---

## TC-02-13 — Monitor Alert (モニターアラート)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The monitor alert feature notifies an administrator when a respondent (monitor) has been inactive or shows abnormal behavior. Two test scripts verify alert configuration and trigger.

**Sub-scenarios:**
1. Alert configuration — set up a monitor alert threshold and verify settings are saved
2. Alert triggering — simulate conditions that trigger the alert; verify alert appears

**Expected Results:**
- Monitor alert is configurable with correct threshold values
- Alert is triggered and displayed when conditions are met

---

## TC-02-14 — Quota Select Condition Configuration (割付セレクト条件設定)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A survey with quota allocation (割付) uses condition-based cell selection (割付セレクト). The condition determines which cell a respondent is assigned to based on their answers.

**Steps:**
1. Create a multi-cell survey with quota allocation.
2. Configure a quota select condition (e.g., assign to Cell 1 if Q1=1, Cell 2 if Q1=2).
3. Save the configuration.
4. Verify the condition is displayed correctly in the settings.

**Expected Results:**
- Quota select condition saves and displays correctly
- Condition logic is shown in the correct format

---

## TC-02-15 — Branch Preview (分岐プレビュー)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The branch preview feature shows an administrator all possible answer paths through a survey based on its logic. Tests verify various configurations.

**Sub-scenarios:**
1. Branch preview with internal SCR and back button enabled
2. Branch preview without internal SCR
3. Branch preview with piping and select conditions combined, back button enabled
4. Branch preview for a screening-referenced survey

**Expected Results:**
- Branch preview correctly represents all answer paths
- Internal SCR end points are shown separately from normal completion paths

---

## TC-02-16 — FA Input Field Selection Check

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** FA (free answer) input fields with selection (dropdown) behavior are verified for correct display and input capture.

**Steps:**
1. Create a question with FA input field selection enabled.
2. Answer the survey using the FA selection dropdown.
3. Verify the selected value is recorded correctly.

**Expected Results:**
- FA selection dropdown displays correctly
- Selected value is stored in TEXT or VALUE as expected

---

## TC-02-17 — AIP Coordinator Survey Creation (AIP担当者調査票作成)

**Scope:** Admin (AIP role)  
**Platform:** Desktop

**Scenario:** A user with AIP coordinator role creates a survey. Verify the AIP-specific workflow and any AIP-specific options are available.

**Expected Results:**
- AIP coordinator can create and configure a survey within their role's permissions
- AIP-specific configuration options are visible and functional

---

## TC-02-18 — Integrated Survey (一体型調査票)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** An integrated survey combines the screening phase and the main survey in a single flow. Tests verify the admin setup and respondent experience.

**Sub-scenarios:**
1. Admin creates integrated survey (admin01 setup)
2. Respondent answers integrated survey
3. Admin completes post-response configuration (admin02)

**Expected Results:**
- Screening and main survey are presented as a single continuous flow
- Screening result correctly gates entry into the main survey portion

---

## TC-02-19 — Screening-Referenced Survey (スクリーニング回答参照型調査票)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** A survey references answers given during a prior screening survey. The referenced answers are used to pre-fill or conditionally display content in the main survey.

**Sub-scenarios:**
1. Open survey with screening reference — scenario 1
2. Open survey with screening reference — scenario 2
3. Quick survey with screening reference — scenario 1
4. Quick survey with screening reference — scenario 2

**Expected Results:**
- Prior screening answers are correctly accessible in the main survey
- Conditional logic using referenced answers evaluates correctly

---

## TC-02-20 — Choice Group Randomization (グループランダマイズ)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Choices are organized into groups, and the groups are displayed in random order (the choices within each group maintain their relative order).

**Sub-scenarios:**
1. Group randomization setup — configure groups and verify the configuration is saved
2. Group randomization at answer time — verify groups appear in randomized order; choices within each group maintain their order

**Expected Results:**
- Groups are randomized correctly
- Individual choice order within each group is preserved
- Answer data records original choice numbers regardless of display order

---

## TC-02-21 — Answer Back Button

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** When the "Back" button is enabled, respondents can return to a previous question. Tests verify behavior under various survey conditions.

**Sub-scenarios:**
1. Page break present (改ページ有) — back button navigates to the previous page
2. No page break (改ページ無) — back button navigates to previous question on same page
3. Internal SCR present — back button behavior when SCR would have triggered
4. Integrated survey (一体型) — back button behavior in combined screening + main flow

**Expected Results:**
- Back button returns respondents to the correct previous state
- Previously entered answers are restored when returning
- SCR interaction does not cause invalid states when navigating back

---

## TC-02-22 — Approval and Preview Display Verification

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The approval and preview screens correctly display all question types and logic features. Tests verify display accuracy for base surveys and surveys with select conditions.

**Sub-scenarios:**
1. Base survey — all question types displayed correctly
2. Survey with choice select (選択肢セレクト) — select conditions reflected in preview
3. Survey with column select (表頭セレクト) — matrix column select shown
4. Survey with IF tags — conditional text visible in preview

**Expected Results:**
- All question types render correctly in approval/preview view
- Logic-driven changes (select conditions, IF tags) are reflected in the preview

---

## TC-02-23 — Mid-Survey Save (途中保存)

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** A respondent partially completes a Quick survey and saves their progress. Later, they resume from where they left off.

**Sub-scenarios:**
1. Manual save — Quick survey respondent manually saves mid-way
2. Auto-save scenario (variant 02)
3. Resume and continue (variant 03)
4. Save then delete and restart (variant 04)
5. Edge case — save at final question (variant 05)

**Expected Results:**
- Saved progress is correctly stored and retrievable
- Resumption starts from the correct position
- All previous answers are preserved after resumption

---

## TC-02-24 — Survey Title Input Validation

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The survey title field enforces length and character restrictions.

**Steps:**
1. Enter a title that is too long (exceeds character limit).
2. Enter a title with special characters.
3. Enter a valid title within the allowed length.

**Expected Results:**
- Overly long titles produce error messages
- Valid titles save without error

---

## TC-02-25 — Conventional-Format Recruitment Survey (コンベンショナル向け募集型)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Recruitment-type surveys for conventional (CCR) response format are tested — both with and without external survey links.

**Sub-scenarios:**
1. Conventional recruitment survey — non-external survey (外部調査票以外)
2. Conventional recruitment survey — with external survey link (外部調査票)

**Expected Results:**
- Recruitment surveys of conventional type are created correctly
- External survey link integration works as expected

---

## TC-02-26 — Horizontal Choice Layout (選択肢方向_横方向回答)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Choices can be displayed horizontally (left to right) instead of vertically (top to bottom). Tests verify the horizontal layout renders and answers correctly.

**Sub-scenarios:**
1. Horizontal layout — variant 01
2. Horizontal layout — variant 02

**Expected Results:**
- Choices display in horizontal layout when configured
- Answer data records the correct choice regardless of display direction

---

## TC-02-27 — Large Survey (大規模調査票)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A large survey with many questions (near or at the maximum) is created and handled without performance issues.

**Steps:**
1. Create a survey with a large number of questions.
2. Save the survey.
3. Open the editor for the large survey.
4. Verify the editor loads and responds within acceptable time.

**Expected Results:**
- Large surveys save without timeout errors
- Editor loads and remains functional for large surveys

---

## TC-02-28 — Comment Questions with JavaScript (コメント質問Javascript)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Comment questions (Note type, display-only) include JavaScript-based interactive elements that are verified for correct functionality.

**Sub-scenarios:**
1. Comment question with JavaScript — variant 1
2. Comment question with JavaScript — variant 2

**Expected Results:**
- JavaScript embedded in comment questions executes correctly in the respondent view
- No JavaScript errors occur in the browser console

---

## TC-02-29 — Button and Text Visibility Hiding (ボタンとテキストの非表示化)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** Certain buttons or text blocks can be hidden from respondents via configuration. Tests verify hide/show behavior.

**Steps:**
1. Configure a survey to hide specific buttons or text elements.
2. Preview as a respondent.
3. Verify hidden elements do not appear.

**Expected Results:**
- Configured hidden elements are not visible to respondents
- Non-hidden elements continue to display correctly

---

## TC-02-30 — MEMBERS Survey Type (MEMBERS調査票種別)

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** A survey designated for the MEMBERS platform is created and configured. MEMBERS-specific settings are verified.

**Steps:**
1. Create a MEMBERS-type survey.
2. Configure MEMBERS-specific settings.
3. Verify the survey detail screen shows the correct MEMBERS configuration.

**Expected Results:**
- MEMBERS survey type is selectable and saves correctly
- MEMBERS-specific fields and settings are available and function correctly

---

## TC-02-31 — Same User Duplicate Check (同一ユーザチェック)

**Scope:** Respondent  
**Platform:** Desktop

**Scenario:** The system prevents the same user from submitting duplicate responses to a survey that has duplicate-check enabled.

**Steps:**
1. Create a survey with same-user duplicate check enabled.
2. First respondent submits successfully.
3. Same respondent attempts to answer again.
4. Verify the second attempt is rejected.

**Expected Results:**
- First submission is accepted normally
- Second attempt by the same user is blocked with an appropriate error/message

---
