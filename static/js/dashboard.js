async function loadDashboardMetrics() {
  try {
    const response = await fetch("/dashboard-metrics");
    const data = await response.json();

   
    document.getElementById("model-name").textContent = data.model_name;
    document.getElementById("total-predictions").textContent = data.total_predictions;
    document.getElementById("good-count").textContent = data.good_count;
    document.getElementById("bad-count").textContent = data.bad_count;

    
    renderPredictionChart(data.good_count, data.bad_count);
    renderAdvancedInsights(data);

  } catch (error) {
    console.error("Error loading dashboard metrics:", error);
  }
}

function renderPredictionChart(goodCount, badCount) {
  const ctx = document.getElementById("predictionChart").getContext("2d");

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Good Wafers", "Bad Wafers"],
      datasets: [{
        label: "Prediction Count",
        data: [goodCount, badCount],
        backgroundColor: ["#22c55e", "#ef4444"]
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: false
        }
      }
    }
  });
}
function renderAdvancedInsights(data) {
  const total = data.total_predictions;
  const good = data.good_count;
  const bad = data.bad_count;

 
  const healthScore = ((good / total) * 100).toFixed(2);
  document.getElementById("health-score").innerText = healthScore + "%";

  
  const riskPercent = ((bad / total) * 100).toFixed(1);
  document.getElementById("risk-fill").style.width = riskPercent + "%";

  
  let riskText = "";
  if (riskPercent > 70) {
    riskText = "⚠️ High defect rate detected. Immediate inspection recommended.";
  } else if (riskPercent > 40) {
    riskText = "⚠️ Moderate risk. Monitor upcoming batches closely.";
  } else {
    riskText = "✅ Production quality is stable.";
  }
  document.getElementById("risk-text").innerText = riskText;

  renderDonutChart(good, bad);
  renderTrendChart(bad);
}
function renderDonutChart(good, bad) {
  const ctx = document.getElementById("donutChart").getContext("2d");
  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Good (%)", "Bad (%)"],
      datasets: [{
        data: [
          ((good / (good + bad)) * 100).toFixed(1),
          ((bad / (good + bad)) * 100).toFixed(1)
        ],
        backgroundColor: ["#22c55e", "#ef4444"]
      }]
    },
    options: {
      plugins: { legend: { position: "bottom" } }
    }
  });
}
function renderTrendChart(badCount) {
  const ctx = document.getElementById("trendChart").getContext("2d");

  const trendData = [
    badCount * 0.3,
    badCount * 0.5,
    badCount * 0.8,
    badCount
  ].map(v => Math.round(v));

  new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Batch-1", "Batch-2", "Batch-3", "Batch-4"],
      datasets: [{
        label: "Bad Wafers",
        data: trendData,
        borderColor: "#ef4444",
        tension: 0.4
      }]
    },
    options: {
      responsive: true
    }
  });
}
// Load data when page loads
window.onload = loadDashboardMetrics;