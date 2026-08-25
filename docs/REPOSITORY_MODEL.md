# Repository model

`aiaiaiai-org/mind-protocol` has exactly one canonical role: **Mind Protocol authority**.

## Physical separation

```text
aiaiaiai-org/mind-protocol
        │
        ├── protocol.yaml
        ├── conformance.yaml
        ├── compatibility.yaml
        ├── schema/
        ├── bootstrap + validators + tests
        └── protocol releases
                 │
                 ▼
       exact immutable release
                 │
       ┌─────────┼──────────────┐
       ▼         ▼              ▼
  0x0sky/mind  aiaiaiai-org/mind  other <identity>/mind
```

Concrete Mind repositories consume protocol releases. They do not define protocol semantics, own protocol tags, or act as templates for one another.

## Why the split exists

Historically `0x0sky/mind` co-located the protocol source with one concrete personal Mind. Explicit routing prevented semantic inheritance, but physical separation is clearer for humans and agents and removes the possibility that repository layout itself implies special authority for one named implementation.

The split preserves the exact protocol Git ancestry through source commit `48a81df7d8e9818d9c01f3e1fe5ac663af29a006`. The concrete personal repository then continues independently as a protocol consumer.

## Authority routing

| Question | Authority |
| --- | --- |
| protocol definition | `protocol.yaml` |
| schema shape | `schema/` |
| conformance | `conformance.yaml` + conformance fixtures/tests |
| compatibility/migration | `compatibility.yaml` + protocol migration docs |
| creation of a new Mind | exact release + `scripts/bootstrap_mind.py` |
| concrete identity/context | that concrete Mind's `manifest.yaml` and registered modules |

`mind-repository.yaml` makes this repository role machine-readable but is itself repository metadata, not a universal Mind contract.

## GitHub fork semantics

A GitHub fork of this repository is valid for protocol development and experimentation. It is not a concrete Mind template.

A concrete Mind starts from an exact immutable release, then receives an explicit subject, publication owner, Identity, context version, visibility, and only genuinely authored modules/resources for that subject.

## Versioning

`protocol.version` belongs here. `mind.context_version` belongs to each concrete Mind. They are independent axes.

Protocol-version tags live in the protocol release authority. Concrete Mind repositories must not reuse those tags as if they described their authored context.

## Historical continuity

The first formal release, `v0.9.0`, was published before the physical split from `0x0sky/mind`. That publication remains immutable historical evidence. The move to `aiaiaiai-org/mind-protocol` does not rewrite or invalidate it.

The RC and subsequent canonical protocol publications are produced from this repository after normal green-PR/tree verification. See [`protocol/AUTHORITY_MIGRATION.md`](protocol/AUTHORITY_MIGRATION.md).

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
