function drawCat(ent, sp){
  var ctx = document.getElementById('myChart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['ENT', 'SP'],
          datasets: [{
              label: 'Categories Count',
              data: [ent, sp],
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
            text: 'Project Categories',
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
              render: 'value',
              fontSize: 14,
              fontStyle: 'bold',
              fontColor: 'white',
              fontFamily: '"Lucida Console", Monaco, monospace'
    }
  }
      }
  });
}

function drawLine(nmberOfSites, completionMonth){
  var ctx = document.getElementById('myLineGraph').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: nmberOfSites,
          datasets: [{
              label: 'Categories Count',
              data: completionMonth,
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
            text: 'Windows Per Month'
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
