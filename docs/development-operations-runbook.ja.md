# 開発運用手順書

[English（正本）](development-operations-runbook.md) | 日本語

## 目的

この文書は、テンプレートを導入済みのリポジトリで、開発workspaceを準備し、
日常的に運用するための人間向け手順書です。

既存文書との責務重複を避けるため、次の境界を維持します。

- `AGENTS.md` はリポジトリ共通の開発・安全ポリシーを管理します。
- `.kiro/steering/` は実行、レビュー、workspace、SDDの詳細ガイダンスを管理します。
- `docs/setup.md` は初回導入・カスタマイズ判断を管理します。
- `.kiro/specs/README.md` はSpecディレクトリとlifecycle規約を管理します。
- この文書は、日常開発で繰り返すoperator手順だけを管理します。

内容が競合した場合は、この手順書より各文書のauthority規則を優先してください。

## 1. clone / 端末ごとの初回セットアップ

### 1.1 cloneしてリポジトリへ移動する

```bash
git clone <repository-url>
cd <repository-directory>
```

意図したrepository rootを開いていることを確認します。

```bash
git rev-parse --show-toplevel
git remote -v
git branch --show-current
```

### 1.2 Git hooksを有効化する

repository管理のhooksを設定します。

```bash
git config core.hooksPath .githooks
git config core.hooksPath
```

`--no-verify` や別の `core.hooksPath` でhooksを迂回しないでください。

### 1.3 workspace permission policyを設定する

レビュー済みpermissionテンプレートは次のファイルです。

```text
templates/permissions.yaml
```

Kiroのactiveなworkspace-scoped permissionは、リポジトリ外の次の場所に保存されます。

```text
~/.kiro/workspace-roots/<hash>/permissions.yaml
```

cloneしたリポジトリ自身がtrustを付与できないよう、この分離は意図的です。
Kiroで対象repository/worktree rootそのものを開き、そのrootにKiroが関連付けた
workspace trust entryを使用してください。`<hash>` を推測・固定しません。

レビュー済みテンプレートをactive fileへ人手でコピーし、project固有の追加が必要な場合は
内容を確認してから使います。agent自身にactive permission fileを書き換えさせないでください。

テンプレートはKiroのcapability ruleを使用します。

- `deny` は操作を拒否します。
- `ask` は人間の承認を要求します。
- `allow` は操作を事前承認します。
- scopeが重なった場合は、より制限の強いruleが優先されます。

`ASK` / `DENY` は制御境界です。コマンド表記、path、toolを変えて迂回しないでください。

Kiro公式リファレンス:

- <https://kiro.dev/docs/ide/whats-new-v1/permissions/>
- <https://kiro.dev/docs/cli/chat/configuration/>

### 1.4 project environmentを準備する

同梱bootstrapを利用するPython/uv projectでは、`docs/setup.md` に記載された
導入固有設定を完了してから実行します。

```bash
./scripts/bootstrap-workspace
./scripts/bootstrap-workspace --check
```

checkがREADYになるまで実装へ進みません。

別stackの場合は、そのrepositoryで承認された代替readiness手順を使用します。
単純な「toolが存在する」確認へ置き換えないでください。

### 1.5 必要toolを確認する

repositoryが実際に利用するtoolを確認します。例:

```bash
command -v git
command -v gh
command -v kiro
command -v uv
command -v markdownlint
```

依存関係の準備はworkspace/bootstrap側の責務です。必要なvalidation toolが無い場合、
task実行中に独自install/upgradeせず、そのcheckを未実行として報告します。

## 2. 新しいIssueを開始する

### 2.1 baselineを更新する

main working copyで実行します。

```bash
git switch main
git pull --ff-only
git status
```

task branch/worktreeを作る前に、`main` がcleanであることを確認します。

### 2.2 専用branch/worktreeを作る

原則として1 Issueを1 branch / 1 PRで管理します。
別worktreeを使う場合は、更新済みbaselineから作成します。

```bash
git worktree add ../<worktree-directory> -b <branch-name> main
```

実装時は、新しいworktreeだけをproject rootとして開きます。

workspace isolationの規則は `.kiro/steering/workspace-isolation.md` が正本です。
この手順書では重複記載しません。

### 2.3 新worktreeを初期化する

新しいworktreeで実行します。

```bash
git config core.hooksPath .githooks
git branch --show-current
git status
./scripts/bootstrap-workspace
./scripts/bootstrap-workspace --check
```

Kiro permissionsはworkspace root単位です。現在開いているworktree rootに対応した
permission fileへレビュー済みテンプレートが適用されていることを確認し、
別worktreeのtrust entryが自動的に適用されるとは仮定しません。

### 2.4 Kiroでworktree rootを開く

複数task worktreeを含む親directoryではなく、対象worktree rootを開きます。

実装開始前に次を確認します。

1. root / branch / repository identity
2. workspace READY
3. applicable steering
4. `#sdd-workflow` によるDirect ChangeまたはSpec route選択

Spec実装taskはKiro native Spec Task Executionから開始します。
補助chat promptはnative task選択の代替ではありません。

## 3. 日次開始・中断後の再開

session開始時や中断後は、過去のprogress summaryより先に実状態を確認します。

```bash
git rev-parse --show-toplevel
git branch --show-current
git status
./scripts/bootstrap-workspace --check
```

その後、対象Issue/PRと、Specの場合は現在の `tasks.md` progress recordを確認します。

bootstrap scriptまたはdependency inputが変更されている場合は、
mutating bootstrapを再実行してから続行します。

## 4. コマンド・tool運用

詳細なcommand policyは `AGENTS.md` と `#execution` を正本とします。
日常運用では次を守ります。

- project executableはrepository rootからrepository-relative pathで実行する。
- provision済みtoolをPATHまたはproject-local environmentから直接実行する。
- lint実行に `npx`、`npm exec`、`pnpm dlx`、`yarn dlx`、`uvx` を使用しない。
- validation toolが無い場合、task中にinstallしない。
- `ASK` / `DENY` を迂回しない。
- disposable scratchは `/tmp` ではなく `.local/kiro-scratch/` を使う。

permissionテンプレートは、通常のread/validation/development操作を許可しつつ、
破壊的Git/filesystem操作やtrust boundary変更をDENYまたは人間承認に残します。

## 5. Validation

導入先repositoryで定義されたcommandを使用します。テンプレート自身の代表例:

```bash
markdownlint "**/*.md"
sh -n scripts/bootstrap-workspace
sh -n scripts/finalize-spec
python3 -m py_compile scripts/finalize_spec.py
```

変更scopeに必要なvalidationだけを実行し、未実行・利用不能checkはそのまま記録します。

Kiro native Spec diagnosticsはMarkdown/source lintとは別物です。
利用中のKiro versionで必要なdiagnosticsが提供されている場合、Spec変更では実行します。

## 6. 公開とレビュー

1つの変更は、同じ専用branchとDraft PRで管理します。

Spec-driven workの詳細gateは `.kiro/specs/README.md` と `#review` が正本です。
運用上は次の順序です。

1. review可能なSpecまたはimplementation revisionをpublishする。
2. 必要なindependent reviewを得る。
3. BLOCKINGを修正する。
4. 修正で無効化されたevidenceだけを再検証する。
5. optional improvementをgate BLOCKINGと混同しない。

automated reviewerは補助evidenceです。quota不足やservice unavailableをPASS扱いしません。

## 7. Review済みSpecをfinalizeする

必要な最終independent reviewがPASSした後、review済みfull commit SHAと
具体的なPASS record URLを指定します。

```bash
./scripts/finalize-spec \
  --spec <issue-number>-<slug> \
  --pr <pr-number> \
  --reviewed-commit <full-reviewed-sha> \
  --review-url <independent-pass-url>
```

archive/Readyの機械的state transitionと、認識済みpartial stateからの復旧は
finalizerが管理します。手作業で同じstate transitionを再現しないでください。

mergeは明示的に委任されない限りhuman/operator actionです。

## 8. よくある失敗と復旧

| 状態 | operator action |
| --- | --- |
| `bootstrap-workspace --check` がREADYでない | mutating bootstrapを実行し、reason tokenに従ってownership/dependency/configuration問題を修正する。 |
| permission結果が`ASK` | commandとside effectが意図どおりの場合だけ承認する。それ以外は拒否し、文書化された操作を使う。 |
| permission結果が`DENY` | 停止する。別表記・別toolでruleを迂回しない。 |
| 間違ったroot/branchを開いた | repository-changing workを停止し、owning worktree rootを開き直す。 |
| 必要toolが無い | validationを利用不能として記録し、environment provisioningへ戻す。 |
| 中断後にSpec task stateが不明 | 実file/diffと`tasks.md`を確認し、有効なevidenceを保持して最初の未完了bounded taskから再開する。 |
| finalizerがBLOCKED | 現在stateを保持し、報告されたPR/tree/review条件を修正して同じhelperを再実行する。 |
| Kiroの実挙動が手順書と異なる | 現在のKiro docs/versionを確認し、local手順を黙って変えずテンプレートをreview経由で更新する。 |

## 9. permissionテンプレートの保守

`templates/permissions.yaml` はレビュー対象となるsource templateであり、
active trust fileではありません。

repositoryに追加permissionが必要な場合:

1. generic development policyかproject固有adaptationかを分類する。
2. secrets/trust-store pathはDENYを維持する。
3. broad wildcardよりexact/narrow command formを優先する。
4. destructive/authority-changing operationは`ASK`または`DENY`に残す。
5. repository templateは通常のPRで変更する。
6. review/merge後、active workspace-scoped fileを人手で更新する。

`~/.kiro/workspace-roots/<hash>/` のactive fileをrepositoryへcommitしないでください。
