# Protocol authority migration

This document records the one-time physical separation of Mind Protocol authority from the concrete `mind@0x0sky` repository.

## Before the split

`0x0sky/mind` historically contained both implementation-independent protocol source and the concrete personal Mind for `person:0x0sky`.

The first formal release, `v0.9.0`, was published there from verified release commit `457844c8ced0318d91d628617ff6f8ec6f428ab7`. That tag and GitHub Release are immutable historical evidence and must not be moved, deleted, or rewritten.

## Split source boundary

The protocol-source tree selected for migration is:

```text
repository: 0x0sky/mind
commit:     48a81df7d8e9818d9c01f3e1fe5ac663af29a006
tree:       410aa4e37e0aeefe9340ef3ce85393e1ffbfa95d
source:     1.0.0-rc.1 candidate
```

The exact Git commit ancestry was imported into `aiaiaiai-org/mind-protocol`; it was not reconstructed as a snapshot with new commit identities.

After that boundary, `0x0sky/mind` advanced independently through its concrete-consumer split and no longer owns protocol source/release authority.

## After the split

Canonical roles are:

- `aiaiaiai-org/mind-protocol` — universal protocol source, conformance, compatibility, bootstrap, release machinery, protocol tags/releases;
- `0x0sky/mind` — concrete consumer for `person:0x0sky`;
- `aiaiaiai-org/mind`, `0xda-market/mind`, `nilx-one/mind` — organization consumers/canaries.

No concrete repository becomes protocol authority by participating in canary validation.

## Release continuity rule

Historical `v0.9.0` provenance remains attached to `0x0sky/mind`. New canonical protocol publication begins from `aiaiaiai-org/mind-protocol` after the repository split receives its own green PR/tree evidence.

`v1.0.0-rc.1` must therefore be published from a post-split merge commit in this repository, not directly from the imported historical commit. The release workflow can then prove that the target merge commit belongs to a PR in this repository and that its tree equals the tested PR-head tree.

A compatibility consumer may preserve historical `0.9.0` provenance while separately recording `aiaiaiai-org/mind-protocol` as the current canonical authority. No old release bytes or tags are silently redefined.

## Invariants

- no history rewrite of historical `v0.9.0`;
- no protocol-version tags in concrete Mind repositories after the authority split;
- no root concrete Mind in the protocol repository;
- no named identity dependency in universal contracts;
- no schema byte mutation merely because repository authority moved;
- RC publication remains a separate explicit action after source merge.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
