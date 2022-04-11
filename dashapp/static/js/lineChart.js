function lineChart(xAxis,completedSites,windowSuccessRate){

var ctx = document.getElementById('myLine')
//ctx.style.backgroundColor = '#f8f8f8';
new Chart(ctx, {
  type: "line",
  data: {
    labels: xAxis,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(226,35,26,0.3)",
      borderColor: "rgba(226,35,26,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Sites Migrated',
      data: completedSites
    },{
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(106,191,75,0.4)",
      borderColor: "rgba(106,191,75,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Window Success Rate',
      data: windowSuccessRate
    }
    /*{
      fill: false,
      lineTension: 2,
      backgroundColor: "rgba(238,210,2,0.6)",
      borderColor: "rgba(238,210,2,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Windows Planned',
      data: custSatisfaction
    }*/
    ]
  },
  options: {
    legend: {display: true,
    		labels: {
                    fontColor: "white",
                    //fontSize: 18
                }
            },
    scales: {
      yAxes: [
      {ticks: {min: 1, max:140, fontColor:'white'}
  	  }
      ],
      xAxes:[
      {
      	ticks: {
      		fontColor:'white'
      	}
      }
      ]
    },
    title:{
            display: true,
            fontColor: "white",
            text: 'Completed Sites and Success Rate for Each Week',
            fontSize: 18
          }
  }
});

}

function lineChart2(xAxis,yAxis1,yAxis2,yAxis3){

var ctx = document.getElementById('myLine2')
//ctx.style.backgroundColor = '#f8f8f8';
new Chart(ctx, {
  type: "line",
  data: {
    labels: xAxis,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(226,35,26,0.5)",
      borderColor: "rgba(226,35,26,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Devices Planned',
      data: yAxis1
    },/*{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(106,191,75,0.8)",
      borderColor: "rgba(106,191,75,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Customer Satisfaction',
      data: yAxis2
    },*/
    {
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(238,210,2,0.5)",
      borderColor: "rgba(238,210,2,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Devices Migrated',
      data: yAxis3
    }
    ]
  },
  options: {
    legend: {display: true,
    		labels: {
                    fontColor: "white",
                    //fontSize: 18
                }
            },
    scales: {
      yAxes: [
      {ticks: {min: 10, max:30, fontColor:'white'}}
      ],
      xAxes:[
      {
      	ticks: {
      		fontColor:'white'
      	}
      }
      ]
    },
    title:{
            display: true,
            fontColor: "white",
            text: 'Windows Planned, Completed and Customer Satisfaction',
            fontSize: 18
          }
  }
});

}


function lineChart3(xAxis,yAxis1){

var ctx = document.getElementById('myLine3')
//ctx.style.backgroundColor = '#f8f8f8';
new Chart(ctx, {
  type: "line",
  data: {
    labels: xAxis,
    datasets: [{
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(238,210,2,0.5)",
      borderColor: "rgba(238,210,2,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Status Value (1 => RED, 2=> AMBER, 3 => GREEN)',
      data: yAxis1
    },/*{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(106,191,75,0.8)",
      borderColor: "rgba(106,191,75,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Customer Satisfaction',
      data: yAxis2
    },
    {
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(238,210,2,0.5)",
      borderColor: "rgba(238,210,2,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Devices Migrated',
      data: yAxis3
    }*/
    ]
  },
  options: {
    legend: {display: true,
        labels: {
                    fontColor: "white",
                    //fontSize: 18
                }
            },
    scales: {
      yAxes: [
      {ticks: {min: 0, max:3, fontColor:'white'}}
      ],
      xAxes:[
      {
        ticks: {
          fontColor:'white'
        }
      }
      ]
    },
    title:{
            display: true,
            fontColor: "#00bceb",
            text: 'Status Information',
            fontSize: 30
          }
  }
});

}


function automationAcrossMigration(xAxis,yAxis1){

var ctx = document.getElementById('averageAutomationAcrossProjects')
//ctx.style.backgroundColor = '#f8f8f8';
new Chart(ctx, {
  type: "line",
  data: {
    labels: xAxis,
    datasets: [{
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(106,191,75,0.5)",
      borderColor: "rgba(106,191,75,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Automation in %',
      data: yAxis1
    }/*{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(106,191,75,0.8)",
      borderColor: "rgba(106,191,75,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Customer Satisfaction',
      data: yAxis2
    },
    {
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(238,210,2,0.5)",
      borderColor: "rgba(238,210,2,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Devices Migrated',
      data: yAxis3
    }*/
    ]
  },
  options: {
    legend: {display: true,
        labels: {
                    fontColor: "white",
                    //fontSize: 18
                }
            },
    scales: {
      yAxes: [
      {ticks: {min: 20, max:90, fontColor:'white'}}
      ],
      xAxes:[
      {
        ticks: {
          fontColor:'white'
        }
      }
      ]
    },
    title:{
            display: true,
            fontColor: "white",
            text: '',
            fontSize: 18
          }
  }
});

}




function individualCertsInfo(xAxis,yAxis1){

var ctx = document.getElementById('individualCertsInfo')
//ctx.style.backgroundColor = '#f8f8f8';
new Chart(ctx, {
  type: "line",
  data: {
    labels: xAxis,
    datasets: [{
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(106,191,75,0.5)",
      borderColor: "rgba(106,191,75,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Certifications of Individual (1 = Certified)',
      data: yAxis1
    }
    ]
  },
  options: {
    legend: {display: true,
        labels: {
                    fontColor: "white",
                    //fontSize: 18
                }
            },
    scales: {
      yAxes: [
      {ticks: {min: 0, max:1, fontColor:'white'}}
      ],
      xAxes:[
      {
        ticks: {
          fontColor:'white'
        }
      }
      ]
    },
    title:{
            display: true,
            fontColor: "white",
            text: 'Certificate Information',
            fontSize: 20
          }
  }
});

}



function individualSkillInfo(xAxis,yAxis1){

var ctx = document.getElementById('individualSkills')
//ctx.style.backgroundColor = '#f8f8f8';
new Chart(ctx, {
  type: "line",
  data: {
    labels: xAxis,
    datasets: [{
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(230, 92, 0,0.6)",
      borderColor: "rgba(230, 92, 0,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "blue",
      label: 'Skills Info (0 = No Knowledge, 1 = Specialist, 2 = SME, 3 = Lead)',
      data: yAxis1
    }
    ]
  },
  options: {
    legend: {display: true,
        labels: {
                    fontColor: "white",
                    //fontSize: 18
                }
            },
    scales: {
      yAxes: [
      {ticks: {min: 0, max:3, fontColor:'white'}}
      ],
      xAxes:[
      {
        ticks: {
          fontColor:'white',
          fontSize: 14
        }
      }
      ]
    },
    title:{
            display: true,
            fontColor: "white",
            text: "Individual's Skills Information",
            fontSize: 20
          }
  }
});

}

function individualSkillInfoSP(xAxis,yAxis1){

var ctx = document.getElementById('individualSkillsSP')
//ctx.style.backgroundColor = '#f8f8f8';
new Chart(ctx, {
  type: "line",
  data: {
    labels: xAxis,
    datasets: [{
      fill: true,
      lineTension: 0,
      backgroundColor: "rgba(100,187,227,0.8)",
      borderColor: "rgba(100,187,227,1.0)",
      hoverBackgroundColor: "rgba(232,105,90,0.8)",
      hoverBorderColor: "orange",
      label: 'Skills Info (0 = No Knowledge, 1 = Specialist, 2 = SME, 3 = Lead)',
      data: yAxis1
    }
    ]
  },
  options: {
    legend: {display: true,
        labels: {
                    fontColor: "white",
                    //fontSize: 18
                }
            },
    scales: {
      yAxes: [
      {ticks: {min: 0, max:3, fontColor:'white'}}
      ],
      xAxes:[
      {
        ticks: {
          fontColor:'white',
          fontSize: 14
        }
      }
      ]
    },
    title:{
            display: true,
            fontColor: "white",
            text: "Individual's Skills Information",
            fontSize: 20
          }
  }
});

}


