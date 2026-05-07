# 36 — Original Tags / オリジナルタグ

**Total scripts:** ~350 files across subdirectories  
**Purpose:** Verify that the custom survey tags allowed in question text, choice text, and sub-question labels display correctly in preview and enforce proper input validation. Tags include both HTML formatting tags (a, br, b, font, img, etc.) and survey-specific logic tags (if, answer, copy, newline, fa, loop, bdcomment, hd, required, disabled, sa, checkcount).

---

## TC-36-01 — HTML Formatting Tags in Question Text and Choices

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator uses standard HTML-style formatting tags in question text, choice text, and sub-question labels. Each tag is verified for correct rendering in preview and correct rejection of unsupported attributes.

**Tags tested:**

| Tag | What is tested |
|-----|----------------|
| `<a>` | href and target attributes (_blank, _top, _self); preview shows working links |
| `<br/>` | Single break creates new line; double break creates blank line; invalid `<br>text</br>` form causes error |
| `<b>` | Bold text renders correctly in choices and question text |
| `<u>` | Underline renders correctly |
| `<font>` | class, size, color attributes work; unsupported attributes (e.g., hoge=) cause error |
| `<hr/>` | Horizontal rule displays; width attribute works; unsupported attributes cause error |
| `<center>` | Text and tags inside are centered |
| `<right>` | Text and tags inside are right-aligned |
| `<img>` | src, height, width, border attributes work; unsupported attributes cause error |

**Steps:**
1. Create a survey with a SAR question.
2. In the question text / choice text, insert each tag above.
3. Save and preview the survey.
4. Verify the tag renders correctly in the browser.
5. Try inserting each tag with an unsupported attribute; verify an error is shown.

**Expected Results:**
- Supported attributes render as expected in preview
- Unsupported attributes are rejected with an error on save
- Tags appear in the correct places (question text, choice text, sub-question labels) as specified by each question type's allowed-tag list

---

## TC-36-02 — `<answer>` Tag: Displaying Previous Answers in Later Questions

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `<answer>` tag allows a later question to display the answer text from a previous question. This tag is tested across all 11 main question types, for valid and invalid configurations, and for correct display during answer.

**Setup:**
- Survey with Q1 as source (various question types) and Q2 or later using `<answer no="Q1"/>`

**Valid usage tests:**
1. Place `<answer no="Q1"/>` in question text of Q2 for each question type (SAR, MAC, MTS, MTM, MTT, FAS, RNK, SAP, SAS, FAL, RAT).
2. Verify that during answer, Q2 shows the answer selected at Q1 as inline text.
3. For SAR/MAC: selected choice text (including FA text if chosen) is shown.
4. For MTS/MTM/MTT: entire question cannot be referenced — only sub-questions (副質問) can be used as no= target; verify sub-question choices display.
5. For FAS: entire question not allowed; only individual sub-question reference works.
6. For FAL/RAT: question-level reference not allowed; error shown.
7. For RNK: question-level reference allowed; ranked choices display in rank order.
8. For SAP/SAS: selected choice text shown.

**Invalid usage tests:**
9. Reference a question that does not exist → error on save.
10. Reference a question that appears AFTER the current question (forward reference) → error on save.
11. Reference a question inside a loop section from outside the loop → error on save.
12. Reference an internal screening-out question → error shown.

**No-answer and N/A cases:**
13. Source question was left unanswered → `<answer>` displays as blank.
14. Source question was skipped due to logic (non-applicable) → `<answer>` displays as blank.

**Expected Results:**
- Valid references correctly display prior answer text during survey answer
- All invalid configurations are caught at save time with appropriate error messages

---

## TC-36-03 — `<copy>` Tag: Copying Choices from a Previous Question

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `<copy>` tag allows a later question to reuse choices from a prior question. This is tested across all supported question types and with various range configurations.

**Valid question types for copy in choices:** SAR, MAC, SAP, SAS, MTS, MTM, MTT, RNK  
**Invalid (error expected):** FAS, RAT

**Invalid configuration tests:**
1. Reference a question that does not exist → error.
2. Reference a question using MT-style sub-question format in a non-MT context → error.
3. Reference an FA-type sub-question format → error.
4. Range value cannot be parsed (letters, full-width digits, malformed like "1,,,3" or "1--3") → error.
5. Range specifies choices beyond the available count (e.g., range="1-5" but source has only 4 choices) → error.

**Valid range tests:**
6. range="1-3" — copies choices 1 through 3.
7. range="1,3" — copies choices 1 and 3.
8. range="1,2,3" — copies choices 1, 2, and 3.
9. range="3,1" — copies choices 3 then 1 (order preserved).
10. range="3,3" — copies choice 3 twice.
11. Source question uses comment/newline tags → copy handles them correctly.
12. Source question itself uses copy tag, and combined count is sufficient → no error.

**Other tests:**
13. Forward references (source is after current question) → no error (copy is evaluated at answer time).
14. Loop-section references → no error.
15. Choice randomization on source question → copy uses original (editor) choice numbering, not display order.
16. Two `<copy>` tags in same choice text: same source question + different source questions.

**Expected Results:**
- Valid copy configurations expand into the correct choice list at answer time
- Invalid configurations produce clear error messages at save time

---

## TC-36-04 — `<newline>` Tag: Row Break in Matrix Sub-Questions

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** The `<newline/>` tag inserts a visual row break in matrix sub-question (row label) lists. It interacts with the automatic header insertion feature.

**Steps:**
1. Add `<newline/>` tags in sub-question labels of a matrix question.
2. Verify that up to 11 sub-questions without `<newline>` causes no break.
3. Add a 12th sub-question — auto-header inserts correctly at position 12.
4. Insert at least one `<newline/>` → auto-header insertion is disabled even at 12 or 13 rows.

**Expected Results:**
- `<newline/>` renders a row break in the sub-question list
- Auto-header insertion is disabled when any `<newline/>` is present in the question

---

## TC-36-05 — `<fa>` Tag: Free Answer Input Type Restrictions

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `<fa>` tag on choice text or sub-question labels adds an inline text input field with configurable type validation. Types: number (half-width digits only), alnum (half-width alphanumeric only), email (valid email format).

**`type` attribute tests:**
1. type="number": respondent can only enter half-width digits; other characters rejected.
2. type="alnum": respondent can only enter half-width alphanumeric characters.
3. type="email": full-width characters rejected; missing "@" rejected.

**`msg` attribute tests (for each type):**
4. msg="on" with type="number": validation hint message "(半角数字)" is displayed.
5. msg="off" with type="number": validation hint message is NOT displayed.
6. msg="on" with type="alnum": hint "(半角英数字)" displayed.
7. msg="off" with type="alnum": hint not displayed.
8. msg="on" with type="email": hint "(Eメールチェック)" displayed.
9. msg="off" with type="email": hint not displayed.

**size attribute and slider tests:**
10. FA with slider type: verify slider renders correctly and value is captured.
11. FA with code type (Fa(codeタイプ)): verify code-entry validation behavior.

**Expected Results:**
- Each `type` value enforces the correct character restriction during answer
- `msg` attribute controls visibility of the hint message
- Slider FA renders and captures numeric value correctly

---

## TC-36-06 — `<if>` Tag: Conditional Display within Question Text

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `<if>` tag allows parts of question text or choice text to be conditionally shown or hidden based on prior answers. The tag is tested across all main question types and for correct logic evaluation.

**Tests:**
1. Place an `<if>` tag in question text of Q2 conditioned on Q1's answer.
2. Answer Q1 so the condition is true → the conditional text is displayed.
3. Answer Q1 so the condition is false → the conditional text is hidden.
4. Test `<if>` tags across all 11 main question types (SAR, MAC, SAP, SAS, MTS, MTM, MTT, FAL, FAS, RAT, RNK).
5. Test auto-generated `<if>` tags (IFタグ生成) — verify they produce correct conditions.
6. Verify that `<if>` tags with invalid syntax or unsupported conditions produce errors.

**Expected Results:**
- `<if>` tag shows/hides text correctly based on the evaluated condition
- All 11 question types correctly handle `<if>` in allowed positions
- Invalid `<if>` configurations show appropriate errors

---

## TC-36-07 — `<bdcomment>` and `<hd>` Tags: Matrix Row Labels

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `<bdcomment>` tag adds a comment row between sub-questions in a matrix; the `<hd>` tag adds a section header row. Both are only available in MTS, MTM, and MTT sub-question labels.

**Tests:**
1. Insert `<bdcomment>Some comment</bdcomment>` between sub-questions — verify it renders as a non-answerable comment row.
2. Insert `<hd>Header text</hd>` — verify it renders as a bold header row grouping sub-questions.
3. Combine bdcomment and hd in the same question.
4. Verify these tags in the normal (non-reversed) sub-question display mode.
5. Verify these tags in the reversed (逆転) sub-question display mode — bdcomment is allowed, hd is not.
6. Use these tags in the allowed positions in MTS, MTM, and MTT question types.

**Expected Results:**
- Comment rows and header rows render correctly in the matrix display
- These tags are not available in non-matrix question types
- In reversed mode, hd tag is rejected

---

## TC-36-08 — `<required>` Tag: Per-Row Required Indication in Matrix

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `<required/>` tag can be placed in a matrix sub-question label to mark that specific row as required independently of the question-level required setting.

**Tests:**
1. Add `<required/>` to one sub-question in an MTS question.
2. Answer the survey and skip that row — verify required error is shown for just that row.
3. Answer the required row — verify the question submits correctly.
4. In MTM: add `<required/>` alongside `<disabled/>` and `<checkcount>` tags.

**Expected Results:**
- `<required/>` enforces per-row required validation
- Other rows without `<required/>` can be left blank without error

---

## TC-36-09 — `<disabled>` and `<sa>` Tags: MTM-Specific Behavior

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `<disabled/>` tag disables a matrix row's input; the `<sa/>` tag forces single-answer behavior for a specific MTM row (normally MTM allows multiple selections per row).

**Tests:**
1. `<disabled/>` on a matrix row (MTM) — that row's checkboxes are grayed out; no selection possible.
2. `<sa/>` on an MTM row — only one choice can be selected in that row (acts like MTS for that row).
3. Combine `<sa/>` with `<required/>` on the same row.

**Expected Results:**
- `<disabled/>` visually disables the row and prevents any input
- `<sa/>` limits the row to single-answer mode
- Combined tags apply all their effects simultaneously

---

## TC-36-10 — `<checkcount>` Tag: MTM Minimum/Maximum Selection Count per Row

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** The `<checkcount>` tag on an MTM sub-question row enforces a minimum or maximum number of checkbox selections for that row.

**Tests:**
1. Set `<checkcount min="2" max="3"/>` on a row — verify respondent must select at least 2 and at most 3.
2. Select fewer than minimum → error shown.
3. Select more than maximum → prevented (checkbox becomes unselectable after max reached).
4. Select within range → no error, question submits.

**Expected Results:**
- Minimum count enforces a required selection threshold per row
- Maximum count prevents over-selection
- Error messages are shown when violations occur

---

## TC-36-11 — Tags in Attribute Questions (Profile Questions)

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Survey attribute questions (f_sar, f_mac, f_sap, f_fas, f_tel, f_zip, f_prm) also support custom tags. The same tag rules apply with some differences (e.g., SAP choices only allow `<copy>`; FAS allows `<fa>` in free areas).

**Question types tested:** f_sar, f_mac, f_sap, f_fas, f_tel (additional), f_zip (additional), f_prm

**Tests:**
1. Insert allowed tags in question text and choice text of each attribute question type.
2. Verify that unsupported tags produce errors.
3. Basic attribute questions (name, email, sex, age, etc.) only allow annotation text — no tag enforcement needed.
4. Internal screening-out questions follow the same tag rules as main questions.

**Expected Results:**
- Allowed tags in attribute questions render correctly in preview
- Unsupported tags are rejected with errors

---

## TC-36-12 — Tags Combined with Logic

**Scope:** Admin / Respondent  
**Platform:** Desktop

**Scenario:** Custom tags and logic features (choiceSelect, questionSelect, piping, etc.) are used together. The combination must work without breaking either the tag rendering or the logic behavior.

**Tests:**
1. Question using `<answer>` tag with source question also controlled by choiceSelect logic.
2. Question using `<copy>` with a source question that has choice randomization.
3. `<if>` tag combined with questionSelect — the if condition and the question select condition both apply.
4. Matrix question with `<newline/>` and `<bdcomment>` also has matrixInclusion logic.

**Expected Results:**
- Tags render correctly even when logic is active
- Logic behavior is not broken by the presence of tags
- Combined features produce correct display and data recording

---
