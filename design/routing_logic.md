# Routing Logic

CarePath uses simple, non-diagnostic routing rules to recommend general support pathways. The goal is not to diagnose users. The goal is to reduce confusion and help users understand what kind of support may be appropriate.

## Basic Urgency Logic

The system checks for the highest level of need first.

### Rule 1: High Urgency

If the user reports crisis indicators or safety concerns, route to **High Urgency**.

Examples:
- User says they feel unsafe
- User reports crisis-level distress
- User says they need urgent help
- User cannot wait for routine support

Recommended options:
- Crisis line
- Mobile crisis support
- Urgent behavioral health center
- Emergency support

---

### Rule 2: Moderate Urgency

If there are no crisis indicators, but the user reports persistent distress, trouble functioning, worsening symptoms, or limited support, route to **Moderate Urgency**.

Examples:
- User has been struggling for multiple days/weeks
- User says symptoms are affecting work, school, or home life
- User has limited support
- User wants help soon, but does not report immediate danger

Recommended options:
- Outpatient therapy
- Telehealth appointment
- Care navigator follow-up
- Community behavioral health referral

---

### Rule 3: Low Urgency

If the user does not report crisis indicators or persistent functional difficulty, route to **Low Urgency**.

Examples:
- User reports stress
- User reports mild anxiety or mood concerns
- User wants coping tools
- User wants routine support

Recommended options:
- Self-guided resources
- Peer support
- Routine appointment
- Digital check-in

## Access Barrier Logic

After CarePath identifies urgency level, the system checks for access barriers. These barriers help adjust the recommended support option.

### Transportation Barrier

If the user reports a transportation barrier, prioritize:
- Telehealth
- Phone-based support
- Local/mobile options
- Services close to the user

### Digital Access Barrier

If the user reports limited internet, device access, or difficulty using online tools, prioritize:
- Phone-based support
- In-person support
- Care navigator outreach
- Simple low-tech resources

### Insurance Barrier

If the user reports an insurance barrier, prioritize:
- Community mental health resources
- Low-cost options
- Sliding-scale providers
- Public programs
- Care navigator support

### Peer Support Preference

If the user prefers peer support, include:
- Peer support groups
- Community-based support
- Support groups
- Warmline or non-crisis peer resources

## Example User Scenarios

### Example 1

User reports mild stress, no safety concern, and wants coping tools.

Routing:
- Urgency level: Low
- Recommended support: Self-guided resources and digital check-in

### Example 2

User reports worsening anxiety, trouble functioning at work, and limited support.

Routing:
- Urgency level: Moderate
- Recommended support: Telehealth appointment or care navigator follow-up

### Example 3

User reports feeling unsafe and needing urgent support.

Routing:
- Urgency level: High
- Recommended support: Crisis line, mobile crisis, or urgent behavioral health support

### Example 4

User reports moderate distress but also has no transportation.

Routing:
- Urgency level: Moderate
- Access adjustment: Prioritize telehealth, phone support, or local/mobile options
