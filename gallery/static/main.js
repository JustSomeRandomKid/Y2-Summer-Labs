function changeBackgroundColor(color){
    document.querySelector(".body").style.backgroundColor = color; 
}
const button = document.querySelector(".colorButton")
button.addEventListener("click",function(){
    changeBackgroundColor("blue");
});