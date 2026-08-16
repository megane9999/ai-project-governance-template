---
id: DEC-0001
title: "Start with synthetic read-only validation"
date: 2030-01-11
status: Approved
decision_type: Strategy
proposed_by_role: AI
approved_by_role: Project Owner
effective_from: 2030-01-11
expires_on: 2030-01-31
related_records: [WRK-0001, RES-0001, EXP-0001]
supersedes: []
---

# DEC-0001: Start with synthetic read-only validation

## Decision

最初の検証は完全な合成データだけを使い、入力を変更しない差異候補生成に限定する。本番接続、外部送信、自動通知は許可しない。

## Reason

検出ruleの成立性は、実データや本番権限を使わずに先に確認できるため。

## Evidence

- [RES-0001](../research/RES-0001-current-process.md): 合成processと未確認事項。
- 確認済み内部事実（合成例）: 既知の差異を含む30行のfixtureを作成可能。

## Alternatives

- 本番read-only接続: 情報管理と権限の確認前なので採用しない。
- 手作業processを先に全面変更: 検出成立性が未確認なので採用しない。
- 検証しない: 現状仮説を判断できないため採用しない。

## Risks and limits

- 合成データに過適合する可能性がある。
- 本番適用を承認しない。
- 期限は2030-01-31。次段階は新しいDecisionを必要とする。

## Revisit condition

EXP-0001完了、または検証が本番情報・外部行為を必要とした時。

## Outcome addenda

未評価。
