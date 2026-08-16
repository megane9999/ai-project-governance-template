---
id: EXP-0001
title: "Synthetic discrepancy detection"
status: Ready
created: 2030-01-12
start_date: 2030-01-15
review_date: 2030-01-17
end_date: ""
owner_role: AI
related_work: [WRK-0001, RES-0001]
approval_decisions: [DEC-0001]
---

# EXP-0001: Synthetic discrepancy detection

## Pre-registration

- Hypothesis: 単純なjoinとvalidation ruleで既知差異を再現可能に検出できる。
- Most valuable uncertainty: 誤検出を抑えながら既知差異を拾えるか。
- Method: 合成30行に既知差異8件を埋め込み、同じcommandを2回実行する。
- Cash cost planned / ceiling: 0。
- Human time planned / ceiling: 30分。
- Success criteria: 8件すべて検出、誤検出2件以下、2回の出力が一致。
- Failure criteria: 検出率90%未満、または再実行結果が不一致。
- Stop-loss: 2時間を超える例外処理が必要なら停止。
- Guardrails: 合成データのみ、network送信なし、入力変更なし。
- Required approvals: DEC-0001の範囲内。追加承認なし。
- Decision rule: Successなら、情報管理と本番接続条件だけを次Researchで確認する。Failureならruleを作り込まず原因を記録してParkする。

## Change log

開始前。変更なし。

## Result

未実施。

## Decision

未評価。
