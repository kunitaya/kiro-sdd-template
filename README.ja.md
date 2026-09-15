# kiro-sdd-template

[English（正本）](README.md) | 日本語

> このファイルは英語版 `README.md` の参考訳です。意味が異なる場合は英語版を優先し、英語版を変更する際はこのファイルも同じ変更で同期してください。

Kiroを用いたSpec-Driven Development（SDD）環境を再利用するためのテンプレートです。実運用向けのAI支援開発フローから、
製品・業務固有の要件だけを除去し、成熟した開発ガバナンスと安全制御を保持することを目的としています。

これは元ワークフローの「短縮版」ではありません。要件の権威、Kiro native Spec構造、worktree分離、決定論的なworkspace readiness、
レビュー収束、fail-closedな最終delivery、人によるmerge gateなど、プロジェクト非依存の重要な運用深度は維持します。

## 収録内容

| パス | 用途 |
| --- | --- |
| `AGENTS.md` | 権威順序、スコープ、Git安全性、検証、レビュー、SDD方針 |
| `.kiro/steering/` | SDD、実行、レビュー、文書、テスト、source、workspace、task運用 |
| `.kiro/specs/_templates/` | Kiro native構造を保持したrequirements/design/bugfix/tasksテンプレートと各種matrix |
| `.kiro/hooks/workspace-bootstrap-check.json` | `PreTaskExec` workspace readiness診断 |
| `.githooks/` | `main`への直接commit/push防止 |
| `scripts/bootstrap-workspace` | Python/uv向け決定論的worktree bootstrapとfail-closedな`--check` |
| `scripts/finalize-spec` / `scripts/finalize_spec.py` | 独立レビュー後の検証付き機械的Spec deliveryとDraft→Ready遷移 |
| `templates/kiro-task-prompt.md` | 境界を絞ったタスクプロンプト |
| `docs/setup.md` | 導入・カスタマイズ手順 |
| `.markdownlint.json` | 共通Markdown検証ベースライン |

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
利用可能なら補助的な自動レビュー
    ↓
Independent Spec Review
    ↓
実装承認
    ↓
Kiro native Spec Task Execution
    ↓
実装 + リスクに見合う検証
    ↓
最終検証 + 同じDraft PRへ公開
    ↓
利用可能なら補助的な自動再レビュー
    ↓
Independent Code / Requirements Review
    ↓
必要な修正 / delta review
    ↓
検証付きの機械的Spec archive + Draft PR Ready
    ↓
人によるmerge gate
```

主な原則:

- 上位の要件を現行コードに合わせて書き換えない。
- 原則として1 Issue = 1 branch = 1 PRとする。
- Kiro nativeのartifact/task lifecycleを独自の簡易形式に置き換えない。
- タスクプロンプトにはタスク固有情報を載せ、リポジトリ共通方針を重複させない。
- worktreeはroot/branch/repository identityを実行時に確認して分離する。
- workspace READYは「Pythonが存在する」ではなく、現在のworktree/runtime/dependency状態が記録された
  bootstrap fingerprintと一致することを意味する。
- lint/validationでは既に用意されたツールを使い、パッケージ取得runnerで代用しない。
- 検証証拠はリスクに応じて取得し、無意味に何度も再実行しない。
- 自動レビューは補助証拠であり、権威や独立レビューの代替ではない。
- BLOCKINGだけを必須修正ラウンドとする。
- 最終deliveryはreview evidence、PR/branch状態、完了checkbox、clean reviewed HEAD、Git safety controlを
  確認してからarchive/Readyへ進む。
- mergeは明示的委任がない限り人の判断とする。

## Workspaceとbootstrap

各Git worktreeを独立した可変開発環境として扱います。同梱bootstrapはPython/uv向けの参照実装です。以下を確認します。

- repository/worktree rootの解決。
- 必須ツールの存在。
- sync前の`uv.lock`整合性。
- symlinkまたは別mountされた`.venv`の拒否。
- `.venv` interpreterが現在worktreeに属すること。
- 物理repository root、Python version、`pyproject.toml`、`uv.lock`を含むstate fingerprint。
- mutating bootstrapの直列化。
- Kiro readiness hookから使う非変更・fail-closedな`--check`。

```bash
./scripts/bootstrap-workspace          # READYを初期化/修復
./scripts/bootstrap-workspace --check  # 非変更のreadiness検証
```

別の技術スタックを使う場合は、**この契約を弱めずに実装だけ置き換えてください**。workspace bootstrap/readiness自体を採用しない場合は、
script・hook・対応するlifecycle checkpointをまとめて外してください。

Kiroの`PreTaskExec` hookはreadiness診断を表示します。ただし、利用中のKiroバージョンで確認していない限りhook自体がタスク開始を
強制停止すると仮定しません。native task実行前のREADY確認はworkspace ownerの責任です。

## Native Spec互換性

`.kiro/specs/_templates/`はKiro native Spec artifactを補強するもので、独自文法への置換ではありません。native workflow/sectionを
保持し、その周囲にworkspace identity、requirement traceability、invariant inventory、review matrix、再開可能なtask state、
delivery checkpointを追加します。

Kiroのnative Spec構造、Task Execution、hook、diagnosticsが変わった場合は、導入中のKiro挙動を確認してテンプレートを更新します。過去のコピーを理由に古いnative contractを固定し続けません。

## レビューとdelivery

Independent Spec Reviewでは、重要な挙動を推測せずに実装へ進めるかを確認します。Independent Code / Requirements Reviewでは、
実装結果を要件と影響を受けるinvariantに照らして確認します。state、identity/provenance、persistence、status/NULL、security、
lifecycleなど高リスク領域では必要なstructural/adversarial matrixを使います。

`scripts/finalize-spec`はfail-closedです。レビューPASSを自分で判断しません。呼び出し側が独立レビュー済みのfull commit SHAと具体的なPASS記録URLを渡します。archive前に少なくとも以下を確認します。

- working tree/indexがcleanで、HEADがレビュー済みcommitと完全一致する。
- repository Git hooksが設定され、実行可能である。
- open Draft PRのhead/baseが現在branchと`main`に一致する。
- remote PR HEADがレビュー済みcommitと一致する。
- 必要なSpec artifactが揃っている。
- 最後の2つの機械的checkpoint以外のtask/review checkboxが完了している。
- archive destinationがまだ存在しない。

その後にだけ、最後の2 checkpointを記録し、PASS参照を保存し、Specをarchiveし、機械的変更をcommit/pushし、同じDraft PRをReadyへ遷移します。mergeは手動のままです。

## 導入

[Setup and Customization](docs/setup.md) を参照してください。導入先では次を明示的に定義・調整します。

- 正式なproject/domain requirements。
- project固有invariantとsecurity/sensitive-data rules。
- source/test file-match pattern。
- validation commandとtool provisioning。
- 利用技術スタックに合ったenvironment/bootstrap実装。
- 自動レビュー連携（利用する場合）。
- `github.com`以外や異なるrepository運用を使う場合のGitHub host/repository規約。

製品・業務要件、顧客固有設定、product schema、業務用語、Issue固有履歴はこの汎用テンプレートへ移しません。

同梱Git hooksを利用する場合は、clone/worktree作成後に次を設定します。

```bash
git config core.hooksPath .githooks
```

## 言語方針

リポジトリ/GitHub成果物は英語を正本とします。この日本語READMEは参考訳です。英語版の意味を変更した場合は同じ変更で同期します。対話形式のoperator報告は利用者が希望する言語で構いません。

## 状態

再利用可能なガバナンスとSDD環境一式を収録しています。ただし、導入先ごとの明示的カスタマイズと、利用中のKiro/toolchainバージョンに対する検証は必要です。

## 位置付け

本リポジトリは独立して保守される非公式テンプレートであり、Kiro、OpenAI、またはそれらの開発元による公式製品・承認物ではありません。

## ライセンス

[MIT License](LICENSE)
