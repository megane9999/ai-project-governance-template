# AI Project Governance Template

GitとMarkdownを使い、AIを主要な実行・整理主体、人間を目的設定・承認・最終判断主体として運用するためのプロジェクト管理テンプレートです。

このリポジトリが管理するのは、単なるタスク一覧ではありません。目的、戦略、証拠、検証、意思決定、リスク、指標、予算、過去の学習を、それぞれ一意の正本として残します。AIとの会話が失われても、次のセッションがリポジトリから現在地を復元できることを目標にしています。

## このテンプレートの設計原則

- 恒久的な目的・制約と、証拠に応じて変える戦略を分離する。
- 事実、外部情報、推定、仮説、未確認を区別する。
- 重要な検証は開始前に成功・失敗・撤退条件を固定する。
- 重要判断は当時の証拠と代案を含む追記型Decisionとして保存する。
- AIが自律実行できる範囲と、人間承認が必要な行為を明示する。
- 会話、リポジトリ文書、GitHub Issue、Pull Requestの正本を分ける。
- 失敗・中止・却下を削除せず、再検討条件と再利用可能な学習を残す。
- 規模が小さい間はMarkdown中心で運用し、必要性が観測されるまでDBやダッシュボードを増やさない。

## 始め方

業務情報をこの公開元リポジトリへ書き込まないでください。推奨フローは次のとおりです。

1. このリポジトリから、会社管理下のPrivateまたはInternalリポジトリを新規作成する。
2. 会社の情報管理規程、AI利用規程、Repository visibility、アクセス権を確認する。
3. [START_HERE.md](START_HERE.md) に従い、GitHub Copilot等のAIへ初期化を依頼する。
4. `project.toml`、[PROJECT.md](PROJECT.md)、Charter、Strategy、Governanceを人間がレビューする。
5. `python tools/validate_repository.py --strict` を実行してから通常運用へ移る。

## 読む順序

1. [導入手順](START_HERE.md)
2. [構造と正本](docs/ARCHITECTURE.md)
3. [プロジェクト憲章](docs/CHARTER.md)
4. [現在の戦略](docs/STRATEGY.md)
5. [運用ルール](docs/OPERATIONS.md)
6. [AI・人間の権限境界](docs/GOVERNANCE.md)
7. [情報管理ポリシー](docs/INFORMATION_POLICY.md)

## 構成

```text
PROJECT.md        現在地と次アクションの入口
docs/             憲章、戦略、運用、権限、情報管理、構造レビュー
initiatives/      成果を生む作業単位と状態の台帳
research/         出典付きの調査・証拠・未確認事項
experiments/      事前登録した検証と結果
decisions/        重要判断・承認・例外の追記型ログ
metrics/          成果指標と運用品質指標
risks/            リスク、対策、受容判断、再評価条件
budget/           予定額と実績額の一意な台帳
archive/          中止・失敗・旧版の学習資産
templates/        各レコードの標準形
tools/            ID採番と構造検証の補助ツール
examples/         実在情報を含まない架空の使用例
```

## CoreとOptional modules

Coreは `PROJECT.md`、`docs/`、`initiatives/`、`research/`、`decisions/`、`metrics/`、`risks/` です。

`experiments/` と `budget/` は任意ですが、仮説検証、PoC、調達、外部支出があるプロジェクトでは有効です。無効化する場合も、初期化Decisionに理由を残してください。

## 重要な注意

- このテンプレート自体は、会社の情報管理規程や法的要件に代わるものではありません。
- 認証情報、秘密鍵、個人データ、顧客データ、規制対象データを、承認なしにリポジトリや外部AIへ入力しないでください。
- `AGENTS.md` はAI運用ルールの正本です。`.github/copilot-instructions.md` はGitHub Copilot向けの入口です。

## License

[MIT License](LICENSE)

## 現在の状態

このリポジトリは `template` modeです。実案件へ利用する際は [START_HERE.md](START_HERE.md) の初期化を完了し、`project.toml` の `mode` を `active` に変更します。
