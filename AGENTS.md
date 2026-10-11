# AGENTS

This repository is the canonical **Mind Protocol authority**. It contains universal protocol source, schemas, conformance, compatibility, migration, bootstrap, release machinery, and protocol documentation. It is not a concrete Mind.

## Read order

1. Read `mind-repository.yaml` to confirm repository role.
2. Read `protocol.yaml` for universal contract discovery.
3. Use `conformance.yaml`, `compatibility.yaml`, `schema/`, and `docs/protocol/` only as required by the task.
4. For new concrete Mind creation, use `docs/protocol/BOOTSTRAP.md` and an exact immutable release tag.

There is intentionally no root concrete `manifest.yaml`. Named personal, organizational, agent, project, or product context belongs in the corresponding concrete Mind repository.

## Authority rules

- `protocol.yaml` is the canonical protocol descriptor.
- `conformance.yaml` is the public conformance suite.
- `compatibility.yaml` owns compatibility and migration policy.
- `schema/` contains published reusable schema contracts.
- `mind-repository.yaml` is repository metadata, not a universal protocol contract.
- No named concrete Mind, provider account, repository owner, renderer, or runtime may define universal protocol truth.

## Concrete Mind boundary

A concrete Mind is created from an exact protocol release:

```text
exact release → neutral baseline → explicit subject/owner/Identity → concrete mind@<id>
```

Do not use a GitHub fork of `master` as a concrete-Mind template. Do not copy authored modules from another concrete Mind. Provider account names are integration evidence, never automatic canonical identity IDs.

## Engineering workflow

- Inspect current state before editing.
- Start from latest `master` on one `feature/` or `fix/` branch per task.
- Prefer the smallest sufficient change and preserve frozen published schema bytes unless a deliberately versioned schema change is required.
- Keep machine contracts, tests, and documentation synchronized.
- Run full correctness CI before merge.
- Do not duplicate correctness work after merge when the tested tree is unchanged.
- Treat release/tag publication as separate from source merge.

## GitHub collaboration

### Shared-account co-authorship

The connected GitHub identity is the commit author; a model name, tool, session,
PR author, or reviewer is not automatically a co-author. Recognize distinct
GitHub accounts `0x0sky` (ChatGPT/Codex) and `x0skai` (Claude Code) as
potential collaborators, not interchangeable author identities.

- Credit the other account only when it actually contributed authored code,
  documentation, tests, or a concrete patch incorporated into this commit.
  A review, approval, prompt, or GitHub login alone does not qualify. Do not
  add a co-author for the sake of an achievement.
- For a commit authored by `0x0sky` with actual contribution by `x0skai`,
  include `Co-authored-by: x0skai <300452669+x0skai@users.noreply.github.com>`.
- For a commit authored by `x0skai` with actual contribution by `0x0sky`,
  include `Co-authored-by: 0x0sky <0x0sky@proton.me>`.
- These are known GitHub-attributed commit addresses, not an invitation to
  assume other addresses. Verify the exact email-to-account association if
  it changes; use that account's confirmed GitHub noreply address when private.
- Put trailers in the *commit message*, each on its own line, after a blank
  line at the end of the message. Attribute only actual co-authors; never
  add the commit author as their own co-author or duplicate a trailer.
- Preserve legitimate tool/model attribution if present, but a line such as
  `Co-Authored-By: Claude Opus <noreply@anthropic.com>` does not identify
  `x0skai` or `0x0sky`. Do not replace a real account with a model label.
- Before merge, inspect the pushed PR commit messages on GitHub, not only
  local configuration or the PR description. Confirm the intended co-author
  trailer survived. A comment, review, approval or PR body is not a substitute.
- For **merge commits**, co-authored commits in the PR must carry their own
  trailers; the final merge commit need not repeat them. For **squash merges**,
  verify the proposed *final squash commit message* includes the applicable
  trailer before merging. Use only merge methods the repository permits.
- Do not manufacture commits, retroactively rewrite merged history, invent
  contributions, or block a valid solo-authored PR merely to earn a badge.
  Report verified commit attribution separately from GitHub Achievement
  eligibility or award status, which may update asynchronously.

## Release integrity

Protocol tags are immutable and belong only to this repository for new canonical publications. A release target must be the verified default-branch merge commit whose tree exactly matches the green PR head tree.

Historical `v0.9.0` publication in `0x0sky/mind` remains immutable migration provenance; never rewrite or delete it to make history look cleaner.

## Safety and integrity

Never add secrets, credentials, access tokens, private personal context, or provider-derived observations presented as authored canonical truth. Preserve upstream attribution and repository MIT licensing. Use the canonical source header `© 2026 aiaiaiai · aiaiaiai.org` with `SPDX-License-Identifier: MIT` where appropriate.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
