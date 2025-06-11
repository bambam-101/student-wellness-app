<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Student BMI & Wellness Planner</title>
  <!-- Google Font -->
  <style>
    @import url("https://fonts.googleapis.com/css?family=Merriweather:400,400i,700");
    body, h1, h5, h6, p, ul, li {
      font-family: 'Merriweather', serif;
    }
    body {
      padding-top: 2rem;
      /* SVG pattern background */
      background-image: url('data:image/svg+xml,%3Csvg width="12" height="24" viewBox="0 0 12 24" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="none" fill-rule="evenodd"%3E%3Cg fill="%239C92AC" fill-opacity="0.4"%3E%3Cpath d="M2 0h2v12H2V0zm1 20c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM9 8c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zm-1 4h2v12H8V12z"/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');
    }
    .week-plan { margin-bottom: 1rem; }
    .page-icon { vertical-align: middle; width: 1.2em; margin-right: 0.5em; fill: currentColor; }
  </style>
  <!-- Bootstrap for base styling -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"/>
</head>
<body>
  <div class="container">
    <h1 class="mb-4">
      <!-- Inline basketball SVG as icon -->
      <svg viewBox="0 0 496 512" class="page-icon" title="basketball-ball">
        <path d="M212.3 10.3c-43.8 6.3-86.2 24.1-122.2 53.8l77.4 77.4c27.8-35.8 43.3-81.2 44.8-131.2zM248 222L405.9 64.1c-42.4-35-93.6-53.5-145.5-56.1-1.2 63.9-21.5 122.3-58.7 167.7L248 222zM56.1 98.1c-29.7 36-47.5 78.4-53.8 122.2 50-1.5 95.5-17 131.2-44.8L56.1 98.1zm272.2 204.2c45.3-37.1 103.7-57.4 167.7-58.7-2.6-51.9-21.1-103.1-56.1-145.5L282 256l46.3 46.3zM248 290L90.1 447.9c42.4 34.9 93.6 53.5 145.5 56.1 1.3-64 21.6-122.4 58.7-167.7L248 290zm191.9 123.9c29.7-36 47.5-78.4 53.8-122.2-50.1 1.6-95.5 17.1-131.2 44.8l77.4 77.4zM167.7 209.7C122.3 246.9 63.9 267.3 0 268.4c2.6 51.9 21.1 103.1 56.1 145.5L214 256l-46.3-46.3zm116 292c43.8-6.3 86.2-24.1 122.2-53.8l-77.4-77.4c-27.7 35.7-43.2 81.2-44.8 131.2z"/>
      </svg>
      Student BMI & Wellness Planner
    </h1>

    <!-- Input form -->
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">Enter Your Information</h5>
        <div class="form-row">
          <div class="form-group col-md-4">
            <label for="age">Age (years)</label>
            <input type="number" class="form-control" id="age" min="5" max="100" value="16">
          </div>
          <div class="form-group col-md-4">
            <label for="weight">Weight (kilograms)</label>
            <input type="number" class="form-control" id="weight" step="0.1" min="10" max="200" value="55.0">
          </div>
          <div class="form-group col-md-4">
            <label for="height">Height (centimetres)</label>
            <input type="number" class="form-control" id="height" step="0.1" min="50" max="250" value="160.0">
          </div>
        </div>
        <button class="btn btn-primary" id="computeBtn">
          👉 Compute Body Mass Index and Identify Health Conditions
        </button>
      </div>
    </div>

    <!-- Results placeholder -->
    <div id="results"></div>
  </div>

  <script>
    // Meal plan alternatives per BMI category (Filipino cuisine)
    const mealPlans = {
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
    };

    // Illness-based adjustment notes
    const illnessAdjustments = {
      "Diabetes": "Please replace sweet fruits with berries, avoid sugary sauces, and choose whole grains.",
      "Hypertension": "Please limit added salt, fish sauce, and fermented condiments; use calamansi and herbs for flavor.",
      "Asthma": "Please include anti-inflammatory foods such as sweet potato leaves, papaya, and fatty fish.",
      "Other": "Please follow any specific medical dietary advice provided by your healthcare professional."
    };

    // Fitness plans by category with YouTube links
    const fitnessPlansByCategory = {
      "Underweight": [
        { week:1, focus:"Daily Active Lifestyle", recommendation:"Thirty minutes of brisk walking or active play every day", video:`<a href="https://www.youtube.com/watch?v=jRWKYOhcWWU" target="_blank">30-Minute Walking Workout for Beginners &amp; Seniors</a>` },
        { week:2, focus:"Strength and Flexibility Exercises", recommendation:"Bodyweight circuit of push-ups, squats, and lunges two times per week", video:`<a href="https://www.youtube.com/watch?v=IODxDxX7oi4" target="_blank">The Perfect Push Up | Do It Right!</a>, <a href="https://www.youtube.com/watch?v=gcNh17Ckjgg" target="_blank">Proper Squat Form</a>, <a href="https://www.youtube.com/watch?v=fydLSJlGx-0" target="_blank">Beginner Lunges</a>` },
        { week:3, focus:"Aerobic and Cardiovascular Exercise", recommendation:"Thirty minutes of light cycling or swimming three times per week", video:`<a href="https://www.youtube.com/watch?v=YKCy0HlH55M" target="_blank">20-Minute Cycling Workout for Beginners</a>, <a href="https://www.youtube.com/watch?v=Rr_CnIfr5u8" target="_blank">Swimming Confidence for Beginners</a>` },
        { week:4, focus:"Flexibility Training", recommendation:"Twenty minutes of yoga or deep-stretch routines two times per week", video:`<a href="https://www.youtube.com/watch?v=T41mYCmtWls" target="_blank">10-Minute Morning Yoga Stretch for Beginners</a>` },
        { week:5, focus:"Progressive Resistance Training", recommendation:"Resistance bands or light dumbbells two times per week", video:`<a href="https://www.youtube.com/watch?v=Lk5PisETE9I" target="_blank">Resistance Band Workout for Beginners</a>` },
        { week:6, focus:"Recreational Sport", recommendation:"One session of basketball drills per week", video:`<a href="https://www.youtube.com/watch?v=ynkhxHilaKA" target="_blank">21 BEST Youth Basketball Drills for BEGINNERS</a>` },
        { week:7, focus:"Rest and Recovery", recommendation:"One full rest day plus cool-down stretches", video:"N/A" },
        { week:8, focus:"Weekly Check-In", recommendation:"Monitor energy levels and adjust intensity as needed", video:"N/A" }
      ],
      "Normal weight": [
        { week:1, focus:"Daily Active Lifestyle", recommendation:"Thirty minutes of brisk walking or playground games every day", video:`<a href="https://www.youtube.com/watch?v=jRWKYOhcWWU" target="_blank">30-Minute Walking Workout for Beginners &amp; Seniors</a>` },
        { week:2, focus:"Strength and Flexibility Exercises", recommendation:"Bodyweight plus resistance-band circuit three times per week", video:`<a href="https://www.youtube.com/watch?v=IODxDxX7oi4" target="_blank">The Perfect Push Up | Do It Right!</a>, <a href="https://www.youtube.com/watch?v=gcNh17Ckjgg" target="_blank">Proper Squat Form</a>, <a href="https://www.youtube.com/watch?v=Lk5PisETE9I" target="_blank">Resistance Band Workout for Beginners</a>` },
        { week:3, focus:"Aerobic and Cardiovascular Exercise", recommendation:"Thirty to forty minutes of jog, cycle, or swim three to four times per week", video:`<a href="https://www.youtube.com/watch?v=YKCy0HlH55M" target="_blank">20-Minute Cycling Workout for Beginners</a>, <a href="https://www.youtube.com/watch?v=Rr_CnIfr5u8" target="_blank">Swimming Confidence for Beginners</a>` },
        { week:4, focus:"Flexibility Training", recommendation:"Twenty minutes of dynamic stretches or yoga twice per week", video:`<a href="https://www.youtube.com/watch?v=T41mYCmtWls" target="_blank">10-Minute Morning Yoga Stretch for Beginners</a>` },
        { week:5, focus:"Progressive Resistance Training", recommendation:"Resistance bands or light dumbbells two times per week", video:`<a href="https://www.youtube.com/watch?v=Lk5PisETE9I" target="_blank">Resistance Band Workout for Beginners</a>` },
        { week:6, focus:"Recreational Sport", recommendation:"One session of team sports or dance per week", video:`<a href="https://www.youtube.com/watch?v=ynkhxHilaKA" target="_blank">21 BEST Youth Basketball Drills for BEGINNERS</a>` },
        { week:7, focus:"Rest and Recovery", recommendation:"One full rest day plus cool-down stretches", video:"N/A" },
        { week:8, focus:"Weekly Check-In", recommendation:"Track progress and increase duration by five minutes each week", video:"N/A" }
      ],
      "Overweight": [
        { week:1, focus:"Daily Active Lifestyle", recommendation:"Thirty minutes of low-impact walking or household chores every day", video:`<a href="https://www.youtube.com/watch?v=jRWKYOhcWWU" target="_blank">30-Minute Walking Workout for Beginners & Seniors</a>` },
        { week:2, focus:"Strength and Flexibility Exercises", recommendation:"Chair-assisted squats and wall push-ups two times per week", video:`<a href="https://www.youtube.com/watch?v=gcNh17Ckjgg" target="_blank">Proper Squat Form</a>, <a href="https://www.youtube.com/watch?v=IODxDxX7oi4" target="_blank">The Perfect Push Up</a>` },
        { week:3, focus:"Aerobic and Cardiovascular Exercise", recommendation:"Twenty-five to thirty minutes of swimming or cycling four times per week", video:`<a href="https://www.youtube.com/watch?v=YKCy0HlH55M" target="_blank">20-Minute Cycling Workout for Beginners</a>, <a href="https://www.youtube.com/watch?v=Rr_CnIfr5u8" target="_blank">Swimming Confidence for Beginners</a>` },
        { week:4, focus:"Flexibility Training", recommendation:"Twenty minutes of gentle yoga twice per week", video:`<a href="https://www.youtube.com/watch?v=1DYH5ud3zHo" target="_blank">Gentle Chair Yoga for Beginners and Seniors</a>` },
        { week:5, focus:"Progressive Resistance Training", recommendation:"Resistance bands two times per week", video:`<a href="https://www.youtube.com/watch?v=Lk5PisETE9I" target="_blank">Resistance Band Workout for Beginners</a>` },
        { week:6, focus:"Recreational Activity", recommendation:"One session of non-competitive games per week", video:`<a href="https://www.youtube.com/watch?v=ynkhxHilaKA" target="_blank">21 BEST Youth Basketball Drills for BEGINNERS</a>` },
        { week:7, focus:"Rest and Recovery", recommendation:"One full rest day plus mindful stretching", video:"N/A" },
        { week:8, focus:"Weekly Check-In", recommendation:"Note comfort levels and adjust duration by five minutes each week", video:"N/A" }
      ],
      "Obese": [
        { week:1, focus:"Daily Active Lifestyle", recommendation:"Fifteen to twenty minutes of easy walking or water aerobics every day", video:`<a href="https://www.youtube.com/watch?v=p-Vi854oZac" target="_blank">Easy Pool Workout #1</a>` },
        { week:2, focus:"Strength and Flexibility Exercises", recommendation:"Seated resistance-band exercises one to two times per week", video:`<a href="https://www.youtube.com/watch?v=1DYH5ud3zHo" target="_blank">Gentle Chair Yoga for Beginners and Seniors</a>` },
        { week:3, focus:"Aerobic and Cardiovascular Exercise", recommendation:"Water-based cardio or stationary cycling thirty minutes three times per week", video:`<a href="https://www.youtube.com/watch?v=YKCy0HlH55M" target="_blank">20-Minute Cycling Workout for Beginners</a>` },
        { week:4, focus:"Flexibility Training", recommendation:"Chair yoga or gentle stretching twice per week", video:`<a href="https://www.youtube.com/watch?v=1DYH5ud3zHo" target="_blank">Gentle Chair Yoga for Beginners and Seniors</a>` },
        { week:5, focus:"Recreational Activity", recommendation:"One group walk or light dance session per week", video:"N/A" },
        { week:6, focus:"Rest and Recovery", recommendation:"Two rest days per week plus breathing exercises and stretches", video:"N/A" },
        { week:7, focus:"Weekly Progression", recommendation:"Increase session length by two to three minutes each week", video:"N/A" },
        { week:8, focus:"Health Check-In", recommendation:"Monitor joint comfort and energy levels", video:"N/A" }
      ]
    };

    // Adjust meals based on selected conditions
    function adjustMeals(category, illnesses) {
      const base = mealPlans[category];
      const notes = illnesses
        .filter(i => i !== "None")
        .map(i => illnessAdjustments[i] || illnessAdjustments["Other"])
        .join(" ");
      return base.map(alts => ({ alternatives: alts, note: notes }));
    }

    // Adjust fitness based on conditions
    function adjustFitness(category, illnesses) {
      let plan = fitnessPlansByCategory[category];
      if (illnesses.some(i => i !== "None")) {
        plan = plan.map(row => ({
          ...row,
          recommendation: row.recommendation + " 🩺 Adapt intensity as advised by your healthcare professional."
        }));
      }
      return plan;
    }

    document.getElementById("computeBtn").addEventListener("click", () => {
      // Compute BMI and category
      const w = +document.getElementById("weight").value;
      const h = +document.getElementById("height").value / 100;
      const bmi = w / (h * h);
      let category = bmi < 18.5 ? "Underweight"
                    : bmi < 25   ? "Normal weight"
                    : bmi < 30   ? "Overweight"
                                 : "Obese";

      // Show illness selection
      const results = document.getElementById("results");
      results.innerHTML = `
        <div class="card mb-3">
          <div class="card-body">
            <h5>Your Body Mass Index is ${bmi.toFixed(1)}</h5>
            <p><strong>Category:</strong> ${category}</p>
            <h6>Select Any Health Conditions</h6>
            <div id="conds">
              ${["Asthma","Diabetes","Hypertension","None","Other"]
                .map(v => `<div><label><input type="checkbox" value="${v}"> ${v}</label></div>`)
                .join("")}
            </div>
            <div id="warn" class="text-warning mt-2" style="display:none;">
              ⚠️ You have selected a condition—recommendations will adjust accordingly.
            </div>
            <button class="btn btn-success mt-3" id="planBtn">
              🎯 Get Personalized Meal and Fitness Plans
            </button>
          </div>
        </div>
        <div id="planSections"></div>
      `;

      // Toggle warning on illness selection
      const boxes = results.querySelectorAll("#conds input");
      boxes.forEach(cb => cb.addEventListener("change", () => {
        const sel = Array.from(boxes).filter(c => c.checked).map(c => c.value);
        document.getElementById("warn").style.display = sel.some(v => v !== "None") ? "block" : "none";
      }));

      // Generate plans when button clicked
      document.getElementById("planBtn").onclick = () => {
        const selected = Array.from(boxes).filter(c => c.checked).map(c => c.value);
        const mealData = adjustMeals(category, selected);
        const fitnessData = adjustFitness(category, selected);

        const sections = document.getElementById("planSections");
        sections.innerHTML = `
          <div class="alert alert-info">
            <h5>Explanation and Reason</h5>
            <p>Based on your Body Mass Index category and any selected health condition(s), we have chosen Filipino dishes that provide balanced nutrients and local flavors while respecting dietary restrictions. The fitness plan follows the Filipino Pyramid Activity Guide, progressing through daily movement, strength and flexibility, aerobic exercise, recreational activity, and recovery. Video tutorials are provided for proper form.</p>
          </div>
          <div class="card mb-3"><div class="card-body">
            <h5>🗓 8-Week Meal Plan (Filipino Cuisine with Choices)</h5>
            <div id="mealPlan"></div>
          </div></div>
          <div class="card mb-3"><div class="card-body">
            <h5>💪 8-Week Fitness Plan (Filipino Pyramid Activity Guide)</h5>
            <div id="fitPlan"></div>
          </div></div>
        `;

        // Render meal plan
        const mp = document.getElementById("mealPlan");
        mealData.forEach((week, i) => {
          mp.innerHTML += `
            <div class="week-plan">
              <strong>Week ${i+1}:</strong>
              <ul>${week.alternatives.map(d => `<li>${d}</li>`).join("")}</ul>
              ${week.note ? `<p><em>Note: ${week.note}</em></p>` : ""}
            </div>
          `;
        });

        // Render fitness plan table
        const fp = document.getElementById("fitPlan");
        const table = document.createElement("table");
        table.className = "table table-bordered";
        table.innerHTML = `
          <thead class="thead-light">
            <tr>
              <th>Week</th>
              <th>Activity Focus</th>
              <th>Recommendation</th>
              <th>Video Tutorial</th>
            </tr>
          </thead>
        `;
        const tbody = document.createElement("tbody");
        fitnessData.forEach(row => {
          const tr = document.createElement("tr");
          tr.innerHTML = `
            <td>${row.week}</td>
            <td>${row.focus}</td>
            <td>${row.recommendation}</td>
            <td>${row.video}</td>
          `;
          tbody.appendChild(tr);
        });
        table.appendChild(tbody);
        fp.appendChild(table);
      };
    });
  </script>
</body>
</html>
