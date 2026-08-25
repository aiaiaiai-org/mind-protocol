# Repository instructions for GitHub Copilot

Operate in `aiaiaiai-org/mind-protocol` as the canonical implementation-independent Mind Protocol repository.

- Read `mind-repository.yaml` first, then `protocol.yaml`.
- Treat `conformance.yaml`, `compatibility.yaml`, `schema/`, protocol docs, validators, bootstrap, and release machinery as repository-owned protocol surfaces.
- There is intentionally no concrete root `manifest.yaml`; named identity/context belongs in a concrete `<identity>/mind` repository.
- Never introduce provider-, renderer-, runtime-, repository-owner-, or named-identity assumptions into universal contracts.
- Preserve published schema bytes and `$id` values unless a deliberately versioned schema revision is being implemented.
- New concrete Minds come from exact immutable release tags through `scripts/bootstrap_mind.py`, never by copying another concrete Mind.
- Inspect current state before editing, keep changes narrowly scoped, synchronize tests/docs, and require green CI before merge.
- Merging protocol source is not publishing a release; tags and GitHub Releases are separate actions.
- Never commit secrets, credentials, private context, or transient runtime state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
