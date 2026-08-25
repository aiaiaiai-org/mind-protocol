# Mind Protocol 1.0 release candidate

Status: **`1.0.0-rc.2` source candidate; `v1.0.0-rc.1` is published and immutable**

Mind Protocol is the implementation-independent contract in this repository. Concrete Minds live in separate repositories and consume exact releases.

See [`../REPOSITORY_MODEL.md`](../REPOSITORY_MODEL.md) for the repository boundary and [`AUTHORITY_MIGRATION.md`](AUTHORITY_MIGRATION.md) for the one-time authority split.

## Machine entry points

- [`../../mind-repository.yaml`](../../mind-repository.yaml) — repository-role routing; not protocol contract;
- [`../../protocol.yaml`](../../protocol.yaml) — implementation-independent protocol descriptor, schema `v3`;
- [`../../conformance.yaml`](../../conformance.yaml) — conformance suite and feature matrix, schema `v2`;
- [`../../compatibility.yaml`](../../compatibility.yaml) — compatibility freeze, schema fingerprints, `1.x` policy, migration floor;
- [`BASELINE.md`](BASELINE.md) — generated abstract neutral baseline;
- [`BOOTSTRAP.md`](BOOTSTRAP.md) — canonical creation path for a new concrete Mind;
- [`RELEASE_POLICY.md`](RELEASE_POLICY.md) — formal publication sequence and release gates.

There is intentionally no root concrete `manifest.yaml` in the protocol repository.

## Authority model

```text
protocol.yaml        → universal Mind semantics
conformance.yaml     → public deterministic conformance
compatibility.yaml   → compatibility and migration policy
<identity>/mind      → concrete authored context only
```

A GitHub fork of this repository is valid for protocol development. A concrete Mind is created from an exact immutable release through the neutral bootstrap path, not from a fork or copy of another concrete Mind.

## Current version model

| Axis | Current reference | Meaning |
| --- | --- | --- |
| Protocol descriptor schema | `3` | Descriptor shape and lifecycle/contract discovery. |
| Manifest schema | `3` | Frozen concrete root shape from `0.9.0`. |
| Protocol | `1.0.0-rc.2` | Corrected canonical-bootstrap integration candidate. |
| Conformance suite schema | `2` | Dual consumer modes and deterministic probes. |
| Compatibility policy schema | `1` | Schema fingerprints, forward compatibility, migration policy. |
| Identity schema | `1` | Universal Identity for all five subject types. |

Concrete `mind.context_version` values are external to this repository and independent from protocol version.

## Frozen manifest and capability model

Manifest schema v3 removes `mind.kind` and provider-specific root projections such as `public_organizations`. Unknown root fields are rejected. Compatible extension happens through optional modules or versioned optional resources.

`module` remains the capability-negotiation unit:

```text
unknown optional module, not requested → ignore
unknown required/default-loaded module → reject
unknown root manifest field            → reject
```

## Compatibility and schema immutability

[`../../compatibility.yaml`](../../compatibility.yaml) fingerprints each published JSON Schema by `$id` and exact Git blob SHA-1. The RC train reuses the `0.9.0` schema identities only because those schema bytes are unchanged.

Supported stable migration sources are `0.6.0`, `0.7.0`, `0.8.0`, and formal `0.9.0`.

## Conformance

The suite covers synthetic `person`, `organization`, `agent`, `project`, and `product` subjects through two independent reader modes. The current RC support range remains `>=1.0.0-rc.1 <1.0.0` and follows strict SemVer 2.0 prerelease precedence.

`rc.2` is inside that range because the delta from `rc.1` is the exact standalone bootstrap/repository-provenance contract, not a compatibility-breaking universal semantic change.

```bash
python scripts/validate_conformance.py --mode all
```

## Neutral baseline and concrete bootstrap

[`../../scripts/generate_baseline.py`](../../scripts/generate_baseline.py) produces a deterministic abstract bundle with explicit `subject: unspecified`, `owner: unspecified`, no concrete Identity module, and no concrete repository content.

[`../../scripts/bootstrap_mind.py`](../../scripts/bootstrap_mind.py) turns an exact checked-out release into a minimal concrete publication. It creates only the required Identity module/resource plus exact protocol locks and never copies authored modules from another concrete Mind.

The corrected bootstrap requires the exact release tag commit and records release repository, tag, and commit in both `mind-repository.yaml` and `protocol.lock.yaml`.

## Release boundary

`0.9.0` remains the first formal GitHub Release and historical publication. `v1.0.0-rc.1` is the first immutable prerelease from the separated canonical protocol repository. The next publication is `v1.0.0-rc.2`, proving the corrected standalone bootstrap path before stable `1.0.0` begins the compatibility-guaranteed `1.x` line.

Merging source is not publishing a release.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
