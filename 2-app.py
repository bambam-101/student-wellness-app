import streamlit as st
import pandas as pd

# Days of the week
DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# === Weekly Meal Plans (7 days × 8 weeks) ===
# Base meal lists per BMI category (7 distinct meals)
meal_bases = {
    "Underweight": [
        "Tapsilog (100g beef tapa, 150g garlic rice, 1 egg)",
        "Arroz caldo (200g rice porridge, 100g chicken, 1 egg)",
        "Pinakbet with pork (150g veggies, 50g pork)",
        "Pork adobo (150g pork, 150g rice)",
        "Beef mechado (150g beef, 100g veggies, 150g rice)",
        "Chicken curry (150g chicken, 100g veggies, 150g rice)",
        "Lechon kawali (100g pork belly, 150g rice)"
    ],
    "Normal weight": [
        "Grilled chicken breast (150g) + salad (100g)",
        "Salmon & asparagus (150g salmon, 100g asparagus)",
        "Beef stir-fry (100g beef, 150g veggies)",
        "Tofu veg soup (200ml, 150g tofu)",
        "Veg lasagna (150g)",
        "Turkey sandwich (100g turkey, 2 slices bread)",
        "Quinoa & chickpea salad (150g)"
    ],
    "Overweight": [
        "Veggie soup (200ml) + tofu (100g)",
        "Grilled fish (150g) + steamed broccoli (100g)",
        "Chicken salad (150g chicken, 100g greens)",
        "Lentil stew (200ml lentils, 100g veggies)",
        "Zucchini noodles (150g)",
        "Egg white omelette (3 egg whites, veggies)",
        "Quinoa bowl (100g quinoa, 100g veggies)"
    ],
    "Obese": [
        "Cucumber & tomato salad (100g each)",
        "Steamed fish (150g) + asparagus (100g)",
        "Baked chicken breast (150g) + kale (100g)",
        "Broccoli soup (200ml) + tofu (100g)",
        "Cauliflower rice bowl (150g)",
        "Spinach & mushroom omelette (3 egg whites, 100g spinach)",
        "Zucchini stir-fry (150g)"
    ]
}

# Generate 8-week meal plan by rotating each base list
meal_plans = {
    cat: [
        [f"{DAYS[d]}: {meals[(d + w) % 7]}" for d in range(7)]
        for w in range(8)
    ]
    for cat, meals in meal_bases.items()
}

# Illness adjustments for meal notes
illness_adjustments = {
    "Diabetes":    "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension":"Limit salt; use calamansi and herbs.",
    "Asthma":      "Include warm soups and breathing-friendly foods.",
    "Other":       "Follow medical dietary advice."
}

# === Weekly Fitness Plans (7 days × 8 weeks) ===
# Base exercise lists per BMI category
fitness_bases = {
    "Underweight": [
        "Bodyweight squats 3×15",
        "Push-ups 3×12",
        "Deadlifts 3×10",
        "Lunges 3×12",
        "Planks 3×60s",
        "Overhead press 3×10",
        "Pull-ups 3×8"
    ],
    "Normal weight": [
        "Jog 30 min",
        "Dumbbell rows 3×12",
        "High-intensity intervals 20 min",
        "Yoga 30 min",
        "Bike 20 min",
        "Push-ups 2×15",
        "Pilates 30 min"
    ],
    "Overweight": [
        "Elliptical 30 min",
        "Bodyweight squats 3×15",
        "Walk/jog intervals 1-min ×20",
        "Stretching 20 min",
        "Low-weight circuit 3 rounds",
        "Crunches 3×20",
        "Stationary bike 40 min"
    ],
    "Obese": [
        "Seated marching 15 min",
        "Water aerobics 30 min",
        "Chair squats 3×15",
        "Gentle full-body stretch 20 min",
        "Walking + light weights 20 min",
        "Pursed-lip breathing 5 min",
        "Gentle yoga 30 min"
    ]
}

# Generate 8-week fitness plan by rotating base exercises
fitness_plans = {
    cat: [
        [f"{DAYS[d]}: {exercises[(d + w) % 7]}" for d in range(7)]
        for w in range(8)
    ]
    for cat, exercises in fitness_bases.items()
}

# Condition-specific overrides (optional)
condition_plans = {
    "Diabetes": {
        "Overweight": [
            [
                "Mon: Post-meal walk 20 min",
                "Tue: Resistance band rows 2×15",
                "Wed: Stationary bike 20 min",
                "Thu: Light jog 15 min",
                "Fri: Seated leg lifts 3×15",
                "Sat: Yoga stretch 20 min",
                "Sun: Rest"
            ] + [[]],  # extend to 8 lists if desired
        ]
    }
}

# === Helper Functions ===

def adjust_meals(category, conditions):
    weeks = meal_plans[category]
    note = " ".join(illness_adjustments[c] for c in conditions if c in illness_adjustments)
    return [{"week": w+1, "days": weeks[w], "note": note} for w in range(8)]


def adjust_fitness(category, conditions):
    # condition override
    for cond in conditions:
        if cond in condition_plans and category in condition_plans[cond]:
            return condition_plans[cond][category]
    return fitness_plans[category]

# === Streamlit UI ===
st.set_page_config(page_title="B.E.A.T.", layout="centered")
st.title("B.E.A.T. – Body Evaluation and Activity Tracker")
st.markdown("An app promoting healthy lifestyles through BMI analysis and WHO-aligned plans.")

age = st.number_input("Age (years)", min_value=5, max_value=100, value=16)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=55.0, step=0.1)
height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=160.0, step=0.1)
conditions = st.multiselect(
    "Health Conditions",
    ["Asthma","Diabetes","Hypertension","None","Other"], default=["None"]
)

if st.button("Compute 8-Week Plans"):
    h = height_cm/100
    bmi = weight/(h*h)
    if bmi < 18.5:
        cat = "Underweight"
    elif bmi < 25:
        cat = "Normal weight"
    elif bmi < 30:
        cat = "Overweight"
    else:
        cat = "Obese"

    meals = adjust_meals(cat, conditions)
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
    # Display as table with days as columns
    fitness_df = pd.DataFrame(fitness, index=[f"Week {i+1}" for i in range(8)])
    fitness_df.columns = DAYS
    st.table(fitness_df)
