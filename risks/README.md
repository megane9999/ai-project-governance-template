# Risk Registry

更新日: `<<YYYY-MM-DD>>`

| ID | Risk | State | Impact | Likelihood | Owner role | Mitigation / next check | Related work |
|---|---|---|---|---|---|---|---|

## Rules

- Risk scoreだけで順位を自動決定せず、影響経路と不確実性を書く。
- `Impact`と`Likelihood`の尺度はプロジェクト内で定義を揃える。
- Mitigation、contingency、early warning、review条件を分ける。
- 残存Riskの`Accepted`には権限者と関連Decisionが必要。
- IssueはRiskそのものの正本にせず、対策作業の実行キューとしてリンクする。
- 閉じたRiskも、将来の再発条件がある場合は残す。
