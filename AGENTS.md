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

## Release integrity

Protocol tags are immutable and belong only to this repository for new canonical publications. A release target must be the verified default-branch merge commit whose tree exactly matches the green PR head tree.

Historical `v0.9.0` publication in `0x0sky/mind` remains immutable migration provenance; never rewrite or delete it to make history look cleaner.

## Safety and integrity

Never add secrets, credentials, access tokens, private personal context, or provider-derived observations presented as authored canonical truth. Preserve upstream attribution and repository MIT licensing. Use the canonical source header `© 2026 aiaiaiai · aiaiaiai.org` with `SPDX-License-Identifier: MIT` where appropriate.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
