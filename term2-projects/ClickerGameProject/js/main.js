//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file
//Warning: Dont edit this file







//////////////////////////////
var cookies = 0;
var rareCookies = 0;
var cpc = 1;
var cursors = 0;
var bakedCookies = 0;
var furnaces = 0;
var money = 0;

function cookieClick(number){
	cookies += number;
	var rareChance = Math.floor((Math.random() * 50) + 1);
	if(rareChance == 5) {
		rareCookies += 1;
	};
	document.getElementById("cookies").innerHTML = cookies;
	document.getElementById('rarecookies').innerHTML = rareCookies;
	document.getElementById("cpc").innerHTML = cpc;
};

function buyCursor(){
	var cursorCost = Math.floor(10 * Math.pow(1.1,cursors)); //works out cost of cursor
	if(cookies >= cursorCost){ //checks that the player can afford
		cursors = cursors + 1; //increases cursors
		cookies = cookies - cursorCost; //removes cookies spent
		document.getElementById('cursors').innerHTML = cursors; //updates number
		document.getElementById('cookies').innerHTML = cookies; //updates cookies
	};
	var nextCost = Math.floor(10 * Math.pow(1.1,cursors)); //increases cost of next cursor
	document.getElementById('cursorCost').innerHTML = nextCost; //updates cursor cost
};

window.setInterval(function(){

		cookieClick(cursors);

}, 1000);

function upgradeCookies(){
	var upgradeCost = Math.floor(100 * Math.pow(1.25,cpc - 1));
	if(cookies >= upgradeCost){
		cpc += 1;
		cookies = cookies - upgradeCost;
	};
	var nextUpgrade = Math.floor(100 * Math.pow(1.25,cpc - 1));
	document.getElementById('upgradeCost').innerHTML = nextUpgrade;
	document.getElementById("cookies").innerHTML = cookies;
	document.getElementById("cpc").innerHTML = cpc;
};

function buyOven(){
	var ovenCost = Math.floor(5 * Math.pow(2.5,furnaces));
	if(rareCookies >= ovenCost){
		furnaces = furnaces + 1;
		rareCookies = rareCookies - ovenCost;
	};
	var nextOven = Math.floor(5 * Math.pow(2.5,furnaces));
	document.getElementById('furnaces').innerHTML = furnaces;
	document.getElementById('rarecookies').innerHTML = rareCookies;
	document.getElementById('ovenCost').innerHTML = nextOven;
};

function ovenBake(){
	if(cookies >= furnaces){
		cookies = cookies - furnaces;
		bakedCookies = bakedCookies + furnaces;
	};
	document.getElementById('bakedcookies').innerHTML = bakedCookies;
};

window.setInterval(function(){

		ovenBake(furnaces);
}, 60000);

function sellBaked(){
	if(bakedCookies > 0){
		bakedCookies = bakedCookies - 1;
		money = money + 1;
	};
	document.getElementById('money').innerHTML = money;
	document.getElementById('bakedcookies').innerHTML = bakedCookies;
};