# Information and AI Data Policy

更新日: `<<YYYY-MM-DD>>`

この文書はテンプレートです。会社の正式な情報管理規程、契約、法令、AI利用規程が常に優先します。

## 1. Repository classification

- Repository classification: `<<PUBLIC_INTERNAL_CONFIDENTIAL_OR_RESTRICTED>>`
- Maximum classification allowed in repository: `<<CLASSIFICATION>>`
- Maximum classification allowed in AI input: `<<CLASSIFICATION>>`
- Approved AI environment: `<<ENVIRONMENT_OR_POLICY_REFERENCE>>`
- Data owner / security approver role: `<<ROLE>>`

`project.toml`の`repository_classification`と`ai_data_ceiling`を、この内容に合わせます。

## 2. Classification model

以下は例です。初期化時に会社の正式区分へ置き換えます。

| Example class | Typical content | Repository | AI input |
|---|---|---|---|
| Public | 公開済み情報、公開可能な方法論 | 許可されたpublic/private | 許可されたAI |
| Internal | 社内手順、未公開計画、一般的な内部情報 | 会社管理private/internal | 会社が承認したAIのみ |
| Confidential | 顧客秘密、価格、契約、詳細設計、個人情報 | 明示承認された保存先のみ | 個別規程と承認に従う |
| Restricted | 認証情報、秘密鍵、高感度個人データ、規制対象データ | 専用システム | 原則入力しない。正式手続に従う |

この表は会社の区分を推測で定義するものではありません。

## 3. Never commit

次をGitへcommitしません。

- Password、API key、access token、秘密鍵、証明書秘密情報。
- `.env`等に置かれた認証情報。
- 許可されていない個人データ、顧客データ、契約秘密。
- 本番データdump、未マスクのログ、security findingの悪用可能な詳細。
- 利用権または再配布権がない第三者資料の全文。

`.gitignore`は補助であり、情報管理の代わりではありません。一度commitした秘密情報は、ファイル削除だけでは履歴から消えません。

## 4. Data minimization

- 判断に必要な最小情報だけを保存する。
- 個人名より役割、実値より安全な集計、原文より必要な主張と正当なリンクを優先する。
- サンプルとテストには合成データまたは承認済み匿名化データを使う。
- Researchには情報そのものを複製せず、出典、使用した主張、確認日を記録する。
- 不要になった高感度データは、会社のretentionと削除手続に従う。

## 5. AI input check

AIへ入力する前に次を確認します。

1. 利用するAI環境が会社から承認されている。
2. 入力情報の区分が`ai_data_ceiling`以下である。
3. 契約、顧客条件、個人情報、越境移転等の制約に適合する。
4. 目的に不要な識別子、原文、ログ、添付を除いている。
5. 出力を自動的に事実または承認済み成果物として扱わない。

不明なら入力せず、Security / Legal / Data Ownerへ確認します。

## 6. External publication and upstream safety

- 業務リポジトリから公開テンプレートへの自動pushを設定しない。
- Public issue、PR、discussionへ内部の例、スクリーンショット、ログを貼らない。
- 方法論改善を公開元へ提案する場合は、固有名、数字、日付、URL、識別可能な事例を除き、一般化した構造だけを書く。
- 公開前にはcommit履歴、branch、tag、release、Actions artifactも確認する。

## 7. Incident response

秘密情報や不適切なデータをcommitまたはAI入力した疑いがある場合:

1. 追加共有とpushを止める。
2. Project OwnerとSecurityの正式手順へ連絡する。
3. 認証情報なら無効化・rotationを優先する。
4. 単なるファイル削除で解決したと判断しない。
5. 会社手順に従って履歴、cache、artifact、外部保持を評価する。
6. 必要な範囲でRiskとDecisionへ事実を記録するが、秘密値そのものは記録しない。
