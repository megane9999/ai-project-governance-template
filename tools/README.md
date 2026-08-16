# Tools

補助ツールはPython標準ライブラリだけで動作します。管理構造の代わりではなく、機械的な漏れを検出・削減するためのものです。

## Validate

```bash
python tools/validate_repository.py --strict
```

検査内容:

- 必須ファイル。
- `project.toml`のmodeとschema。
- Markdown内部link。
- Core recordのID、filename、front matter、必須section、台帳登録。
- `active` modeでの未解決placeholder。
- 代表的なcredential patternとローカル絶対path。
- 任意の個人用denylist。

Public化前の個人用denylistはリポジトリへcommitしません。

```bash
python tools/validate_repository.py --strict --denylist path/to/private-denylist.txt
```

Denylistは1行1語です。氏名、username、組織名、案件名、固有URL、識別可能な数値等を手元だけで指定します。

## Create a record

```bash
python tools/new_record.py initiative "Improve report reliability"
python tools/new_record.py research "Current approval flow"
python tools/new_record.py experiment "Synthetic data validation"
python tools/new_record.py decision "Adopt read-only first"
python tools/new_record.py risk "Unauthorized data exposure"
```

Scriptは次のIDを採番してtemplateをcopyします。内容の記入と対応する`README.md`台帳更新はAIまたは作業者が同じ変更で行います。
