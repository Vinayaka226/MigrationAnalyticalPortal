function drawMyPercent(percent, color){
  var  canvas = document.getElementById("myPercent");
      var  context = canvas.getContext("2d");
      context.clearRect(0,0,canvas.width, canvas.height);
      var centerX = canvas.width / 2;
      var centerY = canvas.height / 2;
      var radius = canvas.height / 2;

      context.beginPath();
      context.arc(centerX, centerY, radius, Math.PI*0.10, Math.PI*-1.1, true);

      var gradience = context.createRadialGradient(centerX, centerY, radius-radius/3, centerX, centerY, radius-radius/8);
       gradience.addColorStop(0, color);
       gradience.addColorStop(1, '#000000');

       context.fillStyle = gradience;
       context.fill();
       context.closePath();
       context.restore();

	context.beginPath();
	context.strokeStyle = '#ffff00';
	context.translate(centerX,centerY);
	var increment = 3;
	context.font="15px Helvetica";
	for (var i=-18; i<=18; i++)
	{
		angle = Math.PI/30*i;
		sineAngle = Math.sin(angle);
		cosAngle = -Math.cos(angle);

		if (i % 5 == 0) {
		context.lineWidth = 8;
		iPointX = sineAngle *(radius -radius/4);
		iPointY = cosAngle *(radius -radius/4);
		oPointX = sineAngle *(radius -radius/7);
		oPointY = cosAngle *(radius -radius/7);

		wPointX = sineAngle *(radius -radius/2.5);
		wPointY = cosAngle *(radius -radius/2.5);
		context.fillText((i+18)*increment,wPointX-2,wPointY+4);
		}
		else
		{
		context.lineWidth = 2;
		iPointX = sineAngle *(radius -radius/5.5);
		iPointY = cosAngle *(radius -radius/5.5);
		oPointX = sineAngle *(radius -radius/7);
		oPointY = cosAngle *(radius -radius/7);
		}
		context.beginPath();
		context.moveTo(iPointX,iPointY);
		context.lineTo(oPointX,oPointY);
		context.stroke();
		context.closePath();
	}
	var numOfSegments = percent/increment;
	numOfSegments = numOfSegments -18;
	angle = Math.PI/30*numOfSegments;
	sineAngle = Math.sin(angle);
	cosAngle = -Math.cos(angle);
	pointX = sineAngle *(3/4*radius);
	pointY = cosAngle *(3/4*radius);

	context.beginPath();
	context.strokeStyle = '#000000';
	context.arc(0, 0, 19, 0, 2*Math.PI, true);
	context.fill();
        context.closePath();

	context.beginPath();
	context.lineWidth=4;
	context.moveTo(0,0);
        context.lineTo(pointX,pointY);
        context.stroke();
        context.closePath();
        context.restore();
        context.translate(-centerX,-centerY);
}
