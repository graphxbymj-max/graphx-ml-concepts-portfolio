# Feature Engineering Project Summary

## Executive Summary

This project uses hotel booking cancellation data to show how feature engineering can improve machine learning performance and interpretability.

The goal is to compare a simple baseline model before feature engineering with an improved model after missing value handling, transformations, date features, interaction features, leakage prevention, and feature selection.

## Dataset

Hotel Booking Demand dataset via TidyTuesday.

## Target Variable

`is_canceled`

- `1`: booking canceled
- `0`: booking not canceled

    ## Baseline Model Performance

    Baseline Logistic Regression before feature engineering:

    ```text
    Accuracy:  0.8138
    Precision: 0.8086
    Recall:    0.6518
    F1-score:  0.7218
    ROC-AUC:   0.8899
    ```

    ## Improved Model Performance

    Logistic Regression after feature engineering and feature selection:

    ```text
    Accuracy:  0.8198
    Precision: 0.8124
    Recall:    0.6677
    F1-score:  0.7330
    ROC-AUC:   0.8979
    ```

    The model improves because the engineered dataset gives it stronger signals: stay length, guest intensity, arrival timing, skew-aware transformations, and business-inspired interactions.

## Engineered Features

Key engineered features include:

- `total_nights`
- `total_guests`
- `weekend_share`
- `adr_per_guest`
- `special_requests_per_guest`
- `lead_time_log`
- `adr_log`
- `arrival_day_of_week`
- `arrival_quarter`
- `season`
- `lead_time_x_total_nights`

    ## Leakage Discussion

    The project removes `reservation_status` and `reservation_status_date` because they reveal the booking outcome. It also removes `assigned_room_type` as a conservative choice because it may not be available at the original booking decision time.

    ## Key Findings

    - Feature engineering improved every major evaluation metric.
    - Log-transformed lead time helped reduce the impact of long-tail values.
    - Date-derived features added booking-timing signal.
    - Ratio and interaction features made guest and stay behavior more explicit.
    - Leakage prevention is just as important as feature creation.

## Limitations

- Feature engineering can overfit if too many features are created without validation.
- Domain assumptions should be checked with business experts.
- Some features may only be available at certain prediction moments.
- Feature importance does not prove causation.

## Future Improvements

- Add time-based train/test split
- Add cost-sensitive evaluation
- Compare multiple models after feature engineering
- Add permutation importance
- Add automated feature validation
