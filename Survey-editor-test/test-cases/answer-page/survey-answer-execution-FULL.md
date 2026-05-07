# \[DRAFT\] 3. Survey Answer Execution

**Status:** DRAFT              
**Count:** ~730 active cases + ~15 out-of-scope stubs — EX (24), SC (16), FC (25), VA (24), C1/C5 (9), EX-LOGIC (95), V-PAGEBREAK-01–31 (31), V-FA-001–008 (8), V-FAL-001–003 (3), V-RAT-CS-001–007 (7), CM-001–012 (12), C-2LOGIC-073–123 (51), C-QTSEL-001–151 (151), C-QTRAND-001–078 (78), C-MATRIX-COUNT-31–63 (33), C-SCREENING-001–024 (24), C-DISABLED-001–026 (26), C-TXTBOX-001–029 (29), V-REQ-Q-01–13 (13), V-REQ-SQ-01–20 (20), V-SPECN-01–38 (38)      
**Scope:** Runtime answer behavior across all question types and flow patterns      
**Format:** Each case includes: Input Setup → Action → Expected Result

---

## Pipeline Cases (EX-001 – EX-024)

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| EX-001 | Single Choice, One Option Selected, Submit | Single-choice question with 3 options | Select option B → click Submit | Option B is visually selected; Only option B is recorded as selected; Survey advances to the next page or completion screen | |
| EX-002 | Multiple Choice, Multiple Options Selected, Submit | Multiple-choice question with 4 options | Select options A and C → click Submit | Options A and C are both visually selected; Both A and C are recorded; Survey advances | |
| EX-003 | Text Input, Value Entered, Submit | Text input question | Type "Hello World" → click Submit | Input field shows "Hello World"; "Hello World" is recorded; Survey advances | |
| EX-004 | Numeric Input, Valid Number Entered, Submit | Numeric input question | Type "42" → click Submit | Input shows "42"; 42 is recorded as a numeric value; Survey advances | |
| EX-005 | Rating Scale, Middle Value Selected, Submit | Rating scale 1–5 | Select rating 3 → click Submit | Rating 3 is highlighted; 3 is recorded; Survey advances | |
| EX-006 | Dropdown, Option Selected, Submit | Dropdown question with 5 options | Open dropdown → select option D → click Submit | Option D is shown in the dropdown field; Option D is recorded; Survey advances | |
| EX-007 | Matrix Question, All Rows Answered, Submit | Matrix with 3 rows × 4 columns (radio per row) | Select column 2 for row 1, column 4 for row 2, column 1 for row 3 → click Submit | All row selections are visually confirmed; Each row's selection is recorded correctly; Survey advances | |
| EX-008 | Slider, Value Dragged, Submit | Slider question range 0–100 | Drag slider to 75 → click Submit | Slider shows 75; 75 is recorded; Survey advances | |
| EX-009 | Date Input, Valid Date Entered, Submit | Date input question | Enter "2024-06-15" → click Submit | Date field shows 2024-06-15; 2024-06-15 is recorded; Survey advances | |
| EX-010 | Required Question, No Answer, Attempt Submit | Required single-choice question | Click Submit without selecting any option | Validation error is shown ("This field is required" or equivalent); Survey does NOT advance; No answer is recorded | |
| EX-011 | Optional Question, No Answer, Submit | Optional text input question | Leave blank → click Submit | No error is shown; Empty/null is recorded; Survey advances | |
| EX-012 | Multi-page Survey, Answer on Page 1, Go to Page 2 | 2-page survey; page 1 has one question | Answer question on page 1 → click Next | Page 2 is displayed; Answer from page 1 is retained; No data is lost between pages | |
| EX-013 | Multi-page Survey, Back Navigation, Answer Preserved | 2-page survey; answer given on page 1, moved to page 2 | Click Back on page 2 | Page 1 is shown; Previously entered answer is still displayed and retained | |
| EX-014 | Multi-page Survey, Back and Re-answer, Then Submit | 2-page survey | Answer page 1 → go to page 2 → go back → change answer on page 1 → go to page 2 → submit | New answer from page 1 is recorded (not the original); Survey completes successfully | |
| EX-015 | Survey with Logic, Condition Met, Branch Followed | Q1 is single-choice; if "Yes" → go to Q3 (skip Q2) | Select "Yes" on Q1 → click Next | Q2 is skipped; Q3 is displayed; Logic branch executes correctly | |
| EX-016 | Survey with Logic, Condition Not Met, Default Path | Same as EX-015 | Select "No" on Q1 → click Next | Q2 is displayed (not skipped); Normal page order followed | |
| EX-017 | Ranking Question, All Items Ranked, Submit | Ranking question with 4 items | Drag items to order: B, D, A, C → click Submit | Final order B > D > A > C is shown; Order is recorded correctly; Survey advances | |
| EX-018 | Image Choice Question, Image Selected, Submit | Image-choice question with 3 image options | Click on image 2 → click Submit | Image 2 is visually highlighted/selected; Image 2 is recorded; Survey advances | |
| EX-019 | Checkbox Grid, Multiple Cells Selected, Submit | Checkbox grid 3 rows × 3 columns | Check (row1, col2), (row2, col1), (row3, col3) → click Submit | All three checked cells are visually confirmed; All three are recorded; Survey advances | |
| EX-020 | Text Area, Long Text Entered, Submit | Text area with no character limit | Paste 500-character text → click Submit | Full text is displayed in the text area; Full text is recorded; Survey advances | |
| EX-021 | Numeric Input, Value at Minimum Boundary, Submit | Numeric input, min=0, max=100 | Enter "0" → click Submit | 0 is accepted without error; 0 is recorded; Survey advances | |
| EX-022 | Numeric Input, Value at Maximum Boundary, Submit | Numeric input, min=0, max=100 | Enter "100" → click Submit | 100 is accepted without error; 100 is recorded; Survey advances | |
| EX-023 | Numeric Input, Value Below Minimum, Submit | Numeric input, min=0, max=100 | Enter "-1" → click Submit | Validation error shown ("Value must be at least 0" or equivalent); Survey does NOT advance; -1 is NOT recorded | |
| EX-024 | Numeric Input, Value Above Maximum, Submit | Numeric input, min=0, max=100 | Enter "101" → click Submit | Validation error shown ("Value must be at most 100" or equivalent); Survey does NOT advance; 101 is NOT recorded | |

## Screening Cases (SC-001 – SC-020)

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| SC-002 | Screener Question, Disqualifying Answer, Terminated | Screener: "Are you 18 or older?" — "No" → terminate | Respondent answers "No" | Respondent is shown a termination/thank-you screen; Respondent is marked as "Screened Out" (not "Complete"); No further questions are shown | |
| SC-003 | Screener Question, Qualifying Answer, Survey Continues | Same screener as SC-002 | Respondent answers "Yes" | Survey continues to the next question; No termination occurs | |
| SC-004 | Multiple Screener Questions, All Pass | 3 screener questions; all must pass to continue | Respondent answers all qualifying answers | Survey continues past all screeners; No termination | |
| SC-005 | Multiple Screener Questions, First Fails | Same as SC-004 | Respondent fails the first screener | Terminated immediately after the first failure; Questions 2 and 3 are NOT shown | |
| SC-006 | Multiple Screener Questions, Second Fails | Same as SC-004 | Respondent passes Q1, fails Q2 | Q1 is shown and passed; Q2 is shown → respondent fails → terminated; Q3 is NOT shown | |
| SC-007 | Screener Based on Age Range, Boundary: Minimum Age | Screener: age must be 18–65 | Respondent enters age "18" | Respondent passes the screener; Survey continues | |
| SC-008 | Screener Based on Age Range, Boundary: Maximum Age | Same as SC-007 | Respondent enters age "65" | Respondent passes the screener; Survey continues | |
| SC-009 | Screener Based on Age Range, Below Minimum | Same as SC-007 | Respondent enters age "17" | Respondent is terminated/screened out; Survey does NOT continue | |
| SC-010 | Screener Based on Age Range, Above Maximum | Same as SC-007 | Respondent enters age "66" | Respondent is terminated/screened out; Survey does NOT continue | |
| SC-014 | Screen-out Rate Tracking | Survey with screener; 100 respondents attempt, 40 qualify | Track completion vs. screen-out in reporting | Report shows 40 Completes, 60 Screen-outs; Screen-out rate = 60% | |
| SC-015 | Soft Launch Limit, Respondent Count at Limit | Soft launch: limit 50 respondents | 51st respondent attempts to start | Survey is paused/closed for that respondent; Respondent does not enter the survey | |
| SC-016 | Screener with Skip Logic, Disqualify via Logic | Q1: "Do you own a car?" → No → Skip to disqualification page | Respondent answers "No" | Disqualification page is shown; No further survey questions are shown | |
| SC-017 | Duplicate Respondent, Same Panel ID, Attempt Re-entry | Respondent with panel ID "P123" has already completed the survey | Same ID "P123" attempts to re-enter | Respondent is shown an "Already completed" message; No new response is recorded | |
| SC-018 | Expired Survey Link, Access Attempt | Survey has expired (past end date) | Respondent clicks the survey link | "Survey closed" or "Expired" message is shown; No data is collected | |
| SC-019 | Preview Mode, Screen-out Logic Bypassed | Admin previews the survey; screener is configured | Admin answers the disqualifying option | In preview mode, the survey continues (or shows a "You would be screened out" message); No actual screen-out is recorded; Preview data is not counted | |
| SC-020 | Respondent Screened Out Mid-Survey | Screener logic is placed on page 3 (not the first page) | Respondent completes pages 1–2, then hits the screener on page 3 with a disqualifying answer | Respondent is terminated at page 3; Partial answers from pages 1–2 are handled per project configuration (discarded or flagged); Respondent is marked "Screen-out", not "Incomplete" | |

## Flow Control Cases (FC-001 – FC-029)

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| FC-001 | Linear Flow, No Logic, All Pages Sequential | 3-page survey with no branching logic | Answer each page → click Next | Pages appear in order: 1 → 2 → 3 → completion; No pages are skipped or repeated | |
| FC-002 | Skip Logic, Condition Met, Page Skipped | If Q1 = "A" → skip page 2, go to page 3 | Select "A" on Q1 → click Next | Page 2 is not shown; Page 3 is shown directly | |
| FC-003 | Skip Logic, Condition Not Met, No Skip | Same as FC-002 | Select "B" on Q1 → click Next | Page 2 is shown normally; Page 3 follows page 2 | |
| FC-004 | Multiple Conditions, All Met, Branch Executes | Branch logic: if Q1 = "Yes" AND Q2 = "Agree" → go to page 5 | Q1 = "Yes", Q2 = "Agree" → click Next | Survey jumps to page 5; Pages 3 and 4 are skipped | |
| FC-005 | Multiple Conditions, One Not Met, No Branch | Same as FC-004 | Q1 = "Yes", Q2 = "Disagree" | No branch executes; Normal page order continues (page 3 next) | |
| FC-006 | OR Logic, Either Condition Triggers Branch | Branch: if Q1 = "X" OR Q1 = "Y" → go to page 4 | Select "Y" | Branch to page 4 executes; Pages 2 and 3 are skipped | |
| FC-007 | Nested Logic, Inner Condition Inside Outer | If Q1 = "Yes" → check Q2: if Q2 = "A" → go to page 5; else → go to page 3 | Q1 = "Yes", Q2 = "A" | Survey goes to page 5 | |
| FC-008 | Nested Logic, Inner Else Branch | Same as FC-007 | Q1 = "Yes", Q2 = "B" | Survey goes to page 3 | |
| FC-009 | Nested Logic, Outer Condition Not Met | Same as FC-007 | Q1 = "No" | Outer condition not met → default flow continues (page 2 next); Inner condition is never evaluated | |
| FC-013 | Randomized Page Order, Pages Shuffled | Page randomization enabled for pages 2, 3, 4 | 10 respondents complete the survey | Pages 2–4 appear in different orders across respondents; Page 1 and page 5 always appear in fixed positions; All respondents see all pages | |
| FC-014 | Randomized Question Order Within Page | Question randomization enabled on page 2 (Q4, Q5, Q6) | 5 respondents answer page 2 | Q4, Q5, Q6 appear in varying orders across respondents; All 3 questions are always shown | |
| FC-015 | Piped Text, Previous Answer Inserted into Question | Q1 captures respondent's name; Q5 uses piped text: "Thank you, [Q1 ], for your time." | Enter "Yuki" for Q1 → proceed to Q5 | Q5 displays: "Thank you, Yuki, for your time." | |
| FC-016 | Piped Text, Source Question Unanswered | Same as FC-015; Q1 is optional and left blank | Skip Q1 → proceed to Q5 | Q5 displays a fallback or blank substitution (e.g., "Thank you,  , for your time." or "Thank you for your time."); No crash or error | |
| FC-018 | End of Survey, Completion Screen Shown | Linear survey, respondent reaches the last page | Click Submit on last page | Completion/thank-you screen is shown; No further questions are displayed | |
| FC-019 | Terminate Early via Logic, Mid-Survey | Logic: if Q5 = "No" → terminate | Q5 = "No" | Termination screen is shown; No further questions are shown; Response is marked as terminated | |
| FC-020 | Survey URL Parameters, Pre-fill Hidden Question | Survey has hidden field "source" populated from URL param | Open survey with URL: `?source=email` | Hidden field "source" is set to "email"; "email" is recorded without being shown to the respondent | |
| FC-021 | Back Navigation Blocked by Logic | Back button disabled on page 3 (configured) | Respondent tries to navigate back on page 3 | Back button is not shown or is disabled; Respondent cannot return to page 2 | |
| FC-022 | Mandatory Page Completion Before Advance | Page 2 has 2 required questions | Answer only 1 of 2 required questions → click Next | Error shown for the unanswered required question; Survey does NOT advance to page 3 | |
| FC-023 | Display Logic, Question Shown Based on Condition | Q7 is only shown if Q3 = "Yes" | Q3 = "Yes" | Q7 is visible on the page | |
| FC-024 | Display Logic, Question Hidden Based on Condition | Same as FC-023 | Q3 = "No" | Q7 is NOT visible (hidden); Q7 is not required and not recorded | |
| FC-025 | Carry-Forward, Selected Options Piped to Next Question | Q2 (multiple choice: A, B, C, D); Q3 carries forward only selected options from Q2 | Select A and C in Q2 → proceed to Q3 | Q3 shows only options A and C; B and D are not shown in Q3 | |
| FC-026 | Carry-Forward, No Options Selected | Same as FC-025; Q2 is optional | Select nothing in Q2 → proceed to Q3 | Q3 shows no options (empty) or a fallback message; No error/crash | |
| FC-027 | Exclusive Option (None of the Above), Deselects Others | Multiple-choice Q with options A, B, C, and "None of the above" (exclusive) | Select A and B → then select "None of the above" | A and B are deselected automatically; Only "None of the above" is selected; "None of the above" is recorded | |
| FC-028 | Exclusive Option, Selecting Other After Exclusive, Deselects It | Same as FC-027 | Select "None of the above" → then select A | "None of the above" is deselected; A is selected; Only A is recorded | |
| FC-029 | Survey Timeout, Session Expired Mid-Survey | Survey session timeout = 30 minutes; respondent is idle for 31 minutes | Respondent attempts to click Next after timeout | Session expiry message is shown; Respondent is prompted to restart or the survey is closed; Partial data handling follows project configuration | |

## Validation Cases (VA-001 – VA-024)

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| VA-001 | Text Input, Minimum Character Limit, Below Minimum | Text input with min characters = 10 | Enter "Hello" (5 chars) → click Submit | Validation error: "Please enter at least 10 characters"; Survey does NOT advance | |
| VA-002 | Text Input, Minimum Character Limit, At Minimum | Same as VA-001 | Enter "HelloWorld" (10 chars) → click Submit | No error; Survey advances | |
| VA-003 | Text Input, Maximum Character Limit, At Maximum | Text input with max characters = 20 | Enter exactly 20 characters → click Submit | No error; All 20 characters are recorded | |
| VA-004 | Text Input, Maximum Character Limit, Above Maximum | Same as VA-003 | Attempt to type 21 characters | Input is capped at 20 characters (character 21 is not accepted); OR validation error on submit; 21 characters are NOT recorded | |
| VA-005 | Email Input, Valid Email Format | Email input question | Enter "[user@example.com](mailto:user@example.com)" → click Submit | No error; "[user@example.com](mailto:user@example.com)" is recorded | |
| VA-006 | Email Input, Invalid Format | Same as VA-005 | Enter "not-an-email" → click Submit | Validation error: "Please enter a valid email address"; Survey does NOT advance | |
| VA-007 | Numeric Input, Non-numeric Characters | Numeric input question | Enter "abc" → click Submit | Validation error or input is rejected; "abc" is NOT recorded | |
| VA-008 | Numeric Input, Decimal Value When Integer Required | Numeric input, integer only | Enter "3.5" → click Submit | Validation error: "Please enter a whole number"; 3.5 is NOT recorded | |
| VA-009 | Numeric Input, Decimal Value When Decimals Allowed | Numeric input, decimals allowed | Enter "3.5" → click Submit | No error; 3.5 is recorded | |
| VA-010 | Date Input, Valid Date | Date input | Enter "2024-03-15" → click Submit | No error; 2024-03-15 is recorded | |
| VA-011 | Date Input, Invalid Date (Non-existent) | Date input | Enter "2024-02-30" → click Submit | Validation error: "Please enter a valid date"; 2024-02-30 is NOT recorded | |
| VA-012 | Date Input, Future Date When Past Required | Date input with restriction: must be in the past | Enter tomorrow's date → click Submit | Validation error: "Date must be in the past"; Future date is NOT recorded | |
| VA-013 | Date Input, Past Date When Future Required | Date input with restriction: must be in the future | Enter yesterday's date → click Submit | Validation error: "Date must be in the future"; Past date is NOT recorded | |
| VA-014 | Required Matrix, Not All Rows Answered | Matrix question (3 rows), all required | Answer rows 1 and 2, leave row 3 blank → click Submit | Validation error: "Please answer all rows"; Survey does NOT advance | |
| VA-015 | Required Matrix, All Rows Answered | Same as VA-014 | Answer all 3 rows → click Submit | No error; All 3 rows are recorded | |
| VA-016 | Checkbox, Minimum Selections Required | Multiple-choice, minimum 2 selections required | Select only 1 option → click Submit | Validation error: "Please select at least 2 options"; Survey does NOT advance | |
| VA-017 | Checkbox, Minimum Selections Met | Same as VA-016 | Select 2 options → click Submit | No error; Both selections are recorded | |
| VA-018 | Checkbox, Maximum Selections Enforced | Multiple-choice, maximum 3 selections allowed | Attempt to select 4 options | 4th selection is blocked (checkbox becomes unselectable or shows error); Only 3 options are recorded | |
| VA-019 | Phone Number Input, Valid Format | Phone number input, format: 10 digits | Enter "09012345678" (11 digits, valid JP format) or format per locale → click Submit | No error (if format matches configuration); Number is recorded | |
| VA-020 | Phone Number Input, Invalid Format | Same as VA-019 | Enter "1234" (too short) → click Submit | Validation error: "Please enter a valid phone number"; "1234" is NOT recorded | |
| VA-021 | URL Input, Valid URL | URL input question | Enter "[https://example.com"](https://example.com%22) → click Submit | No error; URL is recorded | |
| VA-022 | URL Input, Invalid URL | Same as VA-021 | Enter "not a url" → click Submit | Validation error: "Please enter a valid URL"; Invalid value is NOT recorded | |
| VA-023 | Custom Regex Validation, Pattern Matches | Text input with custom regex: `^[A-Z]{3}- d{4}$` | Enter "ABC-1234" → click Submit | No error; "ABC-1234" is recorded | |
| VA-024 | Custom Regex Validation, Pattern Fails | Same as VA-023 | Enter "abc-123" → click Submit | Validation error: custom error message or "Invalid format"; "abc-123" is NOT recorded | |

## Combination Cases

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| C1-EX-FC-001 | Required Question + Skip Logic | Q1 is required; if Q1 = "Yes" → skip Q2 | Leave Q1 blank → click Next | Validation error for Q1 (required); Skip logic does NOT execute until Q1 is answered | |
| C1-EX-FC-002 | Required Question Answered, Skip Executes |  | Q1 = "Yes" → click Next | Q2 is skipped; Survey advances to Q3 | |
| C1-EX-FC-003 | Multiple Required + Carry-Forward | Q2 (multiple choice, required, min 1 selection); Q3 carries forward Q2's selections | Submit without selecting anything in Q2 | Validation error on Q2; Q3 carry-forward does NOT execute | |
| C1-EX-FC-004 | Carry-Forward with Required Destination |  | Select A and B in Q2 → proceed to Q3 | Q3 shows A and B; Q3 is required → both must be ranked/rated/chosen before advancing | |
| C1-EX-VA-001 | Numeric Validation + Display Logic | Q4 numeric input (1–10); Q5 shown only if Q4 ≥ 7 | Enter "11" (out of range) → click Submit | Validation error on Q4; Display logic for Q5 does NOT evaluate until Q4 is valid | |
| C1-EX-VA-002 | Valid Numeric Triggers Display Logic |  | Enter "8" → click Submit | No error; Q5 becomes visible (condition met) | |
| C1-EX-VA-003 | Valid Numeric Below Threshold, Q5 Hidden |  | Enter "5" → click Submit | No error; Q5 stays hidden | |
| C5-FC-SC-001 | Logic + Screening Interaction | Page 2 screener: if Q3 = "None" → terminate | Q3 = "None" → reach page 2 | Termination executes correctly; Response is marked "Screen-out" | |
| C5-FC-SC-002 | Logic Reroute Avoids Screener | Skip logic routes past the screener page | Condition met → screener page is skipped | Screener page is not shown; Respondent is NOT screened out; Survey continues on the alternate path | |

## EX-LOGIC Test Cases

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| EX-LOGIC-001 | Display Logic, Single Condition, Show | Q5 has display logic: show if Q1 = "Yes" | Q1 = "Yes" → reach the page with Q5 | Q5 is visible | |
| EX-LOGIC-002 | Display Logic, Single Condition, Hide | Same as EX-LOGIC-001 | Q1 = "No" | Q5 is hidden | |
| EX-LOGIC-003 | Display Logic, AND Condition, Both Met | Q6 shown if Q1 = "Yes" AND Q2 = "Agree" | Q1 = "Yes", Q2 = "Agree" | Q6 is visible | |
| EX-LOGIC-004 | Display Logic, AND Condition, One Not Met | Same as EX-LOGIC-003 | Q1 = "Yes", Q2 = "Disagree" | Q6 is hidden | |
| EX-LOGIC-005 | Display Logic, OR Condition, One Met | Q7 shown if Q1 = "A" OR Q1 = "B" | Q1 = "B" | Q7 is visible | |
| EX-LOGIC-006 | Display Logic, OR Condition, Neither Met | Same as EX-LOGIC-005 | Q1 = "C" | Q7 is hidden | |
| EX-LOGIC-007 | Display Logic, Nested AND/OR | Q8 shown if (Q1 = "Yes" AND Q2 = "A") OR (Q3 = "X") | Q1 = "No", Q2 = "B", Q3 = "X" | Q8 is visible (OR branch met via Q3) | |
| EX-LOGIC-008 | Display Logic, Nested AND/OR, All False | Same as EX-LOGIC-007 | Q1 = "No", Q2 = "B", Q3 = "Y" | Q8 is hidden | |
| EX-LOGIC-009 | Skip Logic, Single Condition, Skip Executes | Page 3 has skip logic: if Q2 = "Skip" → go to page 5 | Q2 = "Skip" → click Next on page 2 | Page 3 and 4 are skipped; Page 5 is shown | |
| EX-LOGIC-010 | Skip Logic, Single Condition, No Skip | Same as EX-LOGIC-009 | Q2 = "Continue" | Page 3 is shown normally | |
| EX-LOGIC-011 | Skip Logic, Skip to End of Survey | Skip logic: if Q4 = "Done" → skip to completion page | Q4 = "Done" | All remaining pages are skipped; Completion screen is shown; Response is marked "Complete" | |
| EX-LOGIC-012 | Skip Logic, Skip to Termination | Skip logic: if Q4 = "Out" → skip to termination page | Q4 = "Out" | Termination screen is shown; Response is marked "Terminated" or "Screen-out" | |
| EX-LOGIC-013 | Piped Text, Single Source Question | Q10 text: "You selected [Q1 ] earlier." | Q1 = "Option A" → reach Q10 | Q10 displays: "You selected Option A earlier." | |
| EX-LOGIC-014 | Piped Text, Multiple Sources | Q11 text: "Name: [Q1 ], Age: [Q2 ]" | Q1 = "Yuki", Q2 = "28" → reach Q11 | Q11 displays: "Name: Yuki, Age: 28" | |
| EX-LOGIC-015 | Piped Text, Source Is Blank (Optional, Unanswered) | Same as EX-LOGIC-013; Q1 is optional and left blank | Skip Q1 → reach Q10 | Q10 shows a fallback or blank (no crash) | |
| EX-LOGIC-016 | Carry-Forward, Selected Options | Q3 (multiple choice: A, B, C, D); Q4 carries forward selected options only | Select A and C in Q3 → proceed to Q4 | Q4 shows A and C only; B and D are not shown | |
| EX-LOGIC-017 | Carry-Forward, Unselected Options | Q3 same as EX-LOGIC-016; Q4 carries forward UNselected options | Select A and C → proceed to Q4 | Q4 shows B and D only | |
| EX-LOGIC-018 | Carry-Forward, No Selection Made | Q3 optional; Q4 carries forward selected | Select nothing in Q3 → proceed to Q4 | Q4 shows no options; No crash or error | |
| EX-LOGIC-021 | Randomization, Page Order Randomized | Pages 2–4 are set to randomize | 10 respondents complete the survey | Order of pages 2–4 varies across respondents; All respondents see all 3 pages | |
| EX-LOGIC-022 | Randomization, Fixed Anchor Pages | Same as EX-LOGIC-021; page 1 and page 5 are fixed | Verify page positions across respondents | Page 1 always appears first; Page 5 always appears last; Pages 2–4 are randomized | |
| EX-LOGIC-023 | Randomization, Question Order Within Page | Q5, Q6, Q7 on page 2 are set to randomize | 5 respondents reach page 2 | Q5, Q6, Q7 appear in different orders across respondents; All 3 are always shown | |
| EX-LOGIC-024 | Exclusive Option, Deselects Others | Multiple-choice: A, B, C, "None of the above" (exclusive) | Select A, B → then select "None of the above" | A and B are deselected; Only "None of the above" remains selected | |
| EX-LOGIC-025 | Exclusive Option, Non-exclusive Deselects Exclusive | Same as EX-LOGIC-024 | Select "None of the above" → then select A | "None of the above" is deselected; A is selected | |
| EX-LOGIC-026 | Display Logic on Page Level (Not Question Level) | Page 3 is displayed only if Q2 = "Yes" | Q2 = "Yes" | Page 3 is shown in the flow | |
| EX-LOGIC-027 | Display Logic on Page, Condition Not Met | Same as EX-LOGIC-026 | Q2 = "No" | Page 3 is not shown; Survey flows from page 2 directly to page 4 | |
| EX-LOGIC-028 | Logic Evaluates After Answer Change | Q1 display logic on Q5; respondent changes Q1 answer using Back | Q1 = "Yes" → Q5 is shown; Back → Q1 = "No" → Q5 should be hidden | Display logic re-evaluates after Q1 is changed; Q5 is hidden on revisit | |
| EX-LOGIC-029 | Multiple Logic Rules on Same Question | Q8 has two rules: (1) show if Q1 = "A"; (2) hide if Q3 = "X" | Q1 = "A", Q3 = "X" | Conflict resolution per system spec: hide takes precedence (or as defined); Q8 is hidden (if hide > show priority) | |
| EX-LOGIC-030 | Logic on Hidden Question, Answer Not Recorded | Q9 hidden due to display logic; Q9 has a required flag | Q9 is hidden → user does NOT answer → click Next | No validation error for Q9 (hidden questions are exempt from required validation); Survey advances | |
| EX-LOGIC-031 | Skip Logic Conflict: Two Rules, Different Destinations | Q5 has two skip rules: (1) if Q1 = "A" → go to page 5; (2) if Q2 = "B" → go to page 7 | Q1 = "A", Q2 = "B" | System applies first matching rule OR defined priority rule; Only one skip destination is used (no split or error) | |
| EX-LOGIC-032 | Display Logic Based on Numeric Comparison (Greater Than) | Q10 shown if Q4 > 5 | Q4 = 6 | Q10 is visible | |
| EX-LOGIC-033 | Display Logic Based on Numeric Comparison (Not Met) | Same as EX-LOGIC-032 | Q4 = 5 | Q10 is hidden (condition is strictly greater than) | |
| EX-LOGIC-034 | Display Logic Based on Text Contains | Q11 shown if Q5 (text input) contains "urgent" | Q5 = "This is urgent" | Q11 is visible | |
| EX-LOGIC-035 | Display Logic, Text Contains, No Match | Same as EX-LOGIC-034 | Q5 = "This is routine" | Q11 is hidden | |
| EX-LOGIC-036 | Carry-Forward Filtered by Logic | Q6 (multiple choice: A, B, C, D); Q7 carries forward only options where respondent selected AND Q1 = "Yes" | Q1 = "No", Q6 selects A, B | Q7 is empty (filter condition removes all options); No crash | |
| EX-LOGIC-037 | Multiple Carry-Forwards on Same Page | Q8 carries forward from Q2; Q9 carries forward from Q3; both on page 3 | Q2 selects A; Q3 selects B, C → reach page 3 | Q8 shows only A; Q9 shows B and C; Each carry-forward is independent | |
| EX-LOGIC-038 | Piped Text from Carry-Forward Source | Q10 text uses piped label from Q6 (carry-forward source) | Q6 = "Option X" → pipe appears in Q10 | Q10 displays the label "Option X" correctly | |
| EX-LOGIC-039 | Logic Dependent on Hidden Question | Q12 is hidden (display logic: Q1 = "A" not met); Q13 has logic: show if Q12 = "Yes" | Q1 = "B" → Q12 hidden → Q13 logic evaluates | Q12 is hidden (unanswered); Q13 is hidden (because Q12 is not answered / treated as null) | |
| EX-LOGIC-040 | End-to-End: Logic Chain Across Multiple Pages | Q1 → display Q3 (page 2) → Q3 value → skip page 4 → Q5 (page 5) carries forward Q3 | Q1 = "Yes", Q3 = "B", page 4 skipped, Q5 carries "B" | Q3 shown on page 2; Page 4 skipped; Q5 on page 5 shows "B"; Full logic chain executes correctly end-to-end | |
| EX-LOGIC-041 | Display Logic: Show If Answer Is One Of (Multi-select Source) | Q2 is multi-select (A, B, C, D); Q6 shown if Q2 includes "B" | Q2 = {A, B} | Q6 is visible (B is in the selection) | |
| EX-LOGIC-042 | Display Logic: Show If Answer Is One Of, Not Included | Same as EX-LOGIC-041 | Q2 = {A, C} | Q6 is hidden (B not selected) | |
| EX-LOGIC-043 | Display Logic: Show If Answer Is NOT One Of | Q7 shown if Q2 does NOT include "D" | Q2 = {A, B} | Q7 is visible | |
| EX-LOGIC-044 | Display Logic: NOT One Of, Condition Fails | Same as EX-LOGIC-043 | Q2 = {A, D} | Q7 is hidden (D is included) | |
| EX-LOGIC-045 | Skip Logic: Based on Rating Value | Q3 is a rating scale 1–5; if Q3 ≤ 2 → skip to complaint page | Q3 = 2 | Skip to complaint page executes | |
| EX-LOGIC-046 | Skip Logic: Rating Above Threshold, No Skip | Same as EX-LOGIC-045 | Q3 = 3 | No skip; normal flow continues | |
| EX-LOGIC-047 | Display Logic: Date Comparison (After) | Q8 shown if Q4 (date input) is after 2024-01-01 | Q4 = 2024-06-01 | Q8 is visible | |
| EX-LOGIC-048 | Display Logic: Date Comparison, Before Threshold | Same as EX-LOGIC-047 | Q4 = 2023-12-31 | Q8 is hidden | |
| EX-LOGIC-049 | Carry-Forward: Rank Options Piped from Previous Question | Q5 (ranking question: A, B, C, D); Q6 carries forward only rank 1 and rank 2 from Q5 | Q5 rank: 1=B, 2=D, 3=A, 4=C | Q6 shows B and D only | |
| EX-LOGIC-050 | Carry-Forward: Lowest Ranked Option | Same source as EX-LOGIC-049; Q7 carries forward only rank 4 (last) | Q5 rank: 1=B, 2=D, 3=A, 4=C | Q7 shows C only | |
| EX-LOGIC-051 | Piped Text: Label vs. Value Pipe | Q1 is a dropdown; choice "3" has label "Somewhat Agree"; Q9 pipes Q1's label | Q1 = "3" (label: "Somewhat Agree") → reach Q9 | Q9 displays "Somewhat Agree" (label), not "3" (value) | |
| EX-LOGIC-052 | Piped Text: Numeric Value Pipe | Q9 pipes Q1's value (not label) | Q1 = "3" (label: "Somewhat Agree") → reach Q9 | Q9 displays "3" (value) | |
| EX-LOGIC-053 | Display Logic: Multiple Rules, First Match Wins | Q10 has two show rules: Rule 1: Q1 = "A"; Rule 2: Q2 = "B". System applies first-match logic | Q1 = "B", Q2 = "B" | Rule 1 not met; Rule 2 met → Q10 is shown (if first-match allows); OR: Q10 hidden if system requires ALL rules to match (clarify per spec) | |
| EX-LOGIC-054 | Display Logic: Show and Hide Rule on Same Question | Q11: Show if Q1 = "Yes"; Hide if Q3 = "X" | Q1 = "Yes", Q3 = "X" | Conflict: hide rule takes priority per spec; Q11 is hidden | |
| EX-LOGIC-055 | Skip Logic: Chain Skip (Skip from Skip Destination) | Page 3 has skip: if Q3 = "A" → go to page 5. Page 5 has skip: if Q5 = "B" → go to page 8 | Q3 = "A" → land on page 5 → Q5 = "B" | First skip: page 3 → page 5 (pages 4 skipped); Second skip: page 5 → page 8 (pages 6, 7 skipped); Chain executes correctly | |
| EX-LOGIC-056 | Logic Based on Count of Selections | Q12 shown if count of selections in Q2 ≥ 3 | Q2 = {A, B, C} | Q12 is visible (3 selections) | |
| EX-LOGIC-057 | Logic Based on Count, Below Threshold | Same as EX-LOGIC-056 | Q2 = {A, B} | Q12 is hidden (only 2 selections) | |
| EX-LOGIC-058 | Display Logic: Answer Changed via Back Navigation | Q13 shown if Q1 = "Yes"; respondent answers "Yes", sees Q13, goes back, changes to "No" | Q1 = "Yes" → advance → back → Q1 = "No" → advance again | Q13 is hidden on second pass; Any answer previously entered for Q13 is cleared | |
| EX-LOGIC-059 | Carry-Forward: Empty Source After Logic Hides All Options | Q4 carry-forward source Q2; display logic hides all options in Q2; respondent sees Q2 with no options | All options hidden in Q2 → proceed to Q4 | Q4 has no options to carry forward; Q4 displays empty or fallback message (not a crash) | |
| EX-LOGIC-060 | Piped Text: Pipe from Skipped (Unanswered) Page | Page 3 (Q3) is skipped via logic; Q7 (page 5) pipes Q3's answer | Page 3 skipped → Q3 unanswered → Q7 displays | Q7 shows blank/fallback for the Q3 pipe token; No error | |
| EX-LOGIC-061 | Logic: Required + Hidden Interaction | Q9 is required; display logic hides Q9 (condition not met) | Condition not met → Q9 hidden → click Next | No validation error for Q9; Survey advances (hidden required questions are exempt) | |
| EX-LOGIC-062 | Logic: Required + Hidden, Then Shown | Same as EX-LOGIC-061; respondent changes answer to meet condition | Condition now met → Q9 shown → click Next without answering Q9 | Validation error: Q9 is required and visible; Survey does NOT advance | |
| EX-LOGIC-063 | Randomization: Same Seed, Same Order (Reproducibility) | Page randomization with fixed seed per respondent | Same respondent ID re-enters (if allowed) | Page order is the same as the first entry; Randomization is deterministic per respondent ID | |
| EX-LOGIC-064 | Logic: Mutually Exclusive Groups | Q2 has options in two groups; selecting from group 1 deselects group 2 (mutual exclusion between groups) | Select option from group 1 (A) → then select from group 2 (X) | A is deselected; X is selected; Only one group's selection is recorded | |
| EX-LOGIC-065 | Display Logic: Show Based on Slider Value | Q10 shown if Q5 (slider, 0–100) ≥ 80 | Q5 = 80 | Q10 is visible | |
| EX-LOGIC-066 | Display Logic: Slider Below Threshold | Same as EX-LOGIC-065 | Q5 = 79 | Q10 is hidden | |
| EX-LOGIC-067 | Carry-Forward: Matrix Row Carry-Forward | Q3 is a matrix (3 rows × 4 columns); Q5 carries forward row labels where column 1 was selected | Select column 1 for row 1 and row 3 only | Q5 shows row 1 and row 3 labels; Row 2 label is not carried forward | |
| EX-LOGIC-068 | Piped Text: Matrix Cell Value Pipe | Q6 text: "You rated [Q3.Row2.Col ] for Category 2" | Q3 row 2 = column 3 selected | Q6 displays the label for column 3 | |
| EX-LOGIC-069 | Skip Logic: Based on Matrix Answer | If Q3 row 1 = column 4 ("Very Dissatisfied") → skip to feedback page | Q3 row 1 = column 4 | Skip executes → feedback page shown | |
| EX-LOGIC-070 | Skip Logic: Matrix Condition Not Met | Same as EX-LOGIC-069 | Q3 row 1 = column 2 | No skip; normal flow continues | |
| EX-LOGIC-071 | Display Logic: Based on Ranking Position | Q8 shown if Q4 (ranking) has item "B" ranked 1st | Q4 rank 1 = "B" | Q8 is visible | |
| EX-LOGIC-072 | Display Logic: Ranking Position Not Met | Same as EX-LOGIC-071 | Q4 rank 1 = "A" | Q8 is hidden | |
| EX-LOGIC-073 | Carry-Forward: Top N Ranked Options | Q4 (ranking: A, B, C, D, E); Q5 carries forward top 3 ranked items | Q4 order: C, A, E, B, D | Q5 shows C, A, E (top 3) | |
| EX-LOGIC-074 | Carry-Forward: Bottom N Ranked Options | Same Q4 as EX-LOGIC-073; Q6 carries forward bottom 2 | Q4 order: C, A, E, B, D | Q6 shows B, D (bottom 2; rank 4 and 5) | |
| EX-LOGIC-075 | Logic: Compound Condition Across Pages | Q10 shown if Q1 (page 1) = "Yes" AND Q5 (page 3) > 7 | Q1 = "Yes", Q5 = 8 → reach Q10's page | Q10 is visible | |
| EX-LOGIC-076 | Logic: Compound Cross-Page, One Fails | Same as EX-LOGIC-075 | Q1 = "Yes", Q5 = 6 | Q10 is hidden | |
| EX-LOGIC-077 | Display Logic: Recalculate After Carry-Forward | Q7 display logic depends on Q6 (which was carry-forwarded from Q3); Q6 shows "A" after carry-forward | Q6 = "A" (carried) → logic evaluates Q6 = "A" | Display logic reads carried value correctly; Q7 shows or hides as expected | |
| EX-LOGIC-078 | Logic: Hidden Page with Required Questions | Page 4 has 2 required questions; page 4 is hidden via page-level display logic | Condition not met → page 4 hidden → click Next on page 3 | No validation errors from page 4's required questions; Survey advances to page 5 | |
| EX-LOGIC-082 | Display Logic: Show Based on Time of Day | Q11 shown only if survey started between 09:00–17:00 (system time) | Respondent starts at 10:30 | Q11 is visible | |
| EX-LOGIC-083 | Display Logic: Time of Day, Outside Window | Same as EX-LOGIC-082 | Respondent starts at 20:00 | Q11 is hidden | |
| EX-LOGIC-084 | Carry-Forward: Filter by Logic Condition | Q4 multi-select (A, B, C, D); Q5 carries forward options from Q4 where Q1 = "Yes" | Q1 = "Yes", Q4 = {A, B, C} | Q5 shows A, B, C (filter condition met) | |
| EX-LOGIC-085 | Carry-Forward: Filter Condition Not Met | Same as EX-LOGIC-084 | Q1 = "No", Q4 = {A, B, C} | Q5 has no options (filter removes all) | |
| EX-LOGIC-087 | Piped Text: Pipe Count of Selections | Q9 text: "You selected [Q2.count ] items." | Q2 = {A, B, C} | Q9 displays: "You selected 3 items." | |
| EX-LOGIC-088 | Logic: Answer Cleared When Question Hidden | Q8 shown if Q1 = "Yes"; respondent answers Q8 = "X"; back → Q1 = "No" | Return forward past Q8 | Q8 is hidden; Q8's previous answer "X" is cleared/nulled; "X" is NOT recorded in final data | |
| EX-LOGIC-089 | Carry-Forward: Option Labels vs. Values | Q3 options: value=1 label="Strongly Agree", value=2 label="Agree"; Q5 carries forward labels | Q3 = {1, 2} selected → proceed to Q5 | Q5 shows "Strongly Agree" and "Agree" (labels, not values 1 and 2) | |
| EX-LOGIC-090 | Display Logic: Based on Survey Metadata (Language) | Q12 shown only if survey language = "Japanese" | Respondent uses Japanese version | Q12 is visible | |
| EX-LOGIC-091 | Display Logic: Language Mismatch | Same as EX-LOGIC-090 | Respondent uses English version | Q12 is hidden | |
| EX-LOGIC-092 | Skip Logic: Skip Backwards (Loop Back) | Skip logic: if Q5 = "Repeat" → go back to page 2 | Q5 = "Repeat" | Page 2 is shown again (loop back executed); Previously entered answers on page 2 may be reset or preserved per spec | |
| EX-LOGIC-093 | Carry-Forward: From Hidden Question (Source Hidden) | Q3 is hidden (display logic not met); Q5 carries forward Q3's answer | Q3 hidden → no answer → proceed to Q5 | Q5 has no carry-forward options (source unanswered); No crash | |
| EX-LOGIC-094 | Logic: Piped Text from Matrix Row Answer | Q7 text: "Your rating for Product A was [Q3.Row1 ]" | Q3 Row 1 = column 3 (label: "Neutral") | Q7 displays: "Your rating for Product A was Neutral" | |
| EX-LOGIC-095 | Carry-Forward + Required: Empty Carry-Forward, Required Destination | Q5 (required) carries forward from Q2; Q2 has no selections (optional, skipped) | Q2 skipped → Q5 has no options → click Next | Q5 is empty; If Q5 is required and has no options: validation is waived (no options = nothing to require); Survey advances | |
| EX-LOGIC-096 | Skip Logic: Page-Level Skip Within a Display-Logic-Hidden Block | Block of pages (3–5) is hidden via display logic; skip logic targets page 4 (within hidden block) | Skip condition met → attempt to go to page 4 | Page 4 is hidden (display logic overrides); Skip either lands on the next visible page OR produces a defined fallback behavior (per spec) | |
| EX-LOGIC-098 | Logic: Pipe from Numeric Input, Formatted | Q8 text: "You entered [Q4 ] as your score." | Q4 = 87 | Q8 displays: "You entered 87 as your score." | |
| EX-LOGIC-099 | Display Logic: Based on Previous Page's Carry-Forward Result | Q6 carry-forward shows 2 options; Q9 shown if Q6 has at least 1 option visible | Q6 has 2 options carried | Q9 is visible | |
| EX-LOGIC-100 | Display Logic: Carry-Forward Empty, Dependent Hidden | Same as EX-LOGIC-099; Q6 carry-forward is empty | Q6 has 0 options | Q9 is hidden | |

## V-PAGEBREAK Test Cases (Page Break Runtime Behavior)

### Pattern 1: Single Page Break (V-PAGEBREAK-01 – V-PAGEBREAK-10)

These cases test the most common page break scenario: a survey split at a single point, producing exactly two pages.

---

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| V-PAGEBREAK-01 | Two-Page Survey, Page 1 Displayed on Load | Survey has 1 page break after Q2; page 1 = Q1, Q2; page 2 = Q3, Q4 | Open survey | Page 1 is displayed; Q1 and Q2 are visible; Q3 and Q4 are NOT visible; Page indicator shows page 1 of 2 (if shown) | |
| V-PAGEBREAK-02 | Two-Page Survey, Next Button Advances to Page 2 | Same as V-PAGEBREAK-01; Q1 and Q2 are optional | Click "Next" without answering | Page 2 is displayed; Q3 and Q4 are visible; Q1 and Q2 are no longer visible | |
| V-PAGEBREAK-03 | Two-Page Survey, Back Button Returns to Page 1 | Same setup; respondent is on page 2 | Click "Back" | Page 1 is displayed again; Q1 and Q2 are visible; Previously entered answers for Q1 and Q2 are preserved | |
| V-PAGEBREAK-04 | Two-Page Survey, Required Q on Page 1, Unanswered | Q1 is required; Q2 is optional | Click "Next" without answering Q1 | Validation error for Q1; Page 2 is NOT shown | |
| V-PAGEBREAK-05 | Two-Page Survey, Required Q on Page 1, Answered | Same as V-PAGEBREAK-04 | Answer Q1 → click "Next" | No validation error; Page 2 is shown | |
| V-PAGEBREAK-06 | Two-Page Survey, Required Q on Page 2, Unanswered | Q3 is required on page 2 | Reach page 2 → click "Submit" without answering Q3 | Validation error for Q3; Survey does NOT submit | |
| V-PAGEBREAK-07 | Two-Page Survey, All Required Answered, Submit | Q1 required (page 1), Q3 required (page 2); both answered | Answer Q1 → Next → answer Q3 → Submit | No errors; Survey submits successfully; Completion screen is shown | |
| V-PAGEBREAK-08 | Two-Page Survey, Answer on Page 1 Preserved After Back | Q1 = text input; respondent enters "Test" | Enter "Test" → Next → Back | Page 1 shows Q1 with "Test" still entered; No data is lost on back navigation | |
| V-PAGEBREAK-09 | Two-Page Survey, Answer Changed on Page 1 After Back | Same as V-PAGEBREAK-08 | Enter "Test" → Next → Back → change Q1 to "Updated" → Next → Submit | Final recorded answer for Q1 is "Updated" (not "Test") | |
| V-PAGEBREAK-10 | Two-Page Survey, Progress Indicator Updates | Progress bar or page counter is enabled | Start on page 1 → advance to page 2 | Progress indicator updates to reflect page 2 of 2 (or 50% → 100%); Indicator is accurate on each page | |

### Pattern 2: Multiple Page Breaks / Multi-Page Navigation (V-PAGEBREAK-21 – V-PAGEBREAK-30)

These cases test surveys with multiple page breaks, focusing on navigation, state, and validation across more than two pages.

---

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| V-PAGEBREAK-21 | Three-Page Survey, Sequential Forward Navigation | Survey has 2 page breaks: page 1 = Q1–Q2, page 2 = Q3–Q4, page 3 = Q5–Q6; all questions optional | Open survey → click Next on page 1 → click Next on page 2 → click Submit on page 3 | Pages appear in order: 1 → 2 → 3; Completion screen is shown after Submit; No pages are skipped | |
| V-PAGEBREAK-22 | Three-Page Survey, Back Navigation from Page 3 to Page 2 | Same as V-PAGEBREAK-21; respondent is on page 3 | Click "Back" | Page 2 is shown; Q3 and Q4 are visible; Q5 and Q6 are not visible | |
| V-PAGEBREAK-23 | Three-Page Survey, Back Navigation from Page 2 to Page 1 | Same setup; respondent is on page 2 | Click "Back" | Page 1 is shown; Q1 and Q2 are visible | |
| V-PAGEBREAK-24 | Three-Page Survey, Answers Preserved Across All Back Navigations | Respondent enters Q1 = "A", Q3 = "B", Q5 = "C" | Complete page 1 → page 2 → page 3 → back to page 2 → back to page 1 | Q1 still shows "A" on page 1; Q3 still shows "B" when on page 2; Q5 still shows "C" when returning to page 3 | |
| V-PAGEBREAK-25 | Three-Page Survey, Required Q on Middle Page, Validation Blocks Advance | Q3 (page 2) is required | Reach page 2 → leave Q3 blank → click "Next" | Validation error for Q3; Page 3 is NOT shown | |
| V-PAGEBREAK-26 | Three-Page Survey, Required Q on Middle Page, Answered, Advance | Same as V-PAGEBREAK-25 | Answer Q3 → click "Next" | No error; Page 3 is shown | |
| V-PAGEBREAK-27 | Four-Page Survey, Skip from Page 1 to Page 3 via Logic | Survey has 3 page breaks (4 pages); skip logic: if Q1 = "Skip" → go to page 3 | Q1 = "Skip" → click Next on page 1 | Page 2 is skipped; Page 3 is shown directly; Page 2 questions are not shown and not validated | |
| V-PAGEBREAK-28 | Four-Page Survey, Back from Page 3 After Skip Lands on Page 1 (or Page 2) | Same as V-PAGEBREAK-27; respondent is on page 3 after skip | Click "Back" | System follows back navigation spec: either returns to the last visited page (page 1) or the immediately preceding page (page 2, even though it was skipped); No crash or loop | |
| V-PAGEBREAK-29 | Five-Page Survey, Progress Indicator Reflects Current Page | Survey has 4 page breaks (5 pages); progress indicator enabled | Navigate from page 1 through page 3 | Page 1: indicator shows 1/5 (or 20%); Page 2: indicator shows 2/5 (or 40%); Page 3: indicator shows 3/5 (or 60%); Indicator increments correctly with each Next click | |
| V-PAGEBREAK-30 | Multi-Page Survey, Submit Only Available on Last Page | 3-page survey | Check available buttons on each page | Page 1: "Next" button only (no Submit); Page 2: "Back" and "Next" buttons (no Submit); Page 3: "Back" and "Submit" buttons (no Next) | |

### Pattern 3: Back Navigation Skips Auto-Hidden Questions (V-PAGEBREAK-31)

| Test ID | Scenario | Setup | Action | Expected Result | Tested |
|---|---|---|---|---|---|
| V-PAGEBREAK-31 | Back button skips auto-hidden/auto-selected questions; returns to last manually answered question | 3-page survey: Q1 (SAR, required) on p1; Q2 (SAR, required) on p2 — auto-hidden by questionSelect because Q1 answer meets condition; Q3 on p3 | Answer Q1 (condition met) → advance past Q2 (auto-hidden) → reach p3 → click Back | Back navigation bypasses Q2 (auto-hidden); respondent lands on p1 (last page where a manual answer was recorded); Q2 is not presented to the respondent during back navigation | |

## P3 Pattern — Question & Choice Selection Logic (C-QTSEL)

These cases validate questionSelect (question-level show/hide), choiceSelect (choice-level filter), and subQuestionSelect (sub-question row filter) across all question types.

| Test ID | QT | Logic Type | Scenario | Setup | Expected Result | NT |
| --- | --- | --- | --- | --- | --- | --- |
| C-QTSEL-001 | SAR | questionSelect | SAR hidden when condition false | SAR q2; questionSelect: show when q1=choice-A; q1=choice-B | q2 not rendered; no required check; skipped in submission |  |
| C-QTSEL-002 | SAR | questionSelect | SAR shown when condition true | SAR q2; questionSelect: show when q1=choice-A; q1=choice-A | q2 rendered and answerable; required check applies if configured |  |
| C-QTSEL-003 | MAC | questionSelect | MAC hidden when condition false | MAC q2; questionSelect: show when q1=choice-A; q1=choice-B | q2 not rendered; no required check; skipped in submission |  |
| C-QTSEL-004 | MAC | questionSelect | MAC shown when condition true | MAC q2; questionSelect: show when q1=choice-A; q1=choice-A | q2 rendered and answerable; required check applies if configured |  |
| C-QTSEL-005 | SAP | questionSelect | SAP hidden when condition false | SAP q2; questionSelect: show when q1=choice-A; q1=choice-B | q2 not rendered; no required check; skipped in submission |  |
| C-QTSEL-006 | SAP | questionSelect | SAP shown when condition true | SAP q2; questionSelect: show when q1=choice-A; q1=choice-A | q2 rendered and answerable; required check applies if configured |  |
| C-QTSEL-007 | FA | questionSelect | FA hidden when condition false | FA q2; questionSelect: show when q1=choice-A; q1=choice-B | q2 not rendered; no required check; skipped in submission |  |
| C-QTSEL-008 | FA | questionSelect | FA shown when condition true | FA q2; questionSelect: show when q1=choice-A; q1=choice-A | q2 rendered and answerable; required check applies if configured |  |
| C-QTSEL-009 | FAL | questionSelect | FAL hidden when condition false | FAL q2; questionSelect: show when q1=choice-A; q1=choice-B | q2 not rendered; no required check; skipped in submission |  |
| C-QTSEL-010 | FAL | questionSelect | FAL shown when condition true | FAL q2; questionSelect: show when q1=choice-A; q1=choice-A | q2 rendered and answerable; required check applies if configured |  |
| C-QTSEL-011 | RNK | questionSelect | RNK hidden when condition false | RNK q2; questionSelect: show when q1=choice-A; q1=choice-B | q2 not rendered; no required check; skipped in submission |  |
| C-QTSEL-012 | RNK | questionSelect | RNK shown when condition true | RNK q2; questionSelect: show when q1=choice-A; q1=choice-A | q2 rendered and answerable; required check applies if configured |  |
| C-QTSEL-013 | RAT | questionSelect | RAT hidden when condition false | RAT q2; questionSelect: show when q1=choice-A; q1=choice-B | q2 not rendered; no required check; skipped in submission |  |
| C-QTSEL-014 | RAT | questionSelect | RAT shown when condition true | RAT q2; questionSelect: show when q1=choice-A; q1=choice-A | q2 rendered and answerable; required check applies if configured |  |
| C-QTSEL-015 | Note | questionSelect | Note hidden when condition false | Note q2; questionSelect: show when q1=choice-A; q1=choice-B | q2 not rendered; no required check; skipped in submission |  |
| C-QTSEL-016 | Note | questionSelect | Note shown when condition true | Note q2; questionSelect: show when q1=choice-A; q1=choice-A | q2 rendered and answerable; required check applies if configured |  |
| C-QTSEL-017 | MTS | questionSelect | MTS matrix hidden | MTS q2; questionSelect hides entire matrix when q1=B; q1=B | entire matrix not rendered; all SQ required checks skipped |  |
| C-QTSEL-018 | MTS | questionSelect | MTS matrix shown | MTS q2; questionSelect shows when q1=A; q1=A | matrix rendered; SQ required checks apply per config |  |
| C-QTSEL-019 | MTM | questionSelect | MTM matrix hidden | MTM q2; questionSelect hides entire matrix when q1=B; q1=B | entire matrix not rendered; all SQ required checks skipped |  |
| C-QTSEL-020 | MTM | questionSelect | MTM matrix shown | MTM q2; questionSelect shows when q1=A; q1=A | matrix rendered; SQ required checks apply per config |  |
| C-QTSEL-021 | MTT | questionSelect | MTT matrix hidden | MTT q2; questionSelect hides entire matrix when q1=B; q1=B | entire matrix not rendered; all SQ required checks skipped |  |
| C-QTSEL-022 | MTT | questionSelect | MTT matrix shown | MTT q2; questionSelect shows when q1=A; q1=A | matrix rendered; SQ required checks apply per config |  |
| C-QTSEL-023 | SAR | choiceSelect | SAR choice hidden when condition met | SAR q1 5 choices; choiceSelect hides choice-3 when q0=A; q0=A | choice-3 not displayed; respondent selects from 1,2,4,5 |  |
| C-QTSEL-024 | SAR | choiceSelect | SAR all choices hidden | SAR q1 required; choiceSelect hides all 5 choices; condition met | question displays empty; required cannot be satisfied; submit blocked or warning shown |  |
| C-QTSEL-025 | SAR | choiceSelect | SAR choice hidden then revealed | SAR q1; choiceSelect hides choice-2 when q0=A; respondent changes q0 from A to B | choice-2 reappears when condition no longer met; any prior auto-selection cleared |  |
| C-QTSEL-026 | MAC | choiceSelect | MAC choice hidden when condition met | MAC q1 5 choices; choiceSelect hides choice-3 when q0=A; q0=A | choice-3 not displayed; respondent selects from 1,2,4,5 |  |
| C-QTSEL-027 | MAC | choiceSelect | MAC all choices hidden | MAC q1 required; choiceSelect hides all 5 choices; condition met | question displays empty; required cannot be satisfied; submit blocked or warning shown |  |
| C-QTSEL-028 | MAC | choiceSelect | MAC choice hidden then revealed | MAC q1; choiceSelect hides choice-2 when q0=A; respondent changes q0 from A to B | choice-2 reappears when condition no longer met; any prior auto-selection cleared |  |
| C-QTSEL-029 | SAP | choiceSelect | SAP choice hidden when condition met | SAP q1 5 choices; choiceSelect hides choice-3 when q0=A; q0=A | choice-3 not displayed; respondent selects from 1,2,4,5 |  |
| C-QTSEL-030 | SAP | choiceSelect | SAP all choices hidden | SAP q1 required; choiceSelect hides all 5 choices; condition met | question displays empty; required cannot be satisfied; submit blocked or warning shown |  |
| C-QTSEL-031 | SAP | choiceSelect | SAP choice hidden then revealed | SAP q1; choiceSelect hides choice-2 when q0=A; respondent changes q0 from A to B | choice-2 reappears when condition no longer met; any prior auto-selection cleared |  |
| C-QTSEL-032 | MTS | subQuestionSelect | MTS sub-question hidden | MTS q1 3 SQs; subQuestionSelect hides sq-2 when q0=X; q0=X | sq-2 row not shown; its required check skipped; other SQs unaffected |  |
| C-QTSEL-033 | MTS | subQuestionSelect | MTS sub-question shown | MTS q1; subQuestionSelect shows sq-2 when q0=Y; q0=Y | sq-2 row rendered; required check applies if sq-2 is marked required |  |
| C-QTSEL-034 | MTM | subQuestionSelect | MTM sub-question hidden | MTM q1 3 SQs; subQuestionSelect hides sq-2 when q0=X; q0=X | sq-2 row not shown; its required check skipped; other SQs unaffected |  |
| C-QTSEL-035 | MTM | subQuestionSelect | MTM sub-question shown | MTM q1; subQuestionSelect shows sq-2 when q0=Y; q0=Y | sq-2 row rendered; required check applies if sq-2 is marked required |  |
| C-QTSEL-036 | MTT | subQuestionSelect | MTT sub-question hidden | MTT q1 3 SQs; subQuestionSelect hides sq-2 when q0=X; q0=X | sq-2 row not shown; its required check skipped; other SQs unaffected |  |
| C-QTSEL-037 | MTT | subQuestionSelect | MTT sub-question shown | MTT q1; subQuestionSelect shows sq-2 when q0=Y; q0=Y | sq-2 row rendered; required check applies if sq-2 is marked required |  |
| C-QTSEL-038 | MTS | choiceSelect-col | Column hidden from all rows | MTS q1 5 cols; choiceSelect hides col-3 when q0=A; q0=A | col-3 hidden across all SQ rows; respondent selects from 4 remaining columns |  |
| C-QTSEL-039 | MTM | choiceSelect-col | Column hidden reduces available choices | MTM q1 5 cols; specN=max:3; choiceSelect hides col-1; 4 cols remain | 4 cols visible; max:3 applies to these 4; submit allowed with ≤3 selected from 4 |  |
| C-QTSEL-040 | MTT | choiceSelect-col | Bipolar column hidden | MTT q1 5 scale-points; choiceSelect hides scale-point-3; condition met | scale-point-3 not displayed; bipolar scale has gap; respondent picks from 4 points |  |
| C-QTSEL-041 | SAR | choiceSelect+req | Required SAR narrowed to 0 choices | SAR q1 required; choiceSelect hides all choices | All choices hidden; required not satisfiable; survey shows empty required question; submit blocked |  |
| C-QTSEL-042 | MAC | choiceSelect+req | Required MAC narrowed to fewer than specN exact | MAC q1 specN=exact:3 required; choiceSelect hides 3 of 5 choices → 2 visible | 2 choices visible but exact:3 required; submit blocked with specN error |  |
| C-QTSEL-043 | SAR | questionSelect+req | Required question hidden → skipped | SAR q2 required; questionSelect hides q2; condition not met | q2 hidden; required skipped; submit proceeds without q2 answer |  |
| C-QTSEL-044 | MTM | questionSelect+req | Required MTM hidden → all SQ checks skipped | MTM q2 required=all; questionSelect hides q2; condition not met | entire MTM not rendered; no required errors; submit succeeds |  |

---

## P3 Pattern — Randomization Logic Validation (C-QTRAND)

These cases validate randomization modes (random, flip, absolute, fixedLast) across applicable question types. FA, FAL, and Note confirm no randomization applies.

| Test ID | QT | Rand Mode | Scenario | Setup | Expected Result | NT |
| --- | --- | --- | --- | --- | --- | --- |
| C-QTRAND-001 | SAR | random | 5 choices, order varies per run | SAR q1 rand=random 5 choices; 3 runs | Order changes between runs with high probability |  |
| C-QTRAND-002 | SAR | random | 2 choices, 50% each order | SAR q1 rand=random 2 choices | 2 choices in random order; \~50% each permutation |  |
| C-QTRAND-003 | SAR | flip | 5 choices, alternates normal/reversed | SAR q1 rand=flip 5 choices A-E | Half respondents see A-E; half see E-D-C-B-A |  |
| C-QTRAND-004 | SAR | flip | 2 choices A,B | SAR q1 rand=flip 2 choices A,B | Half see A,B; half see B,A |  |
| C-QTRAND-005 | SAR | absolute | Fixed seed: same order on revisit | SAR q1 rand=absolute 5 choices; same respondent revisits | Same order on every visit for that respondent |  |
| C-QTRAND-006 | SAR | fixedLast | Last choice always last; others random | SAR q1 rand=fixedLast; Other flagged fixed; 4 non-fixed | Other always last; A,B,C,D randomized in positions 1-4 |  |
| C-QTRAND-007 | SAR | fixedLast | Multiple fixed choices at bottom | SAR q1 rand=fixedLast; N/A and Other both fixed; 3 non-fixed | N/A and Other always last (original relative order); 3 non-fixed randomized |  |
| C-QTRAND-008 | SAR | random | Random + choiceSelect hides one | SAR q1 rand=random; choiceSelect hides choice-3 | choice-3 hidden; remaining choices randomized among visible positions |  |
| C-QTRAND-009 | MAC | random | Multi-select, order varies | MAC q1 rand=random 5 choices; multi-select | Choices in random order each run; multi-select unaffected |  |
| C-QTRAND-010 | MAC | random | Random + exclusive choice | MAC q1 rand=random; choice-5 exclusive | Exclusive randomized with others; selecting it deselects others |  |
| C-QTRAND-011 | MAC | flip | 4 choices, flip halves | MAC q1 rand=flip 4 choices A,B,C,D | Half see A,B,C,D; half see D,C,B,A |  |
| C-QTRAND-012 | MAC | absolute | Same order per respondent session | MAC q1 rand=absolute 6 choices | Consistent order across page refreshes for same respondent |  |
| C-QTRAND-013 | MAC | fixedLast | Other always last in MAC | MAC q1 rand=fixedLast; Other fixed; 4 non-fixed | Other at bottom; 4 choices randomized above |  |
| C-QTRAND-014 | MAC | random | Random + specN=exact:2 | MAC q1 rand=random specN=exact:2 5 choices | Choices randomized; must select exactly 2 regardless of order |  |
| C-QTRAND-015 | SAP | random | Scale points randomized | SAP q1 rand=random 5 scale points | Scale order randomized each run |  |
| C-QTRAND-016 | SAP | flip | Flip scale direction | SAP q1 rand=flip; original 1-2-3-4-5 | Half see 1→5; half see 5→1 |  |
| C-QTRAND-017 | SAP | fixedLast | N/A option fixed at end | SAP q1 rand=fixedLast; N/A flagged fixed | N/A always rightmost; scale 1-5 randomized |  |
| C-QTRAND-018 | MTS | random | Sub-question rows randomized | MTS q1 4 SQs; rand=random on row order | Row order changes each run; columns fixed; answers by SQ ID |  |
| C-QTRAND-019 | MTS | random | Row random + matrixInclusion | MTS q1 rand=random; matrixInclusion keeps 3 of 5 rows | 3 included rows randomized; excluded rows not shown |  |
| C-QTRAND-020 | MTS | flip | Flip row order | MTS q1 4 rows A,B,C,D; rand=flip | Half see A,B,C,D; half see D,C,B,A |  |
| C-QTRAND-021 | MTS | absolute | Absolute row order on revisit | MTS q1 rand=absolute; same respondent revisits | Same row order on every visit |  |
| C-QTRAND-022 | MTS | fixedLast | Last SQ fixed; others randomized | MTS q1 5 rows; row-5 flagged fixed | Row-5 always last; rows 1-4 randomized |  |
| C-QTRAND-023 | MTS | random | Random rows + required SQs | MTS q1 all rows required; rand=random | Rows in random order; required check applies by SQ ID not position |  |
| C-QTRAND-024 | MTM | random | Row order randomized | MTM q1 3 rows; rand=random on rows | Row order randomized; specN and prohibition rules still apply |  |
| C-QTRAND-025 | MTM | flip | Flip row order | MTM q1 4 rows A,B,C,D; rand=flip | Half see A,B,C,D; half see D,C,B,A |  |
| C-QTRAND-026 | MTM | random | Column order randomized | MTM q1; rand=random on columns | Column display order randomized; specN/prohibition by col ID not position |  |
| C-QTRAND-027 | MTM | fixedLast | Fixed last row | MTM q1 5 rows; row-5 fixed; rand=fixedLast | Row-5 always last; rows 1-4 randomized |  |
| C-QTRAND-028 | MTM | absolute | Absolute order for panel survey | MTM q1 rand=absolute; same respondent twice | Identical row and column order both visits |  |
| C-QTRAND-029 | RNK | random | Items in random order | RNK q1 5 items; rand=random | Presentation order randomized; result recorded by item ID |  |
| C-QTRAND-030 | RNK | flip | Flip item presentation | RNK q1 items A,B,C,D,E; rand=flip | Half see A,B,C,D,E; half see E,D,C,B,A initially |  |
| C-QTRAND-031 | RNK | fixedLast | N/A item always last | RNK q1 5 items; item-5 N/A fixed last | Item-5 always last; items 1-4 randomized |  |
| C-QTRAND-032 | RNK | random | Random + choiceSelect hides one | RNK q1 rand=random; choiceSelect hides item-3 | item-3 hidden; remaining randomized |  |
| C-QTRAND-033 | RNK | absolute | Consistent experience on revisit | RNK q1 rand=absolute 6 items; revisit | Same order both visits |  |
| C-QTRAND-034 | RAT | random | Item rows randomized | RAT q1 5 items; rand=random | Items in random order; scale columns fixed; answers by item ID |  |
| C-QTRAND-035 | RAT | flip | Flip RAT item order | RAT q1 4 items; rand=flip | Half see A,B,C,D; half see D,C,B,A |  |
| C-QTRAND-036 | RAT | fixedLast | N/A item fixed at bottom | RAT q1 4 items + N/A; N/A fixed last | N/A always last row; items 1-4 randomized |  |
| C-QTRAND-037 | RAT | absolute | Absolute order for longitudinal panel | RAT q1 rand=absolute; panel study | Same item order across all sessions for same respondent |  |
| C-QTRAND-038 | RAT | random | Random + all items required | RAT q1 all required; rand=random | Items random; all must be rated; required by item ID not position |  |
| C-QTRAND-039 | FA | N/A | FA has no choices to randomize | FA q1; rand flag set | rand not applicable to FA; editor disables or ignores option |  |
| C-QTRAND-040 | FAL | N/A | FAL has no choices to randomize | FAL q1; rand flag set | rand not applicable; editor disables option |  |
| C-QTRAND-041 | Note | N/A | Note has no choices to randomize | Note q1; rand flag set | rand not applicable; editor disables option |  |
| C-QTRAND-042 | SAR | random | 1 choice — no-op | SAR q1 rand=random 1 choice | 1 choice; randomization no-op; displayed as-is; no error |  |
| C-QTRAND-043 | SAR | fixedLast | All choices flagged fixed | SAR q1 rand=fixedLast; all 5 fixed | All maintain original order; no randomization among fixed-only choices |  |
| C-QTRAND-044 | MTS | random | matrixInclusion removes all rows + rand | MTS q1 rand=random; matrixInclusion removes all rows | No rows to randomize; matrix empty; no error |  |
| C-QTRAND-045 | SAR | absolute | Absolute: same order across devices | SAR q1 rand=absolute; same respondent mobile then desktop | Same order on both devices (seed tied to respondent ID not device) |  |
| C-QTRAND-046 | RNK | random | Result by item ID independent of display | RNK q1 rand=random; item-A displayed last; ranked #1 | Result: item-A=rank-1 regardless of display position |  |
| C-QTRAND-047 | RAT | random | RAT result stored by item ID not position | RAT q1 rand=random; item-B in row-1; score-3 given | Result: item-B=score-3; not position-1=score-3 |  |

---


---

### C-QTSEL Additional Cases (C-QTSEL-045–110)

| Test ID | QT | Logic Type | Scenario | Setup | Expected Result | NT |
|---|---|---|---|---|---|---|
| C-QTSEL-045 | SAR | questionSelect | Condition changes mid-session: shown then hidden | SAR q2 shown (q1=A); respondent views q2; q1 changed to B | q2 disappears; partial answer cleared; required recalculates | |
| C-QTSEL-046 | MAC | questionSelect | Condition changes: hidden then shown | MAC q2 hidden (q1=B); q1 changed to A | q2 appears; state cleared; respondent answers fresh | |
| C-QTSEL-047 | SAP | questionSelect | Multiple conditions AND: both true | SAP q3 shown when q1=A AND q2=B; q1=A q2=B | q3 shown | |
| C-QTSEL-048 | SAP | questionSelect | Multiple conditions AND: one false | SAP q3 shown when q1=A AND q2=B; q1=A q2=C | q3 hidden | |
| C-QTSEL-049 | FA | questionSelect | Multiple conditions OR: one true | FA q2 shown when q1=A OR q1=B; q1=B | q2 shown via OR branch | |
| C-QTSEL-050 | FAL | questionSelect | Nested condition: q2 gated by q1; q3 gated by q2 | FAL q3 shown when q2=X; q2 shown when q1=A; q1=A then q2=X | q3 shown after both conditions propagate | |
| C-QTSEL-051 | RNK | questionSelect | Question shown after several intervening questions | RNK q5 gated by q1=A; 4 questions between; q1=A | q5 shown at its position regardless of distance | |
| C-QTSEL-052 | RAT | questionSelect | Numeric comparison (FA value > 3) | RAT q2 shown when FA q0 > 3; q0=5 | q2 shown (5 > 3) | |
| C-QTSEL-053 | RAT | questionSelect | Numeric comparison (FA value ≤ 3) | RAT q2 shown when FA q0 > 3; q0=2 | q2 hidden (2 not > 3) | |
| C-QTSEL-054 | Note | questionSelect | Note shown conditionally | Note n1 shown when q1=A; q1=A | Note displayed; no required check | |
| C-QTSEL-055 | Note | questionSelect | Note hidden: no empty space | Note n1 shown when q1=A; q1=B | Note not rendered; no blank gap | |
| C-QTSEL-056 | MTS | questionSelect | Matrix shown when MAC includes a choice | MTS q2 shown when MAC q1 includes choice-A; q1=A,C | q2 shown (A included) | |
| C-QTSEL-057 | MTM | questionSelect | Matrix hidden when MAC excludes a choice | MTM q2 hidden when MAC q1 does NOT include choice-B; q1=A,C | q2 hidden | |
| C-QTSEL-058 | MTT | questionSelect | Bipolar shown when RNK ranks item-1 first | MTT q2 shown when RNK q2 item-1 rank=1; item-1 ranked first | q2 shown | |
| C-QTSEL-059 | SAR | choiceSelect | Choice hidden by numeric FA condition | SAR q1 5 choices; choiceSelect hides choice-3 when FA q0 < 10; q0=7 | choice-3 hidden; respondent picks from 1,2,4,5 | |
| C-QTSEL-060 | SAR | choiceSelect | Choice revealed when condition changes | SAR q1; choice-2 hidden when q0=A; q0 changes from A to B | choice-2 reappears | |
| C-QTSEL-061 | SAR | choiceSelect | 3 of 5 choices hidden | SAR q1 5 choices; choiceSelect hides 1,3,5 | 2 choices displayed | |
| C-QTSEL-062 | SAR | choiceSelect | Previously-selected choice hidden | SAR q1; respondent selects choice-3; condition then hides choice-3 | choice-3 disappears; answer cleared; required error if required | |
| C-QTSEL-063 | MAC | choiceSelect | Only exclusive choice remains after filtering | MAC q1 5 choices; choiceSelect hides 1-4; exclusive choice-5 remains | only choice-5 visible; selecting it is the only option | |
| C-QTSEL-064 | MAC | choiceSelect | 2 hidden; specN=max:3 still satisfiable | MAC q1 5 choices specN=max:3; hides 2 → 3 remain | 3 visible; max:3 allows selecting all 3; submit OK | |
| C-QTSEL-065 | MAC | choiceSelect | Previously-selected choice hidden: deselected | MAC q1; choices 1,2,3 selected; choice-2 then hidden | choice-2 auto-deselected; remaining selection: 1,3 | |
| C-QTSEL-066 | SAP | choiceSelect | Middle scale point hidden | SAP q1 5 points; choiceSelect hides point-3; condition met | point-3 not displayed; gap in scale; picks from 1,2,4,5 | |
| C-QTSEL-067 | SAP | choiceSelect | First scale point hidden | SAP q1 5 points; hides point-1 | scale starts at point-2 | |
| C-QTSEL-068 | SAP | choiceSelect | All but one hidden — auto-select fires | SAP required 5 points; hides 4 → point-3 only | remaining point auto-selected; question hidden; required satisfied without respondent interaction | |
| C-QTSEL-069 | MTS | choiceSelect | First column hidden across all rows | MTS q1 5 cols; hides col-1 | col-1 not selectable in any row | |
| C-QTSEL-070 | MTS | choiceSelect | Last column hidden | MTS q1 5 cols; hides col-5 | col-5 gone; 4 cols remain | |
| C-QTSEL-071 | MTS | choiceSelect | 2 columns hidden | MTS q1 5 cols; hides cols 2,4 | rows select from 1,3,5 | |
| C-QTSEL-072 | MTS | choiceSelect | Selected column then hidden mid-session | MTS q1; SQ-1 selected col-3; then col-3 hidden | SQ-1 answer cleared; required error if row required | |
| C-QTSEL-073 | MTM | choiceSelect | Column hidden; specN=max:3 recalculated | MTM q1 5 cols specN=max:3; hides col-1 → 4 remain | max:3 applies to 4 visible cols | |
| C-QTSEL-074 | MTM | choiceSelect | Column hidden: selected col deselected | MTM q1; SQ-2 has col-3 selected; col-3 then hidden | col-3 deselected; specN re-evaluated | |
| C-QTSEL-075 | MTT | choiceSelect | Left half of bipolar scale hidden | MTT q1 7 points; hides points 1,2,3 | only center-right selectable; semantic shift | |
| C-QTSEL-076 | RNK | choiceSelect | One item hidden: list shorter | RNK q1 5 items required=all; hides item-4 → 4 remain | 4 items to rank; required=all covers 4 | |
| C-QTSEL-077 | RNK | choiceSelect | Hidden item was already ranked | RNK q1; item-3 ranked #2; then item-3 hidden | item-3 removed; remaining renumbered; item-3 absent from result | |
| C-QTSEL-078 | RAT | choiceSelect | One row hidden; total enforced on visible | RAT q1 5 items percent=100; hides item-5 → 4 visible | 4 items; total=100 across 4; item-5 excluded | |
| C-QTSEL-079 | RAT | choiceSelect | Multiple items hidden | RAT q1 5 items; hides items 1,2 → 3 visible | 3 items; total enforced on 3 | |
| C-QTSEL-080 | MTS | subQuestionSelect | Multiple SQs hidden simultaneously | MTS q1 5 SQs; hides SQs 2,4 when q0=A; q0=A | SQs 2,4 not shown; required for 2,4 skipped | |
| C-QTSEL-081 | MTS | subQuestionSelect | Required SQ hidden: required bypassed | MTS q1; SQ-3 required; hides SQ-3 when q0=B; q0=B | SQ-3 hidden; required for SQ-3 bypassed | |
| C-QTSEL-082 | MTS | subQuestionSelect | SQ revealed after being hidden | MTS q1; SQ-2 hidden (q0=B); q0 changes to A | SQ-2 appears; fresh empty; respondent answers if required | |
| C-QTSEL-083 | MTM | subQuestionSelect | Multiple SQs hidden; specN on remaining | MTM q1 5 SQs specN=exact:2; hides SQs 3,4,5 → 2 remain | SQs 1,2 shown; each must select exactly 2 | |
| C-QTSEL-084 | MTM | subQuestionSelect | SQ with specN override hidden | MTM q1; SQ-2 override specN=exact:3; SQ-2 hidden | exact:3 for SQ-2 not enforced | |
| C-QTSEL-085 | MTT | subQuestionSelect | Bipolar SQ hidden conditionally | MTT q1 4 SQs; hides SQ-1 when q0=X; q0=X | SQ-1 row hidden; required for SQ-1 bypassed | |
| C-QTSEL-086 | MTT | subQuestionSelect | All SQs hidden: matrix empty | MTT q1 3 SQs; all hidden when q0=Z; q0=Z | matrix empty; all required skipped; submit OK | |
| C-QTSEL-087 | MTS | subQuestionSelect | SQ selected before being hidden | MTS q1; SQ-2 selects col-3; SQ-2 then hidden | SQ-2 hidden; answer cleared from submission | |
| C-QTSEL-088 | MTM | subQuestionSelect | SQ hidden by question-level questionSelect (takes precedence) | MTM q2 hidden at question level by questionSelect; subQuestionSelect also configured | entire MTM hidden; subQuestionSelect within not evaluated | |
| C-QTSEL-089 | SAR | choiceSelect+rand | Random order then choice hidden | SAR q1 rand=random; choiceSelect hides choice-3 after display | choice-3 removed; remaining in adjusted random order | |
| C-QTSEL-090 | MAC | choiceSelect+rand | fixedLast + choiceSelect hides fixed choice | MAC q1 rand=fixedLast; choice-5 fixed; choiceSelect hides choice-5 | choice-5 hidden despite being fixed; 1-4 randomized | |
| C-QTSEL-091 | RNK | choiceSelect+rand | Random presentation then item hidden | RNK q1 rand=random; choiceSelect hides item-2 | item-2 removed; remaining in adjusted random order | |
| C-QTSEL-092 | SAR | questionSelect | MAC-based condition: any-of match | SAR q3 shown when MAC q1 includes choice-B; q1=A,B,C | q3 shown (B included) | |
| C-QTSEL-093 | MAC | questionSelect | Gated by RNK rank position | MAC q3 shown when RNK q2 item-X rank=1; item-X ranked first | q3 shown | |
| C-QTSEL-094 | SAR | questionSelect | OR logic: second path true | SAR q3: show when q1=A OR q2=Y; q1=B q2=Y | q3 shown via second condition | |
| C-QTSEL-095 | FA | questionSelect | FA shown when SAP = specific value | FA q2 shown when SAP q1=scale-point-5; q1=5 | q2 shown; text input available | |
| C-QTSEL-096 | SAR | choiceSelect | Choices filtered by MAC q0 selection | SAR q1 5 choices; hides choices 3,4 when MAC q0 includes choice-A; q0=A,B | choices 3,4 hidden | |
| C-QTSEL-097 | MAC | choiceSelect | Choices filtered by RNK q0 answer | MAC q1; hides choice-2 when RNK q0 item-Y rank=1; item-Y ranked first | choice-2 hidden | |
| C-QTSEL-098 | SAP | choiceSelect | Scale filtered by FA numeric answer | SAP q1; hides points 1,2 when FA q0 > 5; q0=7 | points 1,2 hidden; picks from 3,4,5 | |
| C-QTSEL-099 | SAR | questionSelect | Circular reference rejected | Editor: q1 questionSelect on q2; q2 questionSelect on q1 (circular) | Editor rejects: circular question references not allowed | |
| C-QTSEL-100 | MAC | choiceSelect | Non-existent choice ID referenced | MAC q1; choiceSelect hides choice-9 (only 5 exist) | Editor rejects or ignores: referenced choice must exist | |
| C-QTSEL-101 | MTS | subQuestionSelect | Non-existent SQ referenced | MTS q1; subQuestionSelect hides SQ-7 (only 3 exist) | Editor rejects: referenced SQ must exist | |
| C-QTSEL-102 | SAR | choiceSelect | All choices hidden; question optional: submit OK | SAR q1 optional; choiceSelect hides all 5 | q1 empty; respondent skips; no answer recorded; submit OK | |
| C-QTSEL-103 | MAC | choiceSelect | Condition flips rapidly: no stale state | MAC q1; choiceSelect on dynamic condition; condition changes 5 times | each change correctly updates visible choices; final state correct | |
| C-QTSEL-104 | MTM | subQuestionSelect | All SQs hidden but question not hidden at question level | MTM q1; subQuestionSelect hides all 3 SQs; questionSelect does not hide q1 | matrix container shown but empty; required skipped | |
| C-QTSEL-105 | SAR | choiceSelect+req | Required SAR narrowed to 1: auto-selected and hidden | SAR q1 required 5 choices; hides 4 → 1 remains | remaining choice auto-selected; q1 hidden; answer recorded silently | |
| C-QTSEL-106 | MAC | choiceSelect+req | Required MAC specN=exact:1 narrowed to 1 | MAC q1 required specN=exact:1; hides 4 → 1 remains | auto-selected; q1 hidden; exact:1 satisfied | |
| C-QTSEL-107 | SAP | choiceSelect+req | Required SAP narrowed to 1 | SAP q1 required 5 points; hides 4 → 1 remains | remaining point auto-selected; q1 hidden | |
| C-QTSEL-108 | RNK | choiceSelect+req | Required=All RNK narrowed to 1 | RNK q1 required=all 5 items; hides 4 → 1 remains | single item auto-ranked #1; q1 hidden | |
| C-QTSEL-109 | MTS | choiceSelect+req | All-required MTS narrowed to 1 col per row | MTS required=all 5 SQs; hides 4 cols → 1 remains | each SQ auto-selects remaining col; matrix hidden | |
| C-QTSEL-110 | MTM | choiceSelect+req | Required MTM specN=unspecified narrowed to 1 | MTM required=all specN=unspecified; hides 4 cols → 1 remains | each SQ auto-selects single col; matrix hidden | |


---

### C-QTSEL Additional Cases (C-QTSEL-111–150)

| Test ID | QT | Logic Type | Scenario | Setup | Expected Result | NT |
|---|---|---|---|---|---|---|
| C-QTSEL-111 | SAR | questionSelect | Shown when FA q0 answer equals specific text | SAR q2 shown when FA q0 = 'Tokyo'; respondent types 'Tokyo' | q2 shown; text-match condition evaluated case-sensitively per spec | |
| C-QTSEL-112 | SAR | questionSelect | Hidden when FA q0 answer does not match | SAR q2 shown when FA q0 = 'Tokyo'; respondent types 'Osaka' | q2 hidden; text does not match condition | |
| C-QTSEL-113 | MAC | questionSelect | Shown when SAP q0 ≥ 4 (numeric scale comparison) | MAC q2 shown when SAP q0 ≥ 4; respondent selects scale-point-4 | q2 shown (4 ≥ 4 satisfied) | |
| C-QTSEL-114 | MAC | questionSelect | Hidden when SAP q0 < 4 | MAC q2 shown when SAP q0 ≥ 4; respondent selects scale-point-3 | q2 hidden (3 < 4) | |
| C-QTSEL-115 | FA | questionSelect | Shown when RNK q0 includes item-B in top-2 | FA q2 shown when RNK q0 item-B rank ≤ 2; item-B ranked #1 | q2 shown (rank 1 ≤ 2) | |
| C-QTSEL-116 | FA | questionSelect | Hidden when RNK item not in top-2 | FA q2 shown when RNK q0 item-B rank ≤ 2; item-B ranked #4 | q2 hidden (rank 4 > 2) | |
| C-QTSEL-117 | FAL | questionSelect | Shown when MAC q0 selects exactly 3 choices | FAL q2 shown when MAC q0 selection count = 3; respondent selects A,B,C | q2 shown (count = 3) | |
| C-QTSEL-118 | FAL | questionSelect | Hidden when MAC q0 selects 2 choices (count mismatch) | FAL q2 shown when MAC q0 count = 3; respondent selects A,B only | q2 hidden (count = 2 ≠ 3) | |
| C-QTSEL-119 | SAR | choiceSelect | Choice hidden when RNK q0 item ranks last | SAR q1; choiceSelect hides choice-3 when RNK q0 item-Z rank = last; item-Z ranked last | choice-3 hidden; 4 choices remain | |
| C-QTSEL-120 | MAC | choiceSelect | Choice hidden based on FA text match | MAC q1; choiceSelect hides choice-2 when FA q0 = 'None'; q0='None' | choice-2 hidden; respondent multi-selects from remaining | |
| C-QTSEL-121 | SAP | choiceSelect | Scale point hidden when SAR q0 = specific choice | SAP q1; choiceSelect hides scale-point-1 when SAR q0 = choice-A; q0=choice-A | scale-point-1 hidden; scale starts at point-2 | |
| C-QTSEL-122 | RNK | choiceSelect | 2 items hidden from ranking list | RNK q1 5 items required=all; choiceSelect hides items 2,4; 3 remain | 3 items visible; required=all means rank all 3; items 2,4 excluded | |
| C-QTSEL-123 | RAT | choiceSelect | Item hidden; sum total recalculated on visible | RAT q1 5 items percent=100; choiceSelect hides item-3 → 4 visible | 4 items shown; must sum to 100 across 4; item-3 excluded | |
| C-QTSEL-124 | MTS | choiceSelect | Column filter from MAC q0 answer | MTS q1 5 cols; choiceSelect hides col-2 when MAC q0 includes choice-X; q0 includes X | col-2 hidden across all SQ rows | |
| C-QTSEL-125 | MTM | choiceSelect | Column hidden: specN re-evaluated against visible | MTM q1 5 cols SQ-1 specN=exact:3; choiceSelect hides col-5 → 4 remain; SQ-1 selects 3 from 4 | 3 from 4 visible; exact:3 satisfied; submit OK | |
| C-QTSEL-126 | MTT | choiceSelect | Right half of bipolar scale hidden | MTT q1 7 scale points; choiceSelect hides points 5,6,7 (right half) | right half not selectable; only points 1-4 available; scale skewed left | |
| C-QTSEL-127 | MTS | subQuestionSelect | SQ shown when FA q0 > threshold | MTS q1; SQ-3 shown when FA q0 > 5; q0=7 | SQ-3 row displayed; respondent can answer it | |
| C-QTSEL-128 | MTS | subQuestionSelect | SQ hidden when FA q0 ≤ threshold | MTS q1; SQ-3 shown when FA q0 > 5; q0=3 | SQ-3 row hidden | |
| C-QTSEL-129 | MTM | subQuestionSelect | SQ shown when MAC q0 includes choice | MTM q1; SQ-2 shown when MAC q0 includes choice-B; q0=A,B | SQ-2 shown (B included) | |
| C-QTSEL-130 | MTM | subQuestionSelect | SQ hidden when MAC q0 does not include choice | MTM q1; SQ-2 shown when MAC q0 includes choice-B; q0=A,C | SQ-2 hidden (B not in selection) | |
| C-QTSEL-131 | MTT | subQuestionSelect | Multiple SQs shown/hidden by same condition | MTT q1 4 SQs; SQs 2,3 shown when q0=A; SQs 1,4 always visible; q0=A | SQs 1,2,3,4 all visible; q0=A reveals 2,3 | |
| C-QTSEL-132 | MTS | subQuestionSelect | SQ revealed mid-session: answer starts blank | MTS q1; SQ-4 hidden (q0=B); q0 changes to A (SQ-4 condition now met) | SQ-4 appears with blank state; respondent answers fresh | |
| C-QTSEL-133 | MTM | subQuestionSelect | Hidden SQ had selection: cleared on hide | MTM q1; SQ-3 selects cols 1,2; condition changes to hide SQ-3 | SQ-3 hidden; cols 1,2 selection cleared from submission | |
| C-QTSEL-134 | RNK | questionSelect+choiceSelect | RNK shown; one item hidden by choiceSelect | RNK q2 questionSelect shows q1=A; choiceSelect hides item-3 when q1=A; q1=A | q2 shown; item-3 hidden; 4 items to rank | |
| C-QTSEL-135 | RAT | questionSelect+choiceSelect | RAT shown; one row item hidden | RAT q2 questionSelect shows q1=A; choiceSelect hides item-2 when q1=A; q1=A | q2 shown; item-2 row hidden; 4 items to rate; total enforced on visible | |
| C-QTSEL-136 | FAL | questionSelect+choiceSelect | FA shown; no choices to filter (N/A for FA) | FAL q2 questionSelect shows q1=A; no choiceSelect applicable; q1=A | q2 shown; no choice filtering relevant for FAL; standard text input | |
| C-QTSEL-137 | MTS | choiceSelect+subQuestionSelect | Both: column filter + row filter simultaneously | MTS q1; choiceSelect hides col-3; subQuestionSelect hides SQ-2; both conditions met | col-3 hidden from all rows; SQ-2 row hidden; effective matrix reduced in both dimensions | |
| C-QTSEL-138 | MTM | choiceSelect+subQuestionSelect | Column and row both filtered | MTM q1; choiceSelect hides col-1; subQuestionSelect hides SQ-3; conditions met | col-1 not selectable; SQ-3 not shown; specN recalculated on visible rows and cols | |
| C-QTSEL-139 | SAR | questionSelect | Gated by Note answer (N/A: Note has no answer) | SAR q2 questionSelect referencing Note n1 (no user answer exists) | Editor rejects or treats Note as invalid source; Note cannot gate other questions | |
| C-QTSEL-140 | MAC | questionSelect | Gated by FA numeric: value range condition | MAC q2 shown when FA q0 between 5 and 10; q0=7 | q2 shown (7 in range 5–10) | |
| C-QTSEL-141 | MAC | questionSelect | Gated by FA numeric: out of range | MAC q2 shown when FA q0 between 5 and 10; q0=11 | q2 hidden (11 > 10) | |
| C-QTSEL-142 | SAP | questionSelect | Gated by RAT total sum condition | SAP q3 shown when RAT q2 total > 50; RAT sum = 60 | q3 shown (60 > 50) | |
| C-QTSEL-143 | FA | questionSelect | Gated by RNK: no item ranked (empty ranking) | FA q2 shown when RNK q1 any item ranked; q1 has 0 items ranked | q2 hidden (no items ranked; condition not met) | |
| C-QTSEL-144 | SAR | questionSelect | Rapid question show/hide: no flicker in submission | SAR q2 gated by dynamic slider q1; respondent moves slider 10 times | q2 correctly shown or hidden based on final slider value; intermediate states do not corrupt submission | |
| C-QTSEL-145 | MTM | questionSelect | Matrix shown late in long survey (20+ questions ahead) | MTM q20 gated by q1 answer; 19 questions between; gating condition met | q20 shown at its position; logic resolved correctly across large question distance | |
| C-QTSEL-146 | MTT | choiceSelect+req | Required MTT narrowed to 1 col per row | MTT q1 required=all 4 SQs; choiceSelect hides 4 cols → 1 remains | each SQ auto-selects remaining col; rows hidden; submit OK | |
| C-QTSEL-147 | SAR | choiceSelect+req | Required SAR: auto-select fires when only 1 remains | SAR q2 required; questionSelect shows q2 when q1=A; choiceSelect leaves 1 choice; q1=A | q2 visible; 1 choice; auto-selected and hidden; survey advances | |
| C-QTSEL-148 | RAT | choiceSelect+req | Required RAT narrowed to 1 item: auto-filled | RAT q1 required percent=100; choiceSelect hides 4 → 1 remains | single item auto-filled with 100%; q1 hidden; submit OK | |
| C-QTSEL-149 | SAP | choiceSelect | 2 of 5 scale points remain after filter | SAP q1 5 scale points; choiceSelect hides 3 → 2 remain; not required | 2 scale points displayed; respondent picks one or skips (optional) | |
| C-QTSEL-150 | MAC | choiceSelect+req | Required MAC specN=exact:3 narrowed to exactly 3 → all 3 auto-selected | MAC q1 required specN=exact:3 5 choices; choiceSelect hides 2 → exactly 3 remain | displayed = specN count (3 = 3); all 3 remaining choices auto-selected; question hidden; survey advances without respondent interaction | |
| C-QTSEL-151 | MAC | choiceSelect+req | Required MAC specN=exact:N narrowed to exactly N but one is exclusive — auto-select NOT triggered | MAC q1 required specN=exact:2 5 choices; choiceSelect hides 3 → 2 remain; one of the 2 is exclusive | displayed = specN count BUT one choice is exclusive; ambiguous between (select only exclusive) vs. (select both non-exclusive); per spec, auto-select does NOT fire in this case; question rendered; respondent must choose | |


---

### C-QTRAND Additional Cases (C-QTRAND-048–078)

| Test ID | QT | Rand Mode | Scenario | Setup | Expected Result | NT |
|---|---|---|---|---|---|---|
| C-QTRAND-048 | SAR | random | 10 choices: all permuted | SAR q1 rand=random 10 choices; multiple runs | Order varies; all 10 present each run | |
| C-QTRAND-049 | MAC | random | 10 choices: large set | MAC q1 rand=random 10 choices | All 10 randomized; multi-select unaffected | |
| C-QTRAND-050 | SAR | flip | 10 choices: full reversal | SAR q1 rand=flip 10 choices | Half see 1→10; half see 10→1 | |
| C-QTRAND-051 | MAC | fixedLast | 3 choices fixed at bottom | MAC q1 rand=fixedLast; choices 8,9,10 fixed; 7 non-fixed | 8,9,10 always last in original order; 7 randomized above | |
| C-QTRAND-052 | SAR | random | 3 choices: small set | SAR q1 rand=random 3 choices; many runs | 6 possible orderings; none consistently first | |
| C-QTRAND-053 | RNK | random | 10 items: large ranking list | RNK q1 rand=random 10 items; multiple sessions | 10-item order varies; result by item ID | |
| C-QTRAND-054 | RAT | random | 10 items: large RAT | RAT q1 rand=random 10 items | 10 item rows randomized; total sum enforcement unchanged | |
| C-QTRAND-055 | SAR | random | Required SAR: order random, must answer | SAR q1 rand=random required=ON 5 choices | Choices randomized; required enforced by question ID not position | |
| C-QTRAND-056 | MAC | random | Required MAC specN=exact:2; random | MAC q1 rand=random required specN=exact:2 5 choices | Choices randomized; must select exactly 2 | |
| C-QTRAND-057 | MTS | flip | Required=All MTS rows flip | MTS q1 rand=flip required=all 4 rows | Half see original; half reversed; all rows required in both orderings | |
| C-QTRAND-058 | MTM | random | Required=Custom MTM; marked rows enforced by SQ ID | MTM q1 rand=random required=custom; SQs 1,3 required | Row order randomized; SQs 1,3 still required by ID | |
| C-QTRAND-059 | RNK | random | Required=All RNK: all items must be ranked | RNK q1 rand=random required=all 5 items | Randomized presentation; rank all 5 | |
| C-QTRAND-060 | MAC | random | Exclusive in random pool: position varies | MAC q1 rand=random 5 choices; choice-5 exclusive | choice-5 in varying positions; exclusive deselect unchanged | |
| C-QTRAND-061 | MAC | flip | Exclusive in flipped set | MAC q1 rand=flip 5 choices; choice-5 exclusive | Half see choice-5 at pos-5; half at pos-1; exclusive unchanged | |
| C-QTRAND-062 | MAC | fixedLast | Exclusive choice fixed last | MAC q1 rand=fixedLast; choice-5 exclusive AND fixed | choice-5 always last; 1-4 randomized; exclusive deselects others | |
| C-QTRAND-063 | RNK | fixedLast | Exclusive ranking item fixed last | RNK q1 rand=fixedLast; item-5 exclusive (No Preference); fixed | item-5 always last in list; selecting clears other ranks | |
| C-QTRAND-064 | MAC | absolute | Exclusive in absolute order: same position every visit | MAC q1 rand=absolute; choice-5 exclusive; same respondent | choice-5 always at same position; exclusive logic unchanged | |
| C-QTRAND-065 | SAR | random | Disabled choice in random pool: grayed not selectable | SAR q1 rand=random 5 choices; choice-3 disabled | choice-3 in random position; grayed; not selectable | |
| C-QTRAND-066 | MAC | random | Disabled choice in random pool (MAC) | MAC q1 rand=random 5 choices; choice-2 disabled | choice-2 in random position; grayed; specN calculated excluding disabled | |
| C-QTRAND-067 | MTS | random | Disabled cell in randomized column position | MTS q1 rand=random cols; SQ-1 col-3 disabled | col-3 in random col position; not selectable in SQ-1 regardless of position | |
| C-QTRAND-068 | SAR | random | choiceSelect hides after randomization | SAR q1 rand=random; choiceSelect hides choice-2 mid-session | choice-2 removed; remaining in adjusted order | |
| C-QTRAND-069 | MAC | fixedLast | fixedLast + choiceSelect reveals previously-fixed | MAC q1 rand=fixedLast; choice-5 fixed then hidden then re-shown | choice-5 returns to last position when revealed | |
| C-QTRAND-070 | SAR | absolute | Different respondents get different absolute orders | SAR q1 rand=absolute; respondent A vs respondent B | Each gets own consistent order; A ≠ B (different seeds) | |
| C-QTRAND-071 | MAC | absolute | Absolute order across survey re-opens | MAC q1 rand=absolute; respondent reopens partial survey | Same choice order on reopen; consistent | |
| C-QTRAND-072 | MTS | absolute | Absolute row order across partial submits | MTS q1 rand=absolute; respondent saves and returns | Same row order on return | |
| C-QTRAND-073 | SAR | flip | Flip with 3 choices: clean split | SAR q1 rand=flip 3 choices A,B,C | Half see A,B,C; half see C,B,A | |
| C-QTRAND-074 | RNK | flip | Flip with 100 respondents: ~50/50 | RNK q1 rand=flip 5 items; 100 respondents | ~50 see original; ~50 see reversed; data by item ID | |
| C-QTRAND-075 | RAT | flip | Flip with 10 items | RAT q1 rand=flip 10 items | Half see 1→10; half see 10→1; data by item ID | |
| C-QTRAND-076 | SAR | fixedLast | 0 fixed choices: same as random | SAR q1 rand=fixedLast; no choices flagged fixed | All randomized; equivalent to rand=random | |
| C-QTRAND-077 | SAR | fixedLast | All choices fixed: original order | SAR q1 rand=fixedLast; all 5 flagged fixed | All in original order; no randomization | |
| C-QTRAND-078 | MAC | fixedLast | Fixed choice in middle original position | MAC q1 rand=fixedLast; choice-3 (middle) flagged fixed | choice-3 fixed to last position; 1,2,4,5 randomized in first 4 | |


---

### C-MATRIX-COUNT Answer-Side Cases (C-MATRIX-COUNT-31–60)

| Test ID | Sub-group | QT | Scenario | Setup | Expected Result | NT |
|---|---|---|---|---|---|---|
| C-MATRIX-COUNT-31 | matrixInclusion-runtime | MTM | Initial state: only non-linked choices visible in target | MTM q1; inclusion SQ1→SQ2 for choices 1,2,3; nothing selected in SQ1 | SQ2 shows only choices 4,5; 1,2,3 not visible | |
| C-MATRIX-COUNT-32 | matrixInclusion-runtime | MTM | Select choice in source: revealed in target | MTM q1; inclusion SQ1→SQ2; SQ1 selects choice-1 | choice-1 appears in SQ2 alongside 4,5 | |
| C-MATRIX-COUNT-33 | matrixInclusion-runtime | MTM | Select multiple choices: all revealed | MTM q1; inclusion SQ1→SQ2 choices 1,2,3; SQ1 selects 1,2 | SQ2 shows 1,2,4,5; choice-3 still hidden | |
| C-MATRIX-COUNT-34 | matrixInclusion-runtime | MTM | Deselect in source: removed from target | MTM q1; SQ1 selects choice-1 (SQ2 shows 1,4,5); SQ1 deselects choice-1 | choice-1 removed from SQ2; SQ2 returns to 4,5 | |
| C-MATRIX-COUNT-35 | matrixInclusion-runtime | MTM | Target had revealed choice selected: cleared on deselect | MTM q1; SQ1 selects choice-2 (SQ2 reveals 2); SQ2 selects choice-2; SQ1 deselects choice-2 | choice-2 removed from SQ2; SQ2 choice-2 selection cleared | |
| C-MATRIX-COUNT-36 | matrixInclusion-runtime | MTM | Inclusion + required SQ: selections cover required | MTM q1; SQ2 required specN=unspecified; inclusion SQ1→SQ2; SQ1 selects all linked | SQ2 has linked choices; select ≥1 in SQ2; required satisfied; submit OK | |
| C-MATRIX-COUNT-37 | matrixInclusion-runtime | MTM | Inclusion reveals 0 + required SQ | MTM q1; SQ2 required; inclusion SQ1→SQ2; SQ1 selects nothing | SQ2 shows baseline only; if 0 visible and required: submit blocked | |
| C-MATRIX-COUNT-38 | matrixInclusion-runtime | MTM | Multiple sources → single target: union of revealed | MTM q1; SQ1→SQ3 choices 1,2; SQ2→SQ3 choices 3,4; SQ1 selects 1; SQ2 selects 3 | SQ3 shows 1,3 plus non-linked choices | |
| C-MATRIX-COUNT-39 | matrixInclusion-runtime | MTM | Inclusion + rand: revealed by col ID not position | MTM q1 rand=random cols; inclusion SQ1→SQ2; SQ1 selects choice-ID-2 | choice-ID-2 revealed in SQ2 regardless of column display position | |
| C-MATRIX-COUNT-40 | matrixInclusion-runtime | MTM | Inclusion + prohibition: reveal then immediately hidden | MTM q1; inclusion SQ1→SQ2 + prohibition SQ1↔SQ2; SQ1 selects choice-1 | inclusion reveals choice-1 in SQ2; prohibition hides it; net: choice-1 not selectable in SQ2 | |
| C-MATRIX-COUNT-41 | prohibition-runtime | MTM | Select in SQ1 hides from SQ2 | MTM q1; prohibition SQ1↔SQ2; SQ1 selects choice-1 | choice-1 hidden from SQ2 immediately | |
| C-MATRIX-COUNT-42 | prohibition-runtime | MTM | Deselect in SQ1 restores in SQ2 | MTM q1; prohibition SQ1↔SQ2; SQ1 selects then deselects choice-1 | choice-1 restored in SQ2; selectable again | |
| C-MATRIX-COUNT-43 | prohibition-runtime | MTM | Bidirectional: select in SQ2 hides from SQ1 | MTM q1; prohibition SQ1↔SQ2; SQ2 selects choice-2 | choice-2 hidden from SQ1 | |
| C-MATRIX-COUNT-44 | prohibition-runtime | MTM | Multiple choices prohibited simultaneously | MTM q1; prohibition SQ1↔SQ2; SQ1 selects choices 1,2 | choices 1,2 hidden from SQ2; SQ2 selects from remaining | |
| C-MATRIX-COUNT-45 | prohibition-runtime | MTM | Prohibition reduces pool below specN threshold | MTM q1; prohibition SQ1↔SQ2; SQ2 specN=exact:3; SQ1 selects 3 → 2 remain in SQ2 | 2 choices remain in SQ2; specN=exact:3 not achievable; per disabled/reduced-pool rule, specN ignored; SQ2 selects from 2 visible choices; submit succeeds. If SQ2 ends up with 0 selectable choices from prohibition: no validation error per empty-SQ prohibition rule; survey advances | |
| C-MATRIX-COUNT-46 | prohibition-runtime | MTT | MTT Bipolar does not support prohibition — spec explicitly excludes it | MTT q1; attempt to configure prohibition in editor | Editor disables or prevents prohibition configuration on Bipolar Matrix; prohibition logic is never evaluated; no choice hiding occurs (Note: prohibition IS supported on MTS Matrix Radio and MTM Matrix Checkbox — see CM-61/62) | |
| C-MATRIX-COUNT-47 | prohibition-runtime | MTM | Prohibition chain: SQ1↔SQ2 and SQ2↔SQ3 | MTM q1; prohibition SQ1↔SQ2 and SQ2↔SQ3; SQ1 selects choice-1; SQ2 selects choice-2 | choice-1 hidden in SQ2; choice-2 hidden in SQ3 and SQ1; chain correct | |
| C-MATRIX-COUNT-48 | prohibition-runtime | MTM | Submit with valid non-prohibited selections | MTM q1; prohibition SQ1↔SQ2; SQ1 selects choice-1; SQ2 selects choice-2 (different) | no overlap; both valid; submit OK | |
| C-MATRIX-COUNT-49 | prohibition-runtime | MTM | Inclusion + prohibition: net result | MTM q1; inclusion SQ1→SQ2 + prohibition SQ1↔SQ2; SQ1 selects choice-1 | inclusion reveals; prohibition hides; choice-1 not selectable in SQ2 | |
| C-MATRIX-COUNT-50 | prohibition-runtime | MTM | All choices prohibited: empty SQs — no validation error per spec | MTM q1; prohibition between every pair; SQ1 selects all choices | all choices hidden from all other SQs; per spec, empty SQ resulting from prohibition is NOT a validation error; survey advances on Next regardless of required=ON setting for those SQs | |
| C-MATRIX-COUNT-51 | specN-row-runtime | MTM | Global exact:2: all rows must select exactly 2 | MTM q1 3 SQs global specN=exact:2 5 cols; all rows select 2 | all satisfy exact:2; submit OK | |
| C-MATRIX-COUNT-52 | specN-row-runtime | MTM | Global exact:2: SQ-2 selects 1 — blocked | MTM q1 global specN=exact:2; SQ-2 selects 1 | SQ-2 violates exact:2; submit blocked with per-row error | |
| C-MATRIX-COUNT-53 | specN-row-runtime | MTM | Row override exact:1 on SQ-1; SQ-1 selects 2 | MTM q1 global specN=max:3; SQ-1 override exact:1; SQ-1 selects 2 | SQ-1 violates exact:1; submit blocked for SQ-1 | |
| C-MATRIX-COUNT-54 | specN-row-runtime | MTM | Row override exact:1 satisfied | MTM q1 global specN=max:3; SQ-1 override exact:1; SQ-1 selects 1 | SQ-1 satisfies; others satisfy max:3; submit OK | |
| C-MATRIX-COUNT-55 | specN-row-runtime | MTM | max:3 with 0 selections: allowed (not required) | MTM q1 specN=max:3 required=none; all SQs select 0 | 0 ≤ max:3; not required; submit OK | |
| C-MATRIX-COUNT-56 | specN-row-runtime | MTM | max:3 with exactly 3: allowed | MTM q1 specN=max:3; SQ-1 selects 3 | 3 ≤ max:3; valid | |
| C-MATRIX-COUNT-57 | specN-row-runtime | MTM | max:3 with 4: blocked | MTM q1 specN=max:3; SQ-1 selects 4 | 4 > max:3; submit blocked or 4th selection prevented | |
| C-MATRIX-COUNT-58 | specN-row-runtime | MTM | Exclusive overrides specN | MTM q1 specN=exact:2; SQ-1 col-5 exclusive; SQ-1 selects col-5 | Per spec: exclusive → specN ignored for SQ-1; col-5 alone valid | |
| C-MATRIX-COUNT-59 | specN-row-runtime | MTM | Disabled choice reducing pool → specN ignored | MTM q1 specN=exact:3; SQ-1 col-3 disabled; 4 selectable; SQ-1 selects 2 | Per spec: disabled preventing valid count → specN ignored; 2 accepted | |
| C-MATRIX-COUNT-60 | specN-row-runtime | MTM | specN applied after choiceSelect hides column | MTM q1 SQ-1 specN=exact:3; choiceSelect hides col-3 → 4 remain; SQ-1 selects 3 | 3 from 4 visible; exact:3 satisfied; submit OK | |
| C-MATRIX-COUNT-61 | prohibition-runtime | MTS | MTS (Matrix Radio) supports prohibition: SQ1 selection hides same choice in SQ2 | MTS q1 4 SQs 5 choices; prohibition SQ1↔SQ2; SQ1 selects choice-2 | choice-2 hidden from SQ2 immediately; SQ2 must select from choices 1,3,4,5; prohibition applies to Matrix Radio just as it does to Matrix Checkbox | |
| C-MATRIX-COUNT-62 | prohibition-runtime | MTS | MTS prohibition: empty SQ from prohibition is NOT a validation error | MTS q1 required=All; prohibition SQ1↔SQ2; SQ1 selects the only 1 choice remaining in SQ2 (e.g. all other choices already prohibited away); SQ2 has no selectable choices | SQ2 is empty due to prohibition; per spec, empty SQ from prohibition produces no validation error; survey advances on Next | |
| C-MATRIX-COUNT-63 | prohibition-runtime | MTT | MTT Bipolar does NOT support prohibition — explicitly out of scope | MTT q1; prohibition configured between SQ1 and SQ2 (if editor allows) | Editor should prevent configuration; prohibition rules are not evaluated for Bipolar Matrix; no choice hiding occurs; behavior equivalent to no prohibition configured | |


---

### Screen-Out Logic Cases (C-SCREENING-001–024)

| Test ID | QT | Scenario | Setup | Expected Result | NT |
|---|---|---|---|---|---|
| C-SCREENING-001 | SAR | Single choice triggers screen-out | SAR q1 5 choices; choice-3 flagged screen-out | Respondent selects choice-3 → survey routes to screeningOut; Thank You shown; no further questions | |
| C-SCREENING-002 | SAR | Non-screen-out choice: survey continues | SAR q1 5 choices; choice-3 flagged screen-out; respondent selects choice-1 | Survey continues normally to next question; no screen-out triggered | |
| C-SCREENING-003 | SAR | All choices screen-out: any answer terminates | SAR q1 3 choices; all 3 flagged screen-out | Any selection triggers screen-out; survey ends regardless of which choice selected | |
| C-SCREENING-004 | SAR | Screen-out choice selected after back-navigation | SAR q1 screen-out on choice-2; respondent answers q2, navigates back, then selects choice-2 | Screen-out triggered on re-answer; survey ends; q2 answer discarded | |
| C-SCREENING-005 | SAR | Screen-out on hidden question: not triggered | SAR q2 screen-out on choice-A; questionSelect hides q2; condition not met | q2 hidden; screen-out for q2 not reachable; survey continues | |
| C-SCREENING-006 | MAC | Single choice in multi-select triggers screen-out | MAC q1 5 choices; choice-5 flagged screen-out; respondent selects choice-5 (alone or with others) | Selecting choice-5 triggers screen-out regardless of other selections; survey ends | |
| C-SCREENING-007 | MAC | Screen-out + exclusive: select exclusive screen-out choice | MAC q1; choice-5 exclusive AND screen-out; respondent selects choice-5 | Exclusive deselects others; screen-out fires; survey ends | |
| C-SCREENING-008 | MAC | Non-screen-out multi-select: survey continues | MAC q1; choice-5 screen-out; respondent selects choices 1,2,3 | No screen-out; survey continues with selections 1,2,3 | |
| C-SCREENING-009 | MAC | Screen-out on choice hidden by choiceSelect | MAC q1; choice-5 screen-out; choiceSelect hides choice-5; respondent cannot select it | choice-5 not displayed; screen-out not triggerable; survey continues normally | |
| C-SCREENING-010 | SAP | Scale point triggers screen-out | SAP q1 5 scale points; scale-point-1 flagged screen-out | Respondent selects scale-point-1 → screen-out; survey ends | |
| C-SCREENING-011 | SAP | Non-screen-out scale point: continues | SAP q1; scale-point-1 screen-out; respondent selects scale-point-3 | Survey continues normally | |
| C-SCREENING-012 | SAP | Screen-out on first and last scale points | SAP q1 5 points; points 1 and 5 both screen-out; points 2,3,4 safe | Selecting 1 or 5 → screen-out; selecting 2,3,4 → continues | |
| C-SCREENING-013 | MTS | Sub-question choice triggers screen-out | MTS q1; SQ-1 choice-3 flagged screen-out; respondent selects SQ-1=choice-3 | Screen-out triggered on SQ-1 choice-3 selection; survey ends | |
| C-SCREENING-014 | MTS | Screen-out in one SQ does not affect others at display | MTS q1; SQ-2 choice-1 screen-out; respondent selects SQ-1=choice-2 (no screen-out) | No screen-out on SQ-1 selection; survey continues; SQ-2 still needs answer | |
| C-SCREENING-015 | MTS | Screen-out triggered on submit (not on click) | MTS q1; SQ-3 choice-5 screen-out; respondent selects SQ-3=choice-5; clicks Next | Screen-out evaluated on Next/submit; survey ends after click | |
| C-SCREENING-016 | RNK | Ranked screen-out item triggers exit | RNK q1 5 items; item-3 flagged screen-out; respondent ranks item-3 | Ranking item-3 triggers screen-out; survey ends | |
| C-SCREENING-017 | RNK | Screen-out item not ranked: no exit | RNK q1; item-3 screen-out; respondent ranks items 1,2,4,5 only | item-3 not ranked; screen-out not triggered; survey continues | |
| C-SCREENING-018 | RNK | Screen-out item ranked #1 vs #5: both trigger | RNK q1; item-3 screen-out; respondent ranks item-3 at any position | Any ranking of item-3 (position 1 through 5) triggers screen-out | |
| C-SCREENING-019 | RAT | RAT items cannot trigger screen-out | RAT q1; attempt to flag item as screen-out in editor | Editor disables screen-out on RAT items; no screen-out configuration available | |
| C-SCREENING-020 | SAR | Yellow flag: screen-out with soft flag | SAR q1; choice-2 screen-out with yellow-flag=ON | Respondent selects choice-2 → survey ends; screeningOutFlg=2 (soft-flag screened out) stored in response metadata | |
| C-SCREENING-021 | SAR | Standard screen-out: no yellow flag | SAR q1; choice-2 screen-out with yellow-flag=OFF | Survey ends; screeningOutFlg=1 (standard screened out, no soft flag) stored in response metadata | |
| C-SCREENING-022 | SAR | Screen-out choice randomized: still triggers by ID | SAR q1 rand=random; choice-ID-3 screen-out; many sessions | choice-ID-3 in varying positions; selecting it always triggers screen-out by ID not position | |
| C-SCREENING-023 | MAC | Screen-out + specN: selecting screen-out choice exits before specN check | MAC q1 specN=exact:2; choice-5 screen-out; respondent selects only choice-5 | Screen-out fires immediately; specN validation not reached; survey ends | |
| C-SCREENING-024 | SAR | Multiple screen-out rules on same question | SAR q1 5 choices; choices 2 and 4 both screen-out | Selecting either choice-2 or choice-4 triggers screen-out; choices 1,3,5 safe | |


---

### Disabled Choices Cases (C-DISABLED-001–026)

| Test ID | QT | Scenario | Setup | Expected Result | NT |
|---|---|---|---|---|---|
| C-DISABLED-001 | SAR | Disabled choice: visually grayed, not selectable | SAR q1 5 choices; choice-3 disabled | choice-3 displayed grayed out; clicking has no effect; other choices selectable normally | |
| C-DISABLED-002 | SAR | All choices disabled: question unanswerable | SAR q1 5 choices; all 5 disabled | All choices grayed; no selection possible; required check (if ON) cannot be satisfied; submit blocked or question skipped | |
| C-DISABLED-003 | SAR | Disabled choice + required: required on remaining selectable | SAR q1 required 5 choices; choice-1 disabled; 4 selectable | Respondent must select from 4 non-disabled choices; disabled choice not counted toward required | |
| C-DISABLED-004 | SAR | Disabled choice randomized: stays grayed in any position | SAR q1 rand=random 5 choices; choice-3 disabled | choice-3 in random position each run; always grayed; never selectable | |
| C-DISABLED-005 | SAR | Disabled choice + choiceSelect: both reduce visible/selectable | SAR q1; choice-2 disabled; choiceSelect hides choice-4; condition met | choice-2 grayed (shown but not selectable); choice-4 hidden (not shown); 3 fully selectable | |
| C-DISABLED-006 | MAC | Disabled choice: not selectable in multi-select | MAC q1 5 choices; choice-3 disabled | choice-3 grayed; cannot be selected; other choices multi-selectable normally | |
| C-DISABLED-007 | MAC | Disabled choice + specN=exact:3: specN ignored per spec | MAC q1 specN=exact:3; choice-2 disabled; 4 selectable | Per spec: disabled reducing pool below exact → specN ignored; any count from 4 selectable choices accepted | |
| C-DISABLED-008 | MAC | Disabled exclusive choice: exclusive cannot be triggered | MAC q1; choice-5 exclusive AND disabled | choice-5 grayed; exclusive deselect behavior dormant; multi-select from 1-4 freely | |
| C-DISABLED-009 | MAC | Disabled non-exclusive; exclusive selectable | MAC q1; choice-3 disabled; choice-5 exclusive (not disabled) | choice-3 grayed; choice-5 selectable; selecting choice-5 deselects 1,2,4 as normal | |
| C-DISABLED-010 | MAC | Disabled choice + fixedLast randomization | MAC q1 rand=fixedLast; choice-5 fixed; choice-3 disabled | choice-5 always last; choice-3 in randomized positions above (grayed); positions 1-4 have 3 selectable + choice-3 grayed | |
| C-DISABLED-011 | SAP | Disabled scale point: respondent cannot select it | SAP q1 5 scale points; scale-point-3 disabled | scale-point-3 grayed; clicking has no effect; respondent picks from 1,2,4,5 | |
| C-DISABLED-012 | SAP | All scale points disabled: question unanswerable | SAP q1 5 scale points; all disabled | No selection possible; if required: submit blocked; if optional: answer skipped | |
| C-DISABLED-013 | SAP | Disabled scale points + auto-select: 1 remaining | SAP q1 required 5 points; 4 disabled → 1 selectable | Single non-disabled point auto-selected; question hidden; required satisfied without respondent interaction | |
| C-DISABLED-014 | MTS | Disabled cell in specific SQ-col: not selectable | MTS q1; SQ-1 col-3 disabled via Disable Choices dialog | SQ-1 col-3 grayed; SQ-1 cannot select col-3; other SQ-col combinations unaffected | |
| C-DISABLED-015 | MTS | Disabled cell + required SQ: required on non-disabled | MTS q1 required=all; SQ-2 col-1 disabled; SQ-2 has 4 selectable cols | SQ-2 must select from 4 non-disabled cols; disabled col-1 not counted; required satisfied on any of 4 | |
| C-DISABLED-016 | MTS | Multiple disabled cells across different SQs | MTS q1; SQ-1 col-2 disabled; SQ-3 col-4 disabled; other SQ-col pairs normal | Specific cells grayed per config; no cross-row effect; each SQ independently disabled | |
| C-DISABLED-017 | MTS | Disabled col same as choiceSelect-hidden col: net same result | MTS q1; col-2 disabled AND choiceSelect hides col-2; both conditions met | col-2 not selectable via disabled AND not shown via choiceSelect; net: col-2 fully absent from interaction | |
| C-DISABLED-018 | MTM | Disabled choice in SQ reduces specN pool | MTM q1 SQ-1 specN=exact:2; SQ-1 col-3 disabled; 4 selectable; SQ-1 selects 2 | Per spec: if disabled prevents exact:2, specN ignored for SQ-1; else: select 2 from 4 non-disabled; submit OK | |
| C-DISABLED-019 | MTM | Disabled exclusive choice in SQ | MTM q1; SQ-2 col-5 exclusive AND disabled | col-5 grayed; exclusive for SQ-2 dormant; SQ-2 selects from cols 1-4 freely | |
| C-DISABLED-020 | MTM | Disabled choice + prohibition: both reduce selectable | MTM q1; SQ-1 col-3 disabled; prohibition SQ1↔SQ2 covers col-2 | col-3 always grayed in SQ-1; col-2 hidden in SQ-2 after SQ-1 action; both restrictions coexist | |
| C-DISABLED-021 | RNK | Disabled item: visually shown but not rankable | RNK q1 5 items; item-3 disabled | item-3 shown grayed; cannot be dragged or assigned a rank; other items rankable normally | |
| C-DISABLED-022 | RNK | Disabled item + required=all: required on non-disabled items | RNK q1 5 items required=all; item-3 disabled; 4 rankable | Must rank all 4 non-disabled items; disabled item excluded from required count | |
| C-DISABLED-023 | RAT | Disabled item row: cannot enter value | RAT q1 5 items; item-2 disabled | item-2 row grayed; input field locked; other items enterable; total enforced on non-disabled items | |
| C-DISABLED-024 | RAT | Disabled item + percent total: total enforced on non-disabled | RAT q1 5 items percent=100; item-3 disabled | item-3 locked at 0; remaining 4 items must sum to 100; item-3 not included in total | |
| C-DISABLED-025 | RAT | Multiple disabled items | RAT q1 5 items; items 1 and 5 disabled | items 1,5 locked at 0; items 2,3,4 editable; total=100 enforced on items 2,3,4 | |
| C-DISABLED-026 | FA | FA has no choices to disable | FA q1; disabled flag set (N/A for FA) | Editor disables or does not show disabled-choice option for FA; no disabled behavior | |


---

### Other-Specify Text Box Cases (C-TXTBOX-001–028)

| Test ID | QT | Scenario | Setup | Expected Result | NT |
|---|---|---|---|---|---|
| C-TXTBOX-001 | SAR | Text box appears when other-specify choice selected | SAR q1 5 choices; choice-5 has txtBox=ON ('Other'); respondent selects choice-5 | Text input field appears below choice-5; respondent can type free text | |
| C-TXTBOX-002 | SAR | Text box hidden when other-specify choice deselected | SAR q1; choice-5 has txtBox; respondent selects choice-5 (text box appears) then selects choice-3 | Text box disappears when choice-5 deselected; typed text cleared; choice-3 selected only | |
| C-TXTBOX-003 | SAR | Text box not shown for non-other choice | SAR q1; choice-5 has txtBox; respondent selects choice-2 | No text box shown for choice-2; normal radio button behavior | |
| C-TXTBOX-004 | SAR | Text box required: must fill if other-specify selected | SAR q1 required; choice-5 txtBox=ON required; respondent selects choice-5 but leaves text empty | Submit blocked: text box for choice-5 must be filled when that choice is selected | |
| C-TXTBOX-005 | SAR | Text box optional: can leave empty | SAR q1; choice-5 txtBox=ON not required; respondent selects choice-5 and leaves text empty | Submit allowed; choice-5 recorded with empty other-specify text | |
| C-TXTBOX-006 | SAR | Multiple other-specify choices: only selected one shows box | SAR q1; choices 4 and 5 both have txtBox; respondent selects choice-4 | Text box appears for choice-4 only; choice-5 text box not shown (not selected); SAR is single-select | |
| C-TXTBOX-007 | SAR | Text box + randomization: box follows choice in any position | SAR q1 rand=random; choice-5 txtBox; choice-5 in random position; respondent selects it | Text box appears adjacent to choice-5 regardless of its random display position | |
| C-TXTBOX-008 | MAC | Text box appears for selected other-specify choice | MAC q1 5 choices; choice-5 txtBox=ON; respondent selects choice-5 | Text input appears for choice-5; other selected choices unaffected | |
| C-TXTBOX-009 | MAC | Text box for multiple selected other-specify choices | MAC q1; choices 3 and 5 both have txtBox; respondent selects both 3 and 5 | Text box appears for choice-3 AND choice-5 simultaneously; each independently fillable | |
| C-TXTBOX-010 | MAC | Text box disappears when choice deselected in multi-select | MAC q1; choice-3 txtBox; respondent selects 3 (text box shown, types text); then deselects 3 | Text box disappears; typed text cleared from submission | |
| C-TXTBOX-011 | MAC | Text box + exclusive: exclusive with txtBox selected | MAC q1; choice-5 exclusive AND txtBox; respondent selects choice-5 | Exclusive deselects others; text box for choice-5 appears; respondent fills text | |
| C-TXTBOX-012 | MAC | Text box required + specN=exact:2: both enforced | MAC q1 specN=exact:2; choice-3 and choice-5 have txtBox required; respondent selects both | Exactly 2 selected (choice-3 and 5); both text boxes must be filled; submit blocked if either empty | |
| C-TXTBOX-013 | MAC | Text box + fixedLast: txtBox choice fixed at bottom | MAC q1 rand=fixedLast; choice-5 txtBox AND fixed last; respondent selects choice-5 | choice-5 always last; text box appears when selected; content recorded | |
| C-TXTBOX-014 | SAP | Scale point with txtBox: text appears when point selected | SAP q1 5 scale points; scale-point-5 has txtBox=ON ('Tell us more'); respondent selects point-5 | Text input appears below scale-point-5; respondent types elaboration | |
| C-TXTBOX-015 | SAP | Scale point txtBox not shown for other points | SAP q1; scale-point-5 has txtBox; respondent selects scale-point-3 | No text box shown; normal scale selection behavior | |
| C-TXTBOX-016 | SAP | Scale point txtBox + randomized scale | SAP q1 rand=flip; scale-point-5 txtBox; scale-point-5 in first position after flip | Text box follows scale-point-5 to its new display position; appears when selected | |
| C-TXTBOX-017 | MTS | SQ-col cell has txtBox: text appears on selection | MTS q1; SQ-2 col-4 cell has txtBox=ON; respondent selects SQ-2=col-4 | Text input appears in or adjacent to SQ-2 col-4 cell; respondent enters text | |
| C-TXTBOX-018 | MTS | SQ-col txtBox: text not shown for other SQ selections | MTS q1; SQ-2 col-4 txtBox; respondent selects SQ-2=col-3 | No text box for col-3; SQ-2 col-4 text box not shown | |
| C-TXTBOX-019 | MTS | Multiple SQ-col cells with txtBox: only selected cells show box | MTS q1; SQ-1 col-3 txtBox AND SQ-3 col-5 txtBox; respondent selects both | Text box for SQ-1 col-3 AND SQ-3 col-5 shown; other cells unaffected | |
| C-TXTBOX-020 | MTM | Multi-select cell with txtBox: box appears on selection | MTM q1; SQ-1 col-5 has txtBox=ON; respondent selects SQ-1 col-5 (among others) | Text box appears for col-5 in SQ-1; other selected cols in SQ-1 unaffected | |
| C-TXTBOX-021 | MTM | MTM txtBox + specN: specN still applies to selection count | MTM q1 SQ-1 specN=exact:2; SQ-1 col-4 txtBox; respondent selects cols 3 and 4 | Exactly 2 selected (satisfies specN); text box for col-4 shown and fillable; submit OK if text filled (if required) | |
| C-TXTBOX-022 | MTM | MTM txtBox deselected: box cleared | MTM q1; SQ-2 col-3 txtBox; respondent selects col-3 (text box shown, types text); deselects col-3 | Text box disappears; text cleared from submission for SQ-2 col-3 | |
| C-TXTBOX-023 | RNK | Ranked item with txtBox: text appears when item ranked | RNK q1 5 items; item-5 has txtBox=ON ('Other'); respondent ranks item-5 | Text input appears for item-5 when it is ranked; respondent elaborates | |
| C-TXTBOX-024 | RNK | Ranked txtBox item loses box when unranked | RNK q1; item-5 txtBox; respondent ranks item-5 (text box + text entered); then removes rank | Text box disappears; text cleared; item-5 back to unranked | |
| C-TXTBOX-025 | RNK | txtBox item not ranked: no text box | RNK q1; item-5 txtBox; respondent ranks all items except item-5 | No text box for item-5 (not ranked); text boxes only appear for ranked txtBox items if applicable | |
| C-TXTBOX-026 | SAR | Text box maxLength enforced on other-specify input | SAR q1; choice-5 txtBox with maxLength=50; respondent selects choice-5 and types 60 chars | Text input enforces 50-char limit in real time; characters beyond 50 rejected or truncated | |
| C-TXTBOX-027 | SAR | Text box submission: other-specify text recorded in result | SAR q1; choice-5 txtBox; respondent selects choice-5 and types 'Custom answer'; submits | Submission contains choice-5 selected AND other-specify text = 'Custom answer'; both recorded | |
| C-TXTBOX-028 | MAC | Text box + questionSelect: question hidden, text boxes not shown | MAC q2; choice-3 txtBox; questionSelect hides q2; condition not met | q2 hidden; no text boxes rendered; text box content not included in submission | |
| C-TXTBOX-029 | SAR | Auto-select blocked when sole remaining choice has required textbox | SAR q1 required 5 choices; choiceSelect hides 4 → only choice-5 remains; choice-5 has required textbox | choice-5 is the sole visible choice; auto-selection is NOT triggered because choice-5 has a required textbox that needs manual input; question remains visible; respondent must select choice-5 AND fill the textbox before submit succeeds | |

## Required Validation — Question Level (V-REQ-Q) — Answer Runtime

| Test ID | Scenario | Question Setup | Respondent Action | Expected Result | Tested |
|---|---|---|---|---|---|
| V-REQ-Q-01 | Required=ON; respondent answers | SAR Q1, Required=ON | Select one choice; click Submit | Submission succeeds; no error shown | |
| V-REQ-Q-02 | Required=ON; respondent skips | SAR Q1, Required=ON | Leave Q1 blank; click Submit | Error displayed: "This question is required" (or locale equivalent); submission blocked | |
| V-REQ-Q-03 | Required=OFF; respondent skips | SAR Q1, Required=OFF | Leave Q1 blank; click Submit | Submission succeeds; no error | |
| V-REQ-Q-04 | Required=ON; question hidden by questionSelect (condition false) | SAR Q1, Required=ON; questionSelect: show when Q0=choice-A; Q0=choice-B | Submit without answering Q1 (Q1 not rendered) | Q1 is hidden; required check bypassed; submission succeeds | |
| V-REQ-Q-05 | Required=ON; question on page after screeningOut | Q1 SAR with screeningOut on one choice; Q2 Required=ON on p2 | Respondent selects the screened-out choice on Q1 | Survey terminates at Q1; Q2 is never evaluated; no required error for Q2 | |
| V-REQ-Q-06 | Required flag state after toggle and reload | SAR Q1 toggled ON→OFF→ON; survey saved and reopened | Respondent skips Q1; submits | Required=ON (last saved state); error shown; submission blocked | |
| V-REQ-Q-07 | Required on duplicated question | SAR Q1 Required=ON; survey duplicated; open duplicate | Skip Q1 in duplicate; submit | Required flag preserved on copy; same error behaviour | |
| V-REQ-Q-08 | Required + all choices filtered by choiceSelect → 0 visible | MAC Q1 Required=ON; choiceSelect hides all choices based on Q0 answer; condition active | Navigate to Q1 (0 choices visible); submit | Q1 rendered with no choices; either auto-skipped (no answer possible) OR system ignores required for empty-choice state; no blocking error | |
| V-REQ-Q-09 | FA Required; respondent types exactly 1 character | FA Q1, Required=ON, minLength=1 | Type single non-whitespace character; submit | Submission succeeds; minimum satisfied | |
| V-REQ-Q-10 | FA Required; respondent types only whitespace | FA Q1, Required=ON | Type spaces/tabs only; click Submit | Field trimmed to empty string; required error shown; submission blocked | |
| V-REQ-Q-11 | RNK required=None; partial rank (2 of 5 items ranked) → submit succeeds | RNK Q1, 5 choices, required=OFF | Rank choice-1 as 1st, choice-2 as 2nd; leave choices 3–5 unranked; click Next | Required=None: partial ranking is acceptable; 3 unranked items have no recorded rank; survey advances without error | |
| V-REQ-Q-12 | RNK required=All; partial rank (4 of 5 ranked) → submit blocked | RNK Q1, 5 choices, required=All | Rank 4 of 5 items; leave one unranked; click Next | Required=All: all 5 choices must be ranked; 1 unranked item → error #15 required validation fires (onNext); survey does NOT advance; respondent must rank all 5 | |
| V-REQ-Q-13 | RNK non-consecutive ranks → consecutive-rank error fires | RNK Q1, 5 choices, required=All | Rank choice-1 as rank-1, choice-3 as rank-3 (skip rank-2); click Next | Error #16: `mint.survey_answer.error_summary_ranking_not_consecutive` — ranking must be consecutive with no gaps; survey does NOT advance; respondent must fill rank-2 | |

---

## Required Validation — Sub-question Level (V-REQ-SQ) — Answer Runtime

| Test ID | Mode | Scenario | Question Setup | Respondent Action | Expected Result | Tested |
|---|---|---|---|---|---|---|
| V-REQ-SQ-01 | All | Answer all rows | MTS Q1, Required=All, 4 rows | Select one option per row; submit | Submission succeeds | |
| V-REQ-SQ-02 | All | Skip one row | MTS Q1, Required=All, 4 rows | Leave row 3 blank; submit | Error on row 3 only: row required; other rows pass | |
| V-REQ-SQ-03 | All | Skip all rows | MTS Q1, Required=All, 4 rows | Leave all rows blank; submit | Error shown per unanswered row; all 4 rows flagged | |
| V-REQ-SQ-04 | Custom | Answer only required rows | MTM Q1, Required=Custom, rows 1 and 3 required | Answer rows 1 and 3; leave rows 2, 4, 5 blank; submit | Submission succeeds; non-required rows not enforced | |
| V-REQ-SQ-05 | Custom | Skip a required row | MTM Q1, Required=Custom, rows 1 and 3 required | Answer row 1; skip row 3; submit | Error on row 3; row 1 passes; rows 2,4,5 pass | |
| V-REQ-SQ-06 | Custom | Invalid format on non-required row | MTM Q1, Required=Custom, rows 1–2 required; specifyN=exact 2 on row 4 | Answer rows 1–2; on row 4 select only 1 (violating specifyN); submit | Error on row 4 (format violated) even though row 4 not required; format still enforced | |
| V-REQ-SQ-07 | OFF | Skip entire matrix | MTS Q1, Required=OFF | Leave all rows blank; submit | Submission succeeds; matrix fully optional | |
| V-REQ-SQ-08 | OFF | Partial invalid answer on non-required row | MTM Q1, Required=OFF; specifyN=exact 2 on row 2 | Answer row 2 with 1 choice; submit | Error on row 2 (specifyN violated even though row not required); format enforced on partial answers | |
| V-REQ-SQ-09 | All + hidden row | Required row hidden by subQuestionSelect | MTS Q1, Required=All, 4 rows; subQuestionSelect hides row 2 when condition true; condition true | Answer rows 1, 3, 4; row 2 hidden; submit | Row 2 hidden → required bypassed; submission succeeds | |
| V-REQ-SQ-10 | All + hidden row | Required row hidden by matrixInclusion | MTM Q1, Required=All; matrixInclusion source Q0 includes rows 1, 3, 5 only (row 2, 4 excluded) | Answer rows 1, 3, 5; rows 2 and 4 excluded; submit | Excluded rows bypass required check; submission succeeds | |
| V-REQ-SQ-11 | All + randomization | Rows shuffled; all still required | MTS Q1, Required=All, 4 rows, rand=random | Rows appear in random order; answer all; submit | All rows required regardless of display order; submission succeeds when all answered | |
| V-REQ-SQ-12 | Custom | 0 rows marked required in Custom mode | MTM Q1, Required=Custom, no rows marked required | Skip all rows; submit | Behaves as OFF; submission succeeds | |
| V-REQ-SQ-13 | Custom | All rows marked required in Custom mode | MTM Q1, Required=Custom, all 4 rows marked required | Skip row 3; submit | Equivalent to All Required; error on row 3 | |
| V-REQ-SQ-14 | Recovery | Mode switch state persistence | MTS Q1; mode changed All→Custom→OFF→All; saved; reopened | Skip row 2; submit | Final mode is All Required; error shown on row 2 | |
| V-REQ-SQ-15 | Persistence | Duplicate matrix question | MTM Q1, Required=Custom, rows 1 and 3 required; survey duplicated | Open duplicate; skip row 3; submit | Required=Custom with rows 1 and 3 preserved; error on row 3 | |
| V-REQ-SQ-16 | Cross | Custom required row + specifyN=2; select 1 | MTM Q1, Required=Custom, row 2 required, specifyN=exact 2 | On row 2 select 1 choice; submit | specifyN error on row 2 (must select exactly 2); required separate from specifyN | |
| V-REQ-SQ-17 | Cross | Custom required row + specifyN=2 + exclusive selected | MTM Q1, Required=Custom, row 2 required, specifyN=exact 2; choice-5 exclusive | On row 2 select exclusive choice-5 only; submit | Exclusive override: specifyN rule ignored; row 2 has answer (exclusive); submission succeeds | |
| V-REQ-SQ-18 | Cross | Custom required row + specifyMax=3; select 4 | MTM Q1, Required=Custom, row 2 required, specifyMax=3 | On row 2 select 4 choices; submit | Error: exceeds maximum 3; specifyMax enforced regardless of required | |
| V-REQ-SQ-19 | Edge | Switch Custom to All: previously-unmarked rows now required | MTM Q1, mode was Custom (only row 1 required); switched to All | Skip row 3; submit | All rows now required; error on row 3 | |
| V-REQ-SQ-20 | Edge | Single-row matrix, Custom, row required | MTS Q1, 1 sub-question, Required=Custom, row 1 marked required | Leave row 1 blank; submit | Error on row 1; single required row enforced | |

---

## Specify Number of Choice — Answer Runtime (V-SPECN)

Applies to: MAC (question-level), MTM (per-sub-question). Override rules from spec page 1235321062.

| Test ID | Type | Mode | Scenario | Setup | Respondent Action | Expected Result | Tested |
|---|---|---|---|---|---|---|---|
| V-SPECN-01 | MAC | NONE / Req ON | Required MAC, no count restriction; answer 1 | MAC Q1, Required=ON, specifyN=NONE, 5 choices | Select 1 choice; submit | Submission succeeds; any non-zero count satisfies required | |
| V-SPECN-02 | MAC | NONE / Req ON | Required MAC, skip entirely | MAC Q1, Required=ON, specifyN=NONE | Leave blank; submit | Required error; submission blocked | |
| V-SPECN-03 | MAC | NONE / Req OFF | Optional MAC, skip | MAC Q1, Required=OFF, specifyN=NONE | Leave blank; submit | Submission succeeds | |
| V-SPECN-04 | MAC | NONE / Req OFF | Optional MAC, select multiple | MAC Q1, Required=OFF, specifyN=NONE, 5 choices | Select 3 choices; submit | Submission succeeds; no count restriction | |
| V-SPECN-05 | MAC | Exact=3 / Req ON | Select exactly 3 | MAC Q1, Required=ON, specifyN=exact 3, 5 choices | Select choices 1, 2, 3; submit | Submission succeeds | |
| V-SPECN-06 | MAC | Exact=3 / Req ON | Select fewer than 3 (2) | MAC Q1, Required=ON, specifyN=exact 3, 5 choices | Select choices 1 and 2; submit | Error: must select exactly 3 | |
| V-SPECN-07 | MAC | Exact=3 / Req ON | Select more than 3 (4) | MAC Q1, Required=ON, specifyN=exact 3, 5 choices | Attempt to select 4 choices | UI prevents 4th selection OR error on submit: must select exactly 3 | |
| V-SPECN-08 | MAC | Exact=1 / Req ON | Select exactly 1 | MAC Q1, Required=ON, specifyN=exact 1, 5 choices | Select 1 choice; submit | Submission succeeds | |
| V-SPECN-09 | MAC | Exact=5 (=choiceCount) / Req ON | Select all choices | MAC Q1, Required=ON, specifyN=exact 5, 5 choices | Select all 5; submit | Submission succeeds | |
| V-SPECN-10 | MAC | Exact=3 / Req OFF | Select 3 (exact match) | MAC Q1, Required=OFF, specifyN=exact 3, 5 choices | Select 3; submit | Submission succeeds | |
| V-SPECN-11 | MAC | Exact=3 / Req OFF | Select 0 (skip) | MAC Q1, Required=OFF, specifyN=exact 3, 5 choices | Leave blank; submit | Submission succeeds; Required=OFF and no answer → skip allowed | |
| V-SPECN-12 | MAC | Max=3 / Req ON | Select exactly 3 (at max) | MAC Q1, Required=ON, specifyMax=3, 5 choices | Select 3; submit | Submission succeeds | |
| V-SPECN-13 | MAC | Max=3 / Req ON | Select 1 (under max) | MAC Q1, Required=ON, specifyMax=3, 5 choices | Select 1; submit | Submission succeeds; any count ≤ max satisfies required | |
| V-SPECN-14 | MAC | Max=3 / Req ON | Select 4 (exceeds max) | MAC Q1, Required=ON, specifyMax=3, 5 choices | Attempt to select 4 choices | UI prevents 4th OR error: must not exceed 3 | |
| V-SPECN-15 | MAC | Max=1 / Req ON | Select 1 (at max) | MAC Q1, Required=ON, specifyMax=1, 5 choices | Select 1; submit | Submission succeeds | |
| V-SPECN-16 | MAC | Max=3 / Req OFF | Select 0 | MAC Q1, Required=OFF, specifyMax=3, 5 choices | Leave blank; submit | Submission succeeds; Required=OFF, 0 ≤ max | |
| V-SPECN-17 | MAC | Exact=3 + Exclusive override | Exclusive selected; specifyN ignored | MAC Q1, specifyN=exact 3, choice-5 exclusive; 5 choices | Select only choice-5 (exclusive); submit | Exclusive override: specifyN rule ignored; 1 answer (exclusive) is valid; submission succeeds | |
| V-SPECN-18 | MAC | Exact=3 + Exclusive override | Non-exclusive < 3 after exclusive deselects | MAC Q1, specifyN=exact 3, choice-5 exclusive; select choice-1 then choice-5 | choice-1 deselected by exclusive; only choice-5 remains (1 answer) | Exclusive override applies; 1 answer with exclusive is valid | |
| V-SPECN-19 | MAC | Max=3 + Exclusive override | Exclusive selected; specifyMax ignored | MAC Q1, specifyMax=3, choice-4 exclusive; 5 choices | Select only choice-4 (exclusive); submit | Exclusive override: specifyMax ignored; submission succeeds | |
| V-SPECN-20 | MAC | Exact=3 + Disabled choices (pool reduced to 2) | 2 active choices remain; specifyN ignored | MAC Q1, specifyN=exact 3; choices 4 and 5 disabled; only 3 choices; 1 disabled further | Select all 2 available choices; submit | Disabled choices reduce available pool below N; specifyN rule ignored; 2 answers accepted | |
| V-SPECN-21 | MAC | Max=3 + Disabled choices | Some disabled; effective pool ≥ max | MAC Q1, specifyMax=3; 1 of 5 choices disabled; 4 available | Select 3; submit | Disabled choice does not reduce pool below max; specifyMax still enforced; 3 → OK | |
| V-SPECN-22 | MAC | Exact=3 + non-exclusive < 3 due to one exclusive | Spec example: 1 exclusive in set of 4; select 2 non-exclusive + exclusive → deselects one | MAC Q1, specifyN=exact 3, choice-4 exclusive; 4 choices total | Select choices 1, 2; then select exclusive choice-4; choices 1,2 deselected; only choice-4 remains (1) | Exclusive override active: specifyN rule not applied to exclusive answer; submission succeeds | |
| V-SPECN-23 | MTM | Exact=2 per row / Req All | Answer each row with exactly 2 | MTM Q1, specifyN=exact 2 on all rows, Required=All; 5 choices per row | Select 2 on each row; submit | All rows satisfy specifyN; submission succeeds | |
| V-SPECN-24 | MTM | Exact=2 per row / Req All | One row has 1 selection | MTM Q1, specifyN=exact 2 on all rows, Required=All | On row 3 select only 1; submit | Error on row 3: must select exactly 2; all other rows pass | |
| V-SPECN-25 | MTM | Exact=2 on row / Req Custom (row optional) | Skip optional row entirely | MTM Q1, specifyN=exact 2 on row 3; Required=Custom (row 3 NOT required) | Leave row 3 blank; submit | Row 3 not required; 0 answers on optional row → skip allowed (specifyN only applies when row has an answer) | |
| V-SPECN-26 | MTM | Exact=2 on row / Req Custom (row required) | Select 1 on required row | MTM Q1, specifyN=exact 2 on row 2; Required=Custom, row 2 required | Select 1 on row 2; submit | Error: row 2 required AND specifyN=2 not satisfied | |
| V-SPECN-27 | MTM | Max=3 per row / Req OFF | Select 4 on one row | MTM Q1, specifyMax=3 per row, Required=OFF | On row 1 attempt to select 4 | UI prevents 4th OR error: exceeds max 3 | |
| V-SPECN-28 | MTM | Exact=2 + exclusive on row | Exclusive selected on row; specifyN ignored | MTM Q1, specifyN=exact 2 on row 2, choice-4 exclusive | On row 2 select exclusive choice-4 only; submit | Exclusive override on row 2: specifyN ignored; 1 exclusive answer valid | |
| V-SPECN-29 | MTM | Exact=2 + matrixInclusion reduces choices to 1 | Available choices fall below N after inclusion filter | MTM Q1, specifyN=exact 2; matrixInclusion from Q0 leaves only 1 choice on row 3 | Select only available choice on row 3; submit | Disabled/reduced pool override: specifyN rule ignored for row 3; 1 answer accepted | |
| V-SPECN-30 | MTM | Req=All + specifyN=exact 2; required row + exclusive | Exclusive satisfies required without meeting specifyN | MTM Q1, Required=All, specifyN=exact 2 on all rows, choice-5 exclusive | On row 2 select exclusive choice-5; submit | Exclusive override: specifyN ignored on row 2; required satisfied (row has answer); OK | |
| V-SPECN-31 | MAC | Exact=3 / Req ON; answer changes from 3 to 2 before submit | Back-nav; reduce selection | MAC Q1, specifyN=exact 3 on 2-page survey; Q1 on p1; answer 3 then go to p2 then back; remove one selection | Submit from p2 after back | Error: must select exactly 3; specifyN re-evaluated at submit time | |
| V-SPECN-32 | MAC | Max=N where N equals total choices | Select all | MAC Q1, specifyMax=5, 5 choices, Required=ON | Select all 5; submit | 5 ≤ 5; submission succeeds | |
| V-SPECN-33 | MTM | specifyN=exact 2, Req=OFF per row; answer row with 0 | Leave row completely blank | MTM Q1, specifyN=exact 2 on row 3, Required=OFF | Leave row 3 blank; submit | Required=OFF; 0 answers on optional row → skip allowed (no specifyN error for blank optional row) | |
| V-SPECN-34 | MTM | specifyN=exact 2, Req=OFF per row; answer row with 1 | Partial answer on optional row | MTM Q1, specifyN=exact 2 on row 3, Required=OFF | Select 1 choice on row 3; submit | Row has a partial answer; specifyN enforced on partial responses: error (must select 2) | |
| V-SPECN-35 | MAC | Exact=3; 3 choices disabled, 2 remain | Pool reduced below N | MAC Q1, specifyN=exact 3, 5 choices; choices 3,4,5 disabled | Select both available choices (1 and 2); submit | Disabled override: specifyN=3 rule ignored because pool < N; 2 answers accepted | |
| V-SPECN-36 | MAC | Max=3 / Req ON; skip entirely | Required=ON but no selection | MAC Q1, specifyMax=3, Required=ON | Leave blank; submit | Required error (not specifyMax error); 0 < minimum required | |
| V-SPECN-37 | MTM | Req=All + specifyN=exact 2 + hidden row | Hidden row with Required+specifyN | MTM Q1, Required=All, specifyN=exact 2, row 3 hidden by subQuestionSelect | Answer all visible rows with 2 each; row 3 hidden; submit | Row 3 hidden → Required and specifyN both bypassed; submission succeeds | |
| V-SPECN-38 | MAC | Exact=N with N=choiceCount; one choice disabled | Effective N exceeds active pool | MAC Q1, specifyN=exact 4, 4 choices, choice-3 disabled; 3 choices active | Select all 3 active choices; submit | Disabled override: specifyN rule ignored (available < N); 3 answers accepted | |

---

## Page Break × Required — Answer Runtime (V-PAGEBREAK-11–20)

| Test ID | Scenario | Survey Setup | Respondent Action | Expected Result | Tested |
|---|---|---|---|---|---|
| V-PAGEBREAK-11 | Required Q on page 2; skip it; attempt submit on p2 | 2-page survey; Q1 optional on p1; Q2 Required=ON on p2 | Navigate to p2; leave Q2 blank; click Submit | Error on Q2: required; submission blocked on p2 | |
| V-PAGEBREAK-12 | Required Q on page 2; answer it; submit | 2-page survey; Q1 optional on p1; Q2 Required=ON on p2 | Navigate to p2; answer Q2; submit | Submission succeeds | |
| V-PAGEBREAK-13 | Required Q on page 1 blocks Next | 2-page survey; Q1 Required=ON on p1; Q2 on p2 | Leave Q1 blank; click Next | Navigation to p2 blocked; error on Q1 | |
| V-PAGEBREAK-14 | Required Q on page 1; answer; proceed | 2-page survey; Q1 Required=ON on p1; Q2 on p2 | Answer Q1; click Next | Navigation to p2 allowed; no error | |
| V-PAGEBREAK-15 | Required Q on p2 hidden by logic; bypass check | 2-page survey; Q1 SAR on p1; Q2 Required=ON on p2, hidden by questionSelect (show when Q1=A); Q1=B | Navigate to p2 (Q2 not rendered); submit | Q2 hidden; required check bypassed; submission succeeds | |
| V-PAGEBREAK-16 | Required Q on p2 shown by logic; enforced | 2-page survey; Q1 SAR on p1; Q2 Required=ON on p2, shown when Q1=A; Q1=A | Navigate to p2 (Q2 rendered); leave Q2 blank; submit | Q2 visible; required error; submission blocked | |
| V-PAGEBREAK-17 | Matrix Required=All on p2; skip rows | 2-page survey; MTM Q1 Required=All on p2 | Navigate to p2; leave rows blank; submit | Error per unanswered row; submission blocked | |
| V-PAGEBREAK-18 | Matrix Required=Custom on p2; skip required row | 2-page survey; MTM Q1 Required=Custom rows 1 and 2 required; on p2 | Navigate to p2; skip row 2; submit | Error on row 2; rows 3+ (optional) pass | |
| V-PAGEBREAK-19 | Back navigation; answer changed; re-validate required | 3-page survey; Q2 Required=ON on p2; answer Q2; go to p3; press Back; clear Q2 | Attempt to advance from p2 again after clearing Q2 | Required error on Q2; cleared answer not accepted for advance | |
| V-PAGEBREAK-20 | specifyN + page break; answer meets specifyN across pages | 2-page survey; MAC Q1 specifyN=exact 3 on p2 | Navigate to p2; select exactly 3 choices; submit | specifyN satisfied; submission succeeds | |

---

## FA/FAL Input Type — Answer Runtime (V-FA-001 – V-FA-008)

Tests **FA (Text Box) and FAL input type configuration** variants at Answer runtime. Covers all FA type variants: Text (maxLength), Date, Number (min/max), Email, Phone, URL, and regex pattern. Invalid-input errors (Error #8) fire **realTime** on input action. Required errors (Error #1) fire **onNext** only.

**Columns:** Test ID | Scenario Title | Setup Steps | Action Steps | Expected Outcome | Tested | **Related JIRA**

|Test ID|Scenario Title|Setup Steps|Action Steps|Expected Outcome|Tested|**Related JIRA**|
|---|---|---|---|---|---|---|
|V-FA-001|FA type=Text — maxLength=50 — at boundary and over boundary|Create survey with Q1 (FA, type=Text, maxLength=50, required=ON). Publish.|Open Answer. (a) Enter exactly 50 characters. Click Next. (b) Attempt to type a 51st character.|(a) Valid; survey advances. (b) 51st character is not accepted (input blocked at maxLength=50) OR real-time error displayed. Text capped at 50 characters.|NT|https://macromill.atlassian.net/browse/MINT-5870, https://macromill.atlassian.net/browse/MINT-4482|
|V-FA-002|FA type=Date — invalid input → real-time error; valid date → advances|Create survey with Q1 (FA, type=Date, required=ON). Publish.|Open Answer. (a) Enter "abcdef" (non-date string) and stop typing. (b) Clear and enter a valid date (e.g. "2025-03-15" or via date picker). Click Next.|(a) Real-time validation error fires immediately on invalid input: `mint.survey_answer.error_global_invalid_input` — invalid date format. Survey does not advance. (b) Error clears; survey advances; date recorded correctly.|NT|https://macromill.atlassian.net/browse/MINT-5870, https://macromill.atlassian.net/browse/MINT-7200|
|V-FA-003|FA type=Number — min=1, no max — below min → real-time error; at min and above → valid|Create survey with Q1 (FA, type=Number, min=1, no max configured, required=ON). Publish.|Open Answer. (a) Enter 0. (b) Enter 1. Click Next. (c) Enter 99999. Click Next.|(a) Real-time validation error fires on input: `mint.survey_answer.number_textbox_min_error` — value is below minimum (1). (b) Error clears; survey advances. (c) Valid; advances (no upper limit enforced).|NT|https://macromill.atlassian.net/browse/MINT-5870, https://macromill.atlassian.net/browse/MINT-4482, https://macromill.atlassian.net/browse/MINT-7200|
|V-FA-004|FA type=Number — required=ON — empty field → required error|Create survey with Q1 (FA, type=Number, required=ON). Publish.|Open Answer. Leave the number field empty. Click Next.|RequiredError displayed. Q1 not advanced. Entering any number and clicking Next succeeds.|NT|https://macromill.atlassian.net/browse/MINT-5283, https://macromill.atlassian.net/browse/MINT-5870|
|V-FA-005|FA type=Email — valid email → advances; invalid format → error|Create survey with Q1 (FA, type=Email, required=ON). Publish.|Open Answer. (a) Enter "user@example.com". Click Next. (b) Enter "not-an-email". Click Next.|(a) Valid; survey advances; email recorded. (b) Validation error: invalid email format. Submission blocked.|NT|https://macromill.atlassian.net/browse/MINT-5870|
|V-FA-006|FA type=Phone — valid JP phone → advances; invalid → error|Create survey with Q1 (FA, type=Phone, required=ON). Publish.|Open Answer. (a) Enter "09012345678" (valid 11-digit JP mobile format). Click Next. (b) Enter "123" (too short). Click Next.|(a) Valid; survey advances; number recorded. (b) Validation error: invalid phone number format. Submission blocked.|NT|https://macromill.atlassian.net/browse/MINT-5870|
|V-FA-007|FA type=URL — valid URL → advances; invalid → error|Create survey with Q1 (FA, type=URL, required=ON). Publish.|Open Answer. (a) Enter "https://example.com". Click Next. (b) Enter "not a url". Click Next.|(a) Valid; survey advances; URL recorded. (b) Validation error: invalid URL format. Submission blocked.|NT|https://macromill.atlassian.net/browse/MINT-5870|
|V-FA-008|FA type=Text with regex pattern — matching input → advances; non-matching → error|Create survey with Q1 (FA, type=Text, regex pattern=`^[A-Z]{2}-\d{4}$`, required=ON). Publish.|Open Answer. (a) Enter "AB-1234". Click Next. (b) Enter "ab-1234" (wrong case). Click Next.|(a) Matches regex; valid; survey advances. (b) Validation error: input does not match required pattern. Submission blocked.|NT|https://macromill.atlassian.net/browse/MINT-5870|

---

## Constant Sum / Percent-Total RAT — Answer Runtime (V-RAT-CS)

These cases cover **RAT (Constant Sum / Percent-total mode)** runtime behavior: slider increment snapping, overflow auto-adjustment, and submit-time total enforcement.

**Columns:** Test ID | Scenario Title | Setup Steps | Action Steps | Expected Outcome | Tested | Related JIRA

|Test ID|Scenario Title|Setup Steps|Action Steps|Expected Outcome|Tested|Related JIRA|
|---|---|---|---|---|---|---|
|V-RAT-CS-001|Slider snaps to nearest 10% increment|Create survey with Q1 (RAT, percent-total=100, 5 items). Publish.|Open Answer. Drag slider for item-1 to approximately 75%.|Slider snaps to 80% (nearest multiple of 10); 75% is not an acceptable resting position; displayed value rounds to 80%.|NT||
|V-RAT-CS-002|Overflow auto-adjustment: non-blocking individual notification fires|Create survey with Q1 (RAT, percent-total=100, 5 items). Publish.|Open Answer. Enter 60% for item-1, 60% for item-2 (sum would be 120%).|System automatically corrects total to 100%; individual-level notification shown: `mint.survey_answer.error_individual_total_excessive` — "The total exceeded 100%, so it was automatically corrected." This is non-blocking; no summary/global error. User can immediately click Next without further action.|NT||
|V-RAT-CS-003|Submit blocked when sum is below required total|Create survey with Q1 (RAT, percent-total=100, 5 items, required=ON). Publish.|Open Answer. Enter 40% for item-1, 30% for item-2, leave items 3–5 at 0%. Total = 70%. Click Next.|Error summary: `mint.survey_answer.error_summary_total_insufficient` — "Total must be 100%." Global error: `mint.survey_answer.error_groal_total_insufficient` — "Enter values so that the total is 100%." (Note: key is `error_groal_` not `error_global_` — intentional per spec.) Survey does NOT advance. Setting total to exactly 100% resolves error.|NT||
|V-RAT-CS-004|Button mode (±1%) increments and decrements value by 1 per press|Create survey with Q1 (RAT, percent-total=100, 5 items). Publish.|Open Answer. On item-1, click the "+" button 5 times. Then click "−" once.|Item-1 value increases by 1% per button press (0→1→2→3→4→5%); one "−" press decrements to 4%; total adjusts proportionally; no snap-to-10 constraint for button input (only slider has 10% snap).|NT||
|V-RAT-CS-005|Input field rejects non-numeric characters; accepts integers|Create survey with Q1 (RAT, percent-total=100, 5 items). Publish.|Open Answer. (a) Type "abc" into item-1 input field. (b) Type "50" into item-1 input field.|(a) Non-numeric input rejected; input field remains empty or shows 0; real-time validation if partially entered. (b) "50" accepted; displayed in field; total updates.|NT||
|V-RAT-CS-006|Optional RAT: ALL items left empty → survey advances without error|Create survey with Q1 (RAT, percent-total=100, 5 items, required=OFF). Publish.|Open Answer. Leave all 5 items at 0 (or blank). Click Next.|All items empty (0); per spec: if ALL response items are empty in optional mode → saved as "unanswered"; no total enforcement error; survey advances.|NT||
|V-RAT-CS-007|Optional RAT: at least one item has value → total enforcement triggered|Create survey with Q1 (RAT, percent-total=100, 5 items, required=OFF). Publish.|Open Answer. Enter 30% for item-1 only. Leave items 2–5 at 0%. Click Next.|At least one item has a value; total enforcement is triggered: 30% ≠ 100% → error: `mint.survey_answer.error_summary_total_insufficient`; survey does NOT advance; must bring total to 100% to proceed.|NT||

---

## FAL (Textbox QT) Multi-row — Answer Runtime (V-FAL-001 – V-FAL-003)

These cases cover **FAL** (the answer-side Textbox question type, equivalent to MaUS `FAL`). FAL renders one textbox per row; each row can have its own type constraint (number, code, alnum, email, string). The required mode operates independently of FA: modes are **All** (every row must be filled), **Customize** (specific rows flagged required), **Custom+Minimum** (at least N rows must be filled, no specific row), or **None** (entirely optional).

> **Note:** "Disabled" rows (hidden by logic) have their data deleted from submission; they do NOT count toward required/minimum counts.

**Columns:** Test ID | Scenario Title | Setup Steps | Action Steps | Expected Outcome | Tested | Related JIRA

|Test ID|Scenario Title|Setup Steps|Action Steps|Expected Outcome|Tested|Related JIRA|
|---|---|---|---|---|---|---|
|V-FAL-001|FAL required=All — missing any row blocks submission|Create survey with Q1 (FAL, 3 rows, required=All). Publish.|Open Answer. Fill rows 1 and 2; leave row 3 empty. Click Next.|Row 3 is empty; required=All demands every row be filled; validation error fires (onNext); survey does NOT advance; respondent must fill row 3.|NT||
|V-FAL-002|FAL required=Custom+Minimum — minimum N rows satisfied → advances|Create survey with Q1 (FAL, 5 rows, required=Custom+Minimum, minimum=3). Publish.|Open Answer. Fill rows 1, 2, and 3; leave rows 4 and 5 empty. Click Next.|3 of 5 rows filled ≥ minimum (3); required condition satisfied; survey advances without error. Leaving only 2 filled would block submission.|NT||
|V-FAL-003|FAL per-row type validation — number row rejects non-numeric input (realTime)|Create survey with Q1 (FAL, 2 rows: row-1 type=number, row-2 type=string). Publish.|Open Answer. (a) Type "abc" in row-1 (number row). (b) Type "123" in row-1. (c) Type any text in row-2 (string row).|(a) realTime error fires immediately on invalid input (Error #8: `mint.survey_answer.error_global_invalid_input`); field highlighted; not necessary to click Next. (b) Numeric value "123" accepted; no error. (c) Any string accepted in row-2; no type error.|NT||

---

## Count Matrix — Answer Behavior Cases (CM-001 – CM-012)

> **Count Matrix** (`countif`) is a condition type used within Selection Logic (questionSelect, subquestionSelect, choiceSelect, screeningOut). It counts selections within a matrix question that fall in the intersection of a defined sub-question range AND a choice range, then compares the count using one of 6 operators: `==`, `!=`, `>=`, `<=`, `>`, `<`. Source QT: MTS, MTM, MTT. Disabled choices and prohibition-violating selections are excluded from the count.

**Spec:** [Logic: Count Matrix](https://macromill.atlassian.net/wiki/spaces/survey/pages/1543635029)

**Columns:** Test ID | Scenario Title | Setup Steps | Action Steps | Expected Outcome | Tested | **Related JIRA**

|Test ID|Scenario Title|Setup Steps|Action Steps|Expected Outcome|Tested|**Related JIRA**|
|---|---|---|---|---|---|---|
|CM-001|MTS — countif >= threshold met → target question shown|Create survey: Q1 (MTS, 5 SQs, 5 choices labelled 1–5). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-5","1-2") >= 3. Publish.|Open Answer. In Q1: select choice-1 in SQ1, choice-2 in SQ2, choice-1 in SQ3. Click Next (count = 3).|Count = 3 ≥ 3 → Q2 is shown. Survey advances to Q2.|NT|https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-7730|
|CM-002|MTS — countif >= threshold NOT met → target question hidden|Same setup as CM-001.|In Q1: select choice-1 in SQ1, choice-2 in SQ2 only (count = 2). Click Next.|Count = 2 < 3 → Q2 is hidden. Survey skips Q2.|NT|https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-7730|
|CM-003|MTS — operator == exact match|Q1 (MTS, 4 SQs, 4 choices). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-4","1-2") == 2. Publish.|(a) Select in-range choices in exactly 2 SQs. Click Next. (b) Select in 3 SQs. Click Next.|(a) Count = 2 = 2 → Q2 shown. (b) Count = 3 ≠ 2 → Q2 hidden.|NT|https://macromill.atlassian.net/browse/MINT-7615, https://macromill.atlassian.net/browse/MINT-7730|
|CM-004|MTS — operator != (not equal) inverts condition|Q1 (MTS, 4 SQs, 4 choices). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-4","1-2") != 0. Publish.|(a) Select no in-range choices (count = 0). (b) Select in-range in 1 SQ (count = 1).|(a) Count = 0, equals 0 → Q2 hidden. (b) Count = 1 ≠ 0 → Q2 shown.|NT|https://macromill.atlassian.net/browse/MINT-7615, https://macromill.atlassian.net/browse/MINT-7730|
|CM-005|MTS — partial SQ range: answers outside range not counted|Q1 (MTS, 5 SQs, 4 choices). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-3","1-2") >= 3. Publish.|In Q1: select choice-1 in SQ4 and SQ5 (outside SQ range). Select no in-range choices for SQ1–3. Click Next.|Count = 0 (SQ4 and SQ5 not in range "S1-3"). Q2 hidden.|NT|https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-7730|
|CM-006|MTS — partial choice range: choices outside range not counted|Q1 (MTS, 3 SQs, 5 choices). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-3","1-2") >= 2. Publish.|In Q1: select choice-3 in SQ1, choice-4 in SQ2, choice-5 in SQ3 (all outside choice range 1-2). Click Next.|Count = 0 (choices 3, 4, 5 not in range "1-2"). Q2 hidden. Only choices 1 and 2 are counted.|NT|https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-7730|
|CM-007|MTM — multiple selections per SQ each count individually|Q1 (MTM, 3 SQs, 5 choices). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-3","1-3") >= 5. Publish.|In Q1: SQ1 select choices 1+2 (2 in range), SQ2 select choices 1+2+3 (3 in range), SQ3 select choices 4+5 (0 in range). Click Next.|Count = 2 + 3 + 0 = 5 ≥ 5 → Q2 shown. Each in-range selection in each SQ adds 1 to the total count.|NT|https://macromill.atlassian.net/browse/MINT-7730, https://macromill.atlassian.net/browse/MINT-6520|
|CM-008|MTM — disabled choices excluded from count|Q1 (MTM, 3 SQs, 5 choices; SQ1 choice-1 disabled). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-3","1-3") >= 3. Publish.|In Q1: SQ1 cannot select choice-1 (disabled). Select choice-2 in SQ1, choice-1 in SQ2, choice-1 in SQ3. Click Next.|Count = 1 + 1 + 1 = 3 ≥ 3 → Q2 shown. Disabled choice-1 in SQ1 is not counted even if visually present. Spec confirms: "Disabled choices are excluded from the total count."|NT|https://macromill.atlassian.net/browse/MINT-8144, https://macromill.atlassian.net/browse/MINT-7730|
|CM-009|MTM — specN caps maximum achievable count; condition must be satisfiable|Q1 (MTM, 3 SQs, 5 choices; global Specify=Max 1 per SQ). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-3","1-5") >= 4. Publish.|Attempt to answer Q1 selecting enough in-range choices to reach count ≥ 4.|Max possible count = 1 choice × 3 SQs = 3 (specN ceiling). Count can never reach 4. Q2 is never shown regardless of selections. (Editor-side: this config should be caught as invalid — see CM-ED-006.)|NT|https://macromill.atlassian.net/browse/MINT-8144, https://macromill.atlassian.net/browse/MINT-7615|
|CM-010|MTM — count drives subquestionSelect: SQ2 shown/hidden based on count|Q1 (MTM, 4 SQs, 4 choices). Logic: show SQ2 of Q1 itself if countif(Q1,"S1-4","1-2") >= 2 (self-referential SQ gating). Publish.|(a) Select in-range choices in 2+ SQs. (b) Select in-range in only 1 SQ.|(a) Count ≥ 2 → SQ2 displayed. (b) Count < 2 → SQ2 hidden. Required marks on SQ2 only enforced when SQ2 is visible.|NT|https://macromill.atlassian.net/browse/MINT-7730, https://macromill.atlassian.net/browse/MINT-7910|
|CM-011|MTS — count drives screeningOut: below threshold exits survey|Q1 (MTS, 5 SQs, 5-point scale). Logic: screeningOut if countif(Q1,"S1-5","1-2") < 2 (fewer than 2 positive/top-2-box responses). Publish.|In Q1: select choice-3 or higher in all 5 SQs (0 top-2 responses). Click Next.|Count = 0 < 2 → survey exits to screeningOut. No further questions shown. Respondent reaches Thank You / screeningOut page.|NT|https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-6126, https://macromill.atlassian.net/browse/MINT-7021|
|CM-012|MTT — Bipolar Matrix as countif source|Q1 (MTT Bipolar Matrix, 3 SQs, 5 choices). Q2 (SAR). Logic: show Q2 if countif(Q1,"S1-3","1-2") >= 2. Publish.|In Q1: select choice-1 in SQ1 and SQ2 (2 in-range selections). Click Next.|Count = 2 ≥ 2 → Q2 shown. Confirms Bipolar Matrix (MTT) is a valid source for countif, same as MTS/MTM.|NT|https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-7730|

---

## Additional Logic Combination Cases (C-2LOGIC-073 – C-2LOGIC-121)

Extends the P3 two-logic combination matrix to cover pairings not yet tested: subquestionSelect combinations, Disable Choices with logics, Switch to Radio with logics, textbox interactions, screen-out edge cases, and Count Matrix combinations.

|Test ID|Logic Combination|QT|Scenario|Setup|Expected Result|NT|**Related JIRA**|
|---|---|---|---|---|---|---|---|
|C-2LOGIC-073|required + subquestionSelect|MTS|Required SQ hidden by SQ Selection → required not enforced for that SQ|MTS q1 required=Customize; SQ1 marked required; subquestionSelect hides SQ1 when condition met; condition met|SQ1 not rendered; required mark skipped; submit allowed without SQ1 answer||https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-5283, https://macromill.atlassian.net/browse/MINT-7946|
|C-2LOGIC-074|required + subquestionSelect|MTM|Required-Customize SQ2 hidden → not enforced|MTM q1 required=Customize; SQ2 marked required; subquestionSelect hides SQ2; condition met|SQ2 hidden; required for SQ2 not enforced; submit allowed||https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-5283, https://macromill.atlassian.net/browse/MINT-7946|
|C-2LOGIC-075|specN + subquestionSelect|MTM|Per-SQ specN on SQ that is hidden → specN not enforced|MTM q1 SQ1 specN=exact:2; subquestionSelect hides SQ1; condition met|SQ1 not rendered; specN=exact:2 for SQ1 not enforced; submit without SQ1 answer succeeds||https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-6111, https://macromill.atlassian.net/browse/MINT-7946|
|C-2LOGIC-076|textbox + required|MAC|Required MAC; selected choice has required textbox; must fill textbox|MAC q1 required=ON; choice-3 has required textbox; respondent selects choice-3|Textbox appears; submit without filling → error; fill textbox → submit succeeds||https://macromill.atlassian.net/browse/MINT-4482, https://macromill.atlassian.net/browse/MINT-5283|
|C-2LOGIC-077|textbox + choiceSelect|SAR|choiceSelect hides choice that had textbox; answer cleared|SAR q1; choice-3 has textbox; choiceSelect hides choice-3 when q0=A; q0=A|choice-3 not displayed; textbox not shown; previous textbox answer (if any) cleared from submission||https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-4482|
|C-2LOGIC-078|textbox + questionSelect|SAR|questionSelect hides Q with textbox answer; answer cleared from submission|SAR q2; choice-3 has textbox; respondent fills it; then questionSelect hides q2 (condition changes)|q2 hidden; q2 choice and textbox answer cleared from final submission||https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-4482, https://macromill.atlassian.net/browse/MINT-7309|
|C-2LOGIC-079|Disable Choices + choiceSelect|MTM|Disable Choices removes cells; choiceSelect hides additional columns on top|MTM q1 SQ1: col-1 disabled; choiceSelect hides col-3 when condition met; condition met|col-1 disabled (not selectable); col-3 hidden by choiceSelect; SQ1 selectable from col-2,4,5 only||https://macromill.atlassian.net/browse/MINT-5282, https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-7401|
|C-2LOGIC-080|Disable Choices + prohibition|MTM|Disabled col's prohibition link is moot|MTM q1 SQ1 col-1 disabled; prohibition SQ1↔SQ2 on col-1|col-1 cannot be selected in SQ1; prohibition for col-1 in SQ2 effectively dormant; other prohibitions unaffected||https://macromill.atlassian.net/browse/MINT-5282, https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-7870|
|C-2LOGIC-081|Disable Choices + exclusive|MTM|Disabled col is exclusive; exclusive logic dormant|MTM q1 SQ1 col-5 exclusive AND disabled|col-5 cannot be selected (disabled); exclusive behavior never triggered in SQ1; other cols multi-selectable freely||https://macromill.atlassian.net/browse/MINT-5282, https://macromill.atlassian.net/browse/MINT-4013, https://macromill.atlassian.net/browse/MINT-6112|
|C-2LOGIC-082|switchToRadio + required|MTM|SQ1 is radio mode + required → exactly 1 selection required for SQ1|MTM q1 SQ1 switchToRadio=true; required=All|SQ1 renders as radio row; exactly 1 choice required; submit without SQ1 → required error; select 1 → valid||https://macromill.atlassian.net/browse/MINT-5833, https://macromill.atlassian.net/browse/MINT-5283|
|C-2LOGIC-083|switchToRadio + prohibition|MTM|SQ1 radio + prohibition SQ1↔SQ2 — selecting in SQ1 hides same choice in SQ2|MTM q1 SQ1 switchToRadio=true; prohibition SQ1↔SQ2|Select col-2 in SQ1 (radio); col-2 hidden in SQ2 (prohibition); re-select col-3 in SQ1; col-3 hidden in SQ2||https://macromill.atlassian.net/browse/MINT-5833, https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-7870|
|C-2LOGIC-084|switchToRadio + choiceSelect|MTM|SQ1 radio; choiceSelect hides columns → fewer radio options|MTM q1 SQ1 switchToRadio=true; choiceSelect hides col-4 when condition met; condition met|col-4 not displayed in SQ1 radio row; respondent selects from remaining cols; radio still enforces 1 selection||https://macromill.atlassian.net/browse/MINT-5833, https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-7309|
|C-2LOGIC-085|specN (Exact) + screeningOut|MAC|Exact specN + screen-out choice; select screen-out → exits before specN check|MAC q1 specN=exact:3; choice-5 screen-out; respondent selects choice-5 only|Survey exits to screeningOut without enforcing exact:3; specN check not reached||https://macromill.atlassian.net/browse/MINT-6111, https://macromill.atlassian.net/browse/MINT-6126, https://macromill.atlassian.net/browse/MINT-7021|
|C-2LOGIC-086|required + screeningOut|SAR|Required question; selecting screen-out choice → exits without required error|SAR q1 required=ON; choice-3 screen-out|Selecting choice-3 triggers screen-out; survey exits; no required error displayed (screen-out supersedes required); choosing no option → required error||https://macromill.atlassian.net/browse/MINT-5283, https://macromill.atlassian.net/browse/MINT-6126, https://macromill.atlassian.net/browse/MINT-7021|
|C-2LOGIC-087|matrixInclusion + subquestionSelect|MTM|SQ2 has matrixInclusion from SQ1; SQ2 also hidden by SQ Selection → inclusion moot|MTM q1; matrixInclusion SQ1→SQ2; subquestionSelect hides SQ2; condition met|SQ2 not rendered; matrixInclusion not visible or evaluated; SQ2 answer not recorded||https://macromill.atlassian.net/browse/MINT-7678, https://macromill.atlassian.net/browse/MINT-7880, https://macromill.atlassian.net/browse/MINT-7910|
|C-2LOGIC-088|prohibition + subquestionSelect|MTM|Prohibition SQ1↔SQ2; SQ2 hidden by SQ Selection → prohibition not applied to SQ2|MTM q1; prohibition SQ1↔SQ2; subquestionSelect hides SQ2; condition met|SQ2 not rendered; prohibition for SQ2 not enforced; SQ1 can select any choice freely||https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-7946|
|C-2LOGIC-089|textbox + choiceSelect + required|MAC|3-way: required MAC; choice with required textbox hidden by choiceSelect → textbox not enforced|MAC q1 required=ON; choice-3 has required textbox; choiceSelect hides choice-3 when condition met; condition met|choice-3 not displayed; textbox not shown; required for choice-3 textbox not enforced; respondent selects from remaining choices; submit valid||https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-4482, https://macromill.atlassian.net/browse/MINT-5283|
|C-2LOGIC-090|rand + subquestionSelect|MTS|Row order randomized; SQ Selection hides some rows; remaining rows in random order|MTS q1 rand=random rows; subquestionSelect hides SQ2 when condition met; condition met|SQ2 not rendered; remaining SQs (SQ1, SQ3, SQ4…) in random order; prohibition and required by SQ ID unaffected||https://macromill.atlassian.net/browse/MINT-4129, https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-7946|
|C-2LOGIC-091|questionSelect + prohibition|MTS|Q hidden by questionSelect → prohibition not applied; Q shown → prohibition enforced|MTS q2 prohibition SQ1↔SQ2; questionSelect hides q2 when q1=B; test both q1=A (shown) and q1=B (hidden)|q1=A: q2 shown; prohibition enforced (selecting col-X in SQ1 hides col-X in SQ2). q1=B: q2 hidden; prohibition not evaluated||https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-7309|
|C-2LOGIC-092|questionSelect + prohibition|MTM|Q hidden → prohibition moot; Q shown → prohibition active on visible rows|MTM q2 prohibition SQ1↔SQ2; questionSelect hides q2 when condition not met|q2 hidden: prohibition not evaluated; SQ1 unrestricted. q2 shown: selecting col in SQ1 hides same col in SQ2||https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-7309|
|C-2LOGIC-093|choiceSelect + prohibition|MTM|choiceSelect hides col from all rows; prohibition on that col now moot|MTM q1 prohibition SQ1↔SQ2 on col-3; choiceSelect hides col-3 globally when condition met|col-3 not displayed in any SQ; prohibition for col-3 dormant; SQ1 and SQ2 freely select from remaining cols||https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-7870|
|C-2LOGIC-094|subquestionSelect + randomization|MTM|SQ hidden + remaining SQs randomized — SQ ID tracking unaffected|MTM q1 rand=random rows; subquestionSelect hides SQ2; condition met|SQ2 not rendered; remaining SQs in random order; matrixInclusion and prohibition continue to reference SQs by ID not position||https://macromill.atlassian.net/browse/MINT-4129, https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-7946|
|C-2LOGIC-095|exclusive + screeningOut|MAC|Exclusive choice is also screen-out; selecting it clears others and exits survey|MAC q1 exclusive=choice-5 AND choice-5 screen-out; respondent first selects choices 1+2 then choice-5|Selecting choice-5: deselects 1+2 (exclusive); triggers screen-out; survey exits||https://macromill.atlassian.net/browse/MINT-4013, https://macromill.atlassian.net/browse/MINT-6112, https://macromill.atlassian.net/browse/MINT-6126|
|C-2LOGIC-096|screeningOut + choiceSelect — screen-out choice hidden|SAR|choiceSelect hides the screen-out choice; screen-out no longer reachable|SAR q1; choice-3 screen-out; choiceSelect hides choice-3 when condition met|choice-3 not displayed; respondent cannot reach screen-out from this question; survey continues normally||https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-6126, https://macromill.atlassian.net/browse/MINT-7309|
|C-2LOGIC-097|screeningOut + choiceSelect — non-screen-out choices hidden|MAC|choiceSelect hides non-screen-out choices; screen-out choice remains visible|MAC q1; choice-5 screen-out; choiceSelect hides choices 1-4; choice-5 remains|only choice-5 (screen-out) displayed; selecting it → survey exits||https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-6126, https://macromill.atlassian.net/browse/MINT-7309|
|C-2LOGIC-098|screeningOut + randomization|SAR|Screen-out tied to choice ID, not display position; random order does not break routing|SAR q1 rand=random; choice-ID-3 screen-out; run multiple sessions|choice-ID-3 appears in different positions across sessions; selecting it always triggers screen-out regardless of position||https://macromill.atlassian.net/browse/MINT-4129, https://macromill.atlassian.net/browse/MINT-6126, https://macromill.atlassian.net/browse/MINT-7021|
|C-2LOGIC-099|textbox + randomization|SAR|Choice with textbox appears in random position; textbox still shown when that choice selected|SAR q1 rand=random; choice-ID-3 has textbox; run multiple sessions|choice-ID-3 position varies; selecting it in any position reveals textbox; textbox behavior (optional/required) unaffected by display order||https://macromill.atlassian.net/browse/MINT-4129, https://macromill.atlassian.net/browse/MINT-4482|
|C-2LOGIC-100|textbox + exclusive|MAC|Exclusive choice has a textbox; exclusive behavior + textbox work together|MAC q1 exclusive=choice-5; choice-5 has optional textbox; respondent selects choices 1+2 then choice-5|Selecting choice-5: deselects 1+2 (exclusive); textbox for choice-5 appears; submit without filling → valid (optional)||https://macromill.atlassian.net/browse/MINT-4013, https://macromill.atlassian.net/browse/MINT-6112, https://macromill.atlassian.net/browse/MINT-4482|
|C-2LOGIC-101|matrixInclusion + exclusive|MTM|Inclusion reveals a choice into SQ2 that is marked Exclusive; exclusive applies to revealed choice|MTM q1; matrixInclusion SQ1→SQ2 for choice-3; choice-3 Exclusive in SQ2; SQ1 selects choice-3 (reveals it); respondent selects choice-3 + choice-1 in SQ2|Selecting choice-3 in SQ2: deselects choice-1 (exclusive deselect); only choice-3 remains in SQ2||https://macromill.atlassian.net/browse/MINT-7678, https://macromill.atlassian.net/browse/MINT-7880, https://macromill.atlassian.net/browse/MINT-4013|
|C-2LOGIC-102|prohibition + exclusive|MTM|Exclusive SQ1 selection changes the prohibited col in SQ2|MTM q1 prohibition SQ1↔SQ2; SQ1 has exclusive=col-5; respondent selects col-2+col-3 in SQ1 then col-5|Selecting col-5 in SQ1: exclusive deselects col-2,3; now only col-5 selected in SQ1; prohibition hides col-5 in SQ2; col-2 and col-3 reappear in SQ2||https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-4013, https://macromill.atlassian.net/browse/MINT-6112|
|C-2LOGIC-103|pageBreak + randomization|SAR|Page break before a question with randomized choices; break renders correctly regardless of order|SAR q2 pbBefore=true; rand=random; 5 choices|q2 loads on new page; choice order is randomized on that page; page break not suppressed by randomization||https://macromill.atlassian.net/browse/MINT-7731, https://macromill.atlassian.net/browse/MINT-4129|
|C-2LOGIC-104|switchToRadio + randomization|MTM|SQ1 radio mode; column order randomized; radio enforces exactly 1 selection regardless of position|MTM q1 SQ1 switchToRadio=true; rand=random cols; multiple sessions|col order varies across sessions; SQ1 renders as radio row in each order; exactly 1 selection enforced by ID not position||https://macromill.atlassian.net/browse/MINT-5833, https://macromill.atlassian.net/browse/MINT-4129|
|C-2LOGIC-105|switchToRadio + specN|MTM|SQ1 radio; global specN=Exact 2 on other SQs; SQ1 radio overrides specN for itself|MTM q1 SQ1 switchToRadio=true; global specN=exact:2; SQ2 normal checkbox|SQ1 enforces exactly 1 (radio); SQ2 enforces exactly 2 (specN); submit requires SQ1=1 AND SQ2=2||https://macromill.atlassian.net/browse/MINT-5833, https://macromill.atlassian.net/browse/MINT-6111|
|C-2LOGIC-106|switchToRadio + matrixInclusion|MTM|SQ1 radio drives inclusion into SQ2; re-selection in SQ1 updates SQ2 included choices|MTM q1 SQ1 switchToRadio=true; matrixInclusion SQ1→SQ2 for cols 1-3; SQ1 selects col-1 (included in SQ2); then re-selects col-2|col-1 in SQ2 disappears (SQ1 deselected col-1); col-2 appears in SQ2 (SQ1 now selects col-2)||https://macromill.atlassian.net/browse/MINT-5833, https://macromill.atlassian.net/browse/MINT-7678, https://macromill.atlassian.net/browse/MINT-7880|
|C-2LOGIC-107|Disable Choices + randomization|MTS|Column order randomized; disabled cells remain disabled at their respective IDs regardless of position|MTS q1 rand=random cols; SQ1 col-2 disabled; multiple sessions|col-2 appears in different display positions across sessions; in all cases col-2 cell in SQ1 is not selectable (disabled)||https://macromill.atlassian.net/browse/MINT-5282, https://macromill.atlassian.net/browse/MINT-4129, https://macromill.atlassian.net/browse/MINT-7401|
|C-2LOGIC-108|Disable Choices + specN|MTM|Disabled column reduces selectable count; if specN becomes impossible → specN ignored for that row|MTM q1 SQ1 specN=exact:3; 5 cols; SQ1 col-1 AND col-2 disabled → 3 selectable cols remain|3 selectable cols available; exact:3 still achievable; respondent must select all 3; submit blocked until all 3 selected. (If disabled reduced below specN threshold: specN ignored.)||https://macromill.atlassian.net/browse/MINT-5282, https://macromill.atlassian.net/browse/MINT-6111, https://macromill.atlassian.net/browse/MINT-8144|
|C-2LOGIC-109|Disable Choices + matrixInclusion|MTM|Inclusion reveals choices into SQ2; some revealed choices are disabled in SQ2 → cannot be selected|MTM q1; matrixInclusion SQ1→SQ2 for cols 1-3; SQ2 col-2 disabled; SQ1 selects cols 1,2,3|SQ2 shows cols 1,2,3 (revealed) plus baseline; col-2 remains disabled (cannot select) even though revealed; cols 1,3 selectable||https://macromill.atlassian.net/browse/MINT-5282, https://macromill.atlassian.net/browse/MINT-7678, https://macromill.atlassian.net/browse/MINT-7880|
|C-2LOGIC-110|questionSelect + choiceSelect + exclusive|MAC|3-way: Q shown by questionSelect; choices filtered by choiceSelect; exclusive applies to remaining|MAC q2 exclusive=choice-5; questionSelect shows q2 when q1=A; choiceSelect hides choice-2 when q1=A; q1=A|q2 shown; choice-2 hidden; exclusive choice-5 visible and active; selecting choice-5 deselects all other visible choices||https://macromill.atlassian.net/browse/MINT-7910, https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-4013|
|C-2LOGIC-111|randomization + prohibition + exclusive|MTM|3-way: random col order + prohibition SQ1↔SQ2 + exclusive in SQ1; all by ID not position|MTM q1 rand=random cols; prohibition SQ1↔SQ2; SQ1 exclusive=col-5|Selecting col-5 in SQ1: exclusive deselects others; col-5 hidden in SQ2 (prohibition); col order randomized across sessions; behavior correct by ID in all orderings||https://macromill.atlassian.net/browse/MINT-4129, https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-4013|
|C-2LOGIC-112|matrixInclusion + prohibition + exclusive|MTM|3-way: inclusion reveals choices; prohibition links SQs; exclusive in receiving SQ|MTM q1; matrixInclusion SQ1→SQ2 cols 1-3; prohibition SQ2↔SQ3; SQ2 exclusive=col-3|SQ1 selects col-1,2,3 → revealed in SQ2. In SQ2: selecting col-3 (exclusive) deselects 1,2; col-3 hidden in SQ3 (prohibition)||https://macromill.atlassian.net/browse/MINT-7678, https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-4013|
|C-2LOGIC-113|choiceSelect + matrixInclusion + prohibition|MTM|3-way: column filtering + inclusion + prohibition all interact on same matrix|MTM q1; choiceSelect hides col-4 globally; matrixInclusion SQ1→SQ2 for cols 1-3; prohibition SQ1↔SQ2 on col-2; condition met|col-4 hidden in all SQs; SQ1 selects col-1,2,3 → revealed in SQ2; col-2 hidden in SQ2 (prohibition); effective SQ2 has cols 1,3 from inclusion + baseline (minus col-4 and col-2)||https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-7678, https://macromill.atlassian.net/browse/MINT-7270|
|C-2LOGIC-114|textbox + exclusive + required|MAC|3-way: required MAC; exclusive choice has required textbox; must fill textbox after exclusive selection|MAC q1 required=ON; exclusive=choice-5; choice-5 has required textbox; respondent selects choices 1+2 then choice-5|Selecting choice-5: exclusive deselects 1+2; textbox appears; submit without filling textbox → error; fill textbox → submit valid||https://macromill.atlassian.net/browse/MINT-4013, https://macromill.atlassian.net/browse/MINT-4482, https://macromill.atlassian.net/browse/MINT-5283|
|C-2LOGIC-115|screeningOut + choiceSelect + required|MAC|3-way: required MAC; screen-out choice hidden by choiceSelect; required enforced without screen-out option|MAC q1 required=ON; choice-5 screen-out; choiceSelect hides choice-5 when condition met; condition met|choice-5 not displayed; screen-out not reachable; required still enforced on remaining visible choices; submit without selection → required error||https://macromill.atlassian.net/browse/MINT-5841, https://macromill.atlassian.net/browse/MINT-6126, https://macromill.atlassian.net/browse/MINT-5283|
|C-2LOGIC-116|countMatrix + questionSelect|MTS|countif result drives question visibility — above threshold shows Q; below hides it|MTS q1 (5 SQs, 5 choices); questionSelect on q2: show q2 if countif(q1,"S1-5","1-2")>=3; respondent selects choice-1 or choice-2 in 3+ SQs|Count ≥ 3: q2 shown. Count < 3: q2 hidden. Count evaluated from intersection of SQ1–5 and choices 1–2 only.||https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-7730, https://macromill.atlassian.net/browse/MINT-6520|
|C-2LOGIC-117|countMatrix + subquestionSelect|MTM|countif result drives SQ visibility — threshold met shows SQ2; not met hides SQ2|MTM q1 (3 SQs, 5 choices); subquestionSelect on SQ2: show if countif(q1,"S1-3","1-3")>=2; respondent selects in-range choices|Count ≥ 2: SQ2 shown. Count < 2: SQ2 hidden. SQ2 required only enforced when shown.||https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-7730|
|C-2LOGIC-118|countMatrix + choiceSelect|MTS|countif result drives choice visibility — threshold met reveals additional choice in target Q|MTS q1 (3 SQs, 5 choices); choiceSelect on q2: show choice-5 in q2 if countif(q1,"S1-3","1-2")>=2|Count ≥ 2: choice-5 displayed in q2. Count < 2: choice-5 hidden. Other q2 choices unaffected.||https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-7730|
|C-2LOGIC-119|countMatrix + screeningOut|MTS|count below threshold → screeningOut; count at threshold → continues|MTS q1 (5 SQs, rating 1-5); screeningOut: if countif(q1,"S1-5","1-2")<2 → screen out|Respondent answers: fewer than 2 SQs in choices 1-2 → survey exits to screeningOut. 2 or more → survey continues.||https://macromill.atlassian.net/browse/MINT-7105, https://macromill.atlassian.net/browse/MINT-6126, https://macromill.atlassian.net/browse/MINT-7021|
|C-2LOGIC-120|countMatrix + prohibition|MTM|Prohibition-violating selections excluded from count; prohibition-compliant selections counted|MTM q1; prohibition SQ1↔SQ2; countif(q1,"S1-2","1-3")>=2; respondent selects col-1 in both SQ1 and SQ2 (violates prohibition) + col-2 in SQ1|Prohibition-violating selection (col-1 in SQ2) excluded from count; only valid selections counted (col-1 in SQ1, col-2 in SQ1 = 2); count = 2 ≥ 2 → condition met||https://macromill.atlassian.net/browse/MINT-7730, https://macromill.atlassian.net/browse/MINT-7270, https://macromill.atlassian.net/browse/MINT-7870|
|C-2LOGIC-121|countMatrix + matrixInclusion|MTM|Inclusion reveals choices into SQ2; revealed choices selected in SQ2 count toward countif of SQ2|MTM q1; matrixInclusion SQ1→SQ2 for choices 1-3; countif(q1,"S2","1-3")>=1 drives questionSelect on q2; SQ1 selects choice-1 (reveals into SQ2); SQ2 selects revealed choice-1|Revealed choice-1 in SQ2 is a valid selection; countif(q1,"S2","1-3") = 1 ≥ 1 → q2 shown; confirms that revealed-and-selected choices count toward the countif expression||https://macromill.atlassian.net/browse/MINT-7730, https://macromill.atlassian.net/browse/MINT-7678, https://macromill.atlassian.net/browse/MINT-7880|
|C-2LOGIC-122|RNK exclusive + saved data propagation|RNK|Exclusive RNK choice selected; propagates to all subsequent rank slots in saved response data|RNK q1 5 items; item-5 configured as exclusive (e.g. "No Preference"); respondent selects item-5 as rank-1|item-5 occupies rank-1 slot; in saved response data all subsequent rank slots (2–5) are also populated with item-5's ID (exclusive propagation behavior); non-exclusive items remain unranked; survey advances||https://macromill.atlassian.net/browse/MINT-4013|
|C-2LOGIC-123|RNK exclusive + required=All|RNK|Exclusive RNK choice alone satisfies required=All without forcing the respondent to rank all items|RNK q1 5 items required=All; item-5 exclusive; respondent selects item-5 only|Required=All is satisfied by the exclusive choice selection; no validation error for unranked items 1–4; exclusive overrides the required-all check; submit succeeds||https://macromill.atlassian.net/browse/MINT-4013, https://macromill.atlassian.net/browse/MINT-5283|

---

## Version History

| Date | Change | Case IDs |
|---|---|---|
| 2026-05-07 | Comprehensive 3-pass review (second pass) against all settings/logic combinations. Pass 1: 8 accuracy corrections (C-MATRIX-COUNT-46 corrected from MTS→MTT, prohibition scope clarified, C-MATRIX-COUNT-50 empty-SQ rule, RAT i18n keys added, FA realTime error trigger/keys). Pass 2: +15 new cases (C-MATRIX-COUNT-61–63, C-QTSEL-150–151, V-RAT-CS-004–007, V-FAL-001–003 new section, V-REQ-Q-11–13). Pass 3: count header updated to ~730. | C-MATRIX-COUNT-61–63, C-QTSEL-150–151, V-RAT-CS-004–007, V-FAL-001–003, V-REQ-Q-11–13 |
| 2026-05-07 | 3-pass review against Confluence spec (pages 1554808888, 1554776128, 1247740761) and rosemary-frontend. Pass 1: 4 accuracy corrections (screeningOutFlg values, SAP/disabled auto-select ambiguity removed). Pass 2: +13 new cases (V-FA-005–008, V-RAT-CS-001–003, C-TXTBOX-029, V-PAGEBREAK-31, C-2LOGIC-122–123). Pass 3: count header updated. | V-FA-005–008, V-RAT-CS-001–003, C-TXTBOX-029, V-PAGEBREAK-31, C-2LOGIC-122–123 |
| 2026-04-30 | Added P1 answer-side runtime enforcement: V-REQ-Q-01–10 (10 cases), V-REQ-SQ-01–20 (20 cases), V-SPECN-01–38 (38 cases), V-PAGEBREAK-11–20 (10 cases) | V-REQ-Q, V-REQ-SQ, V-SPECN, V-PAGEBREAK-11–20 |
| 2026-04-27 | Added P3 expansion: C-QTSEL-045–150 (105 cases), C-QTRAND-048–078 (31 cases), C-MATRIX-COUNT-31–60 (30 cases), C-SCREENING-001–024 (24 cases), C-DISABLED-001–026 (26 cases), C-TXTBOX-001–028 (28 cases) | C-QTSEL-045–150, C-QTRAND-048–078, C-MATRIX-COUNT-31–60, C-SCREENING-001–024, C-DISABLED-001–026, C-TXTBOX-001–028 |
| 2026-04-27 | Added P3 base combination matrix cases | C-QTSEL-001–044, C-QTRAND-001–047 |
| 2026-04-26 | Added Pattern 2 page break runtime cases | V-PAGEBREAK-21–30 |
| 2026-04-24 | Added Pattern 1 page break runtime cases | V-PAGEBREAK-01–10 |
| 2026-04-24 | Added logic test cases in plain language (migrated from archived MYLang page 2070478852) | EX-LOGIC-001–EX-LOGIC-100 |

---

## Out of Scope

> These cases cover features not yet developed: **loop block** (repeating question block), **quota** routing/branching, and **user-attribute pre-fill**. They will be activated when the features ship.

### Loop Block Cases

| FC-010 | Loop Logic (Repeat Block), Condition Not Met, No Loop | Repeat block for Q3 while answer ≠ "Done"; Q3 answered as "Done" on first try | Answer "Done" → click Next | Block executes once; No repeat | |
| FC-011 | Loop Logic, Condition Met, Block Repeats | Same as FC-010; Q3 answered "Repeat" first, then "Done" | Answer "Repeat" → block shows again → answer "Done" | Block repeats exactly once; Survey exits the loop after "Done" | |
| FC-012 | Max Iteration Limit on Loop, Loop Terminates | Loop with max iterations = 3; respondent always answers "Repeat" | Answer "Repeat" 3 times | After 3rd iteration, loop terminates regardless of answer; Survey continues to next section | |
| EX-LOGIC-081 | Skip Logic: Skip Inside a Loop Block | Repeating block (max 3 iterations); inside block: if Q_inner = "Exit" → skip remaining questions in iteration | Iteration 1: Q_inner = "Exit" | Remaining questions in iteration 1 are skipped; Block proceeds to iteration 2 (or exits if exit condition met) | |
| EX-LOGIC-086 | Skip Logic: Loop Exit Condition | Repeating block; exit condition: after 3 iterations OR if Q_inner = "Done" | Q_inner = "Done" on iteration 2 | Loop exits after iteration 2; Survey continues past the loop block | |

### Quota Cases

| SC-001 | Quota Full, Respondent Screened Out | Survey with a quota that is already full for "Male, Age 25–34" | Respondent qualifies as Male, Age 30 → attempts to enter survey | Respondent is redirected to the "Quota Full" screen; Respondent is NOT counted in the survey data; Quota count does not increase | |
| SC-011 | Quota-Based Screening, Quota Not Yet Full | Quota: 50 Female respondents needed; current count = 49 | Female respondent enters survey | Respondent is admitted; Quota count increases to 50 | |
| SC-012 | Quota-Based Screening, Quota Exactly Full | Quota: 50 Female; current count = 50 | Another Female respondent attempts to enter | Respondent is redirected to "Quota Full"; Count remains 50 | |
| SC-013 | Multi-cell Quota, One Cell Full, Others Open | Quota cells: Male (full), Female (open) | Male respondent attempts entry | Male respondent is shown "Quota Full"; Female respondent (separate attempt) would pass normally | |
| FC-017 | Quota Branching, Branch Based on Quota Cell | Respondent assigned to "Cell A" quota → show special page | Respondent qualifies for Cell A → proceeds | Special page for Cell A is shown; Other quota cells see different pages | |
| EX-LOGIC-019 | Quota Branching, Cell Assignment | Quota cells: Cell A (Female 18–34), Cell B (Female 35–54) | Female respondent, age 25, enters survey | Respondent is assigned to Cell A; Cell A content/branch is shown | |
| EX-LOGIC-020 | Quota Branching, Cell Full, Redirect | Cell A is full | Female, age 25, attempts to enter | Respondent is shown "Quota Full"; Cell A count does not increase | |
| EX-LOGIC-079 | Quota Branching: Multiple Quota Cells, All Full | Quota cells A, B, C — all full | New respondent attempts entry | Respondent is shown "Survey Full" or "Quota Full"; No cell assignment is made | |
| EX-LOGIC-080 | Quota Branching: Partial Quota Fill, Correct Cell Assigned | Cell A (Female, 18–34): 20/50; Cell B (Female, 35–54): 50/50 (full) | Female, age 40, attempts entry | Cell B is full → respondent shown "Quota Full"; Cell A is not affected | |
| EX-LOGIC-097 | Quota: Real-Time Quota Check During Survey | Quota cell has 1 remaining slot; two respondents reach the quota check simultaneously | Both respondents submit at the same time | Only one respondent fills the last slot; The other is shown "Quota Full"; No double-counting | |

