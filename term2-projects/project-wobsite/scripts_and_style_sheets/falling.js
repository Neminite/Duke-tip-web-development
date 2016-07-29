canvas = new Canvas("falling");
canvas.cursor("default");
canvas.nostroke();
var objects = [];
var bullets = [];

var Obj = function(x) {
	this.x = x;
	this.y = 0;
	this.radius = 5;
	this.speed = 1;
	this.draw = function() {
		this.y += player.weapon+1;
		canvas.circle(this.x, this.y, this.radius);
	};
	this.collision = function(obj) {
		if (dist(obj.x, obj.y, this.x, this.y) < this.radius+obj.rad) {
			return true;
		}	return false;
	};
};

var Bullet = function(x, y) {
	this.x = x;
	this.y = y;
	this.rad = 4;
	this.speed = 4;
	this.draw = function() {
		this.y -= this.speed;
		canvas.circle(this.x, this.y, this.rad);
	};
};

var Flame = function(x, y) {
	this.x = x;
	this.y = y;
	this.rad = 2;
	this.speed = 1;
	this.color = [255, 0, 0, 1];
	this.dead = false;
	this.draw = function() {
		if (!this.dead){
			this.y -= this.speed;
			this.rad += 0.35;
			if (this.color[1] >= 255) {
				if (this.color[3] <= 0.1) {
					this.dead = true;
				} else {this.color[3] -= 0.05;}
			} else {this.color[1] += 5;}
			canvas.fill(...this.color);
			canvas.circle(this.x, this.y, Math.floor(this.rad));
		}else{this.rad=0;}
	}
};

var Bomb = function(x, y) {
	this.x = x;
	this.y = y;
	this.rad = 7;
	this.speed = 5;
	this.color = [0, 0, 0, 1];
	this.dead = false;
	this.exploding = false;
	this.draw = function() {
		if (!this.dead) {
			this.y -= this.speed;
			if(this.speed > 0){this.speed -= 0.15;}
			else {
				if(!this.exploding){this.exploding = true; this.color = [255, 0, 0, 1]};
				if (this.exploding){
					this.color[1] += 10;
					this.color[3] -= 2/51;
					this.rad += 4;
					if (this.color[3] <= 0.1) {
						this.dead = true;
					}
				}
			}
			canvas.fill(...this.color);
			canvas.circle(this.x, this.y, this.rad);
		}
	}
};

var Player = function() {
	this.x = 200;
	this.y = 400;
	this.rad = 10;
	this.speed = 5;
	this.canfire = true;
	this.lives = Math.pow(10,1);
	this.firerate = 150; //ms
	this.score = 0;
	this.weapon = 0;
	this.left = function() {
		this.x -= this.speed;
	};
	this.right = function() {
		this.x += this.speed;
	};
	this.fire = function() {
		if (this.canfire) {
			if (this.weapon == 0) {
				this.canfire = false;
				setTimeout(function(cls){cls.canfire = true;}, this.firerate, this);
				bullets.push(new Bullet(mouseX, this.y));
			}
			else if (this.weapon == 1) {
				this.canfire = false;
				setTimeout(function(cls){cls.canfire = true;}, 150, this);
				bullets.push(new Flame(mouseX, this.y));
			}
			else if (this.weapon == 2){
				this.canfire = false;
				setTimeout(function(cls){cls.canfire = true;}, 500, this);
				bullets.push(new Bomb(mouseX, this.y));
			}
		}
	};
	this.draw = function() {
		//this.x = 
		canvas.fill(0,0,0);
		canvas.circle(mouseX, this.y, this.rad);
	};
};

player = new Player();

var draw = function() {
	canvas.clear();
	canvas.fill(0,0,0);
	canvas.text("Lives: "+player.lives, 20, 20);
	canvas.text("Score: "+player.score, 20, 40)
	for (var i=0; i<objects.length; i++) {
		canvas.fill(200, 100, 100);
		objects[i].draw();
		for (var j=0; j<bullets.length; j++) {
			if (objects[i].collision(bullets[j]) && player.weapon != 2) {
				objects.splice(i, 1);
				if (player.weapon == 0) {bullets.splice(j, 1);}
				player.score += 50;
			}
			else if (objects[i].y > canvas.height) {
				player.lives -= 1;
				objects.splice(i, 1);
			}
			else if (player.weapon == 2 && objects[i].collision(bullets[j])) {
				if (bullets[j].exploding) {
					objects.splice(i, 1);
					player.score += 50;
				}
			}
			if ((player.weapon == 1 || player.weapon == 2) && (bullets[j].dead)) {bullets.splice(j, 1)}
		}
	}
	for(var i=0;i<bullets.length; i++) {
		canvas.fill(150,150,150);
		if (bullets[i].y > 0) {
			bullets[i].draw();
		}
		else {
			bullets.splice(i, 1);
		}
	}
	player.draw();
	checkKeys();
};

var fall = function() {objects.push(new Obj(randint(0, canvas.height)))};

checkKeys = function() {/*
	if (keys[37]) {
		player.left();
	}
	else if (keys[39]) {
		player.right();
	}
	else */if ((keys[32])) {
		player.fire();
	}
};

var checkDeath = function() {
	if (player.lives <= 0) {
		clearInterval(droploop);
		clearInterval(drawloop);
		canvas.clear();
		canvas.fill(255, 0, 0);
		canvas.font(20, "Arial");
		canvas.text("Good Job!\nYour score: "+player.score, 75, 150);
	}
};

droprate = 400;

var level = function(l) {
	clearInterval(droploop);
	droprate = Math.floor(droprate * 0.5);
	droploop = setInterval(fall, droprate);
	player.weapon = l;
}


var flamecheck = setInterval(function(){if (player.score >= 5000) {clearInterval(flamecheck); level(1);}}, 50)
var bombcheck = setInterval(function(){if (player.score >= 15000) {clearInterval(bombcheck); level(2);}}, 50)
var droploop = setInterval(fall, droprate);
var drawloop = setInterval(draw, 20);
var deathloop = setInterval(checkDeath, 100);