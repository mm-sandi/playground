# 44 — Ranking Question Unit and Required-Count Settings (順位回答質問単位変更チェック)

**Total scripts:** 1 survey-creation script + answer scripts  
**Purpose:** Verify that ranking (RNK) question display unit (位/番目/etc.) and required-rank-count settings can be configured correctly, and that the preview reflects the configured settings.

---

## TC-44-01 — Ranking Display Unit and Required Count Configuration

**Scope:** Admin  
**Platform:** Desktop

**Scenario:** An administrator creates surveys with ranking questions using different display-unit settings (位 = rank position, 番目 = ordinal) and different required-count modes (all required, first N required, no requirement). The preview must display the correct unit labels and required indicators.

**Setup:**
- Admin user (ID: admin_50128)
- Survey named "順位回答質問単位指定による動作確認_回答用アンケート[N]"

**Steps:**
1. Admin creates a ranking question with 3 items and "all required" mode.
2. Admin previews — verifies "3位：" label appears, "4位：" does NOT appear, and "【 全て必須 】" indicator is shown.
3. Admin changes display unit to 4 items and turns off required mode.
4. Admin previews — verifies "4位：" appears and "【 全て必須 】" is gone.
5. Admin changes to "required up to rank 2" (ge mode, requiredPlace=2).
6. Admin previews — verifies "【 2位まで必須 】" indicator appears.
7. Admin creates a second ranking question using "番目" unit (ordinal) with "required up to 1st" setting.
8. Admin previews — verifies "3位：" does NOT appear and "【 1番目まで必須 】" indicator shows.
9. Admin creates a third ranking question with 5 choices in free-rank unit (value=99), required up to 4.
10. Admin previews — verifies "【 4まで必須 】" indicator shows.

**Expected Results:**
- Rank display units (位, 番目, free unit) render correctly in preview.
- Required-rank-count indicators ("全て必須", "N位まで必須", "N番目まで必須") display correctly.
- Configuring "required off" removes the required indicator from preview.
- Rank item count limits are respected in the preview display.

---
