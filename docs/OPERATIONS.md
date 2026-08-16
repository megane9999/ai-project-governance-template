# Operating System

## Records and states

| Record | ID | Recommended states |
|---|---|---|
| Initiative | `WRK-NNN` | Inbox / Researching / Planned / Active / Blocked / Parked / Completed / Cancelled |
| Research | `RES-NNN` | Draft / Current / Stale / Superseded |
| Experiment | `EXP-NNN` | Draft / Ready / Running / Completed / Cancelled |
| Decision | `DEC-NNN` | Proposed / Approved / Rejected / Superseded |
| Risk | `RSK-NNN` | Open / Mitigating / Accepted / Closed |

ファイル名は`ID-short-name.md`とします。ID作成は`python tools/new_record.py <type> "<title>"`を優先します。

## One operating cycle

1. `PROJECT.md`、Strategy、各台帳から現在地を復元する。
2. Charterに対して最も価値の高い未確定事項または成果を一つ選ぶ。
3. 必要ならInitiative、Research、Experiment、Riskを登録する。
4. Experimentは開始前に成功・失敗・撤退条件を固定する。
5. GovernanceとInformation Policyの範囲内でAIが作業する。
6. 承認ゲートに該当する直前で止まり、必要情報を添えて人間へ判断を依頼する。
7. 生データまたは成果物へのリンク、観測値、想定外、限界を記録する。
8. Continue / Change / Park / Stop / Scale等の重要判断をDecisionに残す。
9. Initiative、Metrics、Risk、Budget、Strategy、PROJECTを必要な範囲で同期する。

## Evidence labels

- **確認済み内部事実**: 承認済みの内部正本またはリポジトリ内の実測で確認。
- **確認済み外部事実**: 出典、確認日、使用した主張がある外部情報。
- **推定**: 明示した仮定と計算から導出。
- **仮説**: まだ検証していない因果、需要、効果、実現可能性。
- **未確認**: 判断に必要だが、証拠がないか利用できない。

第三者の主張は、出典があっても自組織へそのまま適用できるとは限りません。適用範囲と限界を記録します。

## Pre-registration

重要な検証は開始後に都合よく評価基準を変えないよう、次を固定します。

- Hypothesisと最も価値の高い未確実性。
- Method、対象、サンプル、期間。
- Cash costとHuman timeの上限。
- Success、Failure、Stop-loss。
- Guardrailsと承認が必要な行為。
- 結果に基づく次の判断。

変更が必要な場合は元の記述を消さず、Change logへ理由と解釈への影響を追記します。

## Decision protocol

次はDecisionを作ります。

- Charter、Scope、Strategy、主要優先順位を変える。
- Initiativeを開始、中止、拡大、長期Parkする。
- 支出、外部公開、本番変更、例外を承認する。
- 重要Riskを受容する。
- 将来同じ議論を繰り返す可能性が高い。

軽微で可逆的な実装詳細はDecision化しません。

## Registry synchronization

- 新規レコード作成時に、同じ変更で対応する`README.md`台帳へ追加する。
- 状態変更時に個別レコードと台帳を同時更新する。
- 終了時に`PROJECT.md`の現在地と次アクションを確認する。
- 現金予定・実績は`budget/ledger.csv`を唯一の台帳にする。
- 詳細を複製せず、IDと相対リンクで接続する。

## Review cadence

- 各Experiment終了時: 結果、Decision、Initiative、Metrics、Budget、Riskを同期。
- 定期レビュー: `project.toml`で定めたcadenceに従い、全InitiativeとRiskを再判定。
- 節目: Charterへの到達度、Strategy、AI/人間分担、情報管理を再評価。
- 臨時: 重大な仕様、法令、組織、セキュリティ、予算、外部環境の変化時。

## Reporting format

重要な提案は、原則として次の順にします。

`結論 / 根拠 / 数値または観測 / 不確実性 / 推奨する次の検証 / 必要な人間判断`

## GitHub Issue boundary

Issueを作る条件:

- 現在のセッションで完了しない独立作業。
- 期限、owner、外部依存がある。
- 人間判断が後日に持ち越される。
- 複数commitまたはレビュー工程が必要。

Issue本文は`目的 / 正本リンク / owner / 期限またはreview / 完了条件 / 承認要否`に絞ります。調査結果やDecision本文は正本側へ置きます。

## Handoff

AIの会話を切り替える前に、重要判断、状態、指標、予算、次アクションを既存の正本へ同期します。通常は専用の引継ぎ文書を作らず、新しいAIが開始手順から復元できる状態にします。
