// initializer for drama buttons
for(var i = 1; i < 11; i++)
{
	var dbName = getDramaButtonName(i);
	var fileName = getImageFileName(i);
	document.getElementById(dbName).addEventListener("click", vanish);
//	document.getElementById(dbName).style.backgroundImage = fileName;
}

// returns the url for a dramaButton image
function getImageFileName(num)
{
	return ("url('Images/drama" + num + ".png')");
}

// returns the id of a dramaButton
function getDramaButtonName(num)
{
	return ("dramaButton" + num);
}

// causes the passed element to disappear
function vanish()
{
	this.style.display = "none";
}

// causes all dramaButtons to disappear
function vanishAll()
{
	for(var i = 1; i < 11; i++)
	{
		var dbName = getDramaButtonName(i);
		var fileName = getImageFileName(i);
		document.getElementById(dbName).style.display = "none";
	}
}

// causes all dramabuttons to appear
function unvanishAll()
{
	for(var i = 1; i < 11; i++)
	{
		var dbName = getDramaButtonName(i);
		var fileName = getImageFileName(i);
		document.getElementById(dbName).style.display = "inline";
	}
}
