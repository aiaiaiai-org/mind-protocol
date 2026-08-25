# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Regression coverage for universal Identity using synthetic concrete values."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from bootstrap_mind import concrete_manifest, identity_resource  # noqa: E402
from validate_identity_resources import validate_identity_envelope  # noqa: E402
from validate_manifest import load_schema  # noqa: E402


class IdentityResourceValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = concrete_manifest(
            {"id": "mind", "version": "1.0.0-rc.1"},
            {"type": "person", "id": "fixture-person"},
            {"type": "person", "id": "fixture-person"},
            context_version="0.1.0",
            repository_visibility="public",
        )
        cls.envelope = identity_resource(
            {"type": "person", "id": "fixture-person"}, "Fixture Person"
        )
        cls.envelope_schema = load_schema(ROOT / "schema" / "identity-resource.schema.json")
        cls.identity_schema = load_schema(ROOT / "schema" / "identity.schema.json")

    def validate(self, envelope: dict, manifest: dict | None = None) -> list[str]:
        return validate_identity_envelope(
            envelope,
            self.manifest if manifest is None else manifest,
            self.envelope_schema,
            self.identity_schema,
        )

    def test_synthetic_identity_resource_is_valid(self) -> None:
        self.assertEqual(self.validate(self.envelope), [])

    def test_provider_account_is_outside_universal_identity(self) -> None:
        candidate = copy.deepcopy(self.envelope)
        candidate["identity"]["provider_account"] = "provider-user"
        errors = self.validate(candidate)
        self.assertTrue(any("provider_account" in error for error in errors), errors)

    def test_runtime_state_cannot_leak_into_universal_identity(self) -> None:
        candidate = copy.deepcopy(self.envelope)
        candidate["identity"]["runtime"] = {"model": "synthetic-model"}
        errors = self.validate(candidate)
        self.assertTrue(any("runtime" in error for error in errors), errors)

    def test_identity_must_bind_to_manifest_subject(self) -> None:
        candidate = copy.deepcopy(self.envelope)
        candidate["identity"]["id"] = "other-subject"
        errors = self.validate(candidate)
        self.assertTrue(any("must match manifest mind.subject" in error for error in errors), errors)

    def test_agent_identity_supports_distinct_publication_owner(self) -> None:
        manifest = concrete_manifest(
            {"id": "mind", "version": "1.0.0-rc.1"},
            {"type": "agent", "id": "fixture-agent"},
            {"type": "organization", "id": "fixture-publisher"},
            context_version="0.1.0",
            repository_visibility="private",
        )
        envelope = identity_resource(
            {"type": "agent", "id": "fixture-agent"}, "Fixture Agent"
        )
        self.assertNotEqual(manifest["mind"]["subject"], manifest["mind"]["owner"])
        self.assertEqual(self.validate(envelope, manifest), [])


if __name__ == "__main__":
    unittest.main()
