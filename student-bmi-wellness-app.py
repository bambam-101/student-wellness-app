import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student BMI & Wellness Planner", page_icon="🏃", layout="centered")

st.title("🏃‍♂️ Student BMI & Wellness Planner")

# Input form
st.header("Enter Your Information")
age = st.number_input("Age (years)", min_value=5, max_value=100, value=16)
weight = st.number_input("Weight (kilograms)", min_value=10.0, max_value=200.0, value=55.0, step=0.1)
height_cm = st.number_input("Height (centimetres)", min_value=50.0, max_value=250.0, value=160.0, step=0.1)
height_m = height_cm / 100

if st.button("👉 Compute Body Mass Index and Identify Health Conditions"):
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    st.subheader(f"Your BMI: {bmi:.1f}")
    st.markdown(f"**Category:** {category}")

    illnesses = st.multiselect(
        "Select any health conditions (if none, leave unselected):",
        ["Asthma", "Diabetes", "Hypertension"]
    )

    # Filipino cuisine meal plans
    meal_plans = {
        "Underweight": [
            ["Tapsilog (beef tapa, garlic fried rice, egg)", "Tocilog (tocino, garlic fried rice, egg)", "Longsilog (longganisa, garlic fried rice, egg)"],
            ["Arroz caldo with chicken, ginger, and boiled egg", "Chicken sopas with whole wheat macaroni and vegetables", "Tinolang isda with green papaya"],
            ["Pinakbet with lean pork and extra vegetables", "Ginisang munggo with malunggay and boiled egg", "Ginisang kangkong with tofu"],
            ["Chicken adobo with brown rice", "Inihaw na tilapia with ensaladang talong", "Grilled bangus with green mango salad"],
            ["Fish sinigang with a variety of vegetables", "Laing in light coconut milk with gabi leaves", "Vegetable tinola with malunggay and sayote"],
            ["Beef mechado (lean cuts) with potatoes and carrots", "Pork menudo (lean cuts) with mixed vegetables", "Chicken curry in light coconut milk with vegetables"],
            ["Lechon kawali (drained of excess fat) with steamed veggies", "Bicol express in light coconut milk with eggplant", "Grilled pork belly with tomato and cucumber"],
            ["Bangus sisig with minimal oil and steamed veggies", "Kinilaw na tanigue (fish ceviche) with cucumber", "Kinulob na manok (chicken in coconut milk) with green banana"]
        ],
        "Normal weight": [
            ["Chicken tinola with sayote and malunggay", "Beef sinigang with vegetables", "Fish escabeche with vinegar and pepper"],
            ["Beef menudo (light sauce) with mixed vegetables", "Pork binagoongan (low sodium) with eggplant", "Inihaw na liempo with atchara"],
            ["Ginisang kangkong with garlic and tofu", "Pinaputok na tilapia (stuffed fish)", "Ginataang gulay light"],
            ["Chicken curry with chickpeas and vegetables", "Kare-kare light with vegetables", "Paksiw na isda"],
            ["La Paz batchoy light with vegetables", "Batchoy Tagalog with lean pork", "Batchoy Ilonggo with lean beef"],
            ["Ginisang munggo with vegetables", "Arroz valenciana light with peas and chicken", "Pininyahang manok"],
            ["Fish tinola with ginger and papaya", "Beef caldereta light with vegetables", "Chicken mechado with carrots and potatoes"],
            ["Mixed vegetable lumpia baked", "Ukoy baked", "Smart sandwich (lean meat, whole wheat bread)"]
        ],
        "Overweight": [
            ["Chicken nilaga with cabbage and sitaw", "Tinolang isda with ginger and okra", "Vegetable sopas with whole wheat macaroni"],
            ["Inihaw na manok (skinless) with vegetable sticks", "Grilled bangus with tomato salad", "Inihaw na squid with grilled vegetables"],
            ["Ginisang ampalaya with egg light oil", "Ginisang pechay with garlic and lean pork", "Ginisang talong with tomato"],
            ["Stir-fried tofu with broccoli", "Steamed fish with ginger", "Steamed vegetable casserole"],
            ["Chicken tinola no oil with veggies", "Tinolang hipon with malunggay", "Vegetable kilawin light"],
            ["Fish sinigang with non-starchy vegetables", "Gising-gising light", "Pinangat na isda"],
            ["Paksiw na bangus with ginger", "Kinilaw na isda with vinegar", "Inihaw na salmon with salad"],
            ["Clear vegetable soup with chicken", "Vegetable broth with sitaw", "Munggo soup with malunggay"]
        ],
        "Obese": [
            ["Clear vegetable soup with fish strips", "Steam-boiled chicken with ginger", "Steamed kangkong with garlic"],
            ["Grilled vegetables with tofu", "Mixed vegetable salad with vinegar dressing", "Steamed pechay with calamansi"],
            ["Clear fish broth with sitaw and kalabasa", "Vegetable tinola with gabi", "Chicken broth with vegetables"],
            ["Steam-fried vegetable medley no oil", "Raw vegetable sticks with vinegar dip", "Steamed cauliflower and broccoli"],
            ["Steamed fish with eggplant", "Grilled shrimp with salad", "Fish broth with malunggay"],
            ["Munggo soup light with malunggay", "Ginisang pechay no oil", "Vegetable stew with chicken"],
            ["Steam-boiled egg whites with tomato slices", "Clear vegetable broth with herbs", "Raw cucumber and carrot sticks"],
            ["Clear vegetable soup with leafy greens", "Steam-boiled pechay with garlic", "Vegetable broth with ginger"]
        ]
    }

    illness_notes = {
        "Diabetes": "Replace sweet fruits with berries, avoid sugary sauces, choose whole grains.",
        "Hypertension": "Limit added salt, fish sauce; use calamansi and herbs for flavor.",
        "Asthma": "Include anti-inflammatory foods such as sweet potato leaves, papaya, and fatty fish."
    }

    fitness_plan = [
        (1, "Daily Active Lifestyle", "Thirty minutes of brisk walking or active play every day", "https://www.youtube.com/watch?v=jRWKYOhcWWU"),
        (2, "Strength and Flexibility Exercises", "Bodyweight circuit of push-ups, squats, and lunges two times per week", "https://www.youtube.com/watch?v=IODxDxX7oi4"),
        (3, "Aerobic and Cardiovascular Exercise", "Thirty minutes of light cycling or swimming three times per week", "https://www.youtube.com/watch?v=YKCy0HlH55M"),
        (4, "Flexibility Training", "Twenty minutes of yoga or deep-stretch routines two times per week", "https://www.youtube.com/watch?v=T41mYCmtWls"),
        (5, "Progressive Resistance Training", "Resistance bands or light dumbbells two times per week", "https://www.youtube.com/watch?v=Lk5PisETE9I"),
        (6, "Recreational Sport", "One session of basketball drills per week", "https://www.youtube.com/watch?v=ynkhxHilaKA"),
        (7, "Rest and Recovery", "One full rest day per week plus daily cool-down stretches", ""),
        (8, "Weekly Check-In", "Monitor energy levels and adjust intensity as needed", "")
    ]

    # Explanation and Reason
    st.info(
        "Based on your BMI category and any selected conditions, the meal plan features balanced Filipino dishes with local flavors plus adjustments for conditions. "
        "The fitness plan follows the Filipino Pyramid Activity Guide, progressing through daily movement, strength, cardio, recreation, and recovery. "
        "Video demonstrations ensure correct form."
    )

    # Display Meal Plan
    st.subheader("🗓 8-Week Meal Plan (Filipino Cuisine with Choices)")
    notes = " ".join(illness_notes[c] for c in illnesses if c in illness_notes)
    for i, options in enumerate(meal_plans[category], start=1):
        st.markdown(f"**Week {i}:**")
        for dish in options:
            st.markdown(f"- {dish}")
        if notes:
            st.markdown(f"*Note: {notes}*")

    # Display Fitness Plan Table
    st.subheader("💪 8-Week Fitness Plan (Filipino Pyramid Activity Guide)")
    df = pd.DataFrame(fitness_plan, columns=["Week", "Activity Focus", "Recommendation", "Video Tutorial"])
    df["Video Tutorial"] = df["Video Tutorial"].apply(lambda url: f"[Watch Video]({url})" if url else "N/A")
    st.table(df)
