// Transport Mode Doughnut Chart

new Chart(document.getElementById("transportModeChart"), {
    type: "doughnut",
    data: {
        labels: transportLabels,
        datasets: [{
            data: transportValues,
            backgroundColor: [
                "#2d2828",
                "#05f4a4",
                "#e8b762",
                "#ec4899",
                "#6429ee",
                "#0ec0ed",
                "#ef4444"
            ],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: "65%",
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
            backgroundColor: "#1b5be6",
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