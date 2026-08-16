# AI operating rules

このファイルは、このリポジトリで作業するAIが毎回守る最小ルールの正本です。

## 作業開始時

1. `project.toml` と `PROJECT.md` を読む。
2. `docs/CHARTER.md`、`docs/STRATEGY.md`、`docs/GOVERNANCE.md`、`docs/INFORMATION_POLICY.md` を読む。
3. `initiatives/README.md`、`decisions/README.md`、`metrics/README.md`、`risks/README.md` で現在地を確認する。
4. 進行中作業に関係するResearch、Experiment、Decision、Riskだけを追加で読む。
5. `mode = "template"` なら、通常作業を始めず`START_HERE.md`に従う。

## 正本と事実性

- 会話を長期記憶の正本にしない。重要事項を終了前にリポジトリへ同期する。
- `確認済み内部事実 / 確認済み外部事実 / 推定 / 仮説 / 未確認` を区別する。
- 外部情報には発行主体、公開日、URLまたは文書ID、確認日、使用した主張を残す。
- 変わり得る規約、価格、法令、仕様、組織情報は、重要判断の直前に再確認する。
- 数字には出典、計算式、仮定、またはレンジを付ける。精度を装わない。
- 矛盾を見つけたら黙って一方を採用せず、正本と証拠を特定して解消する。

## AIが自律実行できること

プロジェクトのScope内かつ情報管理ポリシーに適合する場合、次を自律実行してよい。

- リポジトリ内情報の読取、検索、整理、要約、整合性確認。
- 公開情報または承認済み内部情報を使った調査とResearch下書き。
- 文書、コード、テスト、分析、テンプレートの作成・修正。
- 既存方針に沿った台帳、指標、次アクションの更新。
- 承認不要なローカル検証と、結果の記録。

自律実行可能でも、破壊的変更、広範な書換え、復旧困難な操作は事前に対象を確認し、回復可能な方法を優先する。

## 人間承認ゲート

次は実行前に、`docs/GOVERNANCE.md`で定めた人間の承認を得る。

- 外部公開、外部送信、顧客・取引先・従業員への連絡。
- 支払い、発注、契約、金融取引、ライセンス同意。
- アカウント作成、権限変更、秘密情報・個人データの提供。
- 本番環境、顧客環境、共有データへの変更。
- 法的責任、セキュリティ、コンプライアンスへ影響する行為。
- Charter、Scope、成功条件、主要優先順位の変更。
- まとまった人間作業、または他チームへの作業依頼。

承認依頼には、必要性、AIで代替できない理由、対象、金額、人間時間、得られる情報または価値、最大損失、ロールバック、期限を含める。AIは自分の行為を承認しない。

## 記録の作り方

- Initiative: `WRK-NNN`。台帳と個別記録を同じ変更で更新する。
- Research: `RES-NNN`。主張と根拠、鮮度、適用範囲を分ける。
- Experiment: `EXP-NNN`。開始前に成功・失敗・撤退条件を固定し、開始後の変更は追記する。
- Decision: `DEC-NNN`。当時のDecision、Reason、Evidence、Alternatives、Risksを結果に合わせて改変しない。結果はOutcomeへ追記する。
- Risk: `RSK-NNN`。影響、可能性、owner、対策、受容者、再評価条件を残す。
- IDは`python tools/new_record.py`を優先し、手動の場合は対象ディレクトリの最大値+1とする。
- 中止・失敗・旧版は削除せず、Decisionと再検討条件を付けて`archive/`へ移す。

## GitHubの使い分け

- AIとの会話: 相談、説明、短い承認。
- リポジトリ文書: 方針、証拠、設計、結果、判断の正本。
- GitHub Issue: セッションをまたぐ実行項目、期限付き作業、外部依存、保留判断。
- Branch / Pull Request: レビューが必要な差分。

同じ詳細をIssueとMarkdownへ複製しない。Issueは正本リンク、owner、期限、完了条件、承認要否だけを持つ。

## 作業終了時

1. 結果を該当するResearch、Experiment、Decision、Riskへ記録する。
2. Initiative台帳、Metrics、Budget、`PROJECT.md`を必要な範囲で同期する。
3. 次アクション、owner、review条件、blockerを明示する。
4. `python tools/validate_repository.py --strict` を実行する。
5. 未確認事項、承認待ち、検証失敗を成功扱いしない。

## 構造変更

新しいDB、ダッシュボード、分類、ID体系、自動化を、見栄えだけを理由に追加しない。`docs/SELF_REVIEW.md`の再設計条件が満たされた時にDecisionとして検討する。
