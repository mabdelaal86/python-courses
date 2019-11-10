function hide_img() {
    var myImg = document.getElementById("my_img");
    if (myImg.style.visibility == "hidden")
        myImg.style.visibility = "visible";
    else
        myImg.style.visibility = "hidden";
}