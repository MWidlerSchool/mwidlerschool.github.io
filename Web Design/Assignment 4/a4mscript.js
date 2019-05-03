// initializer for drama buttons
for(var i = 1; i < 11; i++)
{
	var dbName = getDramaButtonName(i);
	/*
	document.getElementById(dbName).addEventListener("click", vanish);
	document.getElementById(dbName).innerHTML = getImageString(i) + '<p class="closeField">&times</p>';
	*/
	$(dbName).on("click", vanish);
	$(dbName).html(getImageString(i) + '<p class="closeField">&times</p>');
}

// returns the HTML for a dramaButton image
function getImageString(num)
{
	return '<img class="buttonImg" src="Images/drama' + num + '.png">';
}

// returns the id of a dramaButton
function getDramaButtonName(num)
{
	//return "dramaButton" + num;
	return "#" + "dramaButton" + num;
}

// causes the passed element to disappear
function vanish()
{
	this.style.display = "none";
}

// causes all dramaButtons to disappear
function vanishAll()
{
	$(".dramaButton").hide();
	/*
	for(var i = 1; i < 11; i++)
	{
		var dbName = getDramaButtonName(i);
		document.getElementById(dbName).style.display = "none";
		
	}*/
}

// causes all dramabuttons to appear
function unvanishAll()
{
	$(".dramaButton").show();
	/*
	for(var i = 1; i < 11; i++)
	{
		var dbName = getDramaButtonName(i);
		document.getElementById(dbName).style.display = "inline";
	}
	*/
}
