# 導入手順

この手順は、公開テンプレートから会社管理下の新しいプロジェクトリポジトリを作ることを前提にしています。公開元へ業務情報をcommitまたはpushしないでください。

## 0. リポジトリ境界を確定する

初期化前に人間が次を確認します。

- 新しいリポジトリは会社管理下のPrivateまたはInternalである。
- 公開元ではなく、新規リポジトリの`origin`へpushする設定になっている。
- Repository access、branch protection、backup、retentionが会社方針に適合する。
- 使用するAIが、入力予定の情報区分を扱うことを会社から許可されている。
- 顧客秘密、個人データ、認証情報、規制対象データの保存・AI入力条件が確認されている。

不明な項目があれば、`mode = "template"` のまま止めます。

## 1. AIへ初期化を依頼する

GitHub Copilot等へ、次の依頼をそのまま渡せます。

```text
このリポジトリを新しい業務プロジェクト用に初期化してください。
最初に AGENTS.md、START_HERE.md、docs/CHARTER.md、docs/GOVERNANCE.md、
docs/INFORMATION_POLICY.md を読んでください。

まだファイルを変更せず、初期化に必要な人間判断だけを一覧にしてください。
秘密情報・個人情報・顧客情報の入力は要求しないでください。
回答後、人間が提供した非機密の情報だけで初期化案を作り、
Charter、Strategy、PROJECT.md、project.toml、各台帳を整合させてください。
最後に python tools/validate_repository.py --strict を実行し、
未解決事項と人間の承認が必要な点を報告してください。
```

## 2. 最小限の人間判断

AIは次の内容を推測で確定してはいけません。

1. プロジェクトの目的と成功状態。
2. Scopeと明確なNon-goals。
3. Project Ownerと最終承認者の役割。
4. 期限、予算、人間時間、品質、法務・セキュリティ上の制約。
5. AIが利用できるデータ区分と、利用可能なAI環境。
6. 外部公開、外部連絡、支出、契約、本番変更等の承認者。
7. 初回レビュー日または再検討条件。

個人名が不要なら、`Project Owner`、`Security Approver`のような役割名で記録します。

## 3. 初期化時に更新する正本

- `project.toml`: mode、プロジェクト名、情報区分、使用言語、enabled modules。
- `PROJECT.md`: 現在地、直近の目的、次の人間判断、次のAI作業。
- `docs/CHARTER.md`: 目的、Scope、Non-goals、成功状態、制約、変更権限。
- `docs/STRATEGY.md`: 現在のアプローチ、優先順位、仮説、レビュー条件。
- `docs/GOVERNANCE.md`: AI自律範囲、承認ゲート、承認者の役割。
- `docs/INFORMATION_POLICY.md`: 利用できる情報区分、禁止情報、AI入力条件。
- 各`README.md`: 空の台帳を初期状態にする。
- `decisions/DEC-0001-*.md`: この運用構造を採用した判断と再検討条件。

## 4. 初期化完了条件

- `project.toml` が `mode = "active"` である。
- `<<PLACEHOLDER>>` が、架空例とテンプレート以外に残っていない。
- CharterとGovernanceが人間レビュー済みである。
- 情報区分とAI利用範囲が明示されている。
- 最初のInitiativeまたはResearchが台帳へ登録されている。
- `python tools/validate_repository.py --strict` が成功する。
- 変更がPull Request等、会社のレビュー手順を通っている。

## 5. 通常運用

AIは各作業開始時に`AGENTS.md`の読み順へ従い、終了時に正本を同期します。会話上の結論だけで状態を進めず、重要判断はDecision、調査結果はResearch、検証結果はExperimentへ残します。

## 6. 公開元との関係

公開元は方法論の配布物です。会社側リポジトリは独立した業務記録です。

- 公開元への自動pushや双方向同期を設定しない。
- 更新を取り込む場合は、差分を人間がレビューする。
- 業務側のcommitやファイルを公開元へ送り返さない。
- 公開元の改善提案には、業務事例やログを貼らず、抽象化した方法だけを書く。
