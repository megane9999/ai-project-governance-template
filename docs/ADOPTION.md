# Adoption and Update Guide

## Recommended topology

```text
Public template repository
        |
        | Use this template / one-time copy
        v
Company Private or Internal repository
        |
        +-- actual project knowledge and history
```

公開テンプレートと会社側リポジトリは、継続的な同期関係ではなく、配布元と独立instanceの関係にします。

## Why not clone and keep the public origin

公開元を`origin`のまま使うと、業務commitを誤って公開元へpushするRiskが残ります。GitHubのtemplate機能で新規リポジトリを作るか、clone直後に公開元を`upstream`へ改名し、会社側Private/Internalを`origin`へ設定してください。

最も安全なのは、会社のGitHub UIからtemplateを使い、最初から会社側の新しい履歴と`origin`を作る方法です。

## Initial adoption decisions

会社側の最初のDecisionには次を残します。

- この管理構造を採用する理由。
- 適用するプロジェクトScope。
- AI環境と扱える情報区分。
- 有効化・無効化するmodules。
- 人間承認者の役割。
- レビューcadence。
- 構造を廃止または再設計する条件。

## Receiving future template improvements

自動mergeは推奨しません。

1. 公開元のreleaseまたは変更差分を読む。
2. 方法論の変更だけを会社側branchへ手動で取り込む。
3. 会社側のCharter、Governance、Information Policyと競合しないか確認する。
4. 構造変更ならDecisionを作る。
5. Pull Requestでレビューし、validatorを実行する。

公開元へfeedbackする場合は、会社側ファイルやdiffを送らず、一般化した要望だけを新しく記述します。

## Copilot use

GitHub Copilotは`.github/copilot-instructions.md`を入口にし、`AGENTS.md`を正本として読みます。組織側のCopilot instructionsやpolicyがある場合は、それらが上位です。

AIへ「全部自律的に進めて」と依頼しても、GovernanceのYellow / Red zoneは解除されません。承認を省略したい定型操作がある場合は、対象、上限、期限、データ区分を限定したDecisionを人間が作ります。

## Decommissioning

利用を終了する場合は、会社のretention、legal hold、record managementへ従います。リポジトリ削除だけでなく、clone、fork、artifact、release、backup、AI側の保持条件も評価します。
