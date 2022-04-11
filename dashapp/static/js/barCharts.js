
function projectsBar(projects,resourceCount){


var barColors = ["#6abf4b", "#e2231a","#fbab18","#00bceb","#eed202"];

var ctx = document.getElementById('projectsBarGraph')
//ctx.style.backgroundColor = '#f8f8f8';

new Chart(ctx, {
  type: "horizontalBar",
  data: {
  labels: projects,
  datasets: [{
    backgroundColor: barColors,
    data: resourceCount
  }]
},
  options: {
    title: {
      display: true,
      text: "Resource & Respective Project Allocation",
      fontColor: "white",
      fontSize: 18
    },
    scales: {
      xAxes: [{ticks: {min: 0, max:60,fontColor:"white"}}],
      yAxes: [{ticks: {fontColor:"white"}}]
    },
     legend: {
                labels: {
                    fontColor: "white",
                }
            },
            legend: {display: false},
            
  }
});

}


function certsBar(certificates,certiCount){


var barColors = ["red", "green","blue","orange","brown","#550089"];

var ctx = document.getElementById('certiCount')
//ctx.style.backgroundColor = '#f8f8f8';

new Chart(ctx, {
  type: "horizontalBar",
  data: {
  labels: certificates,
  datasets: [{
    backgroundColor: barColors,
    data: certiCount
  }]
},
  options: {
    legend: {display: true,
    labels: {
                    fontColor: "white",
                }
    },
    plugins:{
              labels: {
              render: 'value',
              fontSize: 12,
              fontStyle: 'bold',
              fontColor: 'white',
              fontFamily: '"Lucida Console", Monaco, monospace'
    }
  },
    title: {
      display: true,
      text: "Resource & Respective Certificates Count",
      fontColor: "white",
      fontSize: 18
    },
    scales: {
      xAxes: [{ticks: {min: 0, max:60,fontColor:"white"}}],
      yAxes:[{ticks:{fontColor:"white"}}]
    }
  }
});

}

function barChart2(nestedData){
	var data = google.visualization.arrayToDataTable([
			nestedData
		]);
	var options = {
  		title:'Resource Project Allocation'
	};

	var chart = new google.visualization.BarChart(document.getElementById('projectsBarGraph'));
  	chart.draw(data, options);
}



function empUnderManagersBar(manager,totalCount,blueCount,redCount){


var barColors = ["#6abf4b", "#e2231a","#fbab18","#00bceb","#eed202"];

var ctx = document.getElementById('managerReportees')
//ctx.style.backgroundColor = '#f8f8f8';

new Chart(ctx, {
  type: "bar",
  data: {
  labels: manager,
  datasets: [{
    label: "Total Employees",
    backgroundColor: '#6abf4b',
    data: totalCount
  },
  {
    label: "Blue Badges",
    backgroundColor: '#00bceb',
    data: blueCount
  },{
    label: "Red Badges",
    fontColor: "white",
    backgroundColor: '#e2231a',
    data: redCount
  }]
},
  options: {
    title: {
      display: true,
      text: "Managers and their reportees",
      fontSize: 18,
      fontColor: 'white'
    },
    scales: {
      xAxes: [{ticks: {min: 0, max:50,fontColor:"white"}}],
      yAxes: [{ticks: {min: 0, max:50,fontColor:"white"}}]
    },
     legend: {
                labels: {
                    fontColor: 'white'
                    
                }
            },
            plugins:{
              labels: {
              render: 'value',
              fontSize: 12,
              fontStyle: 'bold',
              fontColor: 'white',
              fontFamily: '"Lucida Console", Monaco, monospace'
    }
  }
  }
});

}


function drawManagersResourcesCount(manager,totalCount){


var barColors = ["#6abf4b", "#e2231a","#fbab18","#00bceb","#eed202"];

var ctx = document.getElementById('managerReportees')
//ctx.style.backgroundColor = '#f8f8f8';

new Chart(ctx, {
  type: "bar",
  data: {
  labels: manager,
  datasets: [{
    label: "Total Employees",
    backgroundColor: '#6abf4b',
    data: totalCount
  }]
},
  options: {
    title: {
      display: true,
      text: "Managers and their reportees",
      fontSize: 18,
      fontColor: 'white'
    },
    scales: {
      xAxes: [{ticks: {min: 0, max:60,fontColor:"white"}}],
      yAxes: [{ticks: {min: 0, max:60,fontColor:"white"}}]
    },
     legend: {
                labels: {
                    fontColor: 'white'
                    
                }
            },
            plugins:{
              labels: {
              render: 'value',
              fontSize: 12,
              fontStyle: 'bold',
              fontColor: 'white',
              fontFamily: '"Lucida Console", Monaco, monospace'
    }
  }
  }
});

}


function bwUnderManagersBar(managers,mon1,mon2,mon3,mon4,mon5,m1,m2,m3,m4,m5){


var barColors = ["#6abf4b", "#e2231a","#fbab18","#00bceb","#eed202"];

var ctx = document.getElementById('managersBw')
//ctx.style.backgroundColor = '#f8f8f8';

new Chart(ctx, {
  type: "bar",
  data: {
  labels: managers,
  datasets: [{
    label: m1,
    backgroundColor: '#6abf4b',
    data: mon1
  },
  {
    label: m2,
    backgroundColor: '#00bceb',
    data: mon2
  },{
    label: m3,
    fontColor: "white",
    backgroundColor: '#e2231a',
    data: mon3
  },
  {
    label: m4,
    backgroundColor: '#fbab18',
    data: mon4
  },{
    label: m5,
    fontColor: "white",
    backgroundColor: '#1e4471',
    data: mon5
  }]
},
  options: {
    title: {
      display: true,
      text: "Managers and Monthly Available Bandwidth",
      fontSize: 18,
      fontColor: 'white'
    },
    scales: {
      xAxes: [{ticks: {min: 0, max:500,fontColor:"white"}}],
      yAxes: [{ticks: {min: 0, max:600,fontColor:"white"}}]
    },
     legend: {
                labels: {
                    fontColor: 'white'
                    
                }
            },
            plugins:{
              datalabels: {
              display: false,
            }
  }
  }
});

}


function bwUnderManagersResources(managers,mon1,mon2,mon3,mon4,mon5,m1,m2,m3,m4,m5){


var barColors = ["#6abf4b", "#e2231a","#fbab18","#00bceb","#eed202"];

var ctx = document.getElementById('managersResources')
//ctx.style.backgroundColor = '#f8f8f8';

new Chart(ctx, {
  type: "bar",
  data: {
  labels: managers,
  datasets: [{
    label: m1,
    backgroundColor: '#6abf4b',
    data: mon1
  },
  {
    label: m2,
    backgroundColor: '#00bceb',
    data: mon2
  },{
    label: m3,
    fontColor: "white",
    backgroundColor: '#e2231a',
    data: mon3
  },
  {
    label: m4,
    backgroundColor: '#fbab18',
    data: mon4
  },{
    label: m5,
    fontColor: "white",
    backgroundColor: '#1e4471',
    data: mon5
  }]
},
  options: {
    title: {
      display: true,
      text: "Managers and Monthly Available Resources",
      fontSize: 18,
      fontColor: 'white'
    },
    scales: {
      xAxes: [{ticks: {min: 0, max:30,fontColor:"white"}}],
      yAxes: [{ticks: {min: 0, max:15,fontColor:"white"}}]
    },
     legend: {
                labels: {
                    fontColor: 'white'
                    
                }
            },
            plugins:{
              labels: {
              render: 'value',
              fontSize: 12,
              fontStyle: 'bold',
              fontColor: 'white',
              fontFamily: '"Lucida Console", Monaco, monospace'
    }
  }
  }
});

}