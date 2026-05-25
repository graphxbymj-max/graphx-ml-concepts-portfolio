# A/B Testing Interview Questions and Answers

## Conceptual Questions

### 1. What is A/B testing?

A/B testing is a controlled experiment where users are randomly split into two groups. One group sees the current version, called the control. The other sees a changed version, called the treatment. We compare outcomes like conversion rate to estimate whether the change actually helped.

The key idea is fairness. If assignment is random and the groups are comparable, then a meaningful difference in outcomes can be attributed to the treatment more confidently.

### 2. Why do businesses use A/B testing?

Businesses use A/B testing because opinions are unreliable. A button, page, headline, price, or feature can feel better in a meeting and still perform worse with real users.

A/B testing gives teams evidence before they roll changes out broadly. It reduces the risk of launching features that look good but hurt revenue, conversion, retention, or user trust.

### 3. What is a control group?

The control group is the baseline group. It receives the existing experience.

It answers the question: what would have happened if we changed nothing?

Without a control group, it is hard to know whether a performance change came from the product change, seasonality, marketing traffic, randomness, or something else happening in the business.

### 4. What is a treatment group?

The treatment group receives the new version being tested.

If the treatment group converts at a higher rate than the control group, the treatment may be better. But we still need statistical testing because random noise can create apparent differences even when nothing real changed.

### 5. What is a hypothesis?

A hypothesis is a testable claim about what might happen.

Example: changing the checkout CTA will increase conversion rate.

Good hypotheses are specific. They name the change, the expected direction, and the metric that matters.

### 6. What is a null hypothesis?

The null hypothesis says there is no real effect.

In an A/B test, the null might be: the new checkout page has the same conversion rate as the old checkout page.

We start from this skeptical position because experiments are noisy. The treatment has to provide enough evidence before we believe it changed anything.

### 7. What is a p-value?

A p-value tells us how surprising the observed result would be if the null hypothesis were true.

A small p-value means the observed difference would be unlikely under a no-effect world. It does not prove the treatment is good forever. It simply says the data is difficult to explain as random noise alone.

### 8. What is statistical significance?

Statistical significance means the result passed a chosen evidence threshold, often p < 0.05.

It is a guardrail against false excitement. It helps teams avoid launching changes just because one noisy sample happened to look promising.

### 9. What is a confidence interval?

A confidence interval is a range of plausible values for an unknown quantity, such as a conversion rate or treatment lift.

Instead of saying the lift is exactly 1.2 percentage points, we might say the plausible range is 0.3 to 2.1 percentage points. That range is often more useful for decision-making than the point estimate alone.

### 10. Why does randomness matter?

Randomness matters because user behavior varies naturally. Even if two experiences are identical, one group may convert slightly better by luck.

A/B testing is about separating random movement from meaningful signal.

## Practical Questions

### 1. How do you run an A/B test?

Start with a clear hypothesis and success metric. Randomly assign users to control and treatment. Run the experiment until the planned sample size or duration is reached. Check data quality and group balance. Calculate conversion rates, lift, confidence intervals, and statistical significance. Then interpret the result in business context.

### 2. How do you calculate conversion rate?

Conversion rate is:

```text
number of conversions / number of users exposed
```

If 1,100 out of 10,000 treatment users converted, the conversion rate is 11%.

### 3. What is lift?

Lift measures how much the treatment changed performance relative to the control.

Absolute lift is treatment rate minus control rate.

Relative lift is absolute lift divided by control rate.

### 4. Why does sample size matter?

Small samples are noisy. A tiny experiment can show a large difference just by luck.

Larger samples reduce uncertainty and make it easier to detect real effects. If the expected effect is small, the experiment needs more users.

### 5. What is statistical power?

Power is the probability that an experiment detects a real effect when that effect exists.

Low power means the test may miss good ideas. This creates false negatives: the business rejects a treatment that actually helps.

### 6. What are Type I and Type II errors?

A Type I error is a false positive: launching a treatment because the test says it worked, even though it did not.

A Type II error is a false negative: rejecting a treatment because the test does not detect an effect, even though the treatment really helps.

### 7. What is peeking bias?

Peeking bias happens when teams repeatedly check results during an experiment and stop as soon as they see significance.

This inflates false positives because noisy experiments often cross the significance line temporarily.

### 8. How do you detect experiment bias?

Check whether randomization produced balanced groups across traffic source, device, geography, time, and user type. Look for missing data, tracking bugs, unequal exposure, bot traffic, and users appearing in both groups.

The experiment result is only as trustworthy as the assignment and measurement process.

### 9. What happens if sample sizes are too small?

The experiment becomes unstable. Conversion rates swing around, confidence intervals are wide, and real effects may be missed.

Small tests are useful for instrumentation checks, but risky for high-stakes business decisions.

### 10. How do you interpret experiment results?

Look at statistical significance, confidence intervals, practical lift, business value, risk, and implementation cost.

A statistically significant result can still be too small to matter. A non-significant result can still be directionally interesting if the experiment was underpowered.

## Business Questions

### 1. Why can intuition be misleading?

Teams see the product from the inside. Users experience it quickly, emotionally, and in context. A change that seems clearer to a team may distract, confuse, or annoy users.

A/B testing gives the decision back to behavior instead of internal opinion.

### 2. How would you explain statistical significance to a stakeholder?

I would say: statistical significance helps us ask whether the observed improvement is likely to be real or could easily be random noise.

It does not guarantee the future, but it reduces the chance that we make a business decision based on a lucky sample.

### 3. Why are experiments critical in tech companies?

Tech companies change products constantly. Without experiments, they cannot reliably know which changes help and which hurt.

A/B testing turns product development into a learning system.

### 4. What are the dangers of bad experimentation?

Bad experiments create false confidence. They can lead teams to launch harmful features, reject useful ones, waste engineering time, misread customers, and optimize for short-term metrics while damaging long-term trust.
