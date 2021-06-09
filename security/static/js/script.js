// script for navbar
/*
$(document).ready(function () {
    $('.sidenav').sidenav();
});

$(".dropdown-trigger").dropdown({
    inDuration: 0.5,
    outDuration: 1,
    constrain_width: false, // Does not change width of dropdown to that of the activator
    hover: true, // Activate on hover
    gutter: 1, // Spacing from edge
    belowOrigin: true, // Displays dropdown below the button
    coverTrigger: false
});

$(".dropdown-trigger1").dropdown({
    inDuration: 0.5,
    outDuration: 1,
    constrain_width: false, // Does not change width of dropdown to that of the activator
    hover: false, // Activate on hover
    gutter: 1, // Spacing from edge
    belowOrigin: true, // Displays dropdown below the button
    coverTrigger: false
});
*/
// end of nav

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


setTimeout(function(){
    let ele = document.querySelector('#message');
    ele.style.opacity = '0'
}, 5000);
