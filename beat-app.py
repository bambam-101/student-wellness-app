import streamlit as st

# === Define Weekly Menus ===
uw_week1 = [
    "Tapsilog: 100g beef tapa, 150g garlic rice, 1 egg",
    "Arroz caldo: 200g rice porridge, 100g chicken, 1 egg",
    "Pinakbet with pork: 150g mixed veggies, 50g pork",
    "Pork adobo: 150g pork, 100g rice",
    "Beef mechado: 150g beef, 100g veggies",
    "Chicken curry: 150g chicken, 100g veggies, 50g rice",
    "Lechon kawali: 100g pork belly, 100g veggies, 1 cup rice"
]
uw_week2 = [
    "Fruit smoothie: 200ml mixed fruits, 50g oats",
    "Chicken tinola: 150g chicken, 100g rice, 50g veggies",
    "Beef sinigang: 150g beef, 100g veggies, 1 cup rice",
    "Grilled fish: 150g fish, 100g veggies",
    "Pork menudo: 150g pork, 100g veggies, 1 cup rice",
    "Vegetable stir-fry: 150g mixed veggies, 1 cup rice",
    "Beef kaldereta: 150g beef, 100g veggies"
]

nw_week1 = [
    "Chicken tinola: 150g chicken, 100g rice, 50g veggies",
    "Beef sinigang: 150g beef, 100g veggies, 1 cup rice",
    "Grilled fish: 150g fish, 100g veggies",
    "Pork menudo: 150g pork, 100g veggies, 1 cup rice",
    "Chicken adobo: 150g chicken, 100g veggies",
    "Vegetable stir-fry: 150g mixed veggies, 1 cup rice",
    "Vegetable omelette: 2 eggs, 100g mixed veggies"
]
nw_week2 = [
    "Tofu stir-fry: 150g tofu, 100g veggies",
    "Cauliflower rice bowl: 150g cauliflower, 100g veggies",
    "Green salad: 150g mixed greens",
    "Vegetable broth: 200ml clear broth",
    "Zucchini noodles: 150g zucchini, 50g tomato sauce",
    "Cucumber & tomato salad: 100g each",
    "Vegetable soup: 200ml broth, 100g mixed veggies"
]

ow_week1 = [
    "Chicken nilaga: 150g chicken, 100g veggies",
    "Pinakbet: 150g mixed veggies, 50g lean pork",
    "Fish sinigang: 150g fish, 100g veggies",
    "Vegetable soup: 200ml broth, 100g veggies",
    "Grilled chicken: 150g chicken, 100g salad",
    "Stir-fried greens: 150g leafy greens",
    "Tomato & cucumber salad: 100g each"
]
ow_week2 = [
    "Steamed fish: 150g fish, 100g veggies",
    "Lean pork adobo: 150g lean pork, 100g veggies",
    "Vegetable stir-fry: 150g mixed veggies, 1 cup rice",
    "Chicken broth: 200ml, 100g veggies",
    "Eggplant omelette: 2 eggs, 100g eggplant",
    "Lettuce wraps: 100g lettuce, 100g chicken",
    "Pumpkin soup: 200ml, 100g pumpkin"
]

ob_week1 = [
    "Vegetable soup: 200ml broth, 100g mixed veggies",
    "Steamed fish: 150g fish, 100g veggies",
    "Tofu stir-fry: 150g tofu, 100g veggies",
    "Cauliflower rice bowl: 150g cauliflower, 100g veggies",
    "Green salad: 150g mixed greens",
    "Vegetable broth: 200ml clear broth",
    "Zucchini noodles: 150g zucchini, 50g tomato sauce"
]
ob_week2 = [
    "Cucumber & tomato salad: 100g each",
    "Steamed chicken breast: 150g, 100g veggies",
    "Lentil soup: 200ml, 100g lentils",
    "Broccoli stir-fry: 150g broccoli",
    "Bell pepper salad: 100g each",
    "Mushroom soup: 200ml, 100g mushrooms",
    "Spinach omelette: 2 eggs, 100g spinach"
]

# Combine into 8-week plans
meal_plans = {
    "Underweight": [uw_week1, uw_week2] * 4,
    "Normal weight": [nw_week1, nw_week2] * 4,
    "Overweight": [ow_week1, ow_week2] * 4,
    "Obese": [ob_week1, ob_week2] * 4
}

# Illness adjustments
illness_adjustments = {
    "Diabetes":    "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension":"Limit salt; use calamansi and herbs.",
    "Asthma":      "Add papaya, sweet potato leaves, fatty fish.",
    "Other":       "Follow medical dietary advice."
}

# Fitness plans for each category
fitness_plans = {
    "Underweight": [
        {"week":i+1, "focus":"Week %d focus" % (i+1), "recommendation":"Recommend exercise %d" % (i+1), "video":"https://youtu.be/jRWKYOhcWWU"}
        for i in range(8)
    ],
    "Normal weight": [
        {"week":i+1, "focus":"Week %d focus" % (i+1), "recommendation":"Recommend exercise %d" % (i+1), "video":"https://youtu.be/jRWKYOhcWWU"}
        for i in range(8)
    ],
    "Overweight": [
        {"week":i+1, "focus":"Week %d focus" % (i+1), "recommendation":"Recommend exercise %d" % (i+1), "video":"https://youtu.be/jRWKYOhcWWU"}
        for i in range(8)
    ],
    "Obese": [
        {"week":i+1, "focus":"Week %d focus" % (i+1), "recommendation":"Recommend exercise %d" % (i+1), "video":"https://youtu.be/jRWKYOhcWWU"}
        for i in range(8)
    ]
}

# Helper functions

def adjust_meals(category, conditions):
    weeks = meal_plans.get(category, [])
    notes = " ".join(illness_adjustments[c] for c in conditions if c != "None")
    return [{"week":i+1, "days":weeks[i], "note":notes} for i in range(len(weeks))]


def adjust_fitness(category, conditions):
    plan = fitness_plans.get(category, []).copy()
    if any(c != "None" for c in conditions):
        for p in plan:
            p["recommendation"] += " 🩺 adapt intensity."
    return plan

# Streamlit UI
st.set_page_config(page_title="B.E.A.T.", layout="centered")
st.title("B.E.A.T. – Body Evaluation and Activity Tracker")
st.markdown("An app promoting healthy lifestyles through BMI analysis and WHO-aligned fitness programs.")

age = st.number_input("Age (years)", min_value=5, max_value=100, value=16)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=55.0, step=0.1)
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=160.0, step=0.1)

conditions = st.multiselect(
    "Select Health Conditions", ["Asthma", "Diabetes", "Hypertension", "None", "Other"], default=["None"]
)

if st.button("Compute 8-Week Plans"):
    h_m = height / 100.0
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

    st.markdown("### 8-Week Meal Plan (Daily Meals)")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for wk in meals:
        st.write(f"**Week {wk['week']}**")
        for idx, meal in enumerate(wk["days"]):
            st.write(f"- {days[idx]}: {meal}")
        if wk["note"]:
            st.info(f"Note: {wk['note']}")

    st.markdown("### 8-Week Fitness Plan")
    fitness_table = [
        {"Week": f["week"], "Focus": f["focus"], "Recommendation": f["recommendation"], "Video": f"[Link]({f['video']})"}
        for f in fitness
    ]
    st.table(fitness_table)
