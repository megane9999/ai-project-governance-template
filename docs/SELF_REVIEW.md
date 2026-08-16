# Operating System Self-Review

実施日: `<<YYYY-MM-DD>>`

次回レビュー: `<<YYYY-MM-DD_OR_CONDITION>>`

## Conclusion

`<<現行構造を維持、簡素化、または再設計する判断>>`

## Review questions

- AIは新しいセッションで10分以内に現在地を復元できるか。
- 同じ情報が複数の場所で矛盾していないか。
- CharterとStrategyが混ざっていないか。
- Research、Experiment、Decisionの境界が守られているか。
- 承認なしの外部行為、支出、本番変更が起きていないか。
- DecisionのOutcomeが追記され、過去本文が後知恵で改変されていないか。
- 中止や失敗の学習が検索可能か。
- 人間が管理システムの更新に過剰な時間を使っていないか。
- 情報区分とAI入力条件が現在の会社規程に合っているか。

## Minimum metrics

| Metric | Current | Threshold / expectation | Action |
|---|---:|---:|---|
| Registry mismatch | `<<N>>` | 0 | 修正と原因確認 |
| Broken internal links | `<<N>>` | 0 | 修正 |
| Unresolved placeholders in active mode | `<<N>>` | 0 | 初期化完了 |
| Duplicate research in review period | `<<N>>` | `<<THRESHOLD>>` | 検索・index改善 |
| Missed end-of-work sync | `<<N>>` | `<<THRESHOLD>>` | AGENTS / automation改善 |
| Human maintenance time | `<<TIME>>` | `<<THRESHOLD>>` | 構造簡素化 |

## Redesign triggers

次のいずれかを継続的に満たした時だけ、構造追加または外部ツール導入をDecisionとして検討します。

- Active Initiativeが10件を超え、Markdown検索では優先順位を追えない。
- Running Experimentがチームの処理能力を超え、依存関係管理が必要。
- 月2回以上、台帳更新漏れ、重複調査、状態不整合が起きる。
- 月20件以上の予算取引があり、会計・調達システムとの連携が必要。
- 複数AIまたは複数人の同時編集でID衝突やmerge conflictが反復する。
- 監査、権限分離、retention、電子承認など正式統制が必要になる。
- Active Issueが10件を超え、Project boardが明確な追跡価値を持つ。
- 構造検証スクリプトで検出できない重大な更新漏れが反復する。

## Changes deliberately avoided

- `<<必要性が未確認のため追加しなかった仕組み>>`

## Decision

- Related Decision: `<<DEC-NNN_OR_NONE>>`
- Owner: `<<ROLE>>`
- Next review: `<<DATE_OR_CONDITION>>`
