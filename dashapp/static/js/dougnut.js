function redBlue(count){

var xValues = ["Red", "Blue"];
var ctx = document.getElementById('redBlueDougnut')
//ctx.style.backgroundColor = '#f8f8f8';
//var yValues = [55, 49, 44, 24, 15];
var barColors = [
  "#e2231a",
  "#00bceb",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: count
    }]
  },
  options: {
    title: {
      display: true,
      text: "Blue and Red Badges Employee count",
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


function technoDougnut(technologies,technoCount){

var xValues = technologies;
var ctx = document.getElementById('technoCount')
//ctx.style.backgroundColor = '#f8f8f8';
//var xValues = ['abc', 'def','abc', 'def','abc', 'def','abc', 'def','abc', 'def']
//var yValues = [55, 49, 44, 24, 15,25,30,45,50,20];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145",
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: technoCount
    }]
  },
  options: {
    title: {
      display: true,
      text: "Employes Count skilled in Enterprise, SP & Automation Technologies",
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

function leadsvsLeadsCapable(labels,blueBadgesCount){

var xValues = labels;
var ctx = document.getElementById('leadscapableLeads')
//ctx.style.backgroundColor = '#f8f8f8';
//var yValues = [55, 49, 44, 24, 15];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    fontColor: "white",
    datasets: [{
      backgroundColor: barColors,
      data: blueBadgesCount,
    }]
  },
  options: {
    title: {
      display: true,
      text: "Total, Leads and Capable Leads",
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


function blueWithoutProjects(labels,resourcesWithorWithoutProject){

var xValues = labels;
var ctx = document.getElementById('blueWithoutProjects')

var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    fontColor: "white",
    datasets: [{
      backgroundColor: barColors,
      data: resourcesWithorWithoutProject,
    }]
  },
  options: {
    title: {
      display: true,
      text: "Blue Badges count not aligned to any project",
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


function redWithoutProjects(labels,resourcesWithorWithoutProject){

var xValues = labels;
var ctx = document.getElementById('redWithoutProjects')

var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    fontColor: "white",
    datasets: [{
      backgroundColor: barColors,
      data: resourcesWithorWithoutProject,
    }]
  },
  options: {
    title: {
      display: true,
      text: "Red Badges count not aligned to any project",
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


function resourcesSkills(labels,resourcesWithorWithoutProject){

var xValues = labels;
var ctx = document.getElementById('redWithoutProjects')

var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    fontColor: "white",
    datasets: [{
      backgroundColor: barColors,
      data: resourcesWithorWithoutProject,
    }]
  },
  options: {
    title: {
      display: true,
      text: "Enterprise Total Vs Free resources",
      fontColor: "white",
      fontSize: 14
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


function scriptingResourcesShare(labels,resourcesWithorWithoutProject){

var xValues = labels;
var ctx = document.getElementById('redWithoutProjects')

var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    fontColor: "white",
    datasets: [{
      backgroundColor: barColors,
      data: resourcesWithorWithoutProject,
    }]
  },
  options: {
    title: {
      display: true,
      text: "Enterprise  Vs SP Scripting resources",
      fontColor: "white",
      fontSize: 14
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


function projectsAutomated(labels,projectsCount){

var xValues = labels;
var ctx = document.getElementById('totalVsAutomated')

var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    fontColor: "white",
    datasets: [{
      backgroundColor: barColors,
      data: projectsCount,
    }]
  },
  options: {
    title: {
      display: true,
      text: "Total  Vs Automated Projects",
      fontColor: "white",
      fontSize: 14
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

function assignedVsNotAssignedToProjects(labels,assignedCount){

var xValues = labels;
var ctx = document.getElementById('assignedVsNotAssignedToProjects')

var barColors = [
  "#00bceb",
  "#6abf4b",
  "#e2231a",
  "#00aba9",
  "#1e7145",
  "#00aba9"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    fontColor: "white",
    datasets: [{
      backgroundColor: barColors,
      data: assignedCount,
    }]
  },
  options: {
    title: {
      display: true,
      text: "Miscellaneous Skills Count",
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


function certsDougnut(labels,assignedCount){

var xValues = labels;
var ctx = document.getElementById('certiCount')

var barColors = [
  "#2b5797",
  "#6abf4b",
  "#b91d47",
  "#00bceb",
  "#00aba9",
  "#1e7145"
];

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: xValues,
    fontColor: "white",
    datasets: [{
      backgroundColor: barColors,
      data: assignedCount,
    }]
  },
  options: {
    title: {
      display: true,
      text: "Certificates and respective resources count",
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