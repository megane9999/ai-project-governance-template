# AI and Human Governance

更新日: `<<YYYY-MM-DD>>`

承認者の役割: `<<APPROVER_ROLES>>`

## 1. Principle

AIは、情報処理、下書き、分析、実装、テスト、台帳同期を広く担当します。人間は、目的、情報境界、外部責任、支出、例外、重要な優先順位を保持します。

AIの技術的実行能力と、実行権限を混同しません。

## 2. Autonomy zones

### Green: AIが自律実行可能

- 承認済み情報の読み取り、整理、検索、要約。
- Scope内の文書、コード、テスト、分析の作成と修正。
- 公開情報の調査と、出典付きResearchの作成。
- ローカルまたは隔離環境での可逆的な検証。
- 既存Decisionに従う台帳、指標、Risk、次アクションの同期。

### Yellow: 実行直前に人間承認が必要

- 外部公開、外部送信、外部の人間への連絡や作業依頼。
- 支払い、発注、契約、利用規約への同意。
- 本番、顧客環境、共有データ、アクセス権の変更。
- アカウント作成、API key発行、個人データや秘密情報の提供。
- 重要Riskの受容、法務・セキュリティ例外。
- Charter、Scope、成功条件、主要優先順位の変更。
- 大量変更、不可逆変更、まとまった人間作業。

### Red: 明示承認があっても専門手続が必要

- 法令、契約、会社規程が禁止する行為。
- 権限のないデータ利用、機密情報の公開、認証情報のcommit。
- 安全対策や監査証跡を迂回する操作。
- AIが自分自身を承認者とすること。

Red zoneは通常の承認だけで実行可能になるものではありません。該当する専門部門または責任者の手続に従います。

## 3. Approval request schema

承認依頼は次を含めます。

- Requested actionと対象。
- Purposeと、今必要な理由。
- AIだけでは代替できない理由。
- 情報区分、外部送信先、影響範囲。
- Cash cost、Human time、他チームの負担。
- Expected information or value。
- 最大損失、主要Risk、軽減策。
- Rollbackまたは停止方法。
- 有効期限と、承認範囲を使い切る条件。
- 関連するWRK / RES / EXP / RSK。

承認結果は`decision_type: Approval`のDecisionに残します。チャット上の即時承認でも、実行前または作業終了前に正本へ反映します。

## 4. Approval boundaries

- 承認は記録された対象、金額、期間、環境、データ区分の範囲内だけ有効。
- 似た作業への包括的な自動拡張をしない。
- 期限切れ、前提変更、対象拡大、Risk増加時は再承認する。
- 予算枠の存在は支出承認を意味しない。
- Pull Request approvalは、明示されない限り支出・契約・公開承認を兼ねない。

## 5. Decision authority matrix

初期化時に役割を置き換えます。

| Decision | Proposer | Approver | Record |
|---|---|---|---|
| Charter / Scope change | AIまたはチーム | `<<PROJECT_OWNER_ROLE>>` | DEC |
| Strategy change | AIまたはチーム | `<<STRATEGY_APPROVER_ROLE>>` | DEC |
| External publication / contact | AIまたはチーム | `<<EXTERNAL_ACTION_APPROVER_ROLE>>` | DEC |
| Spending / contract | AIまたはチーム | `<<SPENDING_APPROVER_ROLE>>` | DEC + ledger |
| Production change | AIまたはチーム | `<<PRODUCTION_APPROVER_ROLE>>` | PR / DEC as needed |
| Risk acceptance | AIまたはチーム | `<<RISK_OWNER_ROLE>>` | RSK + DEC |
| Routine local work | AI | Governance | normal commit |

## 6. Human review quality

人間レビューは、AI生成物を全文再作成することではありません。重点確認項目は次です。

- 目的とScopeに合っているか。
- 事実、仮説、未確認が分かれているか。
- 情報区分と権限を超えていないか。
- 不都合な代案やRiskが落ちていないか。
- 承認範囲、上限、期限が具体的か。
- 次回、人間が同じ議論を繰り返さず判断できるか。

## 7. Emergency and exception handling

緊急対応や例外が必要な場合も、可能な限り対象、期限、責任者、復旧条件を先に限定します。事後記録が許される条件は会社規程に従い、事後には必ずDecisionとRiskへ経緯を追記します。
