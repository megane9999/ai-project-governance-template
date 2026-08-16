---
id: WRK-0001
title: "Weekly report reliability"
status: Active
owner_role: Project Owner
created: 2030-01-10
updated: 2030-01-14
next_review: 2030-01-17
related_decisions: [DEC-0001]
related_risks: []
---

# WRK-0001: Weekly report reliability

## Conclusion

- Current decision: Continue with synthetic, read-only validation.
- Next evidence: EXP-0001 result.

## Intended outcome

- User / beneficiary: 架空の週次レポート作成担当者。
- Problem: 転記確認に時間がかかり、集計差異が見つかる。
- Outcome: 入力を変更せず、差異候補を再現可能に検出する。
- Contribution to Charter: レポート品質と作成効率の改善。

## Scope

- In scope: 合成CSVの読取、集計、差異一覧の生成。
- Out of scope: 本番データ、システムへの書込、自動配信。
- Dependencies: DEC-0001、EXP-0001。

## Evidence state

| Claim | Label | Evidence / link | Checked |
|---|---|---|---|
| 現在のレポートは3種類の表を結合する | 確認済み内部事実（合成例） | [RES-0001](../research/RES-0001-current-process.md) | 2030-01-10 |
| 差異検出で確認時間を半減できる | 仮説 | [EXP-0001](../experiments/EXP-0001-synthetic-validation.md) | 未検証 |

## Completion and exit

- Completion criteria: 合成30行で既知の差異8件を全件検出し、誤検出2件以下、再実行結果が一致。
- Failure criteria: 既知差異の検出率90%未満、または入力を変更する設計が必要。
- Review: 2030-01-17。

## Resources

- Cash ceiling: 0（合成例）。
- Human-time ceiling: 30分。
- AI work: スクリプト、test、結果整理。
- Human work: 結果の妥当性レビュー。

## Outcome and lessons

- EXP-0001完了後に追記する。
