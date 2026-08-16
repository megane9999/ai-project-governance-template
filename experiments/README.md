# Experiment Registry

更新日: `<<YYYY-MM-DD>>`

Experimentは、重要な仮説を観測可能な結果で検証するための事前登録です。すべての作業をExperiment化する必要はありません。

| ID | Experiment | Related work | State | Cash ceiling | Human-time ceiling | Review | Decision |
|---|---|---|---|---:|---:|---|---|

## Rules

- `Ready`はHypothesis、Method、Success、Failure、Stop-loss、Guardrailsが固定された状態。
- 承認が必要な行為は、承認前に`Running`へ移さない。
- 開始後は事前登録を上書きせず、Change logへ追記する。
- 終了時に実績、観測値、生データまたは成果物、想定外、限界を記録する。
- `Success / Failure / Inconclusive`と、`Continue / Change / Park / Stop / Scale`を分ける。
- 予定支出と実績支出は`budget/ledger.csv`にも記録する。
