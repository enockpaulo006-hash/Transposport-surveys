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
                "#cdded8",
                "#15df3a",
                "#0a0a09e1",
                "#e5f31b",
                "#111014",
                "#0c56eb"
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