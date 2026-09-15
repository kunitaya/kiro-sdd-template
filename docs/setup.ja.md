# セットアップとカスタマイズ

[English（正本）](setup.md) | 日本語

この文書は、テンプレートを導入するときの**初回カスタマイズ**を扱います。
日常の開発運用手順はこの文書の責務ではありません。

clone/worktreeの開始、permissionsのinstall、Issue開始・再開、validation、review、
finalize、復旧については
[開発運用手順書](development-operations-runbook.ja.md)
を参照してください。

## 導入原則

本当にproject固有・stack固有の部分だけをgeneralize / adaptします。
project非依存で成熟したlifecycle、safety、review、isolation、validation controlは維持します。

導入先projectが元projectと異なるという理由だけで、既存のsafety mechanismを
短い近似実装へ書き換えないでください。

## 導入時に決める事項

日常開発を始める前に、導入先repositoryで次を決定・記録します。

1. authoritative requirementsとrepository authority model。
2. project固有のsecurity、sensitive-data、compliance、invariant rules。
3. source/test layoutと適用するsteering file-match pattern。
4. validation commandと必要toolのprovisioning方法。
5. project固有bootstrap設定、または承認済みの代替readiness mechanism。
6. `templates/permissions.yaml` へのproject固有permission追加。
7. Git hook運用（同梱hookを使う場合は `core.hooksPath=.githooks`）。
8. native Spec、Task Execution、hook、diagnostics、permissionsに関する
   現在のKiro実挙動。
9. 利用する場合のautomated-review integration。
10. 同梱GitHub/`gh` finalizer前提と異なるtransport条件。

## Repository skeleton

テンプレートは、最初のcommitから共通development directoryを保持します。

```text
src/
tests/
docs/
docs/spec-archive/
```

空directoryは `.gitkeep` で保持します。実際のtracked contentが入ったら削除できます。
同梱Spec finalizerを使う場合は `docs/spec-archive/` を維持してください。

## Kiro permissionsのadaptation

review済みsource templateは次です。

```text
templates/permissions.yaml
```

activeなworkspace-scoped permission fileは、repository外のKiro workspace trust directoryに
保存されます。install手順は開発運用手順書が責務を持ちます。

導入時は次を守ります。

- genericなsecret/trust/destructive-operation guardは、同等保護を持つ明示的にreview済みの
  replacementがない限り維持する。
- project固有path、tool、exact command、documentation hostは必要な場合だけ追加する。
- destructiveまたはauthority-changing operationは、別の明示的理由がない限り
  `ASK` または `DENY` に残す。
- credential、customer data、local absolute path、machine固有hashをrepository templateへ
  追加しない。
- permissionsを `AGENTS.md` と `#execution` に整合させる。
- lintはprovision済みtoolを直接使い、lint実行のためだけにpackage-acquisition runnerを
  追加しない。

このtemplateは、product固有のinput/output semantics、package/import名、固定runtime version、
test専用environment variable、domain専用hostを意図的に含みません。

## Python/uv bootstrapのadaptation

同梱bootstrapを使うPython/uv projectでは、通常
`scripts/bootstrap-workspace` 冒頭の明示的adaptation constantだけを変更します。

- `EXPECTED_PROJECT_NAME` — `pyproject.toml` の `[project].name`。
- `SOURCE_IMPORT_NAME` — project source packageのimport名。
- `SOURCE_PATH_RELATIVE` — そのimportを所有するrepository-relative path。
- `UV_SYNC_EXTRA` — development environmentで使うoptionalなuv extra。
- `REQUIRED_IMPORTS` — READY前に成功必須のoptional import。

checked-in placeholderは意図的にfail-closedです。bootstrapは自身のscript/configurationも
fingerprintするため、これらの設定変更で以前のREADY stateは無効になります。

generic readiness / isolation contractは `#execution` とbootstrap実装自身が責務を持ちます。
この文書でstate machineを重複記載したり弱めたりしません。

Python/uvを使わないprojectでは、同等のreadiness mechanismへ置き換えるか、
bootstrap script・readiness hook・対応lifecycle checkpointをまとめて外します。

## Specとsteeringのadaptation

`.kiro/specs/_templates/` のtemplateはKiro native workflow conceptを維持しつつ、
repository governanceを追加しています。product/domain contentとrepository固有traceabilityを
適応しますが、短くする目的でnative sectionやsafety sectionを削除しないでください。

`.kiro/steering/source-development.md` と `test-development.md` は実際のsource/test layoutに
合わせます。それ以外のsteering変更は、実際に存在するenvironment/policy差分に限定します。

日常のSpec executionは `.kiro/specs/README.md` と開発運用手順書が責務を持ちます。

## Finalizerのadaptation

`scripts/finalize-spec` / `scripts/finalize_spec.py` は、GitHub、base branch `main`、`gh` CLI、
同梱repository hookを前提とします。

Git hostやdelivery modelが異なる場合、review済みmechanical-delivery state machineを維持したまま
transport/interface boundaryだけを適応します。詳細delivery behaviorは `#execution`、
`.kiro/specs/README.md`、実装自身が責務を持つため、この文書では重複記載しません。

## ValidationとKiro compatibility

テンプレートには共通Markdown baselineとして `.markdownlint.json` が含まれます。
導入先repositoryの実際のsource/test/static-analysis commandを定義し、そのtoolはenvironment setupで
provisionしてください。

Kiro product behaviorはrepository policyとは独立して変化します。native Spec behavior、permissions、
hook、diagnostics、Multi-root behaviorに変更がある場合、利用中のKiro versionに対して再確認します。

利用不能なtoolやdiagnosticsは未検証として記録し、PASS扱いしません。

## Project固有として残すもの

次の内容はgeneric templateではなく、導入先repositoryで管理します。

- product/domain requirementsとterminology。
- customer-specific configurationとsensitive-data rules。
- production-data handlingとcompliance details。
- product schemaとdomain identity。
- Issue固有のdesign decisionとexecution history。
- そのprojectだけで必要なdependency extra、import smoke test、runtime version、permission exception。

テンプレートは再利用可能なdevelopment governanceを管理し、導入先repositoryがproduct truthを
管理します。
