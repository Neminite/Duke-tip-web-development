var difficulty = 3;
var c1 = new Canvas("zerg");
var c1c = [c1.width / 2, c1.height / 2];
var bullets = [], enemies = [];
var mode = 0; // 0 for bullet, 1 for flaemthorwer
var started = false, time = -25;
var cheats = false, txt = "Click to start!";
var hash=function(inp,p1=197,p2=97){return 4*((inp^p1)^p2)},unhash=function(oup,p1=197,p2=97){return ((oup/4)^p2)^p1};

var hiscore = +unhash(getCookie("zergscore"));
if(hiscore == 0)
	hiscore = 1;

var Bullet = function(facing) {
	this.facing = -facing;
	this.r = dist(0, 0, c1.width, c1.height) / 100;
	this.live = true;
	this.dist = 30;
	this.damage = player.damage;
	this.velo = 2 * dist(0, 0, c1.width, c1.height) / 125;
	this.draw = function() {
		c1.circle(player.x + this.dist * Math.cos(this.facing), player.y + this.dist * Math.sin(this.facing), this.r);
		this.dist += this.velo;
		this.velo -= 0.1;
		if(this.dist > dist(0, 0, c1c[0], c1c[1]) + this.r) {
			this.live = false;
		}
	};
};

var Enemy = function() {
	this.theta = Math.random() * 2 * Math.PI;
	this.size = dist(0, 0, c1.width, c1.height) / 50; //size on canvas in radius
	this.r = Math.sqrt(c1.width * c1.width + c1.height * c1.height) + this.size;
	this.k = Math.random();
	this.live = true;
	this.health = difficulty;
	this.maxhealth = this.health;
	this.draw = function() {
		var wj = Math.floor(10 * Math.cos(this.r / 15 + this.k));
		c1.fill(150 - 4 * wj, 35 + 3 * wj, 10 + wj);
		//console.log(c1.c.fillStyle);
		c1.circle(player.x + this.r * Math.cos(this.theta), player.y + this.r * Math.sin(this.theta), this.size);
		var hp = Math.floor(this.health / this.maxhealth * 255);
		var x = this.r * Math.cos(this.theta) + player.x, y = this.r * Math.sin(this.theta) + player.y;
		if(this.health != this.maxhealth) {
			c1.fill(255 - hp, hp, 0);
			c1.rect(x - 1.1 * this.size, y - 1.5 * this.size, 2.2 * this.size * this.health / this.maxhealth, 0.3 * this.size);
		}
		if (this.r <= player.r) {
			player.health -= this.health;
			this.live = false;
		}
		else if(this.health <= 0) {
			this.live = false;
			player.level();
			player.muns += this.maxhealth;
		}	
		else {
			this.r -= dist(0, 0, c1.width, c1.height) / 500;
		}
	};
};

var Turret = function() {
	this.facing = 0;
	this.flares = 2;
	this.score = 0;
	this.muns = 0;
	this.health = 50;
	this.maxhealth = this.health;
	this.damage = 1;
	this.firerate = 100; //ms
	this.lvl = 1;
	this.timeSinceUp = 0;
	this.timeSinceFlare = 500;
	this.dead = false;
	this.canfire = true;
	this.x = c1c[0];
	this.y = c1c[1];
	this.r = dist(0, 0, c1.width, c1.height) / 25;
	this.draw = function() { 
		this.timeSinceFlare++;
		c1.font(c1.width / 20);
		c1.fill(0, 0, 255);
		c1.c.textAlign = "right";
		c1.text("\uD83D\uDCA3 \u00D7 " + this.flares, c1.width - 10, c1.height - 10);
		c1.c.textAlign = "left";
		this.timeSinceUp++;
		this.facing = (mouseX != c1c[0] ? -(Math.atan((mouseY - this.y)/(mouseX - c1c[0])) + (mouseX > c1c[0]? 0 : Math.PI)) : (mouseY > c1c[1] ? -Math.PI/2 : Math.PI / 2));
		//console.log(this.facing + " " + mouseX + " " + mouseY);
		var fck = [Math.cos(this.facing) * 2 * dist(0, 0, c1.width, c1.height) / 25, -Math.sin(this.facing) * 2 * dist(0, 0, c1.width, c1.height) / 25];
		var lol = [Math.sin(this.facing) * 2 * dist(0, 0, c1.width, c1.height) / 125, Math.cos(this.facing) * 2 * dist(0, 0, c1.width, c1.height) / 125];
		c1.fill(183, 65, 14);
		//console.log([[lol[0] + this.x, lol[1]], [lol[0] + fck[0] + this.x, lol[1] + fck[0]], [-lol[0] + fck[0] + this.x, -lol[1] + fck[0]], [-lol[0] + this.x, -lol[1]]]);
		c1.poly([
			[lol[0] + this.x,				lol[1] + this.y],
			[lol[0] + fck[0] + this.x,		lol[1] + fck[1] + this.y],
			[-lol[0] + fck[0] + this.x,		-lol[1] + fck[1] + this.y],
			[-lol[0] + this.x,				-lol[1] + this.y]]);
		c1.circle(this.x, this.y, this.r);
		k = Math.floor(this.health / this.maxhealth * 255);
		c1.fill(255 - k, k, 0);
		c1.rect(this.x - 1.1 * this.r, this.y - 1.5 * this.r, 2.2 * this.r * this.health / this.maxhealth, 0.3 * this.r);
		c1.fill(0, 0, 200);
		c1.text(this.score, 10, c1.height - 10);
		if(this.timeSinceFlare < 60) {
			c1.fill(255, 255, 255, 1 - this.timeSinceFlare / 60);
			c1.rect(0, 0, c1.width, c1.height);
		}
		c1.font(3 * c1.width / 40);
		if(this.timeSinceUp < 20) {
			c1.fill(0, 0, 255, 1 - this.timeSinceUp / 20);
			c1.text("Level " + this.lvl + " reached!", dist(0, 0, c1.width, c1.height) / 50, 2 * dist(0, 0, c1.width, c1.height) / 25);
		}
		if(this.health <= 0) {
			clearInterval(q);
			clearInterval(drawloop);
			c1.clear();
			c1.fill(255, 0, 0);
			setCookie("zergscore", hash(hiscore));
			c1.c.textAlign = "center";
			var k = "LOSER HAHAHAHHAHAH";
			var j = "ONLY ";
			if(this.score >= hiscore) {
				k = "U GOT TO UR HISCORE,";
				j = "";
			}
			if(cheats)
				k = "U CHEATED!!";
			else
				hiscore = Math.max(hiscore, this.score);
			c1.text(k, c1c[0], c1c[1] - 11 * dist(0, 0, c1.width, c1.height) / 50);
			c1.text("U " + j + "GOT " + this.score + " PTS!!", c1c[0], c1c[1] - 3 * dist(0, 0, c1.width, c1.height) / 50);
			c1.text("HISCORE: " + hiscore, c1c[0], c1c[1] + dist(0, 0, c1.width, c1.height) / 10);
			c1.text("CLICK TO PLAY AGAIN!", c1c[0], c1c[1] + 13 * dist(0, 0, c1.width, c1.height) / 50);
			this.dead = true;
		}
	};
};

var spawnrate = 600;

Turret.prototype.level = function() {
	this.score++;
	if((this.score % 100) == 0) {
		difficulty++;
		this.lvl++;
		if(!cheats)
			this.flares++;
		this.firerate *= 0.9;
		this.timeSinceUp = 0;
		clearInterval(q);
		spawnrate = Math.floor(spawnrate * 0.95);
		q = setInterval(function(){enemies.push(new Enemy());}, spawnrate);
		console.log("Level up!");
	}
};
Turret.prototype.fire = function() {
	if(this.canfire) {
		this.canfire = false;
		setTimeout(function(k){k.canfire = true;}, this.firerate, this);
		bullets.push(new Bullet(this.facing));
	}
};
Turret.prototype.flare = function() {
	if(this.flares > 0 && player.timeSinceFlare > 500) {
		if(!cheats)
			this.flares--;
		this.timeSinceFlare = 0;
		for(var i=0;i<enemies.length;i++) {
			if(enemies[i].live) {
				enemies[i].live = false;
				this.level();
			}
		}
	}
};

var collision = function(bullet, enemy) {
	if(Math.sqrt(bullet.dist * bullet.dist + enemy.r * enemy.r - 2 * bullet.dist * enemy.r * Math.cos(bullet.facing - enemy.theta)) <= bullet.r + enemy.size) {
		enemy.health -= bullet.damage;
		bullet.live = false;
		//console.log(enemy.health);
	}
};

var player = new Turret();


c1.nostroke();


draw = function() {
	c1.clear();
	c1.fill(200, 200, 0);
	time++;
	for(var i=0;i<bullets.length;i++)
		if (bullets[i].live) {
			bullets[i].draw();
			for(var j=0;j<enemies.length;j++)
				if(enemies[j].live) {
					collision(bullets[i], enemies[j]); // <-- problem
				}
		}
	for(var i=0;i<enemies.length;i++)
		if(enemies[i].live) {
			enemies[i].draw();
		}
	player.draw();
	if((!started || (cheats && time < 100)) && Math.floor((time % 50) / 25) == 0) {
		c1.c.textAlign = "center";
		c1.text(txt, c1c[0], c1c[1] / 2);
	}
	if(keys[32])
		player.fire();
	if(keys[13])
		player.flare();
	if(keys[71] && !cheats) {
		player.firerate = 0;
		cheats = true;
		time = 0;
		player.flares = 32767;
		player.damage = 3;
		txt = "God Mode ON!";
		player.maxhealth = player.health = 2;
	}

};

drawloop = setInterval(draw, 20);
c1.cvs.onclick = function(e) {
	if(!started) {
		started = true;
		q = setInterval(function(){enemies.push(new Enemy());}, spawnrate);
	}
	else if(player.dead)
		location.reload();
	else
		player.fire();
};
c1.cvs.oncontextmenu = function(e) {
	player.flare();
	return false;
}