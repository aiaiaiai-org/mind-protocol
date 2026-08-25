# Bootstrapping a concrete Mind

A concrete Mind is created from an **exact immutable Mind Protocol release** from `aiaiaiai-org/mind-protocol`, not by copying another concrete Mind or by forking protocol `master` as a template.

## Canonical path

```text
Mind Protocol tag vX.Y.Z
        ↓
neutral protocol baseline
        ↓
subject + publication-owner semantics + Identity
        ↓
concrete mind@<subject.id>
```

The bootstrap copies the released protocol contract set, creates a minimal valid concrete manifest, adds the required Identity module/resource, and records an exact protocol lock. It does not invent or copy relationships, organization hierarchy, provider identities, handles, biography, governance, engineering, knowledge, systems, writing, visual assets, or runtime configuration.

## Protocol fork vs concrete Mind

Forking `aiaiaiai-org/mind-protocol` is valid for protocol development. It is not the construction path for a concrete Mind because a development branch is mutable and is not an immutable release authority.

A concrete Mind also must not be created by renaming IDs inside another concrete Mind. That would copy authored context and create accidental identity inheritance.

## Bootstrap from a release tag

After a protocol version is formally published, check out that exact tag and run the bootstrap tool from that checkout.

```bash
git clone --branch v1.0.0 https://github.com/aiaiaiai-org/mind-protocol.git mind-protocol
cd mind-protocol

python scripts/bootstrap_mind.py \
  --output ../my-organization-mind \
  --source-tag v1.0.0 \
  --subject-type organization \
  --subject-id my-organization \
  --display-name "My Organization" \
  --context-version 0.1.0 \
  --repository-visibility public
```

A distinct publication owner is explicit and atomic:

```bash
python scripts/bootstrap_mind.py \
  --output ../my-agent-mind \
  --source-tag v1.0.0 \
  --subject-type agent \
  --subject-id my-agent \
  --display-name "My Agent" \
  --owner-type organization \
  --owner-id my-organization \
  --context-version 0.1.0 \
  --repository-visibility private
```

If `--owner-type` and `--owner-id` are omitted, owner defaults to the subject. Supplying only one is rejected.

The CLI proves before generating anything that:

- it is running inside the Mind Protocol Git checkout;
- `--source-tag` exactly matches `v{protocol.version}`;
- the supplied tag exists;
- checked-out `HEAD` equals that tag commit exactly;
- `protocol.yaml`, `conformance.yaml`, `compatibility.yaml`, and `schema/` have no tracked modifications.

A floating branch such as `master`, a later branch commit that merely declares the same version string, or a locally modified released contract is rejected.

## Generated minimum

```text
mind@<id>/
├── AGENTS.md
├── README.md
├── mind-repository.yaml
├── manifest.yaml
├── protocol.lock.yaml
├── protocol.yaml
├── conformance.yaml
├── compatibility.yaml
├── identity/
│   ├── module.yaml
│   └── identity.yaml
└── schema/
    └── exact released protocol schemas
```

The generated metadata declares protocol-authority role disabled and concrete-Mind role enabled. The generated `protocol.lock.yaml` records the exact source repository `aiaiaiai-org/mind-protocol`, immutable release tag, contract Git blob fingerprints, schema `$id` values, and floating-branch consumption prohibition.

Folder names are not themselves protocol authority. A concrete implementation may later organize registered modules differently while preserving the manifest/resource contracts.

## Context version

`mind.context_version` is explicit input because it belongs to the concrete authored publication, not to the protocol release. Protocol tags never become concrete-context tags.

## RC usage

A prerelease such as `v1.0.0-rc.1` may be used for compatibility canaries only after that prerelease is formally published. It does not carry the stable `1.x` compatibility guarantee.

## Verification

The protocol regression suite verifies that bootstrap:

- produces a valid manifest schema-v3 concrete Mind;
- requires Identity and binds Identity type/id to the subject;
- preserves distinct subject/publication-owner semantics;
- creates only the requested synthetic subject rather than copying a named implementation;
- rejects a `HEAD` different from the named release tag;
- rejects modified released protocol contracts;
- records `aiaiaiai-org/mind-protocol` and the exact release tag;
- leaves published protocol schemas unchanged.

See [`../REPOSITORY_MODEL.md`](../REPOSITORY_MODEL.md) and [`BASELINE.md`](BASELINE.md).

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
