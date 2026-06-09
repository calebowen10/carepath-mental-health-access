# Data Dictionary

This file defines the variables used in the mock CarePath intake dataset. The dataset is fully synthetic and does not contain real patient or client information.

| Variable | Description |
|---|---|
| user_id | Synthetic user ID for each intake record |
| intake_date | Date the user entered the CarePath intake flow |
| age_group | User age group |
| county | User county |
| presenting_need | Main reason the user is seeking support |
| urgency_level | General routing category: Low, Moderate, or High |
| preferred_support_type | User's preferred form of support |
| insurance_barrier | Whether the user reported insurance-related barriers |
| transportation_barrier | Whether the user reported transportation barriers |
| digital_access_barrier | Whether the user reported internet/device access barriers |
| recommended_support_level | Support option recommended by the routing framework |
| referral_status | Status of the referral after intake |
| days_to_first_contact | Number of days until first contact from support/service team |
| wait_time_days | Estimated wait time before receiving support |
| follow_up_completed | Whether follow-up was completed |
| no_show_risk | General no-show/drop-off risk category |
