
import pandas as pd


def create_future_target(occupancy, steps=6):
    """
    Create future occupancy labels from a regular time series.

    Parameters
    ----------
    occupancy : pandas.Series
        Binary occupancy observations at 5-minute intervals.
    steps : int, default=6
        Number of 5-minute steps into the future.

    Returns
    -------
    pandas.Series
        Future occupancy values aligned with current timestamps.
    """
    if steps < 0:
        raise ValueError("Future steps must be non-negative.")

    return occupancy.shift(-steps)


def get_historical_occupancy(occupancy, minutes):
    """
    Retrieve historical occupancy using exact timestamps.

    Parameters
    ----------
    occupancy : pandas.Series
        Occupancy observations indexed by timestamps.
    minutes : int
        Number of minutes before each observation.

    Returns
    -------
    pandas.Series
        Historical occupancy values aligned with current timestamps.
    """
    past_times = occupancy.index - pd.Timedelta(minutes=minutes)

    return pd.Series(
        occupancy.reindex(past_times).to_numpy(),
        index=occupancy.index
    )
