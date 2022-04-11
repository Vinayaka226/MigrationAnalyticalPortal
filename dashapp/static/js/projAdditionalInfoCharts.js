function drawSites(total, actual){
  var ctx = document.getElementById('mySites').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['Devices Migrated', 'Windows Executed'],
          datasets: [{
              label: 'Migrated Sites',
              data: [total,actual],
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
          legend: {
                labels: {
                    fontColor: "white",
                    //fontSize: 18
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
  },
          title:{
            display: true,
            fontColor: "white",
            text: 'Devices Migrated and Windows Executed',
            fontSize:18
          }
      }
  });
}

function drawDevices(total, actual){
  var ctx = document.getElementById('myDevices').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['Total Devices', 'Migrated Devices'],
          datasets: [{
              label: 'Migrated Sites',
              data: [total, actual],
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
          legend: {
                labels: {
                    fontColor: "white",
                    //fontSize: 18
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
  },
          title:{
            display: true,
            fontColor:'white',
            text: 'Total Vs Migrated (Devices)',
            fontSize: 18

          }
      }
  });
}

//// to be removed later
///////////////////////////
///////////////////////////
function drawSites2(total, actual){
  var ctx = document.getElementById('mySites2').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['Devices Migrated', 'Windows Executed'],
          datasets: [{
              label: 'Migrated Sites',
              data: [total,actual],
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
          legend: {
                labels: {
                    fontColor: "white",
                    //fontSize: 18
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
  },
          title:{
            display: true,
            fontColor: "white",
            text: 'Devices Migrated & MW Executed',
            fontSize:18
          }
      }
  });
}

function drawSites3(total, actual){
  var ctx = document.getElementById('mySites3').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['Devices Migrated', 'Windows Executed'],
          datasets: [{
              label: 'Migrated Sites',
              data: [total,actual],
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
          legend: {
                labels: {
                    fontColor: "white",
                    //fontSize: 18
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
  },
          title:{
            display: true,
            fontColor: "white",
            text: 'Devices Migrated & MW Executed',
            fontSize:18
          }
      }
  });
}
/////////////////////
/////////////////////
/////////////////////
function drawWindows(total, actual, widoutrollback){
  var ctx = document.getElementById('myWindows').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: ['Total Windows', 'Migrated Windows', 'Windows Without Rollback'],
          datasets: [{
              label: 'Migrated Sites',
              data: [total, actual,widoutrollback],
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
          legend: {
                labels: {
                    fontColor: "white",
                    //fontSize: 18
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
  },
          title:{
            display: true,
            fontColor: "white",
            text: 'Migration Windows Information',
            fontSize: 18
          }
      }
  });
}
