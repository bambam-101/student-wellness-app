import streamlit as st
import pandas as pd

# Days of the week
DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# Base meal lists per BMI category (7 distinct meals)
under_base = [
    "Tapsilog (100g beef tapa, 150g garlic rice, 1 egg)",
    "Arroz caldo (200g rice porridge, 100g chicken, 1 egg)",
    "Pinakbet with pork (150g mixed veggies, 50g pork)",
    "Pork adobo (150g pork, 150g rice)",
    "Beef mechado (150g beef, 100g veggies, 150g rice)",
    "Chicken curry (150g chicken, 100g veggies, 150g rice)",
    "Lechon kawali (100g pork belly, 150g rice)"
]
normal_base = [
    "Grilled chicken (150g) + salad (100g mixed greens)",
    "Salmon fillet (150g) + quinoa (100g)",
    "Beef stir-fry (100g beef, 150g veggies)",
    "Pork sinigang (150g pork, 150g veggies)",
    "Tofu vegetable soup (200ml, 150g tofu)",
    "Vegetable lasagna (150g)",
    "Turkey sandwich (100g turkey, 2 slices whole wheat bread)"
]
over_base = [
    "Vegetable soup (200ml) + tofu (100g)",
    "Grilled fish (150g) + steamed broccoli (100g)",
    "Chicken salad (150g chicken, 100g greens)",
    "Lentil stew (200ml lentils, 100g veggies)",
    "Zucchini noodles with pesto (150g)",
    "Egg white omelette (3 egg whites, vegetables)",
    "Quinoa bowl (100g quinoa, 100g veggies)"
]
obese_base = [
    "Cucumber & tomato salad (100g each)",
    "Steamed fish (150g) + asparagus (100g)",
    "Baked chicken breast (150g) + kale (100g)",
    "Broccoli soup (200ml) + tofu (100g)",
    "Cauliflower rice bowl (150g)",
    "Spinach & mushroom omelette (3 egg whites, 100g spinach)",
    "Zucchini & bell pepper stir-fry (150g)"
]

# Generate 8 unique weekly menus by rotating base lists
meal_plans = {
    category: [
        [f"{DAYS[j]}: {meal}" for j, meal in enumerate(base[i:] + base[:i])]
        for i in range(8)
    ]
    for category, base in {
        "Underweight": under_base,
        "Normal weight": normal_base,
        "Overweight": over_base,
        "Obese": obese_base
    }.items()
}

# Illness adjustments for meal notes
illness_adjustments = {
    "Diabetes":    "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension":"Limit salt; use calamansi and herbs.",
    "Asthma":      "Include warm soups and breathing-friendly foods.",
    "Other":       "Follow medical dietary advice."
}

# Base fitness plans per BMI category (distinct per week)
base_plans = {
    "Underweight": [
        {"week":1,"focus":"Strength Building","recommendation":"3×12 deadlifts","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":2,"focus":"Upper Body","recommendation":"3×10 bench press","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":3,"focus":"Lower Body","recommendation":"3×15 squats","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":4,"focus":"Core Stability","recommendation":"3×20 planks","video":"https://youtu.be/T41mYCmtWls"},
        {"week":5,"focus":"Full Body","recommendation":"Circuit training 3 rounds","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":6,"focus":"Progressive Overload","recommendation":"Increase weights 10%","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":7,"focus":"Mixed Strength","recommendation":"Supersets of push/pull","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":8,"focus":"Assessment","recommendation":"Max rep test","video":"https://youtu.be/T41mYCmtWls"}
    ],
    "Normal weight": [
        {"week":1,"focus":"Cardio Endurance","recommendation":"30 min jog","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":2,"focus":"Strength","recommendation":"2×12 dumbbell rows","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":3,"focus":"HIIT","recommendation":"20 min intervals","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":4,"focus":"Flexibility","recommendation":"30 min yoga","video":"https://youtu.be/T41mYCmtWls"},
        {"week":5,"focus":"Mixed Cardio","recommendation":"Bike+Swim combo","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":6,"focus":"Strength Maintenance","recommendation":"3×10 push-ups","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":7,"focus":"Core/Balance","recommendation":"Pilates 30 min","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":8,"focus":"Active Recovery","recommendation":"Light stretching","video":"https://youtu.be/T41mYCmtWls"}
    ],
    "Overweight": [
        {"week":1,"focus":"Low Impact Cardio","recommendation":"Elliptical 30 min","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":2,"focus":"Bodyweight Strength","recommendation":"3×15 squats","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":3,"focus":"Walk/Jog","recommendation":"1-min intervals 20 min","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":4,"focus":"Flexibility","recommendation":"20 min stretch","video":"https://youtu.be/T41mYCmtWls"},
        {"week":5,"focus":"Circuit","recommendation":"Low weight circuit","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":6,"focus":"Core","recommendation":"3×20 crunches","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":7,"focus":"Cardio Progression","recommendation":"Bike 40 min","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":8,"focus":"Assessment","recommendation":"Track endurance","video":"https://youtu.be/T41mYCmtWls"}
    ],
    "Obese": [
        {"week":1,"focus":"Gentle Movement","recommendation":"Seated marching 15 min","video":"https://youtu.be/T41mYCmtWls"},
        {"week":2,"focus":"Water Aerobics","recommendation":"30 min water workout","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":3,"focus":"Chair Exercises","recommendation":"2×15 chair squats","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":4,"focus":"Stretching","recommendation":"Gentle full-body stretch","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":5,"focus":"Low Impact Circuit","recommendation":"Walking+light weights","video":"https://youtu.be/T41mYCmtWls"},
        {"week":6,"focus":"Breathing/Core","recommendation":"Pursed-lip breathing","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":7,"focus":"Gentle Yoga","recommendation":"30 min yoga","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":8,"focus":"Evaluation","recommendation":"Measure progress","video":"https://youtu.be/jRWKYOhcWWU"}
    ]
}

# Specialized condition overrides (example)
condition_plans = {
    "Diabetes": {
        "Overweight": [
            {"week":1,"focus":"Post-meal Walk","recommendation":"Walk 20 min","video":"https://youtu.be/jRWKYOhcWWU"},
            # ... up to week 8 ...
        ]
    }
}

# Helpers

def adjust_meals(category, conditions):
    weeks = meal_plans[category]
    note = " ".join(illness_adjustments.get(c, "") for c in conditions if c!="None")
    return [{"week":i+1, "days":weeks[i], "note":note} for i in range(8)]


def adjust_fitness(category, conditions):
    for cond in conditions:
        if cond in condition_plans and category in condition_plans[cond]:
            return condition_plans[cond][category]
    plan = base_plans[category]
    if "Other" in conditions:
        for p in plan:
            p["recommendation"] += " 🩺 adapt intensity"
    return plan

# Streamlit UI
st.set_page_config(page_title="B.E.A.T.", layout="centered")
st.title("B.E.A.T. – Body Evaluation and Activity Tracker")
st.markdown("An app promoting healthy lifestyles through BMI analysis and WHO-aligned plans.")

age     = st.number_input("Age (years)",   min_value=5,   max_value=100, value=16)
weight  = st.number_input("Weight (kg)",   min_value=10., max_value=200., value=55., step=0.1)
height_cm = st.number_input("Height (cm)", min_value=50.,  max_value=250., value=160., step=0.1)
conditions = st.multiselect("Health Conditions", ["Asthma","Diabetes","Hypertension","None","Other"], default=["None"])

if st.button("Compute 8-Week Plans"):
    h = height_cm/100
    bmi = weight/(h*h)
    if bmi<18.5:       cat="Underweight"
    elif bmi<25:       cat="Normal weight"
    elif bmi<30:       cat="Overweight"
    else:              cat="Obese"

    meals   = adjust_meals(cat, conditions)
    fitness = adjust_fitness(cat, conditions)

    st.subheader(f"Your BMI: {bmi:.1f}")
    st.write(f"**Category:** {cat}")

    st.markdown("### 8-Week Meal Plan")
    for wk in meals:
        st.write(f"**Week {wk['week']}**")
        for d in wk['days']:
            st.write(f"- {d}")
        if wk['note']:
            st.info(f"Note: {wk['note']}")

    st.markdown("### 8-Week Fitness Plan")
    df = pd.DataFrame(fitness)
    st.table(df)
