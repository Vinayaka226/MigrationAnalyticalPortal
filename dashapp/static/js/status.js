function getStatus(){
  var canvas = document.getElementById("status");
  var ctx = canvas.getContext("2d");
  ctx.beginPath();
  ctx.arc(95,50,40,0,2*Math.PI);
  ctx.stroke();
  ctx.fillStyle = 'red';
  ctx.fill();
}
