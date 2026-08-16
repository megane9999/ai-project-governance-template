# Project Charter

更新日: `<<YYYY-MM-DD>>`

変更権限: `<<CHARTER_CHANGE_APPROVER_ROLE>>`

## 1. Purpose

`<<このプロジェクトが存在する理由を、成果または状態として記述する>>`

## 2. Success state

期間または判断時点: `<<DATE_OR_CONDITION>>`

- Minimum acceptable outcome: `<<最低限達成すべき状態>>`
- Target outcome: `<<狙う状態>>`
- Exceptional outcome: `<<上振れ状態。不要なら削除>>`
- Failure / exit state: `<<中止・終了と判断する状態>>`

成功は測定可能な結果で定義し、単なる作業量や成果物の存在だけを成功としません。

## 3. Scope

含むもの:

- `<<IN_SCOPE_ITEM>>`

## 4. Non-goals

含まないもの:

- `<<NON_GOAL>>`

Non-goalsは「今はしない」と「永久にしない」を区別し、再検討条件がある場合は記載します。

## 5. Constraints

- Deadline / review horizon: `<<CONSTRAINT>>`
- Budget: `<<CONSTRAINT>>`
- Human time / staffing: `<<CONSTRAINT>>`
- Quality / reliability: `<<CONSTRAINT>>`
- Legal / compliance / security: `<<CONSTRAINT>>`
- Technology / platform: `<<CONSTRAINT>>`

## 6. Roles

| Role | Responsibility | Decision authority |
|---|---|---|
| Project Owner | 目的、Scope、最終優先順位 | Charter、終了、主要例外 |
| AI agent | 調査、整理、実装、検証、同期 | Governanceで許可された範囲のみ |
| `<<ROLE>>` | `<<RESPONSIBILITY>>` | `<<AUTHORITY>>` |

個人名ではなく役割を正本とし、必要な場合だけ会社側のアクセス管理で個人へ割り当てます。

## 7. Operating values

- 最も安く、早く、可逆的な方法で重要な不確実性を減らす。
- 事実と仮説を混同せず、不都合な証拠も残す。
- 失敗や中止を隠さず、再利用可能な学習へ変換する。
- 人間の注意、他チームの作業、顧客負担をコストとして扱う。
- 重要判断は説明可能で、再検討条件を持つ。

## 8. Change policy

AIはCharterを独断で変更しません。変更案は、必要性、証拠、代案、影響、ロールバックまたは再検討条件を含む新しいDecisionとして提案します。
