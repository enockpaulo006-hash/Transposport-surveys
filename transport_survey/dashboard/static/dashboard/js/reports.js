// Gender Report Chart

new Chart(document.getElementById("reportGenderChart"), {
    type: "doughnut",
    data: {
        labels: genderLabels,
        datasets: [{
            data: genderValues,
            backgroundColor: [
                "#25eb4d",
                "#120d0d"
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


// Transport Report Chart

new Chart(document.getElementById("reportTransportChart"), {
    type: "bar",
    data: {
        labels: transportLabels,
        datasets: [{
            label: "Responses",
            data: transportValues,
            backgroundColor: [
                "#2563eb",
                "#10b981",
                "#f59e0b",
                "#ef4444",
                "#8b5cf6",
                "#06b6d4",
                "#14b8a6"
            ],
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