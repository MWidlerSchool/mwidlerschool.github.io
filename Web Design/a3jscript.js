var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("slides");
  //var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  //for (i = 0; i < dots.length; i++) {
//    dots[i].className = dots[i].className.replace(" active", "");
 // }
  slides[slideIndex-1].style.display = "block";
 // dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}

var editing = false;

var button = document.getElementById("justAButton").addEventListener("click", function(){
    document.getElementById("justAButton").style.visibility='hidden';
    clickedFunction(2);
});

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
