# kiro-sdd-template

[English（正本）](README.md) | 日本語

Kiroを用いたSpec-Driven Development（SDD）環境を再利用するためのテンプレートです。
製品・業務固有のtruthは導入先repositoryに残し、project非依存の成熟した
development governanceとsafety controlをこのテンプレートで維持します。

これは元workflowの「短縮版」ではありません。

## ドキュメント構成

| 文書 | 役割 |
| --- | --- |
| `README.md` / `README.ja.md` | 全体概要と入口 |
| `docs/setup.md` | 初回導入とproject固有customization |
| `docs/development-operations-runbook.md` | 日常開発運用手順書・英語正本 |
| `docs/development-operations-runbook.ja.md` | 日常開発運用手順書・日本語参考訳 |
| `AGENTS.md` | repository共通のAI development / safety policy |
| `.kiro/steering/` | execution、review、workspace、SDD、source、testの詳細guidance |
| `.kiro/specs/README.md` | Spec directoryとlifecycle規約 |

責務を分け、同じ詳細規則や手順を複数文書へ重複記載せず、安定した参照を使用します。

## 収録内容

| path | 用途 |
| --- | --- |
| `.kiro/specs/_templates/` | native-compatible requirements/design/bugfix/tasks template |
| `.kiro/hooks/workspace-bootstrap-check.json` | `PreTaskExec` readiness診断 |
| `.githooks/` | `main`への直接commit/push防止 |
| `scripts/bootstrap-workspace` | Python/uv向け決定論的per-worktree bootstrap |
| `scripts/finalize-spec` / `scripts/finalize_spec.py` | fail-closedなreview済みSpec delivery |
| `templates/permissions.yaml` | review対象となるKiro workspace permission source template |
| `templates/kiro-task-prompt.md` | task prompt template |
| `.markdownlint.json` | 共通Markdown validation baseline |
| `src/`, `tests/`, `docs/` | generic repository skeleton |

## 基本workflow

```text
正式なproject requirements + GitHub Issue
    ↓
semantic riskによりDirect ChangeまたはKiro Specを選択
    ↓
Requirements / Design / Bugfix -> tasks.md
    ↓
専用branch/worktree + Draft PR
    ↓
Independent Spec Review
    ↓
Kiro native Spec Task Execution
    ↓
Implementation + 必要十分なvalidation
    ↓
Independent Code / Requirements Review
    ↓
review済みSpecの機械的delivery + PR Ready
    ↓
human merge gate
```

詳細lifecycleは `#sdd-workflow`、`#review`、`.kiro/specs/README.md` を正本とします。

## 基本原則

- 上位authorityのrequirementsを現行codeに合わせて書き換えない。
- 原則として1 Issueを1 branch / 1 PRで管理する。
- Kiro nativeのartifact/task lifecycleを維持する。
- worktreeをruntime root/branch/repository identityで分離する。
- workspace READYは現在のworktree/runtime/dependency/bootstrap stateを表す。
- validationはtask中に取得したtoolではなくprovision済みtoolを直接使う。
- automated reviewは補助evidenceでありauthorityではない。
- BLOCKINGだけを必須修正roundとする。
- final deliveryはfail-closedとし、明示的委任がない限りmergeはhuman/operator actionとする。

## Kiro permissions

`templates/permissions.yaml` はactive trust fileではなく、**source template**です。

Kiro 1.0のworkspace-scoped permissionsはrepository外へ保存されます。

```text
~/.kiro/workspace-roots/<hash>/permissions.yaml
```

これによりcloneしたrepository自身がtrustを付与できません。
active workspace copyは人手でinstall・reviewします。

テンプレートはgeneric safety ruleを維持し、product固有path、package/import名、
固定runtime version、test専用environment variable、domain固有documentation hostを含めません。

日常のinstall/確認手順は
[開発運用手順書](docs/development-operations-runbook.ja.md)、
project固有adaptationは
[Setup and Customization](docs/setup.md)
を参照してください。

## Workspace readinessとdelivery

同梱bootstrap/finalizerはproduction-derivedなsafety mechanismです。

短い近似実装へ書き直さず、文書化されたproject/transport boundaryだけを適応し、
generic state machineを維持します。

- bootstrap customization: [Setup and Customization](docs/setup.md)
- 日常READY手順: [開発運用手順書](docs/development-operations-runbook.ja.md)
- Spec delivery lifecycle: [.kiro/specs/README.md](.kiro/specs/README.md)

## 言語方針

repository/GitHub artifactは英語を正本とします。

日常的に人間が使用するsetup/operation文書は、日本語参考訳を持つことができます。
開発運用手順書は意図的に英日両方を維持し、同じ変更で同期します。

AI向けpolicy、steering、Spec templateは、導入先repositoryが別のauthority modelを
明示しない限り英語を維持します。

## 状態

再利用可能なgovernanceとSDD環境を収録しています。
導入先ごとのproject customizationと、利用中のKiro/toolchain versionに対する
validationは別途必要です。

## 位置付け

本repositoryは独立して保守される非公式templateであり、Kiro、OpenAI、
またはそれらの開発元による公式製品・承認物ではありません。

## ライセンス

[MIT License](LICENSE)
