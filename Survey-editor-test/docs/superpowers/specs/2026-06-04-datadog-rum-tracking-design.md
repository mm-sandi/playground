# Datadog RUM Tracking Design — Survey Editor

**Status:** DRAFT v0.1  
**Author:** PM  
**Date:** 2026-06-04  
**For Discussion With:** Product, Engineering, UX Design

---

## 1. Overview

### 1.1 Background

The Survey Editor (rosemary-frontend workbench) currently has no systematic user behavior tracking. This document proposes adding Datadog Real User Monitoring (RUM) to capture user activity across the Survey Editor, enabling data-driven product decisions.

### 1.2 Goals

| Goal | Business Question |
|---|---|
| **Feature adoption** | Which question types and logic rules are actually used? Which are rarely touched? |
| **UX / struggle detection** | Where do users make errors, redo actions, or abandon workflows? |
| **Performance monitoring** | How fast are save, publish, and AIRs operations? Are there slow pages? |
| **Error / bug triage** | What errors occur in production, in what context, and how often? |
| **Funnel analysis** | What % of surveys created are saved? Saved to AIRs? Published? |
| **Active time** | How long does it actually take a user to go from creating a survey to Save to AIRs? |

### 1.3 Scope

| Phase | Surfaces Covered |
|---|---|
| **Phase 1 (this document)** | Survey Editor (rosemary-frontend workbench) |
| Phase 2 (future) | Answer page, Admin pages |

---

## 2. Tracking Approach

### 2.1 Tool: Datadog RUM

Datadog RUM automatically captures (no code required):
- Page views and client-side navigation
- JavaScript errors and unhandled exceptions
- Resource load times (XHR, fetch, JS, CSS, images)
- Long tasks (UI freeze indicators, > 50 ms)
- Core Web Vitals (LCP, FID, CLS)

In addition, we fire **custom actions** for Survey Editor-specific user interactions using `datadogRum.addAction(name, context)`.

### 2.2 Event Structure: Hierarchical Name + Rich Context

All custom actions follow a three-part dot-notation name, with all additional data in a context object.

```
{screen}.{category}.{action}
```

| Part | Values | Notes |
|---|---|---|
| `screen` | `editor` | Fixed to Survey Editor for Phase 1. Future: `answer`, `admin` |
| `category` | `survey`, `question`, `logic`, `save`, `lock`, `session`, `nav` | Maps to a feature domain |
| `action` | `add`, `edit`, `delete`, `reorder`, `configure`, `open`, `close`, `start`, `complete`, `fail`, `acquire`, `release`, `expire`, `claim`, `idle`, `resume` | Verbs only; consistent across categories |

**Example:**
```js
datadogRum.addAction('editor.question.add', {
  question_type: 'SAR',
  page_number: 1,
  total_questions_after: 5
})
```

**Why this approach:**
- Event names are short, stable, and hierarchically filterable in Datadog (filter by `editor.question.*` to see all question events)
- Context attributes enable PM-level aggregation ("most-used question type") and engineering drill-down ("save failures by browser version") from the same event stream
- Scales without renaming events — new features add new context keys, not new event names

---

## 3. Naming Rules

| Rule | Correct | Incorrect |
|---|---|---|
| All lowercase, dot-separated | `editor.question.add` | `Editor_Question_Add` |
| Screen → category → action order | `editor.logic.configure` | `configure.logic.editor` |
| Verbs for actions | `add`, `delete`, `complete`, `fail` | `addition`, `removed`, `success` |
| No underscores in event name | `editor.save.complete` | `editor_save_complete` |
| Underscores OK in context attribute keys | `question_type`, `active_time_ms` | `questionType`, `activeTimeMs` |
| Boolean flags: descriptive noun | `had_logic: bool`, `unsaved_changes: bool` | `logic: bool` |
| All durations in milliseconds | `duration_ms`, `active_time_ms` | `duration_s`, `durationSeconds` |

---

## 4. Global Session Context

Set once when the Survey Editor loads. Automatically attached to **every** RUM event in the session — no need to repeat per event.

```js
// User identity
datadogRum.setUser({
  id: 'usr_001',
  email: 'user@macromill.com',
  role: 'creator'  // 'creator' | 'admin'
})

// Survey context
datadogRum.setGlobalContextProperty('survey_id', 'sv_abc123')
datadogRum.setGlobalContextProperty('survey_status', 'draft')  // 'draft' | 'published'
datadogRum.setGlobalContextProperty('editor_mode', 'edit')     // 'edit' | 'read_only'
datadogRum.setGlobalContextProperty('app_version', '1.4.2')
```

**Update on mode change:** When pessimistic locking switches a user to read-only, update the global context immediately:
```js
datadogRum.setGlobalContextProperty('editor_mode', 'read_only')
```

---

## 5. Event Catalog

### 5.1 Survey-Level Events

| Event Name | Trigger | Key Context Attributes |
|---|---|---|
| `editor.survey.create` | New survey started | `is_duplicate: bool` |
| `editor.survey.open` | Existing survey opened in editor | `question_count: int`, `page_count: int` |
| `editor.survey.duplicate` | Duplicate Survey action used | `source_survey_id: str`, `question_count: int` |
| `editor.survey.settings_change` | Survey-level setting changed | `setting: str`, `new_value: str` |
| `editor.page.add` | New page added to survey | `page_count_after: int` |
| `editor.page.delete` | Page removed from survey | `page_count_after: int` |

**Values for `setting` in `editor.survey.settings_change`:**
`"language"`, `"back_button"`, `"screening_out_points"`, `"panel_type"`

---

### 5.2 Question Events

| Event Name | Trigger | Key Context Attributes |
|---|---|---|
| `editor.question.add` | Question added to survey | `question_type: str`, `page_number: int`, `total_questions_after: int` |
| `editor.question.delete` | Question deleted | `question_type: str`, `had_logic: bool`, `total_questions_after: int` |
| `editor.question.reorder` | Question dragged to a new position | `question_type: str`, `from_index: int`, `to_index: int`, `from_page: int`, `to_page: int` |
| `editor.question.duplicate` | Question duplicated | `question_type: str`, `had_logic: bool` |
| `editor.question.configure` | A question-level setting changed | `question_type: str`, `setting: str`, `new_value: str` |

**Question type codes for `question_type`:**

| Code | Full Name |
|---|---|
| `SAR` | Single Answer Radio |
| `MAC` | Multiple Answer Checkbox |
| `SAP` | Dropdown / Scale |
| `FA` | Free Answer (single-line) |
| `FAL` | Free Answer Long (multi-line) |
| `RNK` | Ranking |
| `RAT` | Constant Sum |
| `NOTE` | Note / Informational block |
| `MTS` | Matrix Radio |
| `MTM` | Matrix Checkbox |
| `MTT` | Bipolar Matrix |

**Values for `setting` in `editor.question.configure`:**
`"required"`, `"randomization"`, `"spec_n"`, `"fa_type"`, `"fa_min"`, `"fa_max"`, `"direction"`, `"columns"`, `"exclusive"`, `"textbox_on_choice"`, `"display_format"`

---

### 5.3 Logic Events

| Event Name | Trigger | Key Context Attributes |
|---|---|---|
| `editor.logic.add` | Logic rule added to a question | `logic_type: str`, `source_question_type: str`, `condition_count: int` |
| `editor.logic.configure` | Existing logic rule edited | `logic_type: str`, `condition_count: int` |
| `editor.logic.delete` | Logic rule removed | `logic_type: str`, `auto_cleared: bool` |
| `editor.logic.combination_add` | AND/OR multi-condition logic added | `operand: "AND"\|"OR"`, `condition_count: int` |

> `auto_cleared: true` means the system removed the logic automatically (e.g., when its source question was deleted), as opposed to the user manually deleting it.

**Logic type codes for `logic_type`:**

| Code | Description |
|---|---|
| `questionSelect` | Show/hide a question based on answer |
| `choiceSelect` | Show/hide choices based on answer |
| `subquestionSelect` | Show/hide matrix sub-questions |
| `matrixInclusion` | Dynamically reveal matrix choices |
| `countMatrix` | Count-based matrix logic |
| `screeningOut` | Disqualify respondent |
| `prohibition` | Prevent simultaneous selections |
| `exclusive` | Exclusive choice logic |
| `pageBreak` | Conditional page break |

---

### 5.4 Save / Publish / AIRs Events

| Event Name | Trigger | Key Context Attributes |
|---|---|---|
| `editor.save.start` | Save action initiated by user | `save_type: str` |
| `editor.save.complete` | Save succeeded | `save_type: str`, `duration_ms: int`, `question_count: int`, `page_count: int`, `active_time_ms: int` |
| `editor.save.fail` | Save failed (API or network error) | `save_type: str`, `duration_ms: int`, `error_code: str`, `http_status: int` |
| `editor.save.validation_blocked` | Save blocked by editor-side validation | `save_type: str`, `error_types: str[]`, `error_count: int` |

**Values for `save_type`:**

| Value | Meaning |
|---|---|
| `"save"` | Regular draft save |
| `"save_to_airs"` | Save and submit to AIRs |
| `"publish"` | Publish the survey |

> `active_time_ms` on `editor.save.complete` carries the cumulative active editing time since the session started. See Section 7 for the active time tracking mechanism.

---

### 5.5 Navigation Events

| Event Name | Trigger | Key Context Attributes |
|---|---|---|
| `editor.nav.open` | User enters the editor | `entry_point: "new_survey"\|"edit_existing"\|"duplicate"` |
| `editor.nav.leave` | User leaves the editor | `leave_reason: "manual_nav"\|"tab_close"\|"session_end"`, `unsaved_changes: bool`, `active_time_ms: int` |
| `editor.nav.preview_open` | Preview panel opened | — |
| `editor.nav.preview_close` | Preview panel closed | `preview_duration_ms: int` |

---

### 5.6 Pessimistic Locking Events

Tracking locking behavior is critical for understanding collaboration patterns and identifying lock-related user friction. These events map to the [Pessimistic Locking spec](https://macromill.atlassian.net/wiki/spaces/survey/pages/1961361795/Pessimistic+Locking+-+Preventing+Concurrent+Edit+Conflicts).

**Lock lifecycle summary:**
- Heartbeat sent every **30 seconds**
- Lock becomes **claimable** if no heartbeat for **2 minutes**
- Lock **auto-expires** if no heartbeat for **5 minutes**

| Event Name | Trigger | Key Context Attributes |
|---|---|---|
| `editor.lock.acquire` | User successfully acquires the edit lock | `acquisition_type: "fresh"\|"reclaim"` |
| `editor.lock.release` | Lock intentionally released (user saves and exits, navigates away) | `release_reason: "navigate_away"\|"save_complete"\|"manual_release"`, `hold_duration_ms: int` |
| `editor.lock.expire` | Lock expired due to inactivity (browser crash, idle timeout) | `hold_duration_ms: int`, `last_heartbeat_ms_ago: int` |
| `editor.lock.claim` | User claims a claimable (abandoned) lock from another user | `previous_holder_id: str`, `time_since_claimable_ms: int` |
| `editor.lock.conflict_view` | User sees the read-only banner (lock is held by someone else) | `lock_holder_id: str` |
| `editor.lock.heartbeat_fail` | A heartbeat request failed (network issue) | `consecutive_failures: int` |
| `editor.lock.reconnect` | User reconnected and reclaimed lock after a temporary disconnect | `disconnect_duration_ms: int` |

---

## 6. Session Events

| Event Name | Trigger | Key Context Attributes |
|---|---|---|
| `editor.session.idle` | User goes idle (no activity for 5 continuous minutes) | `active_time_ms: int`, `wall_clock_ms: int` |
| `editor.session.resume` | User returns from idle state | `idle_duration_ms: int` |

---

## 7. Active Time Tracking

### 7.1 Definition

**Active time** = total elapsed time during which the user is actively interacting with the editor, excluding idle periods.

**Idle threshold:** No mouse movement, keyboard input, click, or scroll event for **5 continuous minutes**.

This threshold aligns with the pessimistic lock idle-release timeout (5 minutes), so an idle user loses both the active time counter and the edit lock at the same threshold.

### 7.2 Mechanism

Two session-level counters are maintained client-side:

| Counter | Description |
|---|---|
| `wall_clock_ms` | Total elapsed time from editor open to current moment |
| `active_time_ms` | `wall_clock_ms` minus all accumulated idle intervals |

**Implementation sketch:**

```js
let activeTimeMs = 0
let lastActivityAt = Date.now()
const IDLE_THRESHOLD_MS = 5 * 60 * 1000 // 5 minutes

// Track all user activity signals
['mousemove', 'keydown', 'click', 'scroll'].forEach(eventType => {
  document.addEventListener(eventType, () => {
    const now = Date.now()
    const gap = now - lastActivityAt

    if (gap < IDLE_THRESHOLD_MS) {
      // User was active — count this gap
      activeTimeMs += gap
    } else {
      // Gap exceeded threshold — this was idle time, do not count
      // Fire editor.session.resume if we were previously idle
    }

    lastActivityAt = now
  }, { passive: true })
})

function getActiveTimeMs() {
  const now = Date.now()
  const gap = now - lastActivityAt
  return gap < IDLE_THRESHOLD_MS
    ? activeTimeMs + gap  // User is currently active
    : activeTimeMs        // User is currently idle
}
```

### 7.3 Where Active Time Is Reported

`active_time_ms` is attached to the following events:

| Event | Purpose |
|---|---|
| `editor.save.complete` (all save types) | Measure time spent working per save action |
| `editor.nav.leave` | Total active time for the full editor session |
| `editor.session.idle` | Active time at the point the user went idle |

---

## 8. Create → Save → Save to AIRs Funnel

### 8.1 Funnel Stages

| Stage | Tracked Event | Condition |
|---|---|---|
| **1. Create** | `editor.survey.create` or `editor.nav.open` with `entry_point: "new_survey"` | Survey session begins |
| **2. First Save** | `editor.save.complete` with `save_type: "save"` | First successful draft save |
| **3. Save to AIRs** | `editor.save.complete` with `save_type: "save_to_airs"` | Successful AIRs submission |

### 8.2 Metrics Derivable From This Funnel

| Metric | How to Derive in Datadog |
|---|---|
| Stage 1 → 2 conversion rate | % of `survey.create` sessions that contain at least one `save.complete (save)` |
| Stage 2 → 3 conversion rate | % of saved sessions that also contain `save.complete (save_to_airs)` |
| Active time to first save | `active_time_ms` on the first `save.complete (save)` event |
| Active time to AIRs | `active_time_ms` on `save.complete (save_to_airs)` |
| Save → AIRs ratio by question count | Group `save_to_airs` events by `question_count` |
| Drop-off analysis | Most common last event before `nav.leave` where `unsaved_changes: true` |
| Validation friction | Frequency of `save.validation_blocked` before eventual `save.complete` |

### 8.3 Excluding Read-Only Sessions

> **Open question:** Sessions where `editor_mode = "read_only"` (pessimistic lock observers) should likely be excluded from funnel conversion and active time metrics, since those users cannot save. Confirm with stakeholders.

---

## 9. Performance & Error Tracking

### 9.1 Automatic (No Implementation Required)

Datadog RUM automatically captures out of the box:

| Signal | What it tells you |
|---|---|
| Page load time | How fast the editor loads |
| XHR / fetch durations | Save API, publish API, AIRs API response times |
| Core Web Vitals (LCP, CLS, FID) | Perceived page performance |
| JavaScript errors | Unhandled exceptions and stack traces |
| Long tasks | JS blocking main thread > 50 ms (potential UI freeze) |
| Resource failures | Failed image loads, JS bundles, etc. |

### 9.2 Custom Performance Signals

The `duration_ms` on `editor.save.complete` and `editor.save.fail` provides application-level save latency, split by `save_type`. This supplements the raw XHR timing with business context.

---

## 10. Privacy & Data Governance

### 10.1 Phase 1 (Current)

No content filtering applied in Phase 1. Survey titles, question text, and choice labels may appear in event context attributes if passed by the implementation team. Acceptable for initial rollout.

### 10.2 Recommended Future Constraints (Phase 2+)

| Data Type | Recommendation |
|---|---|
| Survey content (question text, choice labels, survey title) | Redact before sending — send structural metadata only (IDs, types, counts) |
| User email | Acceptable for internal (Macromill) users; review for external/client users |
| Survey ID | OK — non-PII internal identifier |
| Respondent data | Never tracked (out of scope; Answer page is Phase 2) |

### 10.3 Datadog Redaction Options (for Phase 2)

- **`beforeSend` callback** in RUM SDK init — strip or mask fields before they leave the browser
- **Sensitive Data Scanner** — post-ingestion masking in Datadog (regex-based)
- **Allowlist approach** — only explicitly listed context keys are forwarded

---

## 11. SDK Initialization

```js
import { datadogRum } from '@datadog/browser-rum'

datadogRum.init({
  applicationId: '<APPLICATION_ID>',
  clientToken: '<CLIENT_TOKEN>',
  site: 'datadoghq.com',
  service: 'survey-editor',
  env: process.env.NODE_ENV,       // 'production' | 'staging' | 'development'
  version: APP_VERSION,
  sessionSampleRate: 100,           // 100% during initial rollout; tune down if volume is high
  sessionReplaySampleRate: 20,      // Capture full session replay for 20% of sessions
  trackUserInteractions: true,      // Auto-capture click events
  trackResources: true,
  trackLongTasks: true,
  defaultPrivacyLevel: 'mask-user-input'  // Mask all text inputs and textareas by default
})
```

> **Environment isolation:** Consider using separate Datadog RUM applications (different `applicationId`) for production vs staging to keep metrics clean.

---

## 12. Proposed Datadog Dashboards

| Dashboard | Primary Consumer | Key Widgets |
|---|---|---|
| **Feature Adoption** | PM | Question type usage %, logic rule usage by type, settings configured frequency |
| **Funnel Overview** | PM / Management | Create → Save → AIRs conversion rates, avg active time per stage, drop-off points |
| **UX Friction** | UX Design | Save validation errors by type, actions-before-first-save distribution, preview usage rate |
| **Performance** | Engineering | Save API p50/p95/p99 latency by `save_type`, page load time trend, long task frequency |
| **Error Monitor** | Engineering | JS error rate, save fail rate by `http_status`, lock heartbeat failure rate |
| **Lock Behavior** | PM + Engineering | Lock conflicts per day, avg lock hold duration, lock claim frequency, reconnect rate |

---

## 13. Open Questions for Stakeholder Discussion

| # | Question | Suggested Owner | Notes |
|---|---|---|---|
| 1 | Should we track individual choice/option additions within a question, or only question-level events? | PM + UX | More granularity = richer UX data but higher event volume |
| 2 | What session replay sample rate is right? (proposed: 20%) | PM + Engineering | Higher % = more storage cost in Datadog |
| 3 | Which dashboards should be built first? | PM | Need prioritization to scope engineering effort |
| 4 | Should `read_only` sessions (lock observers) be excluded from funnel and active time metrics? | PM + Engineering | They cannot save, so including them skews conversion rates |
| 5 | When should Phase 2 content redaction rules be applied? | PM + Legal/Compliance | Depends on data handling policy for survey content |
| 6 | Should tracking run in staging/development environments? | Engineering | Useful for QA validation but may pollute production dashboards |
| 7 | Is per-user tracking (with email/ID) acceptable, or do we need anonymous sessions? | PM + Legal | Depends on internal privacy policy |
| 8 | Should `editor.lock.heartbeat_fail` (consecutive failures) trigger an alert to on-call? | Engineering | Could indicate widespread network degradation |
| 9 | Do we want a `save_count` or `session_sequence_number` on save events to distinguish first-save from subsequent saves without a full funnel query? | Engineering | Small implementation detail, big query convenience |

---

## 14. Appendix: Full Event Name Reference

| Event Name | Category | Phase |
|---|---|---|
| `editor.survey.create` | Survey | Phase 1 |
| `editor.survey.open` | Survey | Phase 1 |
| `editor.survey.duplicate` | Survey | Phase 1 |
| `editor.survey.settings_change` | Survey | Phase 1 |
| `editor.page.add` | Survey | Phase 1 |
| `editor.page.delete` | Survey | Phase 1 |
| `editor.question.add` | Question | Phase 1 |
| `editor.question.delete` | Question | Phase 1 |
| `editor.question.reorder` | Question | Phase 1 |
| `editor.question.duplicate` | Question | Phase 1 |
| `editor.question.configure` | Question | Phase 1 |
| `editor.logic.add` | Logic | Phase 1 |
| `editor.logic.configure` | Logic | Phase 1 |
| `editor.logic.delete` | Logic | Phase 1 |
| `editor.logic.combination_add` | Logic | Phase 1 |
| `editor.save.start` | Save | Phase 1 |
| `editor.save.complete` | Save | Phase 1 |
| `editor.save.fail` | Save | Phase 1 |
| `editor.save.validation_blocked` | Save | Phase 1 |
| `editor.nav.open` | Navigation | Phase 1 |
| `editor.nav.leave` | Navigation | Phase 1 |
| `editor.nav.preview_open` | Navigation | Phase 1 |
| `editor.nav.preview_close` | Navigation | Phase 1 |
| `editor.lock.acquire` | Locking | Phase 1 |
| `editor.lock.release` | Locking | Phase 1 |
| `editor.lock.expire` | Locking | Phase 1 |
| `editor.lock.claim` | Locking | Phase 1 |
| `editor.lock.conflict_view` | Locking | Phase 1 |
| `editor.lock.heartbeat_fail` | Locking | Phase 1 |
| `editor.lock.reconnect` | Locking | Phase 1 |
| `editor.session.idle` | Session | Phase 1 |
| `editor.session.resume` | Session | Phase 1 |

**Total Phase 1 events: 32**

---

*Document version: 0.1 DRAFT — for stakeholder review and discussion*  
*Next step: align on open questions in Section 13, then hand to engineering for implementation planning*
