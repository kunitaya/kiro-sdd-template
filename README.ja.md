# kiro-sdd-template

[English（正本）](README.md) | 日本語

Kiroを用いたSpec-Driven Development（SDD）環境を再利用するためのテンプレートです。
製品・業務固有のtruthは導入先repositoryに残し、project非依存の成熟した
development governanceとsafety controlをこのテンプレートで維持します。

これは元workflowの「短縮版」ではありません。

## 最初に読む文書

目的に応じて、責務を持つ文書を参照してください。

| 文書 | 役割 |
| --- | --- |
| `docs/setup.md` | 初回導入とproject固有customization・英語正本 |
| `docs/setup.ja.md` | 初回導入とproject固有customization・日本語参考訳 |
| `docs/development-operations-runbook.md` | 日常開発workspace運用手順書・英語正本 |
| `docs/development-operations-runbook.ja.md` | 日常開発workspace運用手順書・日本語参考訳 |
| `AGENTS.md` | repository共通のAI development / safety policy |
| `.kiro/steering/` | execution、review、workspace、SDD、source、testの詳細guidance |
| `.kiro/specs/README.md` | Spec directoryとlifecycle規約 |

各文書の責務を分離し、同じ詳細規則や手順を複数文書へコピーせず、責務を持つ文書への参照を使用します。

## 収録内容

| path | 用途 |
| --- | --- |
| `.kiro/specs/_templates/` | native-compatible requirements/design/bugfix/tasks template |
| `.kiro/hooks/workspace-bootstrap-check.json` | `PreTaskExec` readiness診断 |
| `.githooks/` | `main`への直接commit/push防止 |
| `scripts/bootstrap-workspace` | Python/uv向け決定論的per-worktree bootstrap |
| `scripts/finalize-spec` / `scripts/finalize_spec.py` | fail-closedなreview済みSpec delivery |
| `templates/permissions.yaml` | Kiro workspace permissions用のreview済みsource template |
| `templates/kiro-task-prompt.md` | bounded task prompt template |
| `.markdownlint.json` | 共通Markdown validation baseline |
| `src/`, `tests/`, `docs/` | generic repository skeleton |

## 運用モデル

新しいrepositoryへ導入する場合は、まず
[セットアップとカスタマイズ](docs/setup.ja.md)
を参照してください。

通常のIssue/worktree開始、Kiro workspace permissions、READY確認、validation、review handoff、
finalize、復旧手順は
[開発運用手順書](docs/development-operations-runbook.ja.md)
を参照してください。

SDD/review lifecycleの詳細は `#sdd-workflow`、`#review`、`.kiro/specs/README.md` が責務を持ち、
READMEでは重複して説明しません。

## Kiro permissions

`templates/permissions.yaml` はactive trust fileではなく、review対象となる **source template** です。
Kiroのworkspace-scoped permissionsはrepository外に保存され、cloneしたrepository自身がtrustを付与できない構造です。
active fileのinstall・確認は開発運用手順書、project固有permissionのadaptationは `docs/setup.ja.md` を参照してください。

## 言語方針

repository/GitHub artifactは英語を正本とします。

人間向けのsetup / operation文書は日本語参考訳を持つことができます。
`README.md` / `README.ja.md`、`docs/setup.md` / `docs/setup.ja.md`、開発運用手順書の英日ペアは、
意味を変更する場合に同じ変更で同期します。

AI向けpolicy、steering、Spec templateは、導入先repositoryが別のauthority modelを明示しない限り英語を維持します。

## 状態

再利用可能なgovernanceとSDD環境を収録しています。
導入先ごとのproject customizationと、利用中のKiro/toolchain versionに対するvalidationは別途必要です。

## 位置付け

本repositoryは独立して保守される非公式templateであり、Kiro、OpenAI、
またはそれらの開発元による公式製品・承認物ではありません。

## ライセンス

[MIT License](LICENSE)
