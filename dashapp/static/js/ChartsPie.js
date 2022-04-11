function drawHealth(green,amber,red) {
  var ctx = document.getElementById('myChartPie').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['Green', 'Amber', 'Red'],
          datasets: [{
              label: '# of Votes',
              data: [green, amber, red],
              backgroundColor: [
                  '#3BB300',
                  '#FFB366',
                  '#FF8080'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          title:{
            display: true,
            text: 'Project Health',
            fontColor: "white",
            fontSize: 18
          },
          legend: {
                labels: {
                    fontColor: "white",
                }
            },
            plugins:{
      labels: {
              render: 'percentage',
              fontSize: 14,
              fontStyle: 'bold',
              fontColor: 'white',
              fontFamily: '"Lucida Console", Monaco, monospace'
    }
  }
      }
  });
}
