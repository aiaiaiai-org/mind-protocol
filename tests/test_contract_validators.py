# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Regression tests for correctness-critical Mind contract validators without a root concrete Mind."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from bootstrap_mind import concrete_manifest  # noqa: E402
from validate_manifest import legacy_field_errors, validate_manifest_semantics  # noqa: E402
from validate_relationships import validate_relationships  # noqa: E402


SUBJECT = {"type": "person", "id": "fixture-person"}
OWNER = dict(SUBJECT)


def fixture_manifest() -> dict:
    """Return a synthetic concrete manifest with no filesystem-backed modules."""
    manifest = concrete_manifest(
        {"id": "mind", "version": "1.0.0-rc.1"},
        dict(SUBJECT),
        dict(OWNER),
        context_version="0.1.0",
        repository_visibility="public",
    )
    manifest["modules"]["required"] = []
    manifest["modules"]["registered"] = []
    manifest["modules"]["catalog"] = {}
    manifest["loading"]["default"] = []
    return manifest


def fixture_relationships() -> dict:
    return {
        "schema_version": 1,
        "relationships": [
            {
                "id": "member-of-fixture-org",
                "predicate": "member_of",
                "source": dict(SUBJECT),
                "target": {"type": "organization", "id": "fixture-org"},
                "direction": "directed",
                "provenance": {"kind": "authored", "authority": dict(OWNER)},
                "confirmation": {
                    "state": "reciprocal",
                    "counterpart": {
                        "entity": {"type": "organization", "id": "fixture-org"},
                        "relationship_id": "fixture-member",
                    },
                },
            }
        ],
        "validation": {"schema": "schema/relationships.schema.json"},
    }


class ContractValidatorRegressionTests(unittest.TestCase):
    def test_synthetic_concrete_manifest_semantics_are_valid(self) -> None:
        self.assertEqual(validate_manifest_semantics(fixture_manifest(), ROOT), [])

    def test_removed_mind_kind_has_deterministic_diagnostic(self) -> None:
        candidate = fixture_manifest()
        candidate["mind"]["kind"] = "personal"
        errors = legacy_field_errors(candidate)
        self.assertTrue(any("$.mind.kind" in error for error in errors), errors)

    def test_removed_public_organizations_has_deterministic_diagnostic(self) -> None:
        candidate = fixture_manifest()
        candidate["public_organizations"] = ["provider-only-org"]
        errors = legacy_field_errors(candidate)
        self.assertTrue(any("$.public_organizations" in error for error in errors), errors)

    def test_abstract_subject_requires_unspecified_owner(self) -> None:
        candidate = fixture_manifest()
        candidate["mind"]["name"] = "mind"
        candidate["mind"]["subject"] = {"type": "unspecified", "id": "unspecified"}
        errors = validate_manifest_semantics(candidate, ROOT)
        self.assertTrue(any("abstract minds must use" in error for error in errors), errors)

    def test_validation_paths_cannot_escape_repository(self) -> None:
        candidate = fixture_manifest()
        candidate["validation"]["schema"] = "../mind.schema.json"
        errors = validate_manifest_semantics(candidate, ROOT)
        self.assertTrue(any("path escapes repository" in error for error in errors), errors)

    def test_synthetic_relationship_semantics_are_valid(self) -> None:
        self.assertEqual(validate_relationships(fixture_manifest(), fixture_relationships()), [])

    def test_relationship_authority_must_match_publication_owner(self) -> None:
        candidate = fixture_relationships()
        candidate["relationships"][0]["provenance"]["authority"]["id"] = "other-owner"
        errors = validate_relationships(fixture_manifest(), candidate)
        self.assertTrue(any("must match $.mind.owner" in error for error in errors), errors)

    def test_reciprocal_confirmation_must_reference_other_endpoint(self) -> None:
        candidate = fixture_relationships()
        candidate["relationships"][0]["confirmation"]["counterpart"]["entity"] = dict(SUBJECT)
        errors = validate_relationships(fixture_manifest(), candidate)
        self.assertTrue(any("other relationship endpoint" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
