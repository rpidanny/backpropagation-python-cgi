$(document).ready(function(){
var speed = 500;
setTimeout(function(){
$('#loading').slideUp(speed);
$('#form').slideDown(speed);
}, 1000);

});

$('#login').click(function(){
process();

});

function process(){
var un=$('#un').val();

if(un=="danny" || un=="abhishek" ){
var speed = 500;
$('#form').slideUp(speed); 
$('#mainpage').slideDown(speed);
}
else{
alert("Invalid Password.");}
}