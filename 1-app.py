import streamlit as st
import pandas as pd

# Days of the week
DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# === Meal items for each BMI category ===
# Underweight: 8 weeks of 7 distinct meals (manually defined)
under_week1 = [
    "Tapsilog (100g beef tapa, 150g garlic rice, 1 egg)",
    "Arroz caldo (200g rice porridge, 100g chicken, 1 egg)",
    "Pinakbet with pork (150g mixed veggies, 50g pork)",
    "Pork adobo (150g pork, 150g rice)",
    "Beef mechado (150g beef, 100g veggies, 150g rice)",
    "Chicken curry (150g chicken, 100g veggies, 150g rice)",
    "Lechon kawali (100g pork belly, 150g rice)"
]
under_week2 = [
    "Pancit canton with egg (150g)",
    "Longsilog (100g longganisa, 150g rice, 1 egg)",
    "Beef caldereta (150g beef, 100g vegetables)",
    "Kare-kare (150g oxtail, 100g veggies, bagoong)",
    "Binagoongang baboy (150g pork, 100g veggies)",
    "Bistek Tagalog (150g beef, 100g onions)",
    "Crispy pata (150g pork, 150g rice)"
]
under_week3 = [
    "Beef tapa with garlic rice (100g beef, 150g rice)",
    "Chicken inasal (150g chicken, 150g rice)",
    "Embutido (150g), steamed rice (150g)",
    "Pork barbecue skewers (150g)",
    "Kalderetang kambing (150g goat, 100g veggies)",
    "Chicken pastel (150g), rice (150g)",
    "Pork humba (150g), rice (150g)"
]
under_week4 = [
    "Lengua estofado (150g beef tongue, 100g veggies)",
    "Ribs adobo (150g pork ribs, 150g rice)",
    "Fish sinigang (150g fish, 150g veggies), rice (150g)",
    "Shrimp sinigang (150g shrimp, 150g veggies)",
    "Lechon manok (150g chicken, 150g rice)",
    "Pork mechado (150g pork, 100g veggies)",
    "Mixed grill platter (200g assorted meats)"
]
under_week5 = [
    "Seafood paella (200g rice, 100g seafood)",
    "Crab caldereta (150g crab, 100g veggies)",
    "Grilled tuna steak (150g)",
    "Fish escabeche (150g fish)",
    "Adobong dilis with rice (150g)",
    "Lechon kawali with gravy (150g pork)",
    "Beef salpicao (150g beef)"
]
under_week6 = [
    "Rack of lamb (150g) with rice (150g)",
    "Duck adobo (150g duck, 100g rice)",
    "Beef Wellington fusion (150g)",
    "Beef stroganoff (150g beef, 100g noodles)",
    "Pork hock soup (200ml)",
    "Chorizo with rice (150g)",
    "Beef gyro wrap (150g beef, 2 tortillas)"
]
under_week7 = [
    "Chicken shawarma (150g), rice (150g)",
    "Pork moussaka fusion (150g)",
    "Beef biryani (150g)",
    "Chicken biryani (150g)",
    "Lamb curry (150g)",
    "Mixed kebab platter (200g)",
    "Seafood mechado (150g seafood)"
]
under_week8 = [
    "Pancit palabok (150g)",
    "Lumpia Shanghai (6 pcs, 150g)",
    "Tokwa't baboy (150g tofu+pork)",
    "Sisig (150g)",
    "Dinuguan (150g)",
    "Chicken sopas (200ml)",
    "Beef noodle soup (200ml)"
]

# Normal weight: 56 unique meals generated programmatically as placeholders
normal_items = [
    "Grilled chicken salad (150g chicken, 100g greens)",
    "Salmon & asparagus (150g salmon, 100g asparagus)",
    "Beef stir-fry (100g beef, 150g veggies)",
    "Tofu vegetable soup (200ml, 150g tofu)",
    "Vegetable lasagna (150g)",
    "Turkey sandwich (100g turkey, 2 slices bread)",
    "Tuna poke bowl (150g tuna)",
    "Chicken Caesar wrap (150g)",
    "Quinoa & chickpea salad (150g)",
    "Greek yogurt parfait (200g)",
    "Shrimp stir fry (150g shrimp, 100g veggies)",
    "Veggie omelette (3 eggs, veggies)",
    "Pasta primavera (200g)",
    "Chicken kebabs (150g)",
    "Beef tacos (2 pcs)",
    "Veggie chili (200ml)",
    "Grilled shrimp skewers (150g)",
    "Spinach & feta omelette (3 eggs)",
    "Egg salad sandwich (150g)",
    "Mushroom risotto (200g)",
    "Caprese salad (150g)",
    "Avocado toast (2 slices)",
    "Chickpea curry (200ml)",
    "Sushi rolls (6 pcs)",
    "Fish tacos (2 pcs)",
    "Pork tenderloin & veggies (150g)",
    "Veggie burger (no bun)",
    "Frittata with veggies (150g)",
    "Salmon salad (150g)",
    "Chicken & quinoa bowl (150g)",
    "Beet & goat cheese salad (150g)",
    "Black bean salad (150g)",
    "Grilled veggie skewers (150g)",
    "Shrimp & quinoa salad (150g)",
    "Roast beef wrap (150g)",
    "Tabbouleh (150g)",
    "Falafel wrap (150g)",
    "Baked cod & veggies (150g)",
    "Veggie fajitas (150g)",
    "Pumpkin soup (200ml)",
    "Tofu stir fry (150g)",
    "Chicken fried rice (200g)",
    "Vegetable paella (200g)",
    "Spinach smoothie (200ml)",
    "Egg & veggie muffins (2 pcs)",
    "Cottage cheese & fruit (150g)",
    "Oatmeal & berries (150g)",
    "Lentil soup (200ml)",
    "Broccoli & cheese soup (200ml)",
    "Chorizo salad (150g)",
    "Pasta with veggie sauce (200g)",
    "Fish & veggie bake (200g)"
]

overweight_items = [f"Light Meal {i+1} (approx 200 kcal)" for i in range(56)]
obese_items      = [f"Gentle Meal {i+1} (approx 150 kcal)" for i in range(56)]

# Build meal_plans: 8 weeks of unique daily meals
meal_plans = {
    "Underweight": [under_week1, under_week2, under_week3, under_week4,
                     under_week5, under_week6, under_week7, under_week8],
    "Normal weight": [normal_items[i*7:(i+1)*7] for i in range(8)],
    "Overweight":    [overweight_items[i*7:(i+1)*7] for i in range(8)],
    "Obese":         [obese_items[i*7:(i+1)*7] for i in range(8)]
}

# Illness adjustments
illness_adjustments = {
    "Diabetes":    "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension":"Limit salt; use calamansi and herbs.",
    "Asthma":      "Include warm soups and breathing-friendly foods.",
    "Other":       "Follow medical dietary advice."
}

# === Base fitness plans per BMI category ===
base_plans = {
    "Underweight": [
        {"week":i+1,"focus":f"UW Week {i+1} Strength","recommendation":"3×12 reps heavy lifts","video":"https://youtu.be/IODxDxX7oi4"}
        for i in range(8)
    ],
    "Normal weight": [
        {"week":i+1,"focus":f"NW Week {i+1} Balanced","recommendation":"30 min cardio + 2×10 strength","video":"https://youtu.be/jRWKYOhcWWU"}
        for i in range(8)
    ],
    "Overweight": [
        {"week":i+1,"focus":f"OW Week {i+1} Low Impact","recommendation":"30 min elliptical","video":"https://youtu.be/YKCy0HlH55M"}
        for i in range(8)
    ],
    "Obese": [
        {"week":i+1,"focus":f"OB Week {i+1} Gentle","recommendation":"Seated marching 15 min","video":"https://youtu.be/T41mYCmtWls"}
        for i in range(8)
    ]
}

# Condition-specific overrides (optional)
condition_plans = {
    # Example: Diabetes override for Overweight
    "Diabetes": {
        "Overweight": [
            {"week":1,"focus":"Post-meal Walk","recommendation":"Walk 20 min","video":"https://youtu.be/jRWKYOhcWWU"},
            # ... fill through week 8 ...
        ]
    }
}

# === Helper functions ===

def adjust_meals(category, conditions):
    weeks = meal_plans[category]
    note = " ".join(illness_adjustments[c] for c in conditions if c in illness_adjustments)
    return [{"week":i+1, "days":weeks[i], "note":note} for i in range(8)]


def adjust_fitness(category, conditions):
    # use condition-specific if available
    for cond in conditions:
        if cond in condition_plans and category in condition_plans[cond]:
            return condition_plans[cond][category]
    plan = base_plans[category]
    if "Other" in conditions:
        for p in plan:
            p["recommendation"] += " 🩺 adapt intensity"
    return plan

# === Streamlit UI ===
st.set_page_config(page_title="B.E.A.T.", layout="centered")
st.title("B.E.A.T. – Body Evaluation and Activity Tracker")
st.markdown("An app promoting healthy lifestyles through BMI analysis and WHO-aligned plans.")

age = st.number_input("Age (years)", min_value=5, max_value=100, value=16)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=55.0, step=0.1)
height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=160.0, step=0.1)
conditions = st.multiselect("Health Conditions", ["Asthma","Diabetes","Hypertension","None","Other"], default=["None"])

if st.button("Compute 8-Week Plans"):
    h = height_cm/100
    bmi = weight/(h*h)
    if bmi<18.5:   category="Underweight"
    elif bmi<25:   category="Normal weight"
    elif bmi<30:   category="Overweight"
    else:          category="Obese"

    meals = adjust_meals(category, conditions)
    fitness = adjust_fitness(category, conditions)

    st.subheader(f"Your BMI: {bmi:.1f}")
    st.write(f"**Category:** {category}")

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
