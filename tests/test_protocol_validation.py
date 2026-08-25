# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Regression coverage for protocol source validation independent of a concrete root Mind."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from validate_manifest import load_yaml_mapping  # noqa: E402
from validate_protocol import (  # noqa: E402
    compatibility_lifecycle_errors,
    repository_boundary_errors,
    validate_protocol,
)


class ProtocolValidationTests(unittest.TestCase):
    def test_protocol_source_and_repository_boundary_are_green(self) -> None:
        self.assertEqual(validate_protocol(), [])
        self.assertEqual(repository_boundary_errors(), [])

    def test_release_candidate_lifecycle_is_required(self) -> None:
        protocol = load_yaml_mapping(ROOT / "protocol.yaml")
        candidate = copy.deepcopy(protocol)
        candidate["compatibility"]["status"] = "stable_1_x"
        errors = compatibility_lifecycle_errors(candidate)
        self.assertTrue(any("release lifecycle" in error for error in errors), errors)

    def test_protocol_repository_has_no_root_concrete_manifest(self) -> None:
        self.assertFalse((ROOT / "manifest.yaml").exists())


if __name__ == "__main__":
    unittest.main()
