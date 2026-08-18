// Transport Mode Doughnut Chart

new Chart(document.getElementById("transportModeChart"), {
    type: "doughnut",
    data: {
        labels: transportLabels,
        datasets: [{
            data: transportValues,
            backgroundColor: [
                "#090909",
                "#10b981",
                "#f59e0b",
                "#ec4899",
                "#8b5cf6",
                "#06b6d4",
                "#ef4444"
            ],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: "60%",
        plugins: {
            legend: {
                position: "bottom"
            }
        }
    }
});

// Travel Time Chart

new Chart(document.getElementById("travelTimeChart"), {
    type: "bar",
    data: {
        labels: travelLabels,
        datasets: [{
            label: "Respondents",
            data: travelValues,
            backgroundColor: "#2563eb",
            borderRadius: 8
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    stepSize: 1
                }
            }
        }
    }
});