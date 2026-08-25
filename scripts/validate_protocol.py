#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Validate the implementation-independent Mind Protocol descriptor and linked contracts."""

from __future__ import annotations

import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from semver import SemVer
from validate_manifest import load_schema, load_yaml_mapping, schema_errors


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = ROOT / "protocol.yaml"
PROTOCOL_SCHEMA_PATH = ROOT / "schema/protocol.schema.json"
CONFORMANCE_SCHEMA = "schema/conformance.schema.json"
COMPATIBILITY_SCHEMA = "schema/compatibility.schema.json"
VISUAL_ASSETS_SCHEMA = "schema/visual-assets.schema.json"

EXPECTED_CONTRACTS = {
    "manifest": "schema/mind.schema.json",
    "module": "schema/module.schema.json",
    "identity": "schema/identity.schema.json",
    "identity_resource": "schema/identity-resource.schema.json",
    "relationships": "schema/relationships.schema.json",
    "visual_assets": VISUAL_ASSETS_SCHEMA,
    "conformance": CONFORMANCE_SCHEMA,
    "compatibility": COMPATIBILITY_SCHEMA,
}


def expected_compatibility_status(version: str) -> str:
    parsed = SemVer.parse(version)
    if parsed.major == 0:
        return "frozen_pre_1_0"
    if parsed.major == 1:
        return "release_candidate" if parsed.prerelease else "stable_1_x"
    raise ValueError(
        "protocol descriptor schema v3 defines lifecycle semantics only for pre-1.0 and 1.x releases"
    )


def compatibility_lifecycle_errors(protocol: dict[str, object]) -> list[str]:
    version = protocol["protocol"]["version"]  # type: ignore[index]
    status = protocol["compatibility"]["status"]  # type: ignore[index]
    expected = expected_compatibility_status(str(version))
    if status != expected:
        return [
            "protocol.compatibility.status must match protocol release lifecycle: "
            f"version {version!r} requires {expected!r}, got {status!r}"
        ]
    return []


def repository_file(relative_path: str) -> Path:
    root = ROOT.resolve()
    path = (root / relative_path).resolve()
    if path != root and root not in path.parents:
        raise ValueError(f"path escapes repository: {relative_path}")
    if not path.is_file():
        raise ValueError(f"file does not exist: {relative_path}")
    return path


def repository_boundary_errors() -> list[str]:
    errors: list[str] = []
    metadata = load_yaml_mapping(ROOT / "mind-repository.yaml")
    roles = metadata.get("repository", {}).get("roles", {})
    protocol_role = roles.get("protocol_authority", {})
    concrete_role = roles.get("concrete_mind", {})

    if metadata.get("scope") != "repository_metadata" or metadata.get("protocol_contract") is not False:
        errors.append("mind-repository.yaml must remain repository metadata, not protocol contract")
    if metadata.get("repository", {}).get("id") != "aiaiaiai-org/mind-protocol":
        errors.append("repository metadata must identify aiaiaiai-org/mind-protocol")
    if protocol_role.get("enabled") is not True or protocol_role.get("canonical") is not True:
        errors.append("repository must declare canonical protocol authority enabled")
    if protocol_role.get("release_authority") is not True:
        errors.append("repository must declare protocol release authority")
    if concrete_role.get("enabled") is not False:
        errors.append("protocol repository must not enable a concrete Mind role")

    forbidden_root_paths = (
        "manifest.yaml",
        "protocol.lock.yaml",
        "identity",
        "relationships",
        "knowledge",
        "engineering",
        "systems",
        "writing",
        ".assistant",
    )
    for relative in forbidden_root_paths:
        if (ROOT / relative).exists():
            errors.append(f"protocol repository must not contain concrete root path: {relative}")
    return errors


def validate_protocol() -> list[str]:
    errors: list[str] = []
    protocol = load_yaml_mapping(PROTOCOL_PATH)
    protocol_schema = load_schema(PROTOCOL_SCHEMA_PATH)
    errors.extend(
        f"protocol{error[1:]}"
        for error in schema_errors(Draft202012Validator(protocol_schema), protocol)
    )
    if errors:
        return errors

    errors.extend(compatibility_lifecycle_errors(protocol))
    errors.extend(repository_boundary_errors())

    protocol_ref = {
        "id": protocol["protocol"]["id"],
        "version": protocol["protocol"]["version"],
    }

    contracts = protocol["contracts"]
    for contract_id, expected_schema in EXPECTED_CONTRACTS.items():
        actual_schema = contracts[contract_id]["schema"]
        if actual_schema != expected_schema:
            errors.append(
                f"protocol.contracts.{contract_id}.schema must be {expected_schema!r}"
            )
            continue
        try:
            load_schema(repository_file(actual_schema))
        except ValueError as error:
            errors.append(f"protocol.contracts.{contract_id}.schema: {error}")

    resolver = protocol["visual_identity"]["asset_ref_resolution"]
    if resolver["resource_schema"] != VISUAL_ASSETS_SCHEMA:
        errors.append(
            "protocol.visual_identity.asset_ref_resolution.resource_schema "
            f"must be {VISUAL_ASSETS_SCHEMA!r}"
        )

    conformance_ref = protocol["conformance"]["suite"]
    try:
        conformance = load_yaml_mapping(repository_file(conformance_ref))
        conformance_schema = load_schema(repository_file(CONFORMANCE_SCHEMA))
    except ValueError as error:
        errors.append(f"protocol.conformance.suite: {error}")
    else:
        errors.extend(
            f"conformance{error[1:]}"
            for error in schema_errors(Draft202012Validator(conformance_schema), conformance)
        )
        if conformance.get("protocol") != protocol_ref:
            errors.append("conformance suite must target protocol id/version exactly")

    compatibility_ref = protocol["compatibility"]["policy"]
    try:
        compatibility = load_yaml_mapping(repository_file(compatibility_ref))
        compatibility_schema = load_schema(repository_file(COMPATIBILITY_SCHEMA))
    except ValueError as error:
        errors.append(f"protocol.compatibility.policy: {error}")
    else:
        errors.extend(
            f"compatibility{error[1:]}"
            for error in schema_errors(Draft202012Validator(compatibility_schema), compatibility)
        )
        if compatibility.get("protocol") != protocol_ref:
            errors.append("compatibility policy must target protocol id/version exactly")

    return errors


def main() -> int:
    try:
        errors = validate_protocol()
    except (KeyError, TypeError, ValueError) as error:
        print(f"protocol validation failed:\n- {error}", file=sys.stderr)
        return 1

    if errors:
        print("protocol validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("protocol descriptor, linked contracts, compatibility lifecycle, and repository boundary are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
