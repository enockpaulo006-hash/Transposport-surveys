// Gender Doughnut Chart

new Chart(
    document.getElementById("genderAnalysisChart"),
    {
        type: "doughnut",
        data: {
            labels: genderLabels,
            datasets: [
                {
                    data: genderValues,
                    backgroundColor: [
                        "#070202",
                        "#a6178e"
                    ],
                    borderWidth: 0
                }
            ]
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
    }
);

// Age Group Chart
new Chart(
    document.getElementById("ageChart"),
    {
        type: "bar",
        data: {
            labels: ageLabels,
            datasets: [
                {
                    label: "Respondents",
                    data: ageValues,
                    backgroundColor: "#2563eb",
                    borderRadius: 8
                }
            ]
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
    }
);

// Occupation Chart

new Chart(
    document.getElementById("occupationChart"),
    {
        type: "bar",
        data: {
            labels: occupationLabels,
            datasets: [
                {
                    label: "Respondents",
                    data: occupationValues,
                    backgroundColor: "#10b981",
                    borderRadius: 8
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: "y",
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            }
        }
    }
);