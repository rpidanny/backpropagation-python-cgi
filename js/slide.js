$(document).ready(function(){
var speed = 500;
$('#hr').fadeIn(5000);
$('#paragraph').fadeIn(5000);
$('#likebutton').fadeIn(5000);
$('#demoimg').fadeIn(3000);
$('#form').slideDown(speed);
$('#share').slideDown(speed);
$('#logos').fadeIn(speed);
$('#loading').slideUp(100); 

});



$('#cont').click(function(){
$('#logos').fadeOut(500);
$('#continue').slideUp(500); 
$('#imageboc1').slideDown(1000);
$('#imgdiv1').fadeIn(4000);
$('#imgdiv2').fadeIn(4000);
$('#imgdiv3').fadeIn(4000);
$('#imgdiv4').fadeIn(4000);
$('#quote').fadeIn(4000);
$('#bulb').fadeIn(4000);
$('#pc').fadeIn(4000);
$('#woofer').fadeIn(4000);
$('#tv').fadeIn(4000);
$('#updatestatus').fadeIn(3000);
$('#invitefriends').fadeIn(3000);
$('#download').fadeIn(3000);
$('#utube').fadeIn(3000);
$('#buttontable').fadeIn(4000);
//$('#camerawindowmain').fadeIn(2000);


});

$('#homebutton').click(function(){

$('#camerawindow').fadeOut(500);
$('#about').fadeOut(500);
$('#imgdiv1').fadeIn(1000);
$('#imgdiv2').fadeIn(1000);
$('#imgdiv3').fadeIn(1000);
$('#imgdiv4').fadeIn(1000);
$('#quote').fadeIn(7000);
$('#bulb').fadeIn(1000);
$('#pc').fadeIn(1000);
$('#woofer').fadeIn(1000);
$('#tv').fadeIn(1000);
//$('#camerawindowmain').fadeIn(2000);
});

$('#cambutton').click(function(){
$('#imgdiv1').fadeOut(2000);
$('#imgdiv2').fadeOut(2000);
$('#imgdiv3').fadeOut(2000);
$('#imgdiv4').fadeOut(2000);
$('#quote').fadeOut(2000);
$('#bulb').fadeOut(2000);
$('#pc').fadeOut(2000);
$('#woofer').fadeOut(2000);
$('#tv').fadeOut(2000);
$('#about').fadeOut(2000);
//$('#camerawindowmain').fadeOut(2000);
$('#camerawindow').fadeIn(2000);
});



$('#AboutButton').click(function(){
$('#imgdiv1').fadeOut(2000);
$('#imgdiv2').fadeOut(2000);
$('#imgdiv3').fadeOut(2000);
$('#imgdiv4').fadeOut(2000);
$('#quote').fadeOut(2000);
$('#bulb').fadeOut(2000);
$('#pc').fadeOut(2000);
$('#woofer').fadeOut(2000);
$('#tv').fadeOut(2000);
$('#camerawindow').fadeOut(2000);
//$('#camerawindowmain').fadeOut(2000);
$('#about').fadeIn(2000);
});