// Gender Distribution Chart

const genderChart = new Chart(
    document.getElementById("genderChart"),
    {

        type: 'doughnut',


        data: {

            labels: genderLabels,

            datasets: [

                {

                    data: genderValues,

                    backgroundColor: [

                        "#3bf66d",
                        "#d4350d"

                    ],

                    hoverOffset: 8,

                    borderWidth: 0

                }

            ]

        },

        options: {
            

            responsive: true,

            maintainAspectRatio: false,

            cutout: '50%',

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        usePointStyle: true,

                        padding: 20,

                        font: {

                            size: 13

                        }

                    }

                }

            }

        }

    }

);

// Transport Mode Chart
const transportChart = new Chart(
    document.getElementById("transportChart"),
    {

        type: "bar",

        data: {

            labels: transportLabels,

            datasets: [

                {

                    label: "Number of Respondents",

                    data: transportValues,

                    backgroundColor: [

                        "#2563eb",

                        "#22c55e",

                        "#f59e0b",

                        "#ef4444",

                        "#8b5cf6",

                        "#14b8a6",

                        "#0ea5e9",

                        "#f97316"

                    ],

                    borderRadius: 8,

                    borderSkipped: false

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

                x: {

                    grid: {

                        display: false

                    }

                },

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