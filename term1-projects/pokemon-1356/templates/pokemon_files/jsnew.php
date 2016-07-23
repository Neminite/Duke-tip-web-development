//0.0041

function finishRename() {
		var newname = document.getElementById('renamebox').value
	newname = newname.replace(/&/g,'%26');

	document.getElementById('rename').innerHTML = 'Processing...';
	if (window.XMLHttpRequest) {
		xmlhttp = new XMLHttpRequest();
	}
	else {
		xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
	}
	xmlhttp.onreadystatechange = function () {
		if (xmlhttp.readyState == 4) {
			if (xmlhttp.responseText == 1) {
				location.reload(true);
			} else {
						alert('Failed: '+xmlhttp.responseText);
					document.getElementById('rename').innerHTML = 'Try Again';
			}
		}
	};
	xmlhttp.open('POST', '/functions.php', true);
	xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	xmlhttp.send('newname=' + newname + '&id=2382'+'&action=renamegame');
	
}
function finishMerge() {
	var newgame = document.getElementById('gamesel').value;
	document.getElementById('merge').innerHTML = 'Processing...';
	var curgame = 2382;
	if (newgame == '123456789') {
		alert ('Choose a Game');
		return;
	}
	newgame = newgame.replace(/&/g,'%26');

	if (window.XMLHttpRequest) {
		xmlhttp = new XMLHttpRequest();
	}
	else {
		xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
	}
	xmlhttp.onreadystatechange = function () {
		if (xmlhttp.readyState == 4) {
			if (xmlhttp.responseText == 1) {
				alert('Success! (I think)');
			} else {
						alert('Failed: '+xmlhttp.responseText);
					document.getElementById('merge').innerHTML = 'Try Again';
			}
		}
	};
	xmlhttp.open('POST', '/functions.php', true);
	xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	xmlhttp.send('id=' + curgame + '&newgame='+newgame+'&action=mergegame');
	
}
function youTube(id) {
	document.getElementById('yt'+id).innerHTML = '...';
				var xmlhttp = [];
	if (window.XMLHttpRequest) {
		xmlhttp[id] = new XMLHttpRequest();
	}
	else {
		xmlhttp[id] = new ActiveXObject('Microsoft.XMLHTTP');
	}
	xmlhttp[id].onreadystatechange = function () {
		if (xmlhttp[id].readyState == 4) {
			if (xmlhttp[id].responseText == 1) {
				document.getElementById('yt'+id).innerHTML = 'Added';
			} else {
				alert('Failed: '+xmlhttp[id].responseText);
			}
		}
	};
	xmlhttp[id].open('POST', '/functions.php', true);
	xmlhttp[id].setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	xmlhttp[id].send('id='+id+'&action=uploadvideo');
	
}
