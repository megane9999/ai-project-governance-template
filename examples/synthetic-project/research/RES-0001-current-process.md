---
id: RES-0001
title: "Current weekly report process"
status: Current
created: 2030-01-10
updated: 2030-01-10
owner_role: AI
related_work: [WRK-0001]
recheck_on: "process change"
---

# RES-0001: Current weekly report process

## Conclusion

- Short answer: 架空の現行processは3表の手動結合と目視確認を含む。
- Decision impact: 最初はread-onlyな差異候補生成に限定する。
- Confidence and limits: 合成scenario内では確認済み。本番への適用可能性は未確認。

## Question and scope

- Question: 最小の検証で何を自動化できるか。
- Included: 合成された手順と列定義。
- Excluded: 実在データ、書込、通知、権限設計。
- Inspection date: 2030-01-10。

## Claims and evidence

| Claim | Label | Source | Checked | Applicability / limit |
|---|---|---|---|---|
| 3種類の表をreport keyで結合する | 確認済み内部事実（合成例） | 合成process definition | 2030-01-10 | 架空例のみ |
| 既知の差異は30行中8件 | 確認済み内部事実（合成例） | 合成test fixture | 2030-01-10 | 本番分布を表さない |
| 同じruleが実業務にも適用できる | 未確認 | なし | 2030-01-10 | 本番データなしでは判断不可 |

## Unknowns

- 実データの列揺れ、欠損、権限、retention。
- 担当者が必要とする差異理由の粒度。

## Recommended next step

- [EXP-0001](../experiments/EXP-0001-synthetic-validation.md)で合成fixtureだけを検証する。
