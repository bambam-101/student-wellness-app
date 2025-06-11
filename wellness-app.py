<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Student BMI & Wellness Planner</title>
  <!-- Google Font -->
  <style>
    @import url("https://fonts.googleapis.com/css?family=Merriweather:400,400i,700");
    :root {
      --primary-color: #039BE5;
    }
    body, h1, h5, h6, p, ul, li {
      font-family: 'Merriweather', serif;
      color: #333;
    }
    body {
      padding-top: 2rem;
      background-image: url('data:image/svg+xml,%3Csvg width="12" height="24" viewBox="0 0 12 24" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="none" fill-rule="evenodd"%3E%3Cg fill="%239C92AC" fill-opacity="0.4"%3E%3Cpath d="M2 0h2v12H2V0zm1 20c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM9 8c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zm-1 4h2v12H8V12z"/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');
    }
    .btn-primary {
      background-color: var(--primary-color);
      border-color: var(--primary-color);
    }
    .btn-primary:hover {
      background-color: #027AB9;
      border-color: #027AB9;
    }
    h1 {
      color: var(--primary-color);
    }
    .week-plan { margin-bottom: 1rem; }
    .page-icon { vertical-align: middle; width: 1.2em; margin-right: 0.5em; fill: var(--primary-color); }
  </style>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"/>
</head>
<body>
  <div class="container">
    <h1 class="mb-4">
      <svg viewBox="0 0 496 512" class="page-icon" title="basketball-ball">
        <path d="M212.3 10.3c-43.8 6.3-86.2 24.1-122.2 53.8l77.4 77.4c27.8-35.8 43.3-81.2 44.8-131.2zM248 222L405.9 64.1c-42.4-35-93.6-53.5-145.5-56.1-1.2 63.9-21.5 122.3-58.7 167.7L248 222zM56.1 98.1c-29.7 36-47.5 78.4-53.8 122.2 50-1.5 95.5-17 131.2-44.8L56.1 98.1zm272.2 204.2c45.3-37.1 103.7-57.4 167.7-58.7-2.6-51.9-21.1-103.1-56.1-145.5L282 256l46.3 46.3zM248 290L90.1 447.9c42.4 34.9 93.6 53.5 145.5 56.1 1.3-64 21.6-122.4 58.7-167.7L248 290zm191.9 123.9c29.7-36 47.5-78.4 53.8-122.2-50.1 1.6-95.5 17.1-131.2 44.8l77.4 77.4zM167.7 209.7C122.3 246.9 63.9 267.3 0 268.4c2.6 51.9 21.1 103.1 56.1 145.5L214 256l-46.3-46.3zm116 292c43.8-6.3 86.2-24.1 122.2-53.8l-77.4-77.4c-27.7 35.7-43.2 81.2-44.8 131.2z"/>
      </svg>
      Student BMI & Wellness Planner
    </h1>
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
        <button class="btn btn-primary" id="computeBtn">👉 Compute Body Mass Index and Identify Health Conditions</button>
      </div>
    </div>
    <div id="results"></div>
  </div>
  <script>
    const mealPlans = {
      "Underweight": [
        ["Tapsilog: 100g beef tapa, 150g rice, 1 egg", "Tocilog: 100g tocino, 150g rice, 1 egg"],
        ["Arroz caldo: 200g porridge, 100g chicken, 1 egg"],
        ["Pinakbet: 150g veggies, 50g pork"],
        ["Chicken adobo: 150g chicken, 100g rice"]
      ],
      "Normal weight": [
        ["Chicken tinola: 150g chicken, 100g rice"],
        ["Beef sinigang: 150g beef, 100g veggies, 200ml broth"],
        ["Fish escabeche: 150g fish, 50g veggies"]
      ],
      "Overweight": [
        ["Chicken nilaga: 150g chicken, 100g veggies"],
        ["Grilled bangus: 150g fish, 50g salad"]
      ],
      "Obese": [
        ["Vegetable soup: 200ml broth, 100g veggies"],
        ["Steamed fish: 150g fish, 50g veggies"]
      ]
    };
    const illnessAdjustments = {
      Diabetes: "Replace sweets with berries; avoid sugar; choose whole grains.",
      Hypertension: "Limit salt; use calamansi and herbs.",
      Asthma: "Add papaya, sweet potato leaves, fatty fish." };
    const fitnessPlans = {
      "Underweight": [
        {w:1,f:"Active Lifestyle",r:"30 mins walk daily",v:"https://www.youtube.com/watch?v=jRWKYOhcWWU"},
        {w:2,f:"Strength & Flexibility",r:"3x12 push-ups,3x15 squats,3x12 lunges twice/week",v:"https://www.youtube.com/watch?v=IODxDxX7oi4"},
        {w:3,f:"Cardio",r:"30 mins cycling/swim 3×/week",v:"https://www.youtube.com/watch?v=YKCy0HlH55M"},
        {w:4,f:"Flexibility",r:"20 mins yoga 2×/week",v:"https://www.youtube.com/watch?v=T41mYCmtWls"}
      ],
      "Normal weight": [ {w:1,f:"Active",r:"30 mins walk",v:""} ],
      "Overweight": [ {w:1,f:"Active",r:"30 mins walk",v:""} ],
      "Obese": [ {w:1,f:"Active",r:"20 mins walk",v:""} ]
    };
    function adjustMeals(cat, ill) {
      let plan = mealPlans[cat]||[];
      const notes = ill.filter(i=>i!="None").map(i=>illnessAdjustments[i]||"").join(" ");
      return plan.map(a=>({alts:a,note:notes}));
    }
    function adjustFitness(cat, ill) { let p=fitnessPlans[cat]||[]; if(ill.some(i=>i!="None"))p=p.map(x=>({...x,r:x.r+" 🩺 adapt intensity."})); return p; }
    document.getElementById("computeBtn").addEventListener("click",()=>{
      const w=+document.getElementById("weight").value;const h=+document.getElementById("height").value/100;const bmi=w/(h*h);
      const cat=bmi<18.5?"Underweight":bmi<25?"Normal weight":bmi<30?"Overweight":"Obese";
      const res=document.getElementById("results");res.innerHTML=
        `<div class="card mb-3"><div class="card-body">`+
        `<h5>Your BMI: ${bmi.toFixed(1)}</h5><p><strong>Category:</strong> ${cat}</p>`+
        `<h6>Select Health Conditions</h6><div id="conds">${["Asthma","Diabetes","Hypertension","None","Other"].map(v=>`<div><label><input type="checkbox" value="${v}"> ${v}</label></div>`).join("")}</div>`+
        `<div id="warn" class="text-warning" style="display:none;">⚠️ Condition selected.</div>`+
        `<button class="btn btn-success mt-3" id="planBtn">Get Plans</button>`+
        `</div></div><div id="planSections"></div>`;
      const boxes=res.querySelectorAll("#conds input");boxes.forEach(cb=>cb.addEventListener("change",()=>{const sel=Array.from(boxes).filter(c=>c.checked).map(c=>c.value);res.querySelector("#warn").style.display=sel.some(v=>v!="None")?"block":"none";}));
      document.getElementById("planBtn").onclick=()=>{
        const sel=Array.from(boxes).filter(c=>c.checked).map(c=>c.value);
        const meals=adjustMeals(cat,sel);const fit=adjustFitness(cat,sel);
        const sec=document.getElementById("planSections");sec.innerHTML=`<div class="alert alert-info"><h5>Explanation and Reason</h5><p>Based on your BMI and conditions, we select balanced Filipino dishes with proper portions and adjust for dietary needs. The fitness plan follows the Filipino Pyramid Activity Guide: daily activity, strength, cardio, flexibility, sport, and recovery with durations and video guides.</p></div>`+
          `<div class="card mb-3"><div class="card-body"><h5>Meal Plan</h5><div id="mealPlan"></div></div></div>`+
          `<div class="card mb-3"><div class="card-body"><h5>Fitness Plan</h5><table class="table table-bordered"><thead><tr><th>Week</th><th>Focus</th><th>Recommendation</th><th>Video</th></tr></thead><tbody id="fitTbl"></tbody></table></div></div>`;
        const mp=sec.querySelector("#mealPlan");meals.forEach((wk,i)=>{mp.innerHTML+=`<div class="week-plan"><strong>Week ${i+1}:</strong><ul>${wk.alts.map(d=>`<li>${d}</li>`).join("")}</ul>${wk.note?`<p><em>Note: ${wk.note}</em></p>`:""}</div>`;});
        const ftb=sec.querySelector("#fitTbl");fit.forEach(r=>{ftb.innerHTML+=`<tr><td>${r.week}</td><td>${r.focus}</td><td>${r.r}</td><td>${r.video||'N/A'}</td></tr>`;});
      };
    });
  </script>
</body>
</html>
