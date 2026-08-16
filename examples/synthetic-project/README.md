# Synthetic example: weekly report reliability

> この例は管理構造の説明専用に作った完全な合成データです。実在の会社、個人、顧客、案件、数値とは関係ありません。

## Scenario

架空のチームが、週次業務レポートの転記ミスと作成時間を減らそうとしています。AIに実データを渡す前に、合成CSVでread-onlyな検証を行う例です。

## Record flow

1. [WRK-0001](initiatives/WRK-0001-report-reliability.md)で成果と完了条件を定義。
2. [RES-0001](research/RES-0001-current-process.md)で現状と未確認事項を分離。
3. [DEC-0001](decisions/DEC-0001-read-only-synthetic-first.md)で合成データ・read-only検証を採用。
4. [EXP-0001](experiments/EXP-0001-synthetic-validation.md)で開始前に成功・失敗条件を固定。
5. [Metrics](metrics/README.md)へ結果と運用品質を同期。

実プロジェクトでは、各ディレクトリの`README.md`台帳にも同じIDを登録します。この例は読みやすさのため、個別ファイルと要約だけに絞っています。
