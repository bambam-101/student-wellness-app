import streamlit as st

# === Weekly Meal Plans for Each BMI Category ===
meal_plans = {
    "Underweight": [
        [
            "Mon: Tapsilog (100g beef tapa, 150g garlic rice, 1 egg)",
            "Tue: Beef steak with mashed potatoes (150g beef, 150g potatoes)",
            "Wed: Chicken adobo (150g chicken, 150g rice)",
            "Thu: Pork mechado (150g pork, 100g veggies, 1 cup rice)",
            "Fri: Beef kare-kare (150g beef, 150g veggies, bagoong)",
            "Sat: Fish paksiw (150g fish, 100g rice)",
            "Sun: Sisig with rice (100g pork sisig, 150g rice)"
        ] for _ in range(8)  # same menu weekly can be varied manually if desired
    ],
    "Normal weight": [
        [
            "Mon: Grilled chicken breast (150g) with salad (100g)",
            "Tue: Salmon fillet (150g) with quinoa (100g)",
            "Wed: Beef stir-fry (100g beef, 150g mixed veggies)",
            "Thu: Pork sinigang (150g pork, 150g veggies)",
            "Fri: Tofu vegetable soup (200ml, 150g tofu)",
            "Sat: Vegetable lasagna (150g)",
            "Sun: Turkey sandwich (100g turkey, 2 slices whole wheat bread)"
        ] for _ in range(8)
    ],
    "Overweight": [
        [
            "Mon: Vegetable soup (200ml) with tofu (100g)",
            "Tue: Grilled fish (150g) with steamed broccoli (100g)",
            "Wed: Chicken salad (150g chicken, 100g greens)",
            "Thu: Lentil stew (200ml lentils, 100g veggies)",
            "Fri: Zucchini noodles with pesto (150g)",
            "Sat: Egg white omelette (3 egg whites, veggies)",
            "Sun: Quinoa bowl (100g quinoa, 100g mixed veggies)"
        ] for _ in range(8)
    ],
    "Obese": [
        [
            "Mon: Cucumber and tomato salad (100g each)",
            "Tue: Steamed fish (150g) with asparagus (100g)",
            "Wed: Baked chicken breast (150g) with kale (100g)",
            "Thu: Broccoli soup (200ml) with tofu (100g)",
            "Fri: Cauliflower rice bowl (150g)",
            "Sat: Spinach and mushroom omelette (3 egg whites, 100g spinach)",
            "Sun: Zucchini and bell pepper stir-fry (150g)"
        ] for _ in range(8)
    ]
}

# Illness adjustments
illness_adjustments = {
    "Diabetes":    "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension":"Limit salt; use calamansi and herbs.",
    "Asthma":      "Include warm soups and breathing-friendly foods.",
    "Other":       "Follow medical dietary advice."
}

# === Base Fitness Plans for BMI Categories ===
base_plans = {
    "Underweight": [
        {"week":1, "focus":"Strength Building","recommendation":"3×12 deadlifts, 3×10 bench press","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":2, "focus":"Upper Body Strength","recommendation":"3×10 push-ups, 3×15 pull-downs","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":3, "focus":"Lower Body Strength","recommendation":"3×15 squats, 3×12 lunges","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":4, "focus":"Core Stability","recommendation":"3×20 planks, 3×15 leg raises","video":"https://youtu.be/T41mYCmtWls"},
        {"week":5, "focus":"Full Body","recommendation":"Circuit of 5 exercises, 3 rounds","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":6, "focus":"Strength Progression","recommendation":"Increase weight by 10% each exercise","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":7, "focus":"Mixed Strength","recommendation":"Super-sets of chest/back and legs","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":8, "focus":"Assessment","recommendation":"Test max reps for major lifts","video":"https://youtu.be/T41mYCmtWls"}
    ],
    "Normal weight": [
        {"week":1, "focus":"Cardio Endurance","recommendation":"30 min jog","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":2, "focus":"Strength","recommendation":"2×12 dumbbell rows, 2×15 squats","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":3, "focus":"HIIT","recommendation":"20 min interval sprints","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":4, "focus":"Flexibility","recommendation":"30 min yoga","video":"https://youtu.be/T41mYCmtWls"},
        {"week":5, "focus":"Mixed Cardio","recommendation":"Bike 20 min + swim 20 min","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":6, "focus":"Strength Maintenance","recommendation":"3×10 push-ups, pull-ups","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":7, "focus":"Core and Balance","recommendation":"Pilates 30 min","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":8, "focus":"Eval & Rest","recommendation":"Light activity and stretching","video":"https://youtu.be/T41mYCmtWls"}
    ],
    "Overweight": [
        {"week":1, "focus":"Low Impact Cardio","recommendation":"Elliptical 30 min","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":2, "focus":"Strength","recommendation":"2×15 bodyweight squats","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":3, "focus":"Cardio Intervals","recommendation":"Walk/jog 1 min intervals, 20 min","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":4, "focus":"Flexibility","recommendation":"20 min stretching","video":"https://youtu.be/T41mYCmtWls"},
        {"week":5, "focus":"Circuit","recommendation":"5 exercises, 3 rounds, low weight","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":6, "focus":"Core","recommendation":"3×20 crunches, 3×15 bridges","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":7, "focus":"Cardio Progression","recommendation":"Bike 40 min","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":8, "focus":"Assessment","recommendation":"Measure endurance improvement","video":"https://youtu.be/T41mYCmtWls"}
    ],
    "Obese": [
        {"week":1, "focus":"Gentle Movement","recommendation":"Seated marching 15 min","video":"https://youtu.be/T41mYCmtWls"},
        {"week":2, "focus":"Water Aerobics","recommendation":"30 min water workout","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":3, "focus":"Chair Exercises","recommendation":"2×15 chair squats, arm raises","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":4, "focus":"Stretching","recommendation":"Gentle full-body stretch 20 min","video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":5, "focus":"Low Impact Circuit","recommendation":"Walking + light weights","video":"https://youtu.be/T41mYCmtWls"},
        {"week":6, "focus":"Breathing & Core","recommendation":"Pursed-lip breathing + planks","video":"https://youtu.be/YKCy0HlH55M"},
        {"week":7, "focus":"Mixed Gentle","recommendation":"Pilates & yoga mix","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":8, "focus":"Eval","recommendation":"Track progress metrics","video":"https://youtu.be/jRWKYOhcWWU"}
    ]
}

# Specialized plans remain if conditions override
condition_plans = {
    # Example: Diabetes overrides for Overweight
    "Diabetes": {
        "Overweight": [
            {"week":1,"focus":"Blood Sugar Walk","recommendation":"Walk 20 min post-meal","video":"https://youtu.be/jRWKYOhcWWU"},
            # ... fill eight weeks as needed ...
        ]
    }
}

# Helpers

def adjust_meals(category, conditions):
    weeks = meal_plans.get(category, [])
    note = " ".join(illness_adjustments.get(c, "") for c in conditions if c!="None")
    return [{"week":i+1, "days":weeks[i], "note":note} for i in range(len(weeks))]


def adjust_fitness(category, conditions):
    for cond in conditions:
        if cond in condition_plans and category in condition_plans[cond]:
            return condition_plans[cond][category]
    plan = base_plans.get(category, [])
    if "Other" in conditions:
        for p in plan:
            p["recommendation"] += " 🩺 adapt intensity to condition"
    return plan

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
    import pandas as pd
    df = pd.DataFrame([ {"Week":f["week"],"Focus":f["focus"],"Recommendation":f["recommendation"],"Video":f["video"]} for f in fitness ])
