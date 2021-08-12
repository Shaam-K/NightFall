var display_graph =  document.getElementById('comp_temp').getContext('2d');
var min_max = new Chart(display_graph, {
    type: 'line',
    data : {
        labels: ['Min Temp', 'Max Temp'],
        datasets: [{
            label: 'Temp Comparision',
            data : [
            '{{ item.temp_min }}', 
            '{{ item.temp_max }}',
        ],
            backgroundColor: [
                '#391469',
                '#E63946',
            ]
        }]
    }
})