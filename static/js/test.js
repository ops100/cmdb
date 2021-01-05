window.onload = function () {
    var winw = window.innerWidth;
    var menuw = document.getElementById("menu").offsetWidth;
    var topmenuw = winw-menuw;
    var s = " winw: " + winw + " menuw: " + menuw + " topmenuw: "+  topmenuw
    console.log(s)
    document.getElementById("topmenu").style.width=topmenuw + "px";
    document.getElementById("topmenu").innerText=s;

}
//
// window.onresize = function () {
//     var winw = window.innerWidth;
//     var menuw = document.getElementById("menu").offsetWidth;
//     var topmenuw = winw-menuw;
//     var contentw = topmenuw;
//     var s = "winw: " + winw + "menuw: " + menuw + "topmenuw: "+  topmenuw
//     console.log(s)
//     document.getElementById("topmenu").style.width=topmenuw + "px";
//     document.getElementById("topmenu").innerText=s;
//     document.getElementById("content").innerText=s;
//
// }

document.getElementById("menu").onresize = function () {
    var winw = window.innerWidth;
    var menuw = document.getElementById("menu").offsetWidth;
    var topmenuw = winw-menuw;
    var s = "winw: " + winw + "menuw: " + menuw + "topmenuw: "+  topmenuw
    console.log(s)
    document.getElementById("topmenu").style.width=topmenuw + "px";
    document.getElementById("topmenu").innerText=s;

}
