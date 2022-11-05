import pandas as pd
import os
import datetime as dt
from scipy.stats import norm


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
        "event__actor_type",  # all same values
        "membership_type",  # all non-null values but equal
    ]

    clean_events_df.drop(columns=drop_columns)

    # membership role remove [""] symbols
    clean_events_df["membership_role"] = (
        clean_events_df.membership_role.str.replace('"', "", regex=True)
        .str.replace("[", "", regex=True)
        .str.replace("]", "", regex=True)
    )

    clean_events_df["actor_id"] = clean_events_df.actor_id.str.replace(
        "[", "", regex=True
    ).str.replace("]", "", regex=True)

    clean_events_df["event_time"] = pd.to_datetime(
        clean_events_df.event_time, utc=True
    ).dt.tz_convert(
        "Europe/Berlin"
    )  # .dt.tz_convert("America/Tijuana")

    clean_events_df.rename(columns={"actor_id": "student"}, inplace=True)

    # deal with null membership role?

    return clean_events_df


def group_by_session_data(clean_events_df):

    session_df = clean_events_df.groupby("session_id", as_index=False).agg(
        num_events=("type", "count"),
        student=("student", lambda x: x.value_counts().index[0]),  # most common value
        membership_role=(
            "membership_role",
            lambda x: x.value_counts().index[0],
        ),  # most common value
        session_start=("event_time", "min"),
        session_end=("event_time", "max"),
        object_interactions=(
            "event__object_extensions_asset_name",
            lambda x: x.unique(),
        ),
        image_interactions=(
            "event__object_extensions_asset_name",
            lambda x: x.str.contains("image").sum(),
        ),
        discussion_interactions=(
            "event__object_extensions_asset_name",
            lambda x: x.str.contains("Discussion").sum(),
        ),
        assignment_interactions=(
            "event__object_extensions_asset_name",
            lambda x: x.str.contains("Assignment").sum(),
        ),
        reading_interactions=(
            "event__object_extensions_asset_name",
            lambda x: x.str.contains("Reading").sum(),
        ),
        overview_interactions=(
            "event__object_extensions_asset_name",
            lambda x: x.str.contains("Overview").sum(),
        ),
        other_interactions=(
            "event__object_extensions_asset_name",
            lambda x: sum(
                x.str.contains("image|Overview|Discussion|Assignment|Reading|Overview")
                == False
            ),
        ),
    )

    session_df["session_duration_min"] = (
        session_df.session_end - session_df.session_start
    ).astype("timedelta64[m]")

    session_df.loc[session_df.session_duration_min > 50000, "session_duration_min"] = 0

    return session_df


def timeframe_event_summary(session_df, start_date, end_date):

    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]

    summary_df = session_df.copy(deep=True)

    summary_df = summary_df[
        (summary_df.session_start.dt.date > start_date)
        & (summary_df.session_start.dt.date < end_date)
    ]

    summary_df = summary_df.groupby("student", as_index=False).agg(
        total_events=("num_events", "sum"),
        total_discussion_events=("discussion_interactions", "sum"),
        total_assignment_events=("assignment_interactions", "sum"),
        total_image_events=("image_interactions", "sum"),
        total_overview_events=("overview_interactions", "sum"),
        total_reading_events=("reading_interactions", "sum"),
        # total_session_duration = ("session_duration_min", "sum"),
    )

    # remove image events fromtotal events as they are erroneous
    summary_df.total_events = summary_df.total_events - summary_df.total_image_events
    summary_df.drop(columns=["total_image_events"], inplace=True)

    # remove intructor/null students
    summary_df = summary_df[summary_df.student.str.contains("LEARNER")]

    for col in summary_df.select_dtypes(include=numerics).columns:

        summary_df[f"{col}__mean"] = summary_df[col].mean()
        summary_df[f"{col}__stdev"] = summary_df[col].std()
        summary_df[f"{col}__perc"] = summary_df.apply(
            lambda x: norm(loc=x[f"{col}__mean"], scale=x[f"{col}__stdev"]).cdf(x[col]),
            axis=1,
        )

    perc_columns = summary_df.columns[summary_df.columns.str.contains("__perc")]

    summary_df["avg_percentile"] = summary_df[perc_columns].mean(axis=1)

    return summary_df
