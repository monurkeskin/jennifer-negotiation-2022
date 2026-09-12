"""Exhaustive independent point-table oracle; expected points are not read from configs."""

import json
from pathlib import Path
import pytest
from negotiator.domain import Preference
from negotiator.examples import builtin_domain

ROOT = Path(__file__).resolve().parents[1]
NAMES, TABLE = (
    ("compass", "container", "food", "hammer", "knife", "match", "medicine", "rope"),
    (
        ((5, 20, 7, 13, 10, 22, 6, 17), (13, 22, 17, 6, 5, 20, 7, 10)),
        ((13, 5, 22, 10, 17, 6, 7, 20), (6, 13, 20, 5, 10, 7, 17, 22)),
    ),
)


@pytest.mark.parametrize(
    "path", list((ROOT / "configs").glob("protocol*.json")), ids=lambda p: p.stem
)
@pytest.mark.parametrize("actor", ["human", "agent"])
def test_every_allocation_matches_the_paper_table(path, actor):
    data = json.loads(path.read_text(encoding="utf-8"))
    domain = builtin_domain("island")
    conditions = [c for c in data["conditions"] if not c.get("practice")]
    for index, condition in enumerate(conditions):
        points = TABLE[index][0 if actor == "human" else 1]
        profile = Preference.from_dict(domain, condition[actor + "_profile"])
        count = 0
        for bid in domain.bids():
            owned = [bid[k] if actor == "human" else 1 - bid[k] for k in NAMES]
            expected = sum(p * q for p, q in zip(points, owned, strict=True)) / 100
            assert profile.utility(bid, actor) == pytest.approx(expected, abs=1e-12)
            count += 1
        assert count == 256
