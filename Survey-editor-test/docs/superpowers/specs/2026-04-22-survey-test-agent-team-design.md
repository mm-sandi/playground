# Survey Test Agent Team — Design Document

**Date:** 2026-04-22
**Author:** kurniawan@macromill.com
**Status:** Approved

---

## Context

The Survey Editor (rosemary-frontend) and Survey Answer system are driven by two components:
- **MYLang generator** — converts logic configured in Survey Editor into MYLang source code
- **MYLang executor** — runs that code at survey-answer time to control routing, validation, and display

Survey data is structured as **MaUS** (Macromill Unified Schema), a JSON/YAML format defining questionnaires, variables, logics, visual settings, and quotas.

As both the spec (MaUS schema, MYLang logic types) and the frontend (rosemary-frontend validations) evolve continuously, manually keeping test cases up to date is unsustainable. This document specifies an AI agent team that auto-generates, reviews, and publishes structured E2E test cases to Confluence — notifying the owner on Slack for human review before finalization.

---

## Goals

1. Automatically detect changes in MaUS schema, MYLang docs, and rosemary-frontend
2. Generate comprehensive, categorized test cases covering all 4 test domains
3. Self-review test cases before publishing (Synthesizer + Reviewer loop)
4. Publish draft Confluence pages and notify the owner on Slack weekly
5. Support on-demand runs for new feature test requirements

---

## Agent Team Architecture

### Overview

```
SPEC MONITOR (weekly, Mon 7am JST)
       │ change summary
       ▼
ORCHESTRATOR
       │ routes to relevant experts
   ┌───┴────────────────────────────┐
   ▼         ▼          ▼          ▼
MaUS      MYLang    Survey     Survey
Schema    Logic     Editor     Answer
Expert    Expert    Validator  Expert
   └───┬────────────────────────────┘
       │ domain inputs
       ▼
TEST CASE SYNTHESIZER (draft)
       │ draft test cases
       ▼
TEST CASE REVIEWER (re-reads specs independently)
       │ structured feedback
       ▼
TEST CASE SYNTHESIZER (revision pass)
       │ final test cases
   ┌───┴───┐
   ▼       ▼
Confluence  Slack
Publisher   Notifier
```

### Agent Responsibilities

| Agent | Role |
|---|---|
| **Spec Monitor** | Runs weekly (Mon 7am JST). Compares current version fingerprints of watched sources against `.claude/state/spec-monitor.json`. Triggers Orchestrator if changes detected. |
| **Orchestrator** | Receives change summary and/or manual test requirements. Routes to relevant expert agents. Collects their outputs and passes to Synthesizer. |
| **MaUS Schema Expert** | Reads `maus-definitions/schema/schema-specification.json` (develop branch). Understands question types, variable types, logic field definitions, and schema constraints. |
| **MYLang Logic Expert** | Reads MYLang Confluence pages in SERVEY space. Understands all 25+ logic types, generator input/output, executor behavior, and FE-BE-MYLang interface. |
| **Survey Editor Validator** | Reads `macromill/rosemary-frontend` source code. Understands FE-side validation rules and constraints per question type and logic config. |
| **Survey Answer Expert** | Reads executor documentation in Confluence SERVEY space. Understands how MYLang executor is invoked, parameter passing, and return value handling. |
| **Test Case Synthesizer** | Merges expert outputs into structured test cases in 4 categories. Performs exactly one revision pass after receiving Reviewer feedback, then finalizes. |
| **Test Case Reviewer** | Re-reads source specs independently (does not trust Synthesizer's interpretation). Checks for missing edge cases, incorrect expectations, spec contradictions, and duplicates. Returns structured feedback. |
| **Confluence Publisher** | Creates or updates draft Confluence pages under the designated parent folder. Maintains stable Test IDs. Prefixes page titles with `[DRAFT]`. |
| **Slack Notifier** | Sends a structured summary to kurniawan@macromill.com via Slack DM with counts, category breakdown, Confluence links, and Reviewer notes summary. |

---

## Knowledge Sources

| Agent | Source | Access Method |
|---|---|---|
| Spec Monitor | Confluence SERVEY space (MYLang pages) | Confluence MCP — compare page version numbers |
| Spec Monitor | `maus-definitions` GitHub repo | GitHub API — compare file SHA on develop branch |
| Spec Monitor | `rosemary-frontend` GitHub repo | GitHub API — compare latest commit SHA on main branch |
| MaUS Schema Expert | `maus-definitions/schema/schema-specification.json` | GitHub API raw file fetch |
| MYLang Logic Expert | Confluence SERVEY space: MYLang docs, logic type pages, FE-BE-MYLang interface (page 720175773) | Confluence MCP |
| Survey Editor Validator | `macromill/rosemary-frontend` source | GitHub API — scan validation logic |
| Survey Answer Expert | Confluence SERVEY space: executor docs (page 725057681) | Confluence MCP |
| Test Case Reviewer | Same as Expert agents (re-reads independently) | Confluence MCP + GitHub API |

### State File

`.claude/state/spec-monitor.json` — stores last-seen version fingerprints:

```json
{
  "last_run": "2026-04-21T07:00:00+09:00",
  "sources": {
    "confluence_mylang_pages": { "page_versions": {} },
    "maus_schema": { "sha": "abc123..." },
    "rosemary_frontend": { "commit_sha": "def456..." }
  }
}
```

---

## Test Case Categories & Confluence Structure

**Parent folder:** `survey` space, folder ID `740393274`
URL: https://macromill.atlassian.net/wiki/spaces/survey/folder/740393274

```
📁 survey/folder/740393274  (existing parent)
└── 📁 Survey Editor & Answer — Test Cases
    ├── 📄 [DRAFT] 1. Editor UI Validations
    ├── 📄 [DRAFT] 2. MYLang Logic Generation
    ├── 📄 [DRAFT] 3. Survey Answer Execution
    ├── 📄 [DRAFT] 4. E2E Flow (Editor → Answer)
    └── 📄 Change Log
```

### Test ID Prefixes

| Category | Prefix | Example |
|---|---|---|
| Editor UI Validations | `ED-` | `ED-001` |
| MYLang Logic Generation | `GEN-` | `GEN-042` |
| Survey Answer Execution | `EX-` | `EX-017` |
| E2E Flow | `E2E-` | `E2E-005` |

### Page Column Schemas

**1. Editor UI Validations**
`Test ID | Scenario | Input | Expected Result | MaUS field ref`

**2. MYLang Logic Generation**
`Test ID | Logic Type | Generator Input | Expected MYLang Output | Edge Cases`

**3. Survey Answer Execution**
`Test ID | Logic Type | Survey State | Executor Input | Expected Behavior`

**4. E2E Flow**
`Test ID | Scenario Title | Setup Steps | Answer Steps | Expected Outcome`

### Publishing Rules

- Pages updated in place — new cases appended, existing ones revised if spec changed
- Nothing deleted without a note in the Change Log
- `[DRAFT]` prefix removed by owner after review
- Reviewer notes kept as page comments for traceability

---

## Scheduling & Triggering

### Weekly Automatic Run

**Schedule:** Every Monday at 7:00 AM JST

**Spec Monitor steps:**
1. Load `.claude/state/spec-monitor.json`
2. Check Confluence MYLang page versions via MCP
3. Check `maus-definitions` schema SHA via GitHub API
4. Check `rosemary-frontend` latest commit SHA via GitHub API
5. If no changes → log "no changes detected" → stop
6. If changes → build change summary → invoke Orchestrator
7. Update `.claude/state/spec-monitor.json` with new fingerprints

### On-Demand Run

Start a Claude Code session in this repository and invoke the Orchestrator agent directly with a plain-text test requirement. No schedule needed — runs immediately in the foreground:

```
"Add test cases for the new `notSameInput` logic type.
 It should prevent the same free-text answer being entered
 in two different input boxes within the same question."
```

The on-demand path skips the Spec Monitor's change-detection step and goes directly to the Orchestrator.

---

## Slack Notification Format

```
🤖 Survey Test Agent — Weekly Run (Mon YYYY-MM-DD)

📋 Changes detected:
  • maus-definitions: schema-specification.json updated (vX → vY)
  • rosemary-frontend: N commits since last check

✅ Test cases drafted: N new, N updated
  Category breakdown:
  • Editor UI Validations: N new
  • MYLang Logic Generation: N new, N updated
  • Survey Answer Execution: N new, N updated
  • E2E Flow: N new

🔗 Review here:
  → [1. Editor UI Validations] <link>
  → [2. MYLang Logic Generation] <link>
  → [4. E2E Flow] <link>

⚠️  Reviewer flagged N items — resolved by Synthesizer revision.
    Notes kept in page comments.
```

---

## Domain Reference

### MaUS Logic Types (25+)
`multiAnswerCount`, `multiInputCount`, `inputOrderCount`, `screeningOut`, `questionSelect`, `commentSelect`, `choiceSelect`, `itemSelect`, `inputBoxSelect`, `cellSelect`, `notRequired`, `exclusiveChoices`, `checkAlert`, `autoSelect`, `includeChoices`, `notSameSelect`, `notSameInput`, `inputOrder`, `inputLength`, `checkSum`, `maNotSameColumn`, `questionRandomize`, `choiceRandomize`, `itemRandomize`, `loop`, `daily`

### MaUS Question Types
`singleAnswerSimple`, `multipleAnswerSimple`, `openEndedSimple`, `singleAnswerMatrix`, `multipleAnswerMatrix`, `openEndedMatrix`, `rankingAnswer`, `ratioAnswer`

### Key Confluence Pages (SERVEY space)
- MYLang overview: page `876118215`
- FE-BE-MYLang interface: page `720175773`
- Executor parameter passing: page `725057681`
- MYLang source repos: page `785580154`

### Key GitHub Repos
- MaUS schema: `macromill/maus-definitions` (branch: `develop`)
- Survey Editor FE: `macromill/rosemary-frontend`

---

## Files Created / Modified

| Path | Purpose |
|---|---|
| `.claude/state/spec-monitor.json` | Version fingerprints for watched sources |
| `.claude/scheduled-tasks/spec-monitor/SKILL.md` | Spec Monitor agent definition |
| `agents/orchestrator/SKILL.md` | Orchestrator agent definition |
| `agents/maus-schema-expert/SKILL.md` | MaUS Schema Expert definition |
| `agents/mylang-logic-expert/SKILL.md` | MYLang Logic Expert definition |
| `agents/survey-editor-validator/SKILL.md` | Survey Editor Validator definition |
| `agents/survey-answer-expert/SKILL.md` | Survey Answer Expert definition |
| `agents/test-case-synthesizer/SKILL.md` | Test Case Synthesizer definition |
| `agents/test-case-reviewer/SKILL.md` | Test Case Reviewer definition |
| `agents/confluence-publisher/SKILL.md` | Confluence Publisher definition |
| `agents/slack-notifier/SKILL.md` | Slack Notifier definition |
| `docs/superpowers/specs/2026-04-22-survey-test-agent-team-design.md` | This document |
