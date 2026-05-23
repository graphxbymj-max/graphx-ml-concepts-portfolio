"""Feature creation helpers for hotel booking cancellation modeling."""

import numpy as np
import pandas as pd

MONTH_MAP = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12,
}


def create_hotel_booking_features(df):
    """Create domain-inspired hotel booking features."""
    df = df.copy()
    df["children"] = df["children"].fillna(0)
    df["country"] = df["country"].fillna("Unknown")
    df["agent"] = df["agent"].fillna(0)
    df["company"] = df["company"].fillna(0)
    df["arrival_month_number"] = df["arrival_date_month"].map(MONTH_MAP)
    df["arrival_date"] = pd.to_datetime(
        dict(year=df["arrival_date_year"], month=df["arrival_month_number"], day=df["arrival_date_day_of_month"]),
        errors="coerce",
    )
    df["arrival_day_of_week"] = df["arrival_date"].dt.dayofweek
    df["arrival_is_weekend"] = df["arrival_day_of_week"].isin([5, 6]).astype(int)
    df["arrival_quarter"] = df["arrival_date"].dt.quarter
    df["total_nights"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]
    df["total_guests"] = (df["adults"] + df["children"] + df["babies"]).replace(0, 1)
    df["weekend_share"] = df["stays_in_weekend_nights"] / df["total_nights"].replace(0, 1)
    df["adr_per_guest"] = df["adr"] / df["total_guests"]
    df["special_requests_per_guest"] = df["total_of_special_requests"] / df["total_guests"]
    df["has_children"] = ((df["children"] + df["babies"]) > 0).astype(int)
    df["has_agent"] = (df["agent"] != 0).astype(int)
    df["has_company"] = (df["company"] != 0).astype(int)
    df["lead_time_log"] = np.log1p(df["lead_time"].clip(lower=0))
    df["adr_log"] = np.log1p(df["adr"].clip(lower=0))
    df["lead_time_x_total_nights"] = df["lead_time"] * df["total_nights"]
    df["requests_x_parking"] = df["total_of_special_requests"] * df["required_car_parking_spaces"]
    df["is_long_stay"] = (df["total_nights"] >= 7).astype(int)
    df["is_last_minute"] = (df["lead_time"] <= 7).astype(int)
    df["season"] = df["arrival_month_number"].map(
        lambda m: "winter" if m in [12, 1, 2] else "spring" if m in [3, 4, 5] else "summer" if m in [6, 7, 8] else "fall"
    )
    return df


def remove_leakage_columns(df):
    """Drop columns that leak booking outcome information."""
    leakage_columns = ["reservation_status", "reservation_status_date", "assigned_room_type", "arrival_date"]
    return df.drop(columns=[c for c in leakage_columns if c in df.columns])
