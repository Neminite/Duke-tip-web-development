var getID = function(x){return document.getElementById(x);}
var money = 0;
var increase = 1;
var inccost = 10;
var incamt = 1;
var doucost = 500;
var automoney = [0, 2, 10, 75, 250, 1500, 5000, 17500, 75000, 300000, 1000000, 6000000, 20000000, 200000000, 1000000000, 50000000000];
var autolvl = 0;
var autotime = 2000;
var autocost = 100;
var autotimecost = 10000;

function updateTickers() {
	getID("money").innerHTML = "$" + money + "<br>$" + increase + " per click<br>$" + ((automoney[autolvl]/autotime)*1000) + " / sec from Autos";
	getID("plusone").innerHTML = "Upgrade: $"+inccost;
	getID("double").innerHTML = "Double: $"+doucost;
	getID("splitter").innerHTML = "Double Autos: $"+autotimecost;
	getID("autotune").innerHTML = "Upgrade Autos: $"+autocost;
}

function getCookie(name) {
    var name = name + "=";
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
function getCookieData() {
	cookie = +getCookie("verify");
	if (cookie == 1) {
		money = +getCookie("money");
		increase = +getCookie("increase");
		inccost = +getCookie("inccost");
		incamt = +getCookie("incamt");
		doucost = +getCookie("doucost");
		autolvl = +getCookie("autolvl");
		autotime = +getCookie("autotime");
		autocost = +getCookie("autocost");
		autotimecost = +getCookie("autotimecost");
	};
	return 0;
}
getCookieData()

function restart() {
	money = 0;
	increase = 1;
	inccost = 10;
	incamt = 1;
	doucost = 500;
	autolvl = 0;
	autotime = 2000;
	autocost = 100;
	autotimecost = 10000;
	updateTickers();
	save();
}

function buttonclick() {
	money += increase;
	updateTickers();
};

function upgrade() {
	if (money >= inccost){
		money -= inccost;
		increase += incamt;
		inccost *= 2;
		updateTickers();
	}
};

function doubleclick() {
	if (money >= doucost) {
		money -= doucost;
		doucost *= 4;
		increase *= 2;
		incamt *= 2;
		updateTickers();
	}
};

function auto1() {
	money += automoney[autolvl]
	updateTickers();
};

function doubleauto() {
	if (money >= autotimecost) {
		money -= autotimecost;
		autotimecost *= 10;
		clearInterval(v);
		autotime /= 2;
		

		v = setInterval(auto1, autotime);
		updateTickers();
	}
};

function upgradeautos() {
	if (autolvl < automoney.length-1 && money >= autocost) {
		money -= autocost;
		autocost *= 7;
		autolvl += 1;
		updateTickers();
	}
};

var v = setInterval(auto1, autotime);

function save() {
	document.cookie = "verify=1;";
	document.cookie = "money="+money+";";
	document.cookie = "increase="+increase+";";
	document.cookie = "inccost="+inccost+";";
	document.cookie = "incamt="+incamt+";";
	document.cookie = "doucost="+doucost+";";
	document.cookie = "autolvl="+autolvl+";";
	document.cookie = "autotime="+autotime+";";
	document.cookie = "autocost="+autocost+";";
	document.cookie = "autotimecost="+autotimecost+";";
	document.cookie = "expires="+(365*52*7*24*60*60*1000)+";";
	return 0;
}