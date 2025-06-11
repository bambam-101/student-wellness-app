# app.py
import streamlit as st

st.set_page_config(
    page_title="Student BMI & Wellness Planner",
    page_icon="💪",
    layout="centered",
)

st.title("🏃‍♂️ Student BMI & Wellness Planner")

# --- 1. Input form ---
st.header("Enter Your Information")
age = st.number_input("Age (years)", min_value=5, max_value=100, value=16)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=55.0, format="%.1f")
height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=160.0, format="%.1f")
height_m = height_cm / 100

# --- 2. Compute BMI & category ---
if st.button("👉 Compute BMI & Get Plan"):
    bmi = weight / (height_m ** 2)
    st.subheader(f"Your BMI: {bmi:.1f}")
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    st.markdown(f"**Category:** {category}")

    # --- 3. Checklist of illnesses ---
    st.header("Health Conditions (check all that apply)")
    options = ["Asthma", "Diabetes", "Hypertension", "None", "Other"]
    selected = st.multiselect("", options, default=["None"])
    if "None" not in selected:
        st.warning("⚠️ Since you have one or more conditions, please consult a healthcare professional before starting.")

    # --- 4. Plans data ---
    meal_plans = {
        "Underweight": [
            "Increase calorie intake with 3 meals + 2 nutrient-dense snacks daily (nuts, smoothies). Follow WHO macros: 50–60% carbs, 15–20% protein, 20–30% fats.",
            "Include whole‐grain bread, peanut butter, fruit smoothies; lean proteins like chicken, fish, tofu.",
            "Add healthy oils (olive oil) to meals; eat dairy (yogurt, cheese) added to snacks.",
            "Boost calories with trail mix, full‐fat milk; maintain balanced macros per WHO guidelines.",
            "Rotate protein sources (eggs, beans, lean meats); plenty of fruits & veggies; 2 snacks/day.",
            "Blend shakes with oats, bananas, protein powder; add nut butters to snacks.",
            "Try avocado toast, yogurt parfaits; prioritize calorie‐dense healthy foods.",
            "Maintain same structure to reach healthy weight; monitor progress weekly."
        ],
        "Normal weight": [
            "3 balanced meals per day: ¼ plate protein, ¼ whole grains, ½ fruits/vegetables (per WHO healthy plate).",
            "Add one light snack (fruit or yogurt) to keep energy up through classes.",
            "Rotate protein: fish, eggs, legumes; follow WHO guidance on limiting sugar and salt.",
            "Aim for variety: include colorful veggies and whole grains each meal.",
            "Snack on nuts or fresh fruit; stay hydrated with water, avoid sugary drinks.",
            "Practice portion control; maintain macros: 50% carbs, 20% protein, 30% fats.",
            "Introduce herbal teas or infused water; keep processed foods minimal.",
            "Continue this balanced approach to maintain healthy BMI."
        ],
        "Overweight": [
            "3 smaller meals + 1 healthy snack: focus on vegetables, lean protein, whole grains.",
            "Limit refined carbs and added sugars; follow WHO advice on reducing free sugars to <10% of energy.",
            "Use low‐fat dairy, lean meats; bulk meals with veggies and legumes.",
            "Snack on raw veggies or a piece of fruit; avoid deep-fried foods.",
            "Monitor portion sizes; use smaller plates and mindful eating.",
            "Include a colorful salad with every lunch or dinner.",
            "Replace soda with water or unsweetened drinks; stick to WHO salt limit (<5g/day).",
            "Maintain this calorie‐controlled, nutrient‐rich plan to reduce weight gradually."
        ],
        "Obese": [
            "3 portion-controlled meals: lots of non-starchy vegetables + lean protein.",
            "Skip frying; use steaming, grilling, or baking methods per WHO recommendations.",
            "One small fruit snack; avoid processed and sugary items.",
            "Increase fiber with legumes, whole grains; limit saturated fats.",
            "Stay within WHO guideline: <30% daily energy from fats, <10% from sugars.",
            "Use portion plates (½ veg, ¼ protein, ¼ grains); avoid snacking on high-calorie foods.",
            "Drink ≥8 glasses of water; reduce soft drinks to zero.",
            "Continue strict portion control and healthy cooking methods."
        ]
    }

    fitness_plans = {
        "Underweight": [
            "Week 1–2: 30 min brisk walk + basic bodyweight strength (push-ups, squats) 3×/week.",
            "Week 3–4: Increase to 45 min walk + add light dumbbell exercises 2×/week.",
            "Week 5–6: 30 min jog + strength circuit (lunges, planks) 3×/week.",
            "Week 7–8: 3 sessions of mixed cardio (bike/swim) + strength training per Filipino Pyramid guide."
        ],
        "Normal weight": [
            "Week 1–2: 30 min moderate activity (brisk walk, dance) 5×/week.",
            "Week 3–4: Add 2 days of basic strength (bodyweight) per week.",
            "Week 5–6: 40 min mixed cardio + 2× strength sessions.",
            "Week 7–8: Follow Filipino Pyramid: daily active play + 3 structured workouts weekly."
        ],
        "Overweight": [
            "Week 1–2: 20 min low-impact cardio (walking) daily + light stretching.",
            "Week 3–4: 30 min swim or bike 5×/week + introduction to bodyweight exercises.",
            "Week 5–6: 40 min mixed cardio + 1 strength session per Filipino Pyramid guide.",
            "Week 7–8: 45 min cardio + 2 strength sessions; focus on joint-friendly moves."
        ],
        "Obese": [
            "Week 1–2: 15 min low-impact (water aerobics, walking) daily.",
            "Week 3–4: 25 min swim or cycle 4×/week + chair-based strength.",
            "Week 5–6: 30 min mixed low-impact cardio + light resistance exercises.",
            "Week 7–8: 35 min daily activity + Filipino Pyramid: balance rest & activity; consult doctor."
        ]
    }

    # --- 5. Display Plans ---
    st.header("🗓 8-Week Meal Plan")
    for idx, week_text in enumerate(meal_plans[category], start=1):
        st.markdown(f"**Week {idx}:** {week_text}")

    st.header("💪 8-Week Fitness Plan")
    # note: some categories have only 4 entries; repeat pattern twice if needed
    fitness = fitness_plans[category]
    if len(fitness) == 4:
        fitness = fitness * 2
    for idx, week_text in enumerate(fitness, start=1):
        st.markdown(f"**Week {idx}:** {week_text}")

    st.success("✅ Plan generated!")
