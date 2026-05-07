# 01 — Release Smoke Tests (リリース時動作確認)

**Total scripts:** 120 test HTML files (excluding TestSuite\_ and suiteFile\_ wrappers), grouped into **20 test case groups**  
**Purpose:** Run before every release to verify core survey-builder features still work end-to-end across admin, client, and respondent (monitor) roles.

---

## TC-01 — Full Questionnaire Creation and Response (All Question Types)

**Scope:** Admin + Monitor  
**Platform:** Desktop + Smartphone

**Scenario:** An administrator creates a new survey containing every supported question type (single-choice radio, multi-choice checkbox, pulldown, scale, matrix single, matrix multi, matrix bipolar, free-text long, free-text multi-row, ratio, and ranking). A respondent then logs in, finds the survey, and submits answers to each question page by page, ending with a thank-you confirmation.

**Setup:**
- Admin user (ID 4001) with access to the survey builder
- Monitor (respondent) test account: test\_m2@airs.macromill.com
- Survey named `ECONE_TEST_[today]_01`

**Steps:**
1. Admin logs in to the survey builder and creates a new survey with today's date in the name.
2. Admin adds one question of each of the 11 supported question types (SAR, MAC, SAP, SAS, MTS, MTM, MTT, FAL, FAS, RAT, RNK), configuring question text and previewing each before moving to the next.
3. Admin marks certain questions as containing personal information (個人情報).
4. Admin finalizes the questionnaire.
5. Respondent logs in to the monitor portal (desktop or smartphone), locates the survey by today's date, and opens it.
6. Respondent answers each question — selecting choices, entering free text, ranking items — and clicks "Next" on each page.
7. Respondent clicks "Submit" (finishButton) on the final page.

**Expected Results:**
- All question types are saved and displayed correctly during preview.
- The respondent can answer every question type without errors.
- The thank-you message ("ご協力ありがとうございました") appears after submission.
- The respondent can return to their My Page (link present).

---

## TC-02 — Logic Check: Routing and Display (RD Logic)

**Scope:** Admin + Monitor  
**Platform:** Desktop + Smartphone

**Scenario:** An administrator builds a survey that uses multiple display-logic features: question selection (セレクト), forward piping (パイピング), reverse piping (逆パイピング), and matrix-answer piping. A respondent completes the survey and the automation verifies that skipped questions do not appear, and piped choices match earlier answers exactly.

**Setup:**
- Admin user with survey builder access
- Monitor test account: test\_m2@airs.macromill.com
- Survey named `ECONE_TEST_[today]_02`

**Steps:**
1. Admin creates a new survey and adds questions configured for: selection source/destination, forward piping source/destination, reverse piping source/destination, and matrix-answer piping source/destination.
2. Admin sets each question to "not required" and saves the survey.
3. Respondent logs in, finds the survey, and starts responding.
4. Respondent selects choice "3" (C) on Q1.
5. On subsequent pages, the automation checks that Q2 (a skipped question) is absent, and that Q4's displayed choices match exactly what was selected in Q3 (piping).
6. Respondent continues through all pages, selecting choices that were piped from earlier answers.
7. Respondent submits the survey.

**Expected Results:**
- Skipped questions (controlled by selection logic) do not appear.
- Piped choices in downstream questions match the selected answers from upstream questions.
- Reverse-piped choices display only those NOT selected earlier.
- Matrix-answer piped labels appear correctly in the destination question.
- The thank-you message is shown after submission.

---

## TC-03 — Logic Check: Randomization

**Scope:** Admin + Monitor  
**Platform:** Desktop + Smartphone

**Scenario:** An administrator sets up a survey with choice randomization, matrix header/row randomization, question-block randomization, grouped-choice randomization, an uploaded image question, a CM (commercial media) question, and a J-Stream video requirement. A respondent answers the survey, and the test confirms the survey completes successfully.

**Setup:**
- Admin user with access to the survey builder and a local upload folder containing test image files (`03_01_UploadFile.jpg`)
- Monitor test account: test\_m2@airs.macromill.com
- Survey named `ECONE_TEST_[today]_03`

**Steps:**
1. Admin creates a survey and adds questions with: choice randomization (選択肢ランダマイズ), matrix row/header randomization (表頭・表側ランダマイズ), question-block randomization (質問ランダマイズ1/2), an image upload embedded in a question, a Flash CM question, a J-Stream video question with mandatory viewing time, and a grouped-choice randomization question.
2. Admin configures J-Stream viewing requirements (mandatory viewing time of 10 seconds, group number set).
3. Admin saves the survey.
4. Respondent logs in, finds the survey, answers all questions (selecting fourth/last choices, filling free-text fields), and submits.

**Expected Results:**
- All randomization settings are accepted without error.
- Image upload succeeds and the image is embedded in the question.
- J-Stream CM settings are saved.
- Respondent can complete and submit the survey.
- Thank-you message appears; respondent can return to My Page.

---

## TC-04 — OPEN Survey Creation and Response

**Scope:** Admin  
**Platform:** Desktop + Smartphone

**Scenario:** An administrator creates an OPEN-type survey (one that can be accessed via a direct URL without a monitor panel login), adds a main question and multiple attribute (profile) questions of different types, configures delivery cells, and then simulates a respondent completing the survey by opening the URL with a URL parameter.

**Setup:**
- Admin user with access to the survey builder
- Survey named `ECONE_TEST_[today]_04` (desktop) or `[Smart]ECONE_TEST_[today]_04` (smartphone)

**Steps:**
1. Admin selects "Open" survey type from the My Page and creates a new survey.
2. Admin adds a main question (SAR type, marked as personal information).
3. Admin adds attribute questions: SAR, MAC, SAP, ID (with URL parameter binding and repeat-answer enabled), FAS, TEL, and ZIP types.
4. Admin finalizes attribute questions and configures delivery conditions (sets order ID, disables same-user check).
5. Admin configures additional delivery cells.
6. Admin searches for the survey and retrieves the OPEN survey URL.
7. Admin opens the URL with an appended URL parameter (`&param=test1`).
8. Respondent answers the main question (choosing option 4 with a free-text "その他" entry).
9. Respondent fills in all attribute fields (name, email, gender, age, postal code, prefecture, address, phone, etc.) and submits.

**Expected Results:**
- The OPEN survey URL is accessible without a monitor panel login.
- All attribute question types are displayed and can be filled.
- Submission shows the thank-you message ("ご協力ありがとうございました").

---

## TC-05 — Survey Reuse (Questionnaire Copy)

**Scope:** Admin + Monitor

**Scenario:** An administrator duplicates an existing survey (from TC-02's survey) to create a new one, imports questions from another existing survey (TC-01) using the question database, reconfigures delivery conditions including uploading a monitor CSV file, and verifies that respondents see correct logic (including a question skipped for user 1 but present for user 2) when they answer the reused survey.

**Setup:**
- Admin user with access to the survey builder
- Existing surveys from TC-01 and TC-02 must exist
- A `monitor.csv` file for uploading respondent cell assignments
- Survey named `ECONE_TEST_[today]_05`

**Steps:**
1. Admin searches for the TC-02 survey, selects it, and initiates a copy (流用).
2. Admin renames the copy to today's TC-05 name.
3. Admin opens the question database, searches for TC-01's survey, selects all 11 questions (Q1–Q11), and imports them.
4. Admin finalizes question settings and enables "apply to all" (allChange).
5. Admin configures delivery: sets order ID, disables same-user check, changes delivery method, uploads monitor CSV, and sets sample count.
6. Multiple respondents log in and answer the survey; the automation verifies that piped choices, skipped questions, and filtered options behave correctly according to each respondent's prior answers.

**Expected Results:**
- The copied survey is created successfully with imported questions.
- All logic from the original survey is preserved.
- Delivery conditions (CSV upload, cell settings) are saved without error.
- Respondents see the correct questions and logic based on their previous answers.

---

## TC-06 — Client User: OPEN Survey Workflow

**Scope:** Client + Admin

**Scenario:** A client user logs in to the client portal and creates an OPEN-type survey with a conditional display rule (showing a "SELECTED SAR" question only when certain answers to Q1 are given). The client applies the survey and submits it for review. An admin then processes the survey: configures delivery conditions, cell criteria, email notification settings, confirms the survey, and activates it.

**Setup:**
- Client user: CR4UKPQX with password "password"
- Admin user: admin\_4001 with admin access
- Survey named `ECONE_TEST_[today]_06_02`

**Steps:**
1. Client logs in to the client portal, selects "Open" survey type, and creates a new survey.
2. Client adds a SAR question (Q1) and a "SELECTED SAR" question whose display is conditional on Q1 answers 1 and 2.
3. Client adds an attribute question (SAR type) and finalizes the questionnaire.
4. Client sets sample count to 100 and submits the survey application.
5. Client logs out.
6. Admin logs in, finds the survey, edits it, marks all cells as changed, and verifies status is "確認中".
7. Admin configures delivery: sets order ID, disables same-user check, adds redirect URLs (before start and after finish), and saves.
8. Admin configures cell criteria (based on Q1 answer range 1–3), sets sample count to 2, and recalculates.
9. Admin configures email notification (turns off client email sending).
10. Admin configures attribute output conditions and finalizes setup.
11. Admin confirms the survey start.

**Expected Results:**
- Client can create and submit an OPEN survey with conditional question logic.
- Admin can configure all delivery and cell settings without error.
- Survey status progresses correctly from "確認中" to "開始確認待ち".

---

## TC-07 — Client User: Quick Survey Workflow with Respondent Answers

**Scope:** Client + Admin + Monitor

**Scenario:** A client creates a Quick-type survey (a simplified survey type for rapid deployment) with a conditional question, sets the sample count, and submits it. An admin then processes it — configures delivery with two cells from uploaded text files, sets answer-time validation, and activates the survey. Two different respondents then answer the survey from the monitor portal.

**Setup:**
- Client user: CR4UKPQX
- Admin user: admin\_4001
- Two monitor users: test\_m1 and test\_m2
- Two cell files: file1.txt and file2.txt
- Survey named `ECONE_TEST_[today]_07`

**Steps:**
1. Client creates a Quick survey with a SAR question (Q1) and a "SELECTED SAR" question (Q2) shown conditionally based on Q1 answers.
2. Client sets sample count to 100 and submits the application.
3. Client logs out.
4. Admin finds the survey, edits questionnaire to mark all cells changed, verifies status is "確認中".
5. Admin configures delivery: sets order ID, delivery method, point amount (0), collection coefficient (100%), answer-time cleaning enabled.
6. Admin uploads two cell files and sets sample counts of 1 per cell.
7. Admin configures answer-time judgment and attribute-change exclusion settings.
8. Admin activates the survey.
9. Monitor user 1 (test\_m1) logs in, finds the survey, accepts consent, and answers Q1=choice 1 and Q2=choice 1, then submits.
10. Monitor user 2 (test\_m2) logs in, finds the survey, answers Q1=choice 3 (which causes the survey to end immediately due to screening), and submits.

**Expected Results:**
- Client can create a Quick survey and submit for review.
- Admin can configure dual-cell delivery with file uploads without error.
- User 1 completes the full survey and sees the thank-you message.
- User 2 is screened out (Q2 not shown) and still sees the thank-you message.

---

## TC-08 — Screening Survey: Creation and Mid-Survey Edit

**Scope:** Admin

**Scenario:** An admin creates a Screening-type survey (used for pre-qualifying respondents) with multiple question types, runs an initial wave of responses, then temporarily pauses the survey, adds a new question to the questionnaire, adds a second delivery cell by uploading a new file, and restarts the survey. The admin then verifies that the updated questionnaire is correctly displayed to respondents.

**Setup:**
- Admin user with access to the survey builder
- A monitor user (ID 3000001) pre-enrolled in the survey
- A CSV/text file for the second cell
- Survey named `ECONE_TEST_[today]_08`

**Steps:**
1. Admin creates a Screening survey with questions of types SAR, MAC, MTS, MTM, and MTT.
2. Admin finalizes the survey and activates it.
3. After initial responses, admin pauses the survey ("一時終了時修正").
4. Admin adds a new question (rank-type, with 5 answer items) to the questionnaire.
5. Admin finalizes the edited questionnaire and resets the survey status.
6. Admin adds a second delivery cell by uploading a file, sets sample count to 1, recalculates, and restarts the survey.
7. Admin (acting as respondent) opens the survey URL and verifies the original questions are displayed with correct choices.

**Expected Results:**
- The Screening survey is created and activated without error.
- Mid-survey questionnaire editing (adding a question) succeeds.
- A second delivery cell can be added after the survey is paused.
- After restart, the questionnaire displays all original questions with the correct choice text.

---

## TC-09 — Excluded from Aggregation (集計対象外) Setting

**Scope:** Admin  
**Platform:** Desktop + Smartphone

**Scenario:** An admin creates a survey where one question branch is flagged as "excluded from aggregation" (集計対象外). The survey is configured with specific screening criteria so that only respondents meeting a condition are counted. The test verifies that the exclusion flag is set correctly and delivery is configured.

**Setup:**
- Admin user (ID 4001 for smartphone variant, or credential-based for desktop)
- A monitor CSV file for cell upload
- Survey named `ECONE_TEST_[today]_09` or `[Smart]ECONE_TEST_[today]_09`

**Steps:**
1. Admin creates a new survey and adds two questions (one SAR and one MAC type).
2. Admin marks the first question's branch as "excluded from aggregation" (集計対象外チェックボックス).
3. Admin finalizes the questionnaire and records the survey ID.
4. Admin configures delivery: sets order ID, disables same-user check, sets point amount (0), and for the smartphone variant, sets device type to smartphone-only.
5. Admin uploads a monitor CSV for the delivery cell and sets sample count.
6. Admin configures screening criteria (any(Q1, '1')) and enables answer-time judgment and attribute-change exclusion.
7. Admin configures email notification (turns off client email) and finalizes setup.

**Expected Results:**
- The "excluded from aggregation" flag is accepted on the questionnaire.
- Delivery conditions including screening criteria are saved without error.
- The survey is ready for activation.

---

## TC-10 — Image Upload Functionality (All Locations)

**Scope:** Admin

**Scenario:** An administrator verifies that the image upload feature works correctly in all parts of the survey editor: the OPEN survey header/footer editor, the attribute header/footer editor, the survey title/comment editor, and the question editor for each of the 11 question types (SAR, MAC, SAP, SAS, MTS, MTM, MTT, FAL, FAS, RAT, RNK), plus the survey detail page. The test covers single-file upload, named uploads, overwriting an existing file, ZIP file uploads containing multiple images, and tag modification.

**Setup:**
- Admin user with access to the survey builder and a local folder containing: `UploadFile01.jpg`, `UploadFile02.jpg`, `ZipFiles.zip` (containing ZipFile01–03.jpg), `test_bmp.bmp`, `test_gif.gif`, `test_jpg.jpg`, and corresponding HTML tag files
- A separate OPEN survey is created for each upload location (10_01 through 10_16)

**Steps (repeated for each upload location):**
1. Admin creates an OPEN survey and navigates to the target upload area (header/footer editor, attribute editor, title editor, or a specific question-type editor).
2. Admin uploads `UploadFile01.jpg` with border styling — verifies the file tag button appears.
3. Admin uploads `UploadFile02.jpg` with a custom name "ファイルB" and no-border styling — verifies the file tag button appears.
4. Admin uploads `UploadFile01.jpg` again with the name "上書きファイル" to overwrite — verifies the overwrite message is shown.
5. Admin navigates back to the editor and verifies the image tag is present in the text area.
6. Admin clicks the tag button for UploadFile02 and manually edits the tag text, then confirms.
7. Admin uploads `ZipFiles.zip` (no custom name) — verifies all three extracted images (ZipFile01–03.jpg) appear as tags.
8. Admin uploads `ZipFiles.zip` again with name "Zipファイル上書き" and border styling to test overwrite of a ZIP batch.
9. For TC-10-15 only: Admin also tests uploading BMP, GIF, and JPG file types and verifies each generates a correct image tag in the question editor.
10. For TC-10-16 only: Admin accesses the upload feature from the survey detail page (調査明細) instead of the editor.

**Expected Results:**
- Images upload successfully in every supported editor location.
- Overwriting an existing filename updates the tag rather than creating a duplicate.
- ZIP uploads extract and register all contained images.
- Uploaded image tags appear correctly in the text editor after returning from the upload screen.
- BMP, GIF, and JPG formats are all accepted.

---

## TC-11 — Button Operation Check (All Editor Buttons)

**Scope:** Admin

**Scenario:** An administrator creates a survey with a comprehensive set of questions (including piping, randomization, image-embedded, CM-video, and conditional-logic questions) and then systematically tests every button and control in the questionnaire editor: adding, editing, reordering, previewing, copying, and deleting questions, as well as testing all logic/randomization setting controls.

**Setup:**
- Admin user with access to the survey builder
- A local folder with a test image file (`cat.jpg`)
- Survey named `ECONE_TEST_[today]_14_02` (part 1) and `ECONE_TEST_[today]_14_01` (part 2)

**Steps (TC-11-01: Piping and logic buttons):**
1. Admin creates a survey with SAR-type source/destination questions for selection, forward piping, reverse piping, and matrix-answer piping.
2. Admin also adds a free-area input source question.
3. Admin tests setting up piping configurations between questions using the editor buttons.

**Steps (TC-11-02: Randomization and section buttons):**
1. Admin creates a survey with randomization questions, an image-upload question, and a Flash CM question.
2. Admin configures Flash CM settings (URL, access limit, viewing time).
3. Admin tests setting and clearing randomization types (選択肢ランダマイズ, 表頭/表側ランダマイズ, 質問ランダマイズ) using the corresponding editor buttons.
4. Admin tests the section setting button and question-group randomization controls.

**Expected Results:**
- All editor buttons (add, preview, save, delete, copy, reorder) function without error.
- Piping configurations can be set and saved.
- Randomization settings can be applied and cleared.
- CM settings (Flash URL, access limit) are saved correctly.

---

## TC-12 — Input Validation: Admin Survey Editor (運用者側)

**Scope:** Admin

**Scenario:** An administrator verifies that the survey editor enforces all input validation rules: required fields cannot be left blank, and text fields reject input that exceeds their maximum length limits. This covers the survey title/name fields, question text, choice text, and HTML comment fields, tested for SAR (TC-12-01), MTS matrix (TC-12-02), and FAS free-area (TC-12-03) question types.

**Setup:**
- Admin user with access to the survey builder

**Steps:**
1. Admin opens a new survey editor (title page).
2. Admin attempts to save with empty survey name and title — verifies required-field error message appears.
3. Admin enters text that exceeds each field's maximum length (using long Japanese strings and long numeric strings) and tries to save — verifies each field's specific character-limit error message.
4. Admin enters valid-length text that reaches but does not exceed the limit and confirms it is accepted.
5. Admin navigates to the question editor and attempts to save a question with no question text and no choices — verifies required-field errors appear.
6. Admin enters oversized text in question comments, question text, and choice fields — verifies character-limit error messages for each field.
7. Tests are repeated for each question type (SAR in TC-12-01, MTS in TC-12-02, FAS in TC-12-03).

**Expected Results:**
- Submitting blank required fields shows the specific required-field error message for each field.
- Submitting text above the character limit shows the exact limit-exceeded error (e.g., "調査名は半角4000文字以内…").
- Both Japanese (全角) and ASCII (半角) oversized inputs are caught.
- Valid-length inputs are accepted and saved.

---

## TC-13 — Input Validation: Client Survey Editor (クライアント側)

**Scope:** Client

**Scenario:** A client user verifies that the client-facing survey editor enforces the same input validation rules as the admin editor. Part 1 (TC-13-01) tests SAR (radio button) questions; Part 2 (TC-13-02) tests MTT (bipolar matrix) questions, including additional validations for left/right shoulder comments and column/row count limits.

**Setup:**
- Client user: CR4UKPQX

**Steps:**
1. Client logs in and opens a new survey.
2. Client attempts to save with empty name/title fields — verifies required-field errors.
3. Client enters over-length text in name, title, and comment fields — verifies character-limit errors.
4. Client enters valid text and navigates to the question editor.
5. Client attempts to save a question with empty question text and empty choices — verifies required-field errors.
6. Client enters over-length text in question and comment fields — verifies character-limit errors.
7. Client enters a choice that is over 2000 characters — verifies per-choice length error.
8. For TC-13-02 (MTT type): client also verifies that over-length left/right shoulder comments are caught, that column count below 2 or above 200 is rejected, and that item labels (table sides) are required.

**Expected Results:**
- All required-field and character-limit validations work identically for client users as for admin users.
- MTT-specific validations (left/right comments, column count 2–200) are enforced.

---

## TC-14 — Input Validation: Attribute Questions — Admin (属性質問・運用者側)

**Scope:** Admin

**Scenario:** An administrator verifies input validation for attribute (profile) questions in OPEN surveys. Part 1 (TC-14-01) tests the title/header/footer fields; Part 2 (TC-14-02) tests individual attribute question types (SAP pulldown, ID parameter, FAS free-area, etc.).

**Setup:**
- Admin user with access to the OPEN survey builder

**Steps (TC-14-01):**
1. Admin creates an OPEN survey and enters over-limit text in all title/comment fields — verifies character-limit errors for each.
2. Admin enters over-limit text in attribute header/footer HTML fields — verifies errors for header HTML, title HTML, footer HTML, and top/bottom comment fields.

**Steps (TC-14-02):**
1. Admin creates an OPEN survey, deletes the default attribute question, and adds a SAP (pulldown) attribute question.
2. Admin attempts to save with no question text — verifies required-field error.
3. Admin enters over-length question text and annotation text — verifies character-limit errors.
4. Admin tests with full-width Japanese characters to verify the same limits apply.
5. Admin adds additional attribute question types (ID, FAS) and verifies their specific validation rules (e.g., choices required, parameter column setting length limit).

**Expected Results:**
- All attribute question fields have the same validation behavior as regular questionnaire fields.
- Annotations have a stricter limit (200 full-width / 400 half-width characters).
- Blank required fields and oversized inputs are consistently caught.

---

## TC-15 — Input Validation: Attribute Questions — Client (属性質問・クライアント側)

**Scope:** Client

**Scenario:** A client user verifies input validation for attribute questions in their OPEN survey editor, including required fields, character length limits, and minimum choice count for SAR and checkbox-type attribute questions.

**Setup:**
- Client user: CR4UKPQX

**Steps:**
1. Client creates an OPEN survey and navigates to the attribute question editor.
2. Client attempts to save a SAR attribute question with no question text — verifies required-field error.
3. Client enters over-length question text — verifies character-limit error.
4. Client attempts to save with no choices — verifies choices-required error.
5. Client enters a choice that is over 2000 characters — verifies per-choice length error.
6. Client repeats similar steps for a checkbox-type attribute question.

**Expected Results:**
- Required fields and character limits are enforced in the client attribute editor.
- The same error messages shown to admin users appear for client users.

---

## TC-16 — FA Tag Count Limit Check

**Scope:** Admin + Client

**Scenario:** An administrator (with input from a client user) verifies that the system enforces the maximum number of free-answer (FA) tags allowed per question. Questions are created at or near the limit (200 FA tags) and the test confirms that exceeding the limit triggers a validation error.

**Setup:**
- Admin user (admin\_4001) and client user (CR4UKPQX)
- Survey named `ECONE_TEST_[today]_16`

**Steps:**
1. Client logs in and creates a new survey. Admin also logs in.
2. Survey editor is accessed through the client interface.
3. Admin adds a SAR question with exactly 200 FA-tagged choices — confirms it is accepted.
4. Admin adds a MAC question with 99 FA-tagged choices — confirms it is accepted.
5. Admin adds an MTS matrix with 200 FA-tagged rows — confirms it is accepted.
6. Admin adds an MTM matrix with 200 FA-tagged rows — confirms it is accepted.
7. Admin adds an FAS free-area question with 200 FA tags — confirms it is accepted.
8. Admin attempts to add a SAR question with 201 FA-tagged choices — verifies the error "選択肢は2つ以上200以内で設定してください" appears.
9. Admin attempts to add a MAC question with 201 FA tags — verifies the same error.

**Expected Results:**
- Questions with exactly 200 FA tags are accepted without error.
- Questions with 201 FA tags trigger the appropriate limit-exceeded validation error.

---

## TC-17 — Advanced Survey Reuse (Full Question Type Coverage)

**Scope:** Admin

**Scenario:** An administrator creates a comprehensive survey with all major question types (radio, checkbox, pulldown, scale, matrix radio, matrix checkbox, bipolar matrix, long free-text, multi-row free-text, ratio, ranking, and a comment question), then reuses/copies it to verify that all question types and their settings are correctly carried over.

**Setup:**
- Admin user with access to the survey builder
- Survey name uses a date-based identifier `ECONETESTTEMP[today]17`

**Steps:**
1. Admin creates a new survey and adds one question of each of the 12 question types (including a "comment" question type).
2. Each question is given a unique name including the question number (e.g., Q01–Q12).
3. Admin saves and finalizes the survey.
4. The survey is then used as a source for a reuse operation (testing that all 12 question types can be successfully imported into a new survey via the question database).

**Expected Results:**
- All 12 question types are created and saved without error.
- The survey can be used as a source for copying/reuse in subsequent tests.

---

## TC-18 — Duplicate Choice Warning Check

**Scope:** Admin

**Scenario:** An administrator verifies that when a question is saved with duplicate choice text (identical text appearing more than once), the system displays a warning dialog prompting the operator to confirm before proceeding, rather than silently accepting the duplicate choices. This is tested for all applicable question types.

**Setup:**
- Admin user with access to the survey builder
- Survey named `INTEC_TEST_[today]_18`

**Steps:**
1. Admin creates a new survey and adds a SAR question where choices contain duplicates (e.g., "選択肢A", "選択肢B", "選択肢A", "選択肢B").
2. Admin clicks Preview — verifies a confirmation dialog warning about duplicate choices appears.
3. Admin confirms the dialog and continues, then repeats the process for: MAC, SAP, SAS, MTS (duplicate column headers and duplicate row labels), MTM, and MTT question types.

**Expected Results:**
- For every applicable question type, saving with duplicate choice text triggers a warning confirmation dialog.
- After confirming the dialog, the question can still be saved (the warning is non-blocking).
- The test confirms the warning behavior is consistent across all question types.

---

## TC-19 — Custom Logic (カスタムロジック): IF Conditions, Answer Display, and Screen-Out

**Scope:** Admin  
**Platform:** Desktop + Smartphone

**Scenario:** An administrator creates surveys that use the custom logic feature, including: internal screen-out conditions (内部SCRアウト), IF/ELSE conditional text display in question text and choices (using `<if>` tags), answer display tags (`<answer>` tags), and question jump verification. Three script variants cover progressively more complex configurations. A "(ジャンプ確認なし)" variant skips the page-jump verification step.

**Setup:**
- Admin user
- Multiple monitor users (IDs 3000001, 3000002, 3000003)
- Survey groups named `ECONE_TEST_[today]_19_01`, `_19_02`, `_19_03`

**Steps (TC-19-01: Basic custom logic):**
1. Admin creates a survey with 6 questions (4 MAC-type and 2 matrix-type).
2. Admin adds IF-condition logic to the questionnaire.
3. For the smartphone variant, questions are added using the smartphone editing interface.

**Steps (TC-19-02: IF/ELSE tags and answer display):**
1. Admin creates a survey with an internal screen-out question (SQ1: screen out if answers 1–3 are selected).
2. Admin adds questions that use `<if exp="...">` tags in their question text, header comments, and choice labels to show conditional text based on Q1's answer.
3. Admin adds questions that use `<answer no="Q2"/>` tags to display prior answers inline in question text and choices.
4. Admin configures screen-out criteria on the survey level.

**Steps (TC-19-03: Multi-condition screen-out with matrix questions):**
1. Admin creates a survey with screen-out questions including SAR (SQ1), MAC (SQ2), MTS matrix (SQ3), and MTM matrix (SQ4).
2. Admin reorders a screen-out question (moves SQ4 to appear before SQ3).
3. Admin configures internal screen-out rules for SQ2 (yellow card: screen out if answer 1 selected) and SQ3.
4. Admin resets one condition and re-tests.
5. Admin finalizes the survey and opens the preview-all mode to verify question flow.

**Expected Results:**
- Internal screen-out questions are added and conditions are saved correctly.
- Custom logic tags (`<if>`, `<answer>`) are accepted in question text, comments, and choices without validation errors.
- Question reordering in the screen-out section works correctly.
- Yellow-card and regular screen-out conditions are saved and can be reset independently.
- Preview mode opens correctly after finalizing.

---

## TC-20 — Auto-Code (AC) Questionnaire: Creation and Response by Cell

**Scope:** Admin + Monitor  
**Platform:** Desktop + Smartphone

**Scenario:** An administrator creates a survey with an Auto-Code (割付コード / AC) condition block that assigns respondents to different conditions (A, B, C, D) before the main questions. The survey includes a screening question (SQ1) and a comprehensive set of question types (SAR, SAP, SAS, MAC, MTS, MTM, MTT, FAL, FAS, RAT, RNK) all referencing the assigned condition via `<answer no="AC1"/>` tags. Two respondents answer the survey from different cells (cell1 and cell4) and the automation verifies that the correct condition label is shown in each question's header comment.

**Setup:**
- Admin user
- Monitor users: test\_m2 (cell 1) and test\_m5 (cell 4)
- Survey named `AC質問_TEST_[today]_20_01` or `[Smart]AC質問_TEST_[today]_20_01`

**Steps:**
1. Admin creates a new survey and adds an Auto-Code condition block with 3 initial conditions (A, B, C).
2. Admin verifies that an invalid tag in choices triggers the error "選択肢に不正なオリジナルタグがあります."
3. Admin edits the conditions to 4 (A, B, C, D) and confirms valid.
4. Admin adds the main questionnaire questions (Q1 SAR through Q11+ RNK and comment types), each with `AC=<answer no="AC1"/>` in the header comment so respondents see their assigned condition.
5. Admin finalizes the survey and configures delivery cells.
6. Monitor user test\_m2 (cell 1, assigned condition A) answers the screening question, then the main survey pages, verifying that "AC=割付条件A" appears in the header comment of each question, and that piped choices match the AC condition's choices.
7. Monitor user test\_m5 (cell 4, assigned condition D) answers the survey and verifies "AC=割付条件D" appears throughout, with different piped choices.

**Expected Results:**
- The Auto-Code block validates that `<br/>` tags in AC choices are rejected.
- Four AC conditions (A–D) are accepted.
- All question types display the AC answer tag correctly.
- Respondents in different cells see the correct condition label in every question.
- Piped choices (row/column labels sourced from earlier answers) are correctly scoped to each cell's condition.
- Survey completes successfully for both respondents.

---

*Document generated from 71 Selenium RC test scripts in `/Users/kurniawan/Survey-editor-test/airs_testcase/01_リリース時動作確認/`.*
