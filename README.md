# Mind Protocol

> Canonical, implementation-independent contract for versioned Mind identity, context, conformance, compatibility, and deterministic bootstrap.

This repository defines **what a Mind is**. It does not contain the authored Mind of any person, organization, agent, project, or product.

## Repository boundary

| Repository | Role |
| --- | --- |
| `aiaiaiai-org/mind-protocol` | canonical Mind Protocol source and release authority |
| `<identity>/mind` | one concrete Mind publication and protocol consumer |

A concrete Mind never becomes protocol authority merely by implementing or testing the protocol. A GitHub fork of this repository is valid for protocol development; it is **not** a template for a concrete Mind.

Machine-readable repository routing lives in [`mind-repository.yaml`](mind-repository.yaml). The full authority model is documented in [`docs/REPOSITORY_MODEL.md`](docs/REPOSITORY_MODEL.md).

## Canonical construction path

```text
exact immutable Mind Protocol release
                ↓
         neutral baseline
                ↓
subject + publication-owner semantics + Identity
                ↓
          concrete mind@<id>
                ↓
 only authored modules/resources for that subject
```

Use [`scripts/bootstrap_mind.py`](scripts/bootstrap_mind.py) from an exact published release checkout. Never consume floating `master` as a release contract and never create a concrete Mind by copying another concrete Mind's authored content.

## Machine entry points

| Entry point | Authority |
| --- | --- |
| [`mind-repository.yaml`](mind-repository.yaml) | repository-role routing; repository metadata, not protocol contract |
| [`protocol.yaml`](protocol.yaml) | protocol descriptor and universal contract discovery |
| [`conformance.yaml`](conformance.yaml) | synthetic fixtures, feature matrix, supported ranges, deterministic probes |
| [`compatibility.yaml`](compatibility.yaml) | compatibility state, schema fingerprints, forward-compatibility and migration policy |
| [`schema/`](schema/) | published JSON Schema contracts |
| [`docs/protocol/BOOTSTRAP.md`](docs/protocol/BOOTSTRAP.md) | exact-release creation of a concrete Mind |
| [`docs/protocol/RELEASE_POLICY.md`](docs/protocol/RELEASE_POLICY.md) | formal release gates and publication semantics |

There is intentionally **no root `manifest.yaml`** in this repository. Concrete manifests belong to concrete Mind repositories or synthetic test fixtures.

## Current source

The current source contract is **Mind Protocol `1.0.0-rc.1`**. It is still an unpublished release candidate until the separate prerelease workflow succeeds.

Protocol descriptor schema is `3`; manifest schema is `3`; conformance schema is `2`. The reusable JSON Schema bytes frozen for `0.9.0` remain unchanged in the RC candidate.

## Identity

[`schema/identity.schema.json`](schema/identity.schema.json) defines the universal Identity value for `person`, `organization`, `agent`, `project`, and `product`. Identity is provider-, repository-, storage-, renderer-, and runtime-independent.

Concrete publication packaging uses [`schema/identity-resource.schema.json`](schema/identity-resource.schema.json). Canonical visual bytes resolve separately through [`schema/visual-assets.schema.json`](schema/visual-assets.schema.json).

Provider accounts, runtime/model state, synthetic portraits, and repository slugs do not silently become canonical Identity.

## Manifest and capability model

Manifest schema v3, frozen in `0.9.0`, removes compatibility-only root concepts that do not belong in the provider-agnostic contract. Unknown root fields are rejected; compatible extension is negotiated through optional modules and versioned resources.

`module` is the capability unit:

```text
unknown optional module, not requested → ignore
unknown required/default-loaded module → reject
unknown root manifest field            → reject
```

## Conformance

The public conformance suite covers synthetic `person`, `organization`, `agent`, `project`, and `product` subjects through two consumer modes:

- `schema` — JSON Schema plus shared semantic validators;
- `minimal` — independent core-reader behavior over the same deterministic probes.

For the RC candidate, the supported range is `>=1.0.0-rc.1 <1.0.0`. Range evaluation follows SemVer 2.0 prerelease precedence.

```bash
python scripts/validate_conformance.py --mode all
```

## Compatibility

[`compatibility.yaml`](compatibility.yaml) carries the `0.9.0` freeze into the release candidate: exact schema fingerprints, manifest-v3 behavior, module capability negotiation, migration floor `0.6.0`, and provider-login/canonical-id separation.

```bash
python scripts/validate_compatibility.py
```

## Neutral baseline and bootstrap

[`scripts/generate_baseline.py`](scripts/generate_baseline.py) produces the deterministic abstract protocol baseline. Its manifest has `subject: unspecified`, no concrete Identity module, and is not itself a concrete Mind.

[`scripts/bootstrap_mind.py`](scripts/bootstrap_mind.py) turns an exact checked-out release into a minimal concrete Mind with explicit subject, display name, context version, repository visibility, Identity, and exact protocol lock. Publication owner defaults to the subject unless a complete distinct owner is explicitly supplied.

```bash
python scripts/generate_baseline.py --check
```

See [`docs/protocol/BASELINE.md`](docs/protocol/BASELINE.md) and [`docs/protocol/BOOTSTRAP.md`](docs/protocol/BOOTSTRAP.md).

## Version axes

Protocol version and concrete context version are independent:

- `protocol.version` identifies the Mind Protocol release and is tagged here;
- `mind.context_version` identifies durable authored content in one concrete Mind and is versioned there.

A protocol bump does not imply a context bump. Concrete Mind repositories must not use protocol-version tags as if those tags described their own authored context.

## Release continuity

`0.9.0`, the first formal Mind Protocol GitHub Release, was historically published from `0x0sky/mind` before protocol authority was physically separated. That immutable publication remains historical evidence and is never rewritten.

The exact protocol-source ancestry through commit `48a81df7d8e9818d9c01f3e1fe5ac663af29a006` was preserved in this repository before the RC publication. Canonical protocol source/release authority is now `aiaiaiai-org/mind-protocol`; concrete `0x0sky/mind` is only a consumer.

See [`docs/protocol/AUTHORITY_MIGRATION.md`](docs/protocol/AUTHORITY_MIGRATION.md).

## Publication sequence

1. `0.9.0` — first formal release; historical publication preserved;
2. `1.0.0-rc.1` — next GitHub prerelease from this canonical repository;
3. `1.0.0` — first compatibility-guaranteed stable release.

Merging source does not publish a release. Tags and GitHub Releases remain separate explicit publication actions.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
