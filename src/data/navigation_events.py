import pandas as pd
import os


def load_events_data(filepath):

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File: {filepath} not found")

    events_df = pd.read_csv(filepath, parse_dates=True)

    return events_df


def preprocess_events_data(events_df):

    clean_events_df = events_df.copy(deep=True)

    # drop event__eventTime, type, event__eventType, event__action, event__object_extensions_http_method, event__edApp_type, event__object_id_type
    drop_columns = [
        "event__eventTime",
        "type",
        "event__type",
        "event__action",
        "event__object_extensions_http_method",
        "event__edApp_type",
        "event__object_id_type",
    ]

    clean_events_df.drop(columns=drop_columns)

    # membership role remove [""] symbols
    clean_events_df["membership_role"] = (
        clean_events_df.membership_role.str.replace('"', "", regex=True)
        .str.replace("[", "", regex=True)
        .str.replace("]", "", regex=True)
    )

    clean_events_df["event_time"] = pd.to_datetime(clean_events_df.event_time)

    # deal with null membership role?

    return clean_events_df
