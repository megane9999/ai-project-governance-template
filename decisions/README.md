# Decision Registry

更新日: `<<YYYY-MM-DD>>`

Decisionは、重要判断、承認、例外、Risk受容を当時の証拠とともに保存します。後から結果に合わせて元本文を改変せず、Outcome addendaへ追記します。

| ID | Date | Type | Decision | Status | Authority / approver role | Revisit condition |
|---|---|---|---|---|---|---|

## Decision types

- `Governance`: 目的、Scope、運用、権限、情報境界。
- `Strategy`: 優先順位、開始、中止、拡大、資源配分。
- `Technical`: 長期影響または大きな切替費用がある技術判断。
- `Approval`: 外部行為、支出、本番変更、権限変更等の限定承認。
- `Exception`: 既存方針からの期限付き例外。
- `Risk acceptance`: 残存Riskを権限者が受容する判断。

## Rules

- 軽微で可逆的な実装選択はDecision化しない。
- AIは提案者になれるが、承認者にはならない。
- ApprovalとExceptionは対象、上限、期限、情報区分、最大損失を明示する。
- 方針変更時は旧Decisionを削除せず、新Decisionから`Supersedes`を記録する。
- Outcomeが出たら、日付付きで結果、想定との差、学習、次の再検討を追記する。
