import streamlit as st

# === Data ===
meal_plans = {
    "Underweight": [
        ["Tapsilog: 100g beef tapa, 150g garlic rice, 1 egg"],
        ["Arroz caldo: 200g rice porridge, 100g chicken, 1 egg"],
        ["Pinakbet with pork: 150g mixed veggies, 50g pork"],
        ["Pork adobo: 150g pork, 100g rice"],
        ["Beef mechado: 150g beef, 100g veggies"],
        ["Chicken curry: 150g chicken, 100g veggies, 50g rice"],
        ["Lechon kawali: 100g pork belly, 100g veggies, 1 cup rice"],
        ["Fruit smoothie: 200ml mixed fruits, 50g oats"]
    ],
    "Normal weight": [
        ["Chicken tinola: 150g chicken, 100g rice, 50g veggies"],
        ["Beef sinigang: 150g beef, 100g veggies, 1 cup rice"],
        ["Grilled fish: 150g fish, 100g veggies"],
        ["Pork menudo: 150g pork, 100g veggies, 1 cup rice"],
        ["Chicken adobo: 150g chicken, 100g veggies"],
        ["Vegetable stir-fry: 150g mixed veggies, 1 cup rice"],
        ["Beef kaldereta: 150g beef, 100g veggies"],
        ["Vegetable omelette: 2 eggs, 100g mixed veggies"]
    ],
    "Overweight": [
        ["Chicken nilaga: 150g chicken, 100g veggies"],
        ["Pinakbet: 150g mixed veggies, 50g lean pork"],
        ["Fish sinigang: 150g fish, 100g veggies"],
        ["Vegetable soup: 200ml broth, 100g veggies"],
        ["Grilled chicken: 150g chicken, 100g salad"],
        ["Stir-fried greens: 150g leafy greens"],
        ["Tomato and cucumber salad: 100g each"],
        ["Steamed fish: 150g fish, 100g veggies"]
    ],
    "Obese": [
        ["Vegetable soup: 200ml broth, 100g mixed veggies"],
        ["Steamed fish: 150g fish, 100g veggies"],
        ["Tofu stir-fry: 150g tofu, 100g veggies"],
        ["Cauliflower rice bowl: 150g cauliflower, 100g veggies"],
        ["Green salad: 150g mixed greens"],
        ["Vegetable broth: 200ml clear broth"],
        ["Zucchini noodles: 150g zucchini, 50g tomato sauce"],
        ["Cucumber and tomato salad: 100g each"]
    ]
}

illness_adjustments = {
    "Diabetes": "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension": "Limit salt; use calamansi and herbs.",
    "Asthma": "Add papaya, sweet potato leaves, fatty fish.",
    "Other": "Follow medical dietary advice."
}

fitness_plans = {
    "Underweight": [
        {"week":1, "focus":"Active Lifestyle",     "recommendation":"Walk 30 min daily",             "video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":2, "focus":"Strength & Flexibility","recommendation":"3×12 push-ups, 3×15 squats twice/week","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":3, "focus":"Cardio",               "recommendation":"Cycle or swim 30 min, 3×/week", "video":"https://youtu.be/YKCy0HlH55M"},
        {"week":4, "focus":"Flexibility",          "recommendation":"20 min yoga, 2×/week",          "video":"https://youtu.be/T41mYCmtWls"},
        {"week":5, "focus":"Strength Progression", "recommendation":"3×10 bench press, 3×12 deadlifts","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":6, "focus":"HIIT",                 "recommendation":"20 min HIIT, 3×/week",           "video":"https://youtu.be/YKCy0HlH55M"},
        {"week":7, "focus":"Pilates & Core",       "recommendation":"25 min Pilates, 2×/week",        "video":"https://youtu.be/T41mYCmtWls"},
        {"week":8, "focus":"Combined Routine",     "recommendation":"2 days cardio + 2 days strength","video":"https://youtu.be/jRWKYOhcWWU"}
    ],
    "Normal weight": [
        {"week":1, "focus":"Active Lifestyle", "recommendation":"Walk 30 min daily",            "video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":2, "focus":"Strength Basics",  "recommendation":"2×10 push-ups, 2×15 squats",  "video":"https://youtu.be/IODxDxX7oi4"},
        {"week":3, "focus":"Cardio",           "recommendation":"Jog 20 min, 3×/week",         "video":"https://youtu.be/YKCy0HlH55M"},
        {"week":4, "focus":"Flexibility",      "recommendation":"15 min stretching daily",    "video":"https://youtu.be/T41mYCmtWls"},
        {"week":5, "focus":"Strength Build",   "recommendation":"3×10 dumbbell rows",         "video":"https://youtu.be/IODxDxX7oi4"},
        {"week":6, "focus":"HIIT",             "recommendation":"15 min HIIT, 3×/week",        "video":"https://youtu.be/YKCy0HlH55M"},
        {"week":7, "focus":"Core & Balance",   "recommendation":"20 min core workout",        "video":"https://youtu.be/T41mYCmtWls"},
        {"week":8, "focus":"Mixed Routine",    "recommendation":"1 rest + 3 mixed days",      "video":"https://youtu.be/jRWKYOhcWWU"}
    ],
    "Overweight": [
        {"week":1, "focus":"Active Lifestyle",    "recommendation":"Walk 30 min daily",             "video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":2, "focus":"Low-Impact Strength", "recommendation":"2×10 chair squats, wall push-ups","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":3, "focus":"Cardio",              "recommendation":"Dance workout 30 min, 3×/week", "video":"https://youtu.be/YKCy0HlH55M"},
        {"week":4, "focus":"Flexibility",         "recommendation":"15 min yoga daily",             "video":"https://youtu.be/T41mYCmtWls"},
        {"week":5, "focus":"Strength",            "recommendation":"2×12 resistance band rows",     "video":"https://youtu.be/IODxDxX7oi4"},
        {"week":6, "focus":"HIIT",                "recommendation":"10 min low-impact HIIT",        "video":"https://youtu.be/YKCy0HlH55M"},
        {"week":7, "focus":"Core Stability",      "recommendation":"20 min plank & bridges",        "video":"https://youtu.be/T41mYCmtWls"},
        {"week":8, "focus":"Mixed Routine",       "recommendation":"2 cardio + 1 strength day",     "video":"https://youtu.be/jRWKYOhcWWU"}
    ],
    "Obese": [
        {"week":1, "focus":"Active Lifestyle", "recommendation":"Walk 20 min daily",             "video":"https://youtu.be/jRWKYOhcWWU"},
        {"week":2, "focus":"Seated Strength",  "recommendation":"2×10 seated leg lifts, arm raises","video":"https://youtu.be/IODxDxX7oi4"},
        {"week":3, "focus":"Gentle Cardio",    "recommendation":"Water aerobics 30 min",        "video":"https://youtu.be/YKCy0HlH55M"},
        {"week":4, "focus":"Flexibility",      "recommendation":"10 min gentle stretching",     "video":"https://youtu.be/T41mYCmtWls"},
        {"week":5, "focus":"Resistance Bands", "recommendation":"2×12 band pulls",               "video":"https://youtu.be/IODxDxX7oi4"},
        {"week":6, "focus":"HIIT Lite",        "recommendation":"5 min low-impact HIIT",        "video":"https://youtu.be/YKCy0HlH55M"},
        {"week":7, "focus":"Core & Balance",   "recommendation":"15 min seated core",           "video":"https://youtu.be/T41mYCmtWls"},
        {"week":8, "focus":"Mixed Routine",    "recommendation":"1 rest + 2 mixed days",        "video":"https://youtu.be/jRWKYOhcWWU"}
    ]
}

def adjust_meals(category, conditions):
    base = meal_plans.get(category, [])
    notes = " ".join(illness_adjustments[c] for c in conditions if c != "None")
    return [{"week": i+1, "items": items, "note": notes} for i, items in enumerate(base)]

def adjust_fitness(category, conditions):
    plan = fitness_plans.get(category, [])
    if any(c != "None" for c in conditions):
        for p in plan:
            p["recommendation"] += " 🩺 adapt intensity."
    return plan

# === Streamlit UI ===
st.set_page_config(page_title="B.E.A.T.", layout="centered")
st.title("B.E.A.T. – Body Evaluation and Activity Tracker")
st.markdown("An app promoting healthy lifestyles through BMI analysis and WHO-aligned fitness programs.")

age = st.number_input("Age (years)",   min_value=5,   max_value=100, value=16)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=55.0, step=0.1)
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=160.0, step=0.1)

conditions = st.multiselect(
    "Select Health Conditions",
    ["Asthma", "Diabetes", "Hypertension", "None", "Other"],
    default=["None"]
)

if st.button("Compute 8-Week Plans"):
    h_m = height / 100
    bmi = weight / (h_m * h_m)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    meals = adjust_meals(category, conditions)
    fitness = adjust_fitness(category, conditions)

    st.subheader(f"Your BMI: {bmi:.1f}")
    st.write(f"**Category:** {category}")

    st.markdown("### 8-Week Meal Plan")
    for wk in meals:
        st.write(f"**Week {wk['week']}:**")
        for item in wk["items"]:
            st.write(f"- {item}")
        if wk["note"]:
            st.info(f"Note: {wk['note']}")

    st.markdown("### 8-Week Fitness Plan")
    st.write("| Week | Focus               | Recommendation                                | Video |")
    st.write("|------|---------------------|-----------------------------------------------|-------|")
    for f in fitness:
        video_md = f"[Video]({f['video']})"
        st.write(f"| {f['week']}    | {f['focus']} | {f['recommendation']} | {video_md} |")
