import streamlit as st
import pandas as pd

# Days of the week
DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# === Weekly Meal Plans (unchanged) ===
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
meal_plans = {cat: [[f"{DAYS[d]}: {meals[(d + w) % 7]}" for d in range(7)] for w in range(8)] for cat, meals in meal_bases.items()}
illness_adjustments = {
    "Diabetes":    "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension":"Limit salt; use calamansi and herbs.",
    "Asthma":      "Include warm soups and breathing-friendly foods.",
    "Other":       "Follow medical dietary advice."
}

# === Weekly Fitness Plans with Video Links ===
# Each tuple is (exercise_description, video_url)
fitness_bases = {
    "Underweight": [
        ("Bodyweight squats 3×15", "https://youtu.be/IODxDxX7oi4"),
        ("Push-ups 3×12", "https://youtu.be/jRWKYOhcWWU"),
        ("Deadlifts 3×10", "https://youtu.be/YKCy0HlH55M"),
        ("Lunges 3×12", "https://youtu.be/T41mYCmtWls"),
        ("Planks 3×60s", "https://youtu.be/IODxDxX7oi4"),
        ("Overhead press 3×10", "https://youtu.be/jRWKYOhcWWU"),
        ("Pull-ups 3×8", "https://youtu.be/YKCy0HlH55M")
    ],
    "Normal weight": [
        ("Jog 30 min", "https://youtu.be/jRWKYOhcWWU"),
        ("Dumbbell rows 3×12", "https://youtu.be/IODxDxX7oi4"),
        ("HIIT 20 min", "https://youtu.be/YKCy0HlH55M"),
        ("Yoga 30 min", "https://youtu.be/T41mYCmtWls"),
        ("Bike 20 min", "https://youtu.be/jRWKYOhcWWU"),
        ("Push-ups 2×15", "https://youtu.be/IODxDxX7oi4"),
        ("Pilates 30 min", "https://youtu.be/YKCy0HlH55M")
    ],
    "Overweight": [
        ("Elliptical 30 min", "https://youtu.be/YKCy0HlH55M"),
        ("Bodyweight squats 3×15", "https://youtu.be/IODxDxX7oi4"),
        ("Walk/jog intervals 20 min", "https://youtu.be/jRWKYOhcWWU"),
        ("Stretching 20 min", "https://youtu.be/T41mYCmtWls"),
        ("Low-weight circuit 3 rounds", "https://youtu.be/YKCy0HlH55M"),
        ("Crunches 3×20", "https://youtu.be/IODxDxX7oi4"),
        ("Stationary bike 40 min", "https://youtu.be/jRWKYOhcWWU")
    ],
    "Obese": [
        ("Seated marching 15 min", "https://youtu.be/T41mYCmtWls"),
        ("Water aerobics 30 min", "https://youtu.be/YKCy0HlH55M"),
        ("Chair squats 3×15", "https://youtu.be/IODxDxX7oi4"),
        ("Gentle stretch 20 min", "https://youtu.be/jRWKYOhcWWU"),
        ("Walk + light weights 20 min", "https://youtu.be/T41mYCmtWls"),
        ("Pursed-lip breathing 5 min", "https://youtu.be/YKCy0HlH55M"),
        ("Gentle yoga 30 min", "https://youtu.be/IODxDxX7oi4")
    ]
}
# Rotate to 8 weeks
fitness_plans = {
    cat: [[
        f"{DAYS[d]}: [{ex}]({vid})"
        for d, (ex, vid) in enumerate([base[(d + w) % 7] for d, base in enumerate([fitness_bases[cat]]*7)])
    ] for w in range(8)]
    for cat in fitness_bases
}

# Helper functions

def adjust_meals(category, conditions):
    weeks = meal_plans[category]
    note = " ".join(illness_adjustments[c] for c in conditions if c in illness_adjustments)
    return [{"week": w+1, "days": weeks[w], "note": note} for w in range(8)]


def adjust_fitness(category, conditions):
    return fitness_plans[category]

# Streamlit UI
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
    fitness_df = pd.DataFrame(fitness, index=[f"Week {i+1}" for i in range(8)])
    fitness_df.columns = DAYS
    st.write("*Click links to view exercise videos* ")
    st.table(fitness_df)
