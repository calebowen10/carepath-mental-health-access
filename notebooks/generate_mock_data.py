import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# Number of fake intake records
n = 1000

# Possible values
age_groups = ["13-17", "18-24", "25-34", "35-44", "45-54", "55+"]
counties = ["Hartford", "New Haven", "Fairfield", "Middlesex", "New London", "Litchfield", "Tolland", "Windham"]
presenting_needs = [
    "Anxiety/stress",
    "Depression/mood",
    "Crisis/safety",
    "Family conflict",
    "Substance-related concern",
    "School/work stress",
    "Trauma-related concern"
]
preferred_support_types = ["Telehealth", "In-person therapy", "Peer support", "Crisis support", "Care navigator", "Self-guided resources"]
referral_statuses = ["Completed", "Pending", "Abandoned", "Referred elsewhere", "No response"]

# Date range
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 6, 30)
date_range_days = (end_date - start_date).days

rows = []

for i in range(1, n + 1):
    intake_date = start_date + timedelta(days=random.randint(0, date_range_days))

    presenting_need = random.choice(presenting_needs)

    # Simple urgency logic
    if presenting_need == "Crisis/safety":
        urgency_level = random.choices(
            ["High", "Moderate"],
            weights=[85, 15]
        )[0]
    elif presenting_need in ["Depression/mood", "Trauma-related concern", "Substance-related concern"]:
        urgency_level = random.choices(
            ["Moderate", "High", "Low"],
            weights=[65, 20, 15]
        )[0]
    else:
        urgency_level = random.choices(
            ["Low", "Moderate", "High"],
            weights=[55, 40, 5]
        )[0]

    # Barriers
    insurance_barrier = random.choices(["Yes", "No"], weights=[25, 75])[0]
    transportation_barrier = random.choices(["Yes", "No"], weights=[20, 80])[0]
    digital_access_barrier = random.choices(["Yes", "No"], weights=[15, 85])[0]

    # Recommended support based on urgency
    if urgency_level == "High":
        recommended_support_level = random.choice(["Crisis line", "Mobile crisis", "Urgent behavioral health center", "Emergency support"])
        wait_time_days = random.randint(0, 2)
    elif urgency_level == "Moderate":
        recommended_support_level = random.choice(["Telehealth appointment", "Outpatient therapy", "Care navigator follow-up", "Community behavioral health referral"])
        wait_time_days = random.randint(2, 14)
    else:
        recommended_support_level = random.choice(["Self-guided resources", "Peer support", "Routine appointment", "Digital check-in"])
        wait_time_days = random.randint(7, 30)

    days_to_first_contact = max(0, wait_time_days - random.randint(0, 3))

    # Referral status
    if urgency_level == "High":
        referral_status = random.choices(referral_statuses, weights=[55, 20, 10, 10, 5])[0]
    elif urgency_level == "Moderate":
        referral_status = random.choices(referral_statuses, weights=[45, 25, 15, 10, 5])[0]
    else:
        referral_status = random.choices(referral_statuses, weights=[35, 20, 25, 10, 10])[0]

    follow_up_completed = "Yes" if referral_status == "Completed" and random.random() < 0.75 else "No"

    # No-show risk
    barrier_count = [insurance_barrier, transportation_barrier, digital_access_barrier].count("Yes")
    if barrier_count >= 2 or referral_status in ["No response", "Abandoned"]:
        no_show_risk = random.choice(["High", "Moderate"])
    elif barrier_count == 1:
        no_show_risk = random.choice(["Moderate", "Low"])
    else:
        no_show_risk = random.choice(["Low", "Moderate"])

    rows.append({
        "user_id": f"U{i:04d}",
        "intake_date": intake_date.strftime("%Y-%m-%d"),
        "age_group": random.choice(age_groups),
        "county": random.choice(counties),
        "presenting_need": presenting_need,
        "urgency_level": urgency_level,
        "preferred_support_type": random.choice(preferred_support_types),
        "insurance_barrier": insurance_barrier,
        "transportation_barrier": transportation_barrier,
        "digital_access_barrier": digital_access_barrier,
        "recommended_support_level": recommended_support_level,
        "referral_status": referral_status,
        "days_to_first_contact": days_to_first_contact,
        "wait_time_days": wait_time_days,
        "follow_up_completed": follow_up_completed,
        "no_show_risk": no_show_risk
    })

df = pd.DataFrame(rows)

# Save the dataset
df.to_csv("data/mock_intake_data.csv", index=False)

print("Mock CarePath dataset created successfully.")
print(df.head())
