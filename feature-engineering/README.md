# Feature Engineering Explained Intuitively

## Hotel Booking Cancellation Prediction

Welcome to the GraphX Labs Feature Engineering project.

This project treats feature engineering as the hidden superpower behind great machine learning models.

Theme:

> Better features often matter more than better algorithms.

## Business Problem

Hotels lose revenue when bookings are canceled. If a hotel can identify bookings with high cancellation risk, it can improve inventory planning, staffing, pricing, and customer follow-up.

Target variable:

```text
is_canceled
```

- `1`: booking was canceled
- `0`: booking was not canceled

## Dataset

Dataset: Hotel Booking Demand dataset via TidyTuesday.

Raw file:

```text
feature-engineering/data/raw/hotel_bookings.csv
```

Processed file:

```text
feature-engineering/data/processed/hotel_bookings_feature_engineered.csv
```

## Why Feature Engineering Matters

Raw data is not always model-ready. Good feature engineering translates messy business reality into signals a model can learn from.

This project demonstrates:

- missing value handling
- categorical encoding
- scaling
- log transformations
- date feature engineering
- interaction features
- ratio features
- feature selection
- PCA intuition
- target leakage prevention

    ## Workflow

1. Load and inspect hotel booking data
2. Train a baseline model before feature engineering
3. Handle missing values
4. Encode categorical variables
5. Scale numerical features
6. Transform skewed variables
7. Create domain-inspired features
8. Remove leakage columns
9. Select useful features
10. Train an improved model
    11. Compare before vs after performance

    ## Baseline vs Improved Model

    Same model family: Logistic Regression.

    ```text
    Before feature engineering
    Accuracy:  0.8138
    Precision: 0.8086
    Recall:    0.6518
    F1-score:  0.7218
    ROC-AUC:   0.8899

    After feature engineering
    Accuracy:  0.8198
    Precision: 0.8124
    Recall:    0.6677
    F1-score:  0.7330
    ROC-AUC:   0.8979
    ```

    The improvement is not magic. The model sees cleaner, richer signals after feature engineering.

    ## Key Engineered Features

    - `total_nights`
    - `total_guests`
    - `weekend_share`
    - `adr_per_guest`
    - `special_requests_per_guest`
    - `lead_time_log`
    - `arrival_day_of_week`
    - `arrival_quarter`
    - `season`
    - `lead_time_x_total_nights`

## Medium Articles

Project article:

```text
articles/feature-engineering/feature_engineering_project_article.md
```

Interview article:

```text
articles/feature-engineering/feature_engineering_interview_questions.md
```

Built with care for the GraphX Labs ML Concepts Portfolio.
