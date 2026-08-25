# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Regression coverage for the pure protocol repository authority boundary."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from validate_manifest import load_yaml_mapping  # noqa: E402


class RepositoryModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = load_yaml_mapping(ROOT / "mind-repository.yaml")

    def test_metadata_is_not_a_protocol_contract(self) -> None:
        self.assertEqual(self.model["scope"], "repository_metadata")
        self.assertFalse(self.model["protocol_contract"])

    def test_repository_is_only_protocol_authority(self) -> None:
        self.assertEqual(self.model["repository"]["id"], "aiaiaiai-org/mind-protocol")
        roles = self.model["repository"]["roles"]
        self.assertTrue(roles["protocol_authority"]["enabled"])
        self.assertTrue(roles["protocol_authority"]["canonical"])
        self.assertTrue(roles["protocol_authority"]["release_authority"])
        self.assertEqual(roles["protocol_authority"]["entrypoint"], "protocol.yaml")
        self.assertFalse(roles["concrete_mind"]["enabled"])

    def test_no_concrete_root_mind_exists(self) -> None:
        for path in (
            "manifest.yaml",
            "protocol.lock.yaml",
            "identity",
            "relationships",
            "knowledge",
            "engineering",
            "systems",
            "writing",
            ".assistant",
        ):
            self.assertFalse((ROOT / path).exists(), path)

    def test_concrete_creation_is_exact_release_bootstrap(self) -> None:
        concrete = self.model["fork_policy"]["concrete_mind_creation"]
        self.assertEqual(concrete["github_fork_of_master"], "forbidden_as_template")
        self.assertEqual(concrete["source"], "exact_immutable_protocol_release")
        self.assertEqual(concrete["mechanism"], "neutral_bootstrap")
        bootstrap = self.model["bootstrap"]
        self.assertEqual(bootstrap["command"], "scripts/bootstrap_mind.py")
        self.assertEqual(bootstrap["input_authority"], "exact_protocol_release_tag")
        self.assertEqual(bootstrap["floating_master"], "forbidden_for_release_consumption")

    def test_history_records_non_destructive_authority_split(self) -> None:
        history = self.model["history"]
        self.assertEqual(history["authority_split_source"]["repository"], "0x0sky/mind")
        self.assertEqual(
            history["authority_split_source"]["commit"],
            "48a81df7d8e9818d9c01f3e1fe5ac663af29a006",
        )
        self.assertEqual(history["first_formal_release"]["version"], "0.9.0")
        self.assertTrue(history["first_formal_release"]["immutable"])


if __name__ == "__main__":
    unittest.main()
