import sys
from pathlib import Path

import pandas as pd
import pytest

# Import functions from the project's source directory
project_dir = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_dir / "src"))

from occupancy_utils import (
    create_future_target,
    get_historical_occupancy,
)


def test_future_target_alignment():
    """Verify that six 5-minute steps represent 30 minutes."""
    times = pd.date_range(
        "2025-01-01",
        periods=10,
        freq="5min"
    )

    occupancy = pd.Series(
        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        index=times
    )

    target = create_future_target(occupancy)

    assert target.iloc[0] == occupancy.iloc[6]
    assert target.iloc[1] == occupancy.iloc[7]
    assert pd.isna(target.iloc[-1])


def test_historical_feature_alignment():
    """Verify that historical features use exact timestamps."""
    times = pd.to_datetime([
        "2025-01-01 09:00",
        "2025-01-01 09:05",
        "2025-01-01 09:15"
    ])

    occupancy = pd.Series([0, 1, 0], index=times)

    lag = get_historical_occupancy(occupancy, minutes=5)

    assert pd.isna(lag.iloc[0])
    assert lag.iloc[1] == 0
    assert pd.isna(lag.iloc[2])


def test_invalid_future_step():
    """Verify that negative future steps raise ValueError."""
    occupancy = pd.Series([0, 1, 0, 1])

    with pytest.raises(ValueError):
        create_future_target(occupancy, steps=-1)
