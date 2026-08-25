# Mind Protocol release policy

Mind Protocol source merge and formal release publication are separate operations. `aiaiaiai-org/mind-protocol` is the canonical protocol source/release authority; GitHub is the publication channel, not runtime protocol authority.

## Release sequence

1. `0.9.0` — first formal GitHub Release, historically published before the physical repository split;
2. `1.0.0-rc.1` — first immutable GitHub prerelease from the separated canonical protocol repository;
3. `1.0.0-rc.2` — corrected canonical-bootstrap integration candidate;
4. `1.0.0` — first compatibility-guaranteed stable release after final integration evidence.

Earlier `0.6.0`, `0.7.0`, and `0.8.0` remain source milestones and are not retroactively published.

## Historical authority migration

`v0.9.0` was published from `0x0sky/mind` before protocol authority was physically separated. That tag, release, and target commit remain immutable historical evidence.

The exact protocol ancestry through `0x0sky/mind@48a81df7d8e9818d9c01f3e1fe5ac663af29a006` was preserved in `aiaiaiai-org/mind-protocol`. New canonical publication begins only from a post-split PR merge in this repository. No old tag is rewritten to manufacture a cleaner history.

See [`AUTHORITY_MIGRATION.md`](AUTHORITY_MIGRATION.md).

## Verified release evidence

Full correctness CI runs on the pull-request head. A releasable `master` commit must prove:

- it is the merge commit of the approved protocol PR into `master`;
- that PR head has a successful `Mind Contract CI` run;
- the merge-commit tree equals the tested PR-head tree exactly;
- deterministic release packaging is produced from that exact merge commit;
- the release tag points to that exact commit.

If the tree differs, publication fails and the changed tree must receive new correctness evidence. Full CI is not rerun after merge solely to obtain a new merge SHA.

## Manual publication inputs

`Publish Mind Protocol Release` exposes only:

- GitHub's native **Use workflow from** branch selector;
- publication kind: `release` or `prerelease`.

The workflow derives target SHA, protocol version, tag, title, release notes, and artifact names from verified repository state. It rejects a non-default branch, branch movement after dispatch, publication kind inconsistent with SemVer state, a pre-existing immutable tag, or missing green PR/tree evidence.

## Schema identity

Published JSON Schema `$id` values identify schema shapes, not one GitHub release number. If a schema is reused across `0.9.0`, the RC train, and stable `1.0.0`, its bytes remain unchanged. Any real shape change requires a new versioned schema identity.

Exact protocol-release binding remains semantic and machine-checked:

- `protocol.yaml`, `conformance.yaml`, and `compatibility.yaml` target the same exact protocol id/version;
- compatibility lifecycle state matches that version;
- migration-source lines match the release target;
- every schema is fingerprinted by immutable `$id` and exact Git blob SHA-1;
- concrete Minds validate their own exact release binding independently and never define protocol truth.

## `0.9.0`

`0.9.0` froze the public compatibility surface before `1.0`: manifest schema v3, Identity/resource contracts, relationships/provenance, loading/module behavior, visual references, neutral baseline, conformance, compatibility, schema fingerprints, migration floor, and provider-login/canonical-id separation.

The historical first formal release remains valid at its original repository and commit. It is not republished under a different commit merely because protocol authority moved.

## Compatibility canaries

After `v0.9.0`, a deliberately small set of real concrete Minds synchronized as compatibility canaries. Canary repositories consume the protocol and never become protocol authority. Their named content, provider data, visuals, or rollout state cannot become universal requirements merely because they expose a defect.

## `1.0.0-rc.1`

`v1.0.0-rc.1` is published and immutable. It proved the frozen protocol contract, SemVer prerelease behavior, schema immutability, required synthetic fixtures, dual-mode conformance, neutral baseline, and four real concrete consumers.

A post-publication defect was then found in canonical concrete-Mind bootstrap/repository provenance: generated metadata did not carry the exact release repository/tag/commit in the same canonical shape already proven by the real consumers. `rc.1` is never mutated to absorb that correction.

## `1.0.0-rc.2`

`rc.2` promotes the corrected bootstrap/provenance path without introducing new universal protocol semantics. Publication requires:

- a green post-`rc.1` PR in `aiaiaiai-org/mind-protocol`;
- verified merge-tree equality;
- tag `v1.0.0-rc.2` created from that exact merge commit;
- clean protocol validation, conformance, compatibility, baseline generation, deterministic release bundle, bootstrap/regression tests;
- unchanged frozen JSON Schema bytes and `$id` values;
- exact bootstrap release repository, tag, and commit provenance;
- no named-identity dependency;
- no required provider dependency.

The RC conformance range remains `>=1.0.0-rc.1 <1.0.0` because the bootstrap correction is compatible with the frozen universal contract.

After publication, the real canary Minds and independent `mind-web` consumer must exercise the exact `rc.2` release before stable promotion.

## `1.0.0`

Stable `1.0.0` is the first compatibility-guaranteed `1.x` release and should promote the accepted final RC contract. Any universal semantic change after the final RC requires renewed review, conformance evidence, and—when blocking—another RC rather than silent stable-only drift.

Stable publication requires final evidence from the corrected standalone create/load/auth/repair path and no unresolved universal protocol blocker.

## Delivery boundary

Merging source is not releasing. Release/tag creation is a separate explicit publication action after the verified `master` commit is known. Do not duplicate already-green correctness checks unless inputs materially changed.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
