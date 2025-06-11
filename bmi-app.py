import streamlit as st

# === Define Weekly Menus ===
uw_week1 = [
    "Mon: Tapsilog (100g beef tapa, 150g garlic rice, 1 egg)",
    "Tue: Arroz caldo (200g rice porridge, 100g chicken, 1 egg)",
    "Wed: Pinakbet with pork (150g mixed veggies, 50g pork)",
    "Thu: Pork adobo (150g pork, 100g rice)",
    "Fri: Beef mechado (150g beef, 100g veggies)",
    "Sat: Chicken curry (150g chicken, 100g veggies, 50g rice)",
    "Sun: Lechon kawali (100g pork belly, 100g veggies, 1 cup rice)"
]
uw_week2 = [
    "Mon: Fruit smoothie (200ml mixed fruits, 50g oats)",
    "Tue: Chicken tinola (150g chicken, 100g rice, 50g veggies)",
    "Wed: Beef sinigang (150g beef, 100g veggies, 1 cup rice)",
    "Thu: Grilled fish (150g fish, 100g veggies)",
    "Fri: Pork menudo (150g pork, 100g veggies, 1 cup rice)",
    "Sat: Vegetable stir-fry (150g mixed veggies, 1 cup rice)",
    "Sun: Beef kaldereta (150g beef, 100g veggies)"
]
# Repeat or rotate for 8 weeks
meal_plans = {
    "Underweight": [uw_week1, uw_week2] * 4,
    "Normal weight": [uw_week1, uw_week2] * 4,
    "Overweight": [uw_week1, uw_week2] * 4,
    "Obese": [uw_week1, uw_week2] * 4
}

# Illness adjustments for meals
illness_adjustments = {
    "Diabetes":    "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension":"Limit salt; use calamansi and herbs.",
    "Asthma":      "Add papaya, sweet potato leaves, fatty fish.",
    "Other":       "Follow medical dietary advice."
}

# Base fitness plans by BMI category
base_plans = {
    "Underweight": [
        {"week":i+1, "focus":"Build Strength",     "recommendation":"Bodyweight squats 3×15, push-ups 3×10","video":"https://youtu.be/IODxDxX7oi4"}
        for i in range(8)
    ],
    "Normal weight": [
        {"week":i+1, "focus":"Maintain Fitness",  "recommendation":"Brisk walk 30 min daily","video":"https://youtu.be/jRWKYOhcWWU"}
        for i in range(8)
    ],
    "Overweight": [
        {"week":i+1, "focus":"Low-Impact Cardio","recommendation":"Stationary bike 30 min, 3×/week","video":"https://youtu.be/YKCy0HlH55M"}
        for i in range(8)
    ],
    "Obese": [
        {"week":i+1, "focus":"Gentle Movement",   "recommendation":"Seated marching 15 min daily","video":"https://youtu.be/T41mYCmtWls"}
        for i in range(8)
    ]
}

# Specialized plans for health conditions
condition_plans = {
    "Diabetes": {
        "Underweight": [
            {"week":1,"focus":"Gentle Walk","recommendation":"Walk 20 min daily","video":"https://youtu.be/jRWKYOhcWWU"},
            {"week":2,"focus":"Resistance Bands","recommendation":"2×15 light band rows","video":"https://youtu.be/iodxdxX7oi4"},
            # ... up to 8 weeks ...
        ],
        # ... other categories ...
    },
    "Hypertension": {
        "Overweight": [
            {"week":1,"focus":"Breathing Exercises","recommendation":"Diaphragmatic breathing 10 min","video":"https://youtu.be/abc"},
            # ...
        ],
        # ... other categories ...
    },
    "Asthma": {
        "Underweight": [
            {"week":1,"focus":"Breathing Drills","recommendation":"Pursed-lip breathing 5 min","video":"https://youtu.be/def"},
            # ...
        ],
        # ...
    }
}

# Function to select fitness plan based on BMI and condition

def adjust_fitness(category, conditions):
    # If a specialized plan exists for a condition, use it
    for cond in conditions:
        if cond in condition_plans:
            cat_plans = condition_plans[cond].get(category)
            if cat_plans:
                return cat_plans
    # Otherwise return base plan; append note if other condition
    plan = base_plans.get(category, [])
    if "Other" in conditions:
        for p in plan:
            p["recommendation"] += " 🩺 adapt intensity to condition."
    return plan

# Meal adjustment stays same

def adjust_meals(category, conditions):
    weeks = meal_plans.get(category, [])
    note = " ".join(illness_adjustments[c] for c in conditions if c!="None")
    return [{"week":i+1, "days":weeks[i], "note":note} for i in range(len(weeks))]

# Streamlit UI
st.set_page_config(page_title="B.E.A.T.", layout="centered")
st.title("B.E.A.T. – Body Evaluation and Activity Tracker")
st.markdown("An app promoting healthy lifestyles through BMI analysis and WHO-aligned fitness programs.")

age = st.number_input("Age (years)", min_value=5, max_value=100, value=16)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=55.0, step=0.1)
height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=160.0, step=0.1)
conditions = st.multiselect("Select Health Conditions", ["Asthma","Diabetes","Hypertension","None","Other"], default=["None"])

if st.button("Compute 8-Week Plans"):
    h = height_cm/100
    bmi = weight/(h*h)
    if bmi<18.5: category="Underweight"
    elif bmi<25: category="Normal weight"
    elif bmi<30: category="Overweight"
    else:        category="Obese"

    meals = adjust_meals(category, conditions)
    fitness = adjust_fitness(category, conditions)

    st.subheader(f"Your BMI: {bmi:.1f}")
    st.write(f"**Category:** {category}")

    st.markdown("### 8-Week Meal Plan (Daily Meals)")
    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for wk in meals:
        st.write(f"**Week {wk['week']}**")
        for i,meal in enumerate(wk['days']): st.write(f"- {days[i]}: {meal}")
        if wk['note']: st.info(f"Note: {wk['note']}")

    st.markdown("### 8-Week Fitness Plan")
    st.table([{"Week":f["week"],"Focus":f["focus"],"Recommendation":f["recommendation"],"Video":f"Link"} for f in fitness])
