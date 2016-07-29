function randint(min, max) {
	return Math.floor(Math.random() * (max - min)) + min;
}
function dist(x1, y1, x2, y2) {
	return Math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1));
}
var keys = [], keysPressed = 0, mouseX = 0, mouseY = 0;
var ufill="FILL", ustroke="STROKE", ufillstroke="FILLSTROKE";

var Canvas = function(id) {
	this.id = id;
	this.cvs = document.getElementById(id);
	this.cvs.contentEditable = true;
	this.cvs.style.cursor = "crosshair";
	this.cvs.autofocus = true;
	this.cfill = "#ffffff";
	this.cstroke = "#000000";
	this.cvs.onmousemove = function(e) {
		mouseX = e.clientX - this.offsetLeft;
		mouseY = e.clientY - this.offsetTop;
	};
	this.cvs.onkeydown = function(e) {
		keys[e.keyCode] = true;
		keysPressed++;
	};
	this.cvs.onkeyup = function(e) {
		keys[e.keyCode] = false;
		keysPressed--;
	};
	this.c = this.cvs.getContext("2d");
	this.width = Number(this.cvs.width);
	this.height = Number(this.cvs.height);
	this.cursor = function(name) {
		this.cvs.style.cursor = name;
	}
};

Canvas.prototype.fill = function(rval, gval, bval, aval=1) {
	this.cfill = "rgba(" + rval + ", " + gval + ", " + bval + ", " + aval + ")";
};
Canvas.prototype.stroke = function(r, g, b) {
	this.cstroke = "rgb(" + r + ", " + g + ", " + b + ")";
};
Canvas.prototype.nostroke = function() {
	this.cstroke = "rgba(0, 0, 0, 0)";
};
Canvas.prototype.clear = function(r, g, b) {
	this.c.clearRect(0, 0, this.width, this.height);
};
Canvas.prototype.font = function(size, font="Arial") {
	this.c.font = size + "px " + font;
};
Canvas.prototype.text = function(text, x, y) {
	this.c.beginPath();
	this.c.fillStyle = this.cfill;
	this.c.strokeStyle = this.cstroke;
	this.c.fillText(text, x, y);
	this.c.closePath();
};
Canvas.prototype.circle = function(x, y, r, mode=ufill) {
	this.c.beginPath();
	this.c.fillStyle = this.cfill;
	this.c.strokeStyle = this.cstroke;
	this.c.arc(x, y, r, 0, 2*Math.PI);
	//console.log(mode);
	this.c.fill();
	this.c.stroke();
	this.c.closePath();
	//console.log("Coicle drowen");
};

Canvas.prototype.rect = function(x, y, w, h) {
	this.c.beginPath();
	this.c.fillStyle = this.cfill;
	this.c.strokeStyle = this.cstroke;
	this.c.rect(x, y, w, h);
	this.c.fill();
	this.c.stroke();
	this.c.closePath();
};

Canvas.prototype.image = function(img, x, y, w=img.width, h=img.height) {
	if(!w) {
		w = +img.width;
		h = +img.height;
	}
	else if (!h) {
		w = +w;
		h = +img.height*w/+img.width;
	}
	this.c.beginPath();
	this.c.drawImage(img, x, y, width, height);
	this.c.endPath();
};
Canvas.prototype.poly = function(arr) {
	this.c.beginPath();
	this.c.fillStyle = this.cfill;
	this.c.strokeStyle = this.cstroke;
	this.c.moveTo(arr[0][0], arr[0][1]);
	for(var i=1; i<arr.length;i++) 
		this.c.lineTo(arr[i][0], arr[i][1]);
	this.c.fill();
	this.c.closePath();
};
var draw = function() {
	{{draw}}
};
drawloop = setInterval(draw, 20);
function setCookie(cname, cvalue) {
    var d = new Date();
    d.setTime(d.getTime() + (365*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
} 
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length,c.length);
        }
    }
    return "";
} 