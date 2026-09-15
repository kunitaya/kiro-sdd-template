# kiro-sdd-template

[English（正本）](README.md) | 日本語

> このファイルは英語版 `README.md` の参考訳です。意味が異なる場合は英語版を優先し、英語版を変更する際はこのファイルも同じ変更で同期してください。

Kiroを用いたSpec-Driven Development（SDD）環境を再利用するためのテンプレートです。実運用向けのAI支援開発フローから、製品・業務固有の要件を除去して汎化しています。

リポジトリ共通のエージェント方針、Steering、Kiro標準と整合するSpecテンプレート、worktree分離、ネイティブTask Execution、bootstrap/readiness、Git安全フック、委譲・レビュー・デリバリー手順を含みます。

## 収録内容

| パス | 用途 |
| --- | --- |
| `AGENTS.md` | 権威順序、スコープ、安全性、検証、レビュー、SDD方針 |
| `.kiro/steering/` | SDD、実行、レビュー、文書、テスト、ソース、workspace、task運用 |
| `.kiro/specs/_templates/` | requirements/design/bugfix/tasksテンプレート |
| `.kiro/hooks/workspace-bootstrap-check.json` | `PreTaskExec` readiness診断 |
| `.githooks/` | `main`への直接commit/push防止 |
| `scripts/bootstrap-workspace` | Python/uv向け汎用worktree bootstrap例と`--check` |
| `scripts/finalize-spec` | Spec archiveの最小補助スクリプト |
| `templates/kiro-task-prompt.md` | 境界を絞ったタスクプロンプト |
| `docs/setup.md` | 導入・カスタマイズ手順 |

## 基本フロー

```text
正式なプロジェクト要件 + GitHub Issue
    ↓
意味上のリスクに応じてDirect ChangeまたはKiro Specを選択
    ↓
requirements/design/bugfix -> tasks.md
    ↓
検証して専用branch + Draft PRへ公開
    ↓
Independent Spec Review
    ↓
Kiro native Spec Task Execution
    ↓
実装 + リスクに見合う検証
    ↓
Independent Code / Requirements Review
    ↓
Spec archive -> Draft PR Ready
    ↓
人によるmerge gate
```

主な原則は、上位要件を現行コードに合わせて書き換えないこと、原則1 Issue = 1 branch = 1 PRとすること、タスクプロンプトにリポジトリ共通方針を重複させないこと、native Spec Task Executionを維持すること、worktreeのroot/branch/repository identityを実行時に確認すること、検証証拠を必要以上に再実行しないこと、自動レビューを補助証拠として扱うこと、BLOCKINGだけを必須修正ラウンドとすること、mergeは明示的委任がない限り人の判断とすることです。

## Workspaceとbootstrap

各Git worktreeを独立した可変開発環境として扱います。同梱のbootstrapはPython/uv向けの例です。他の技術スタックでは置き換えてください。ただし、次の契約は再利用価値があります。

```bash
./scripts/bootstrap-workspace          # 初期化/修復
./scripts/bootstrap-workspace --check  # 非変更のreadiness確認
```

Kiroの`PreTaskExec` hookはこの確認結果を表示します。ただし、使用中のKiroバージョンで確認していない限り、hookがタスク開始を強制的に停止すると仮定しません。native task実行前のREADY確認はworkspace ownerの責任です。

lintは事前に用意されたツールを直接実行し、lintのためだけに`npx`、`npm exec`、`pnpm dlx`、`yarn dlx`等のパッケージ取得ランナーを使用しません。

## 導入

[Setup and Customization](docs/setup.md) を参照してください。製品・業務要件、検証コマンド、セキュリティ規則、source/testパス、環境bootstrap、自動レビュー連携などは導入先で明示的に設定します。業務固有の意味論はこのテンプレートに持ち込みません。

同梱Git hooksを利用する場合は、clone/worktree作成後に次を設定します。

```bash
git config core.hooksPath .githooks
```

## 言語方針

リポジトリ/GitHub成果物は英語を正本とします。この日本語READMEは参考訳です。対話形式のoperator報告は利用者が希望する言語で構いません。

## 状態

再利用可能なガバナンスとSDD環境一式を収録しました。ただし、導入先ごとの明示的なカスタマイズは必要です。万能な製品設定ではありません。

## 位置付け

本リポジトリは独立して保守される非公式テンプレートであり、Kiro、OpenAI、またはそれらの開発元による公式製品・承認物ではありません。

## ライセンス

[MIT License](LICENSE)
