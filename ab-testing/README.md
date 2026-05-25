# A/B Testing Explained Intuitively

## Teaching Businesses to Make Decisions With Evidence

Welcome to the A/B Testing project in the GraphX Labs ML Concepts Portfolio.

This project is built around one central idea:

> What if we could scientifically test whether a business decision actually works?

A/B testing is how modern product teams move from opinion to evidence. Instead of arguing about whether a new checkout design, email subject line, recommendation module, or onboarding flow is better, we run a controlled experiment and let user behavior answer.

---

# Business Problem

This project simulates an ecommerce checkout experiment.

The company wants to know whether a new checkout call-to-action improves conversions:

- **Control A:** old checkout CTA
- **Treatment B:** new secure checkout CTA

The business question is simple:

> Did the new checkout experience actually improve conversion, or did it just get lucky in this sample?

That question is the heartbeat of experimentation.

---

# Dataset

Dataset type:

```text
Simulated ecommerce checkout A/B test
```

Raw file:

```text
ab-testing/data/raw/checkout_ab_test_raw.csv
```

Processed file:

```text
ab-testing/data/processed/checkout_ab_test_processed.csv
```

Rows:

```text
50,000 users
```

Core fields:

- `user_id`
- `timestamp`
- `group`
- `variant`
- `device`
- `country`
- `traffic_source`
- `converted`
- `revenue`

Target outcome:

```text
converted
```

---

# Why A/B Testing Matters

Businesses are full of confident opinions.

A designer may believe the new page is clearer. A marketer may believe a headline is stronger. A product manager may believe a feature will increase activation.

But users do not always behave the way teams expect.

A/B testing protects the business from false confidence. It asks:

> Is this change truly better, or are we seeing random noise dressed up as progress?

---

# Experimentation Intuition

A/B testing compares two versions fairly:

- randomly assign users to groups
- keep everything else as equal as possible
- measure the outcome that matters
- quantify uncertainty
- make a decision based on evidence

It is the product analytics version of a clinical trial.

The control group tells us what would have happened under the old experience.

The treatment group tells us what happened under the new experience.

The difference is the estimated effect.

---

# Hypothesis Testing

The project introduces hypothesis testing without turning it into a formula dump.

The null hypothesis says:

> The new checkout CTA does not change conversion.

The alternative hypothesis says:

> The new checkout CTA changes conversion.

The p-value asks whether the observed difference would be surprising if the null hypothesis were true.

---

# Statistical Significance

Statistical significance helps separate meaningful signal from random fluctuation.

A small p-value does not mean the treatment is magically guaranteed to work forever. It means the observed difference is unlikely under the no-effect assumption.

That distinction matters because experiments are noisy.

---

# Confidence Intervals

A confidence interval gives a range of plausible values for the conversion rate or treatment effect.

Instead of pretending one number is perfect, it says:

> Here is the zone where the true effect likely lives.

That is often more useful for business decisions than a single score.

---

# Lift Analysis

Lift translates experimentation into business language.

The notebook calculates:

- control conversion rate
- treatment conversion rate
- absolute lift
- relative lift
- incremental conversions
- estimated revenue impact

A small percentage-point lift can matter enormously when applied to hundreds of thousands of monthly visitors.

---

# Practical Pitfalls

The project also covers real experimentation traps:

- peeking too early
- underpowered tests
- novelty effects
- seasonality
- selection bias
- multiple testing
- confusing statistical significance with business significance

These are the places where experiments can quietly lie.

---

# Project Files

```text
ab-testing/
├── data/
├── images/
├── notebooks/ab_testing_project.ipynb
├── reports/ab_testing_summary.md
├── src/
├── README.md
├── article_outline.md
├── interview_questions.md
└── requirements.txt
```

---

# Medium Articles

Companion article drafts live in:

```text
articles/ab-testing/
```

Included:

- `ab_testing_project_article.md`
- `ab_testing_interview_questions.md`
- `medium_publishing_notes.md`

---

# Key Learning

A/B testing is not just statistics.

It is the discipline of making decisions under uncertainty.

GraphX Labs takeaway:

> Opinions can start the conversation. Experiments decide what survives.
