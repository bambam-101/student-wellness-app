import streamlit as st

# === Data ===
# Weekly meal plans: each week has 7 different daily meals
meal_plans = {
    "Underweight": [
        [  # Week 1
            "Tapsilog: 100g beef tapa, 150g garlic rice, 1 egg",
            "Arroz caldo: 200g rice porridge, 100g chicken, 1 egg",
            "Pinakbet with pork: 150g mixed veggies, 50g pork",
            "Pork adobo: 150g pork, 100g rice",
            "Beef mechado: 150g beef, 100g veggies",
            "Chicken curry: 150g chicken, 100g veggies, 50g rice",
            "Lechon kawali: 100g pork belly, 100g veggies, 1 cup rice"
        ],
        [  # Week 2
            "Fruit smoothie: 200ml mixed fruits, 50g oats",
            "Chicken tinola: 150g chicken, 100g rice, 50g veggies",
            "Beef sinigang: 150g beef, 100g veggies, 1 cup rice",
            "Grilled fish: 150g fish, 100g veggies",
            "Pork menudo: 150g pork, 100g veggies, 1 cup rice",
            "Vegetable stir-fry: 150g mixed veggies, 1 cup rice",
            "Beef kaldereta: 150g beef, 100g veggies"
        ],
        [  # Week 3: rotate list
            "Beef mechado: 150g beef, 100g veggies",
            "Chicken curry: 150g chicken, 100g veggies, 50g rice",
            "Lechon kawali: 100g pork belly, 100g veggies, 1 cup rice",
            "Tapsilog: 100g beef tapa, 150g garlic rice, 1 egg",
            "Arroz caldo: 200g rice porridge, 100g chicken, 1 egg",
            "Pinakbet with pork: 150g mixed veggies, 50g pork",
            "Pork adobo: 150g pork, 100g rice"
        ],
        [  # Week 4
            "Fruit smoothie: 200ml mixed fruits, 50g oats",
            "Chicken tinola: 150g chicken, 100g rice, 50g veggies",
            "Beef sinigang: 150g beef, 100g veggies, 1 cup rice",
            "Grilled fish: 150g fish, 100g veggies",
            "Pork menudo: 150g pork, 100g veggies, 1 cup rice",
            "Vegetable stir-fry: 150g mixed veggies, 1 cup rice",
            "Beef kaldereta: 150g beef, 100g veggies"
        ],
        [  # Week 5 (repeat week1)
            "Tapsilog: 100g beef tapa, 150g garlic rice, 1 egg",
            "Arroz caldo: 200g rice porridge, 100g chicken, 1 egg",
            "Pinakbet with pork: 150g mixed veggies, 50g pork",
            "Pork adobo: 150g pork, 100g rice",
            "Beef mechado: 150g beef, 100g veggies",
            "Chicken curry: 150g chicken, 100g veggies, 50g rice",
            "Lechon kawali: 100g pork belly, 100g veggies, 1 cup rice"
        ],
        [  # Week 6 (repeat week2)
            "Fruit smoothie: 200ml mixed fruits, 50g oats",
            "Chicken tinola: 150g chicken, 100g rice, 50g veggies",
            "Beef sinigang: 150g beef, 100g veggies, 1 cup rice",
            "Grilled fish: 150g fish, 100g veggies",
            "Pork menudo: 150g pork, 100g veggies, 1 cup rice",
            "Vegetable stir-fry: 150g mixed veggies, 1 cup rice",
            "Beef kaldereta: 150g beef, 100g veggies"
        ],
        [  # Week 7 (repeat week3)
            "Beef mechado: 150g beef, 100g veggies",
            "Chicken curry: 150g chicken, 100g veggies, 50g rice",
            "Lechon kawali: 100g pork belly, 100g veggies, 1 cup rice",
            "Tapsilog: 100g beef tapa, 150g garlic rice, 1 egg",
            "Arroz caldo: 200g rice porridge, 100g chicken, 1 egg",
            "Pinakbet with pork: 150g mixed veggies, 50g pork",
            "Pork adobo: 150g pork, 100g rice"
        ],
        [  # Week 8 (repeat week4)
            "Fruit smoothie: 200ml mixed fruits, 50g oats",
            "Chicken tinola: 150g chicken, 100g rice, 50g veggies",
            "Beef sinigang: 150g beef, 100g veggies, 1 cup rice",
            "Grilled fish: 150g fish, 100g veggies",
            "Pork menudo: 150g pork, 100g veggies, 1 cup rice",
            "Vegetable stir-fry: 150g mixed veggies, 1 cup rice",
            "Beef kaldereta: 150g beef, 100g veggies"
        ]
    ],
    # ... replicate similar weekly structure for "Normal weight", "Overweight", "Obese" ...
}

illness_adjustments = {
    "Diabetes":    "Replace sweets with berries; avoid sugar; choose whole grains.",
    "Hypertension":"Limit salt; use calamansi and herbs.",
    "Asthma":      "Add papaya, sweet potato leaves, fatty fish.",
    "Other":       "Follow medical dietary advice."
}

fitness_plans = {
    # ... same as before ...
}


def adjust_meals(category, conditions):
    weeks = meal_plans.get(category, [])
    notes = " ".join(illness_adjustments[c] for c in conditions if c != "None")
    return [
        {"week": i+1, "days": weeks[i], "note": notes}
        for i in range(len(weeks))
    ]


# Streamlit UI
st.set_page_config(page_title="B.E.A.T.", layout="centered")
st.title("B.E.A.T. – Body Evaluation and Activity Tracker")
st.markdown("An app promoting healthy lifestyles through BMI analysis and WHO-aligned fitness programs.")

age = st.number_input("Age (years)", min_value=5, max_value=100, value=16)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=55.0, step=0.1)
height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=160.0, step=0.1)

conditions = st.multiselect(
    "Select Health Conditions",
    ["Asthma", "Diabetes", "Hypertension", "None", "Other"],
    default=["None"]
)

if st.button("Compute 8-Week Plans"):
    h = height_cm / 100.0
    bmi = weight / (h * h)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    meals = adjust_meals(category, conditions)

    st.subheader(f"Your BMI: {bmi:.1f}")
    st.write(f"**Category:** {category}")

    st.markdown("### 8-Week Meal Plan (Daily Meals)")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for wk in meals:
        st.write(f"**Week {wk['week']}**")
        for idx, meal in enumerate(wk['days']):
            st.write(f"- {days[idx]}: {meal}")
        if wk['note']:
            st.info(f"Note: {wk['note']}")

    # Fitness plan display remains unchanged
    # ...
