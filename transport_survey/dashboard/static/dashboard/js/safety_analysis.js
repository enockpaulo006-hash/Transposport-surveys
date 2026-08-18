// Safety Perception Chart
console.log(document.getElementById("safetyChart"));
console.log(document.getElementById("harassmentChart"));
console.log(safetyLabels);
console.log(harassmentLabels);

new Chart(document.getElementById("safetyChart"), {
    type: "doughnut",
    data: {
        labels: safetyLabels,
        datasets: [{
            data: safetyValues,
            backgroundColor: [
                "#10b981",
                "#3b82f6",
                "#f59e0b",
                "#ef44b9",
                "#8b5cf6",
                "#06b6d4"
            ],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: "50%",
        plugins: {
            legend: {
                position: "bottom"
            }
        }
    }
});

// Harassment Reports Chart

new Chart(document.getElementById("harassmentChart"), {
    type: "bar",
    data: {
        labels: harassmentLabels,
        datasets: [{
            label: "Responses",
            data: harassmentValues,
            backgroundColor: "#ef4444",
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