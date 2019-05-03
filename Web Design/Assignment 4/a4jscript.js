var slideIndex = 0;
var editing = false;
$("#justAButton").on("click", hideAndNotify);

showSlides();

function showSlides() {
  slideIndex++;
  if(slideIndex > 4)
	slideIndex = 0;
  
  $(".slides").hide();
  $("#slide" + slideIndex).show();

  setTimeout(showSlides, 3000); // Change image every 3 seconds
}

function hideAndNotify()
{
	$("#justAButton").hide();
    clickedFunction(2);
}

function clickedFunction(option) {
    var paraNode = document.getElementById("editMe");
    if (editing == false) {
        editing = true;
        var paraText = document.getElementById("editMe").textContent;
        document.getElementById("justAButton").style.visibility='visible';
        var para = document.createElement('TEXTAREA');
        para.style.height='200px';
        para.style.width='400px';
    }
    else if (option == 2 && editing == true){
        var paraText = document.getElementById("editMe").value;
        editing = false;
        var para = document.createElement('P');
    }
    try{
        para.id="editMe";
        var parentOfP = paraNode.parentNode;
        parentOfP.insertBefore(para,paraNode);
        para.innerHTML = paraText;
        parentOfP.removeChild(paraNode);
    } catch (Exception) {
        // just practicing my try/catch blocks
        console.log("Nothing to see here, move along");
        return;
    }
}

