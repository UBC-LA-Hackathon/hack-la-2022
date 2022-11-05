import pandas as pd
import os


def load_events_data(filepath):

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File: {filepath} not found")

    events_df = pd.read_csv(filepath, parse_dates=True)

    return events_df


def preprocess_events_data(events_df):

    # drop event__eventTime
    # membership role remove [""] symbols
    # remove type column, and event__eventType
    # deal with null membership role?

    return None
