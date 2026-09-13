"""Paper-specific study contracts, independently executable without a robot."""

import json
from pathlib import Path
import pytest
from negotiator.application.contracts import StudySpec
from negotiator.application.protocol import (
    ordered_conditions,
    protocol_digest,
    protocol_readiness,
)

ROOT = Path(__file__).resolve().parents[1]
CONFIGS = list((ROOT / "configs").glob("protocol*.json"))


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_published_templates_pin_behavior_and_expose_unrecovered_evidence(path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    assert spec.purpose == "published-protocol"
    assert spec.protocol.configuration_sha256 == protocol_digest(spec)
    assert spec.protocol.requirements
    assert protocol_readiness(spec), (
        "Historical evidence is still unrecovered; do not imply a runnable original experiment."
    )
    assert not spec.synthetic


def test_demo_is_explicit_and_device_free():
    spec = StudySpec.model_validate_json(
        (ROOT / "configs/synthetic.json").read_text(encoding="utf-8")
    )
    assert spec.purpose == "demonstration"
    assert spec.synthetic
    assert spec.output == "text"
    assert all(c.output in (None, "text", "avatar") for c in spec.conditions)
    assert not spec.speech_device and not spec.perception_device


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_notification_stages_and_gesture_condition_are_explicit(path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    assert spec.interaction_protocol == "ready-offer-response"
    assert spec.conditions[0].practice and spec.conditions[0].duration_seconds == 300
    for condition in spec.conditions:
        if not condition.practice:
            assert condition.duration_seconds == 600
            assert condition.mood_policy.startswith("jennifer-")
            if condition.label == "No gesture":
                assert not condition.gestures


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_tactic_between_groups_and_fifteen_minute_break(path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    main = [c for c in spec.conditions if not c.practice]
    assert len({c.strategy for c in main}) == 1
    assert main[0].break_after_seconds == 900
    assert len(spec.position_profiles) == 2
    assert spec.cohort == main[0].strategy


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_paper_score_target_does_not_prohibit_below_target_agreement(path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    for condition in spec.conditions:
        if condition.practice:
            continue
        assert condition.human_profile["reservation"] == 0
        assert condition.score_targets["human"] == 0.3
        assert condition.reward_minimums == {}


@pytest.mark.parametrize("path", sorted((ROOT / "configs").glob("*.json")), ids=lambda p: p.stem)
def test_social_reaction_threshold_is_recorded_separately_from_reservation(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for condition in data["conditions"]:
        if condition.get("mood_policy", "generic").startswith("jennifer-"):
            assert condition["mood_parameters"]["offended_threshold"] == 0.3
