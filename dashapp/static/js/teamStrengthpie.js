function drawTeamStrength(newProjects,completed,current){
  var ctx = document.getElementById('teamStrength');
  var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['Completed', 'Current Projects', 'New'],
          datasets: [{
              label: '# of Votes',
              data: [completed,current,newProjects],
              backgroundColor: [
                '#3BB300',
                '#00bceb',
                '#eed202'
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
            text: 'FY Project Status',
            fontColor: "white",
            fontSize: 18
          },

           plugins:{
              labels: {
              render: 'value',
    fontSize: 20,
    fontStyle: 'bold',
    fontColor: 'white',
    fontFamily: '"Lucida Console", Monaco, monospace'
    
  }
  },

          legend: {
                labels: {
                    fontColor: "white",
                }
               
            }
      }
  });
}
