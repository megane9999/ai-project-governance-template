# GitHub Copilot repository instructions

`AGENTS.md` がこのリポジトリのAI運用ルールの正本です。作業前に必ず全文を読み、競合する指示がある場合は、より上位の組織ポリシーと人間の明示指示に続いて`AGENTS.md`を優先してください。

特に次を守ってください。

- `project.toml` が `mode = "template"` の間は、通常の案件作業を始めず`START_HERE.md`に従う。
- Charter、Strategy、Governance、Information Policy、各台帳から現在地を復元する。
- 会話だけを正本にせず、証拠・検証・判断・リスクを対応するMarkdownへ同期する。
- 事実ラベル、出典、確認日、仮定、未確認事項を明示する。
- 外部行為、支出、契約、権限変更、本番変更、機密情報入力は、人間承認なしに実行しない。
- 重要なDecisionの元本文を結果に合わせて書き換えず、Outcomeへ追記する。
- 作業終了時に`python tools/validate_repository.py --strict`を実行する。

会社や組織のAI利用規程がこのリポジトリより厳しい場合は、会社・組織の規程を優先してください。
