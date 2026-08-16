# Metrics

基準日: `<<YYYY-MM-DD>>`

次回更新: `<<YYYY-MM-DD_OR_EVENT>>`

## Outcome metrics

Charterの成功状態に直接つながる指標だけを置きます。

| Metric | Current | Target / threshold | Source | Interpretation |
|---|---:|---:|---|---|
| `<<OUTCOME_METRIC>>` | `<<VALUE>>` | `<<TARGET>>` | `<<SOURCE>>` | `<<MEANING>>` |

## Leading indicators

| Metric | Current | Expected direction | Source | Decision use |
|---|---:|---|---|---|
| `<<LEADING_METRIC>>` | `<<VALUE>>` | `<<UP_DOWN_RANGE>>` | `<<SOURCE>>` | `<<USE>>` |

## Operating quality

| Metric | Current | Expectation |
|---|---:|---:|
| Active initiatives | `<<N>>` | チームの処理能力以内 |
| Running experiments | `<<N>>` | 明示した上限以内 |
| Open critical risks | `<<N>>` | ownerとreview条件が100%存在 |
| Registry mismatches | `<<N>>` | 0 |
| Broken internal links | `<<N>>` | 0 |
| Pre-registration rate | `<<PERCENT>>` | 重要Experimentで100% |
| Decisions with revisit condition | `<<PERCENT>>` | 重要Decisionで100% |
| Human maintenance time | `<<TIME_PER_PERIOD>>` | 明示した上限以内 |

## Interpretation rules

- 測定可能だからという理由だけで指標を増やさない。
- 指標にはsource、定義、期間、単位を付ける。
- ProxyをOutcomeとして扱わない。
- 数値の変化が判断を変えない場合、測定をやめることも検討する。
- 不都合な結果や欠測を削除しない。

## Current learning

- `<<EVIDENCE_BACKED_LEARNING_WITH_LINK>>`
