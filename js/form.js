function process(){
var un=$('#un').val();

if(un=="danny" || un=="roboticskec" || un=="jyotika" || un=="rishikesh"){
var speed = 500;
$('#form').slideUp(speed); 
$('#mainpage').slideDown(speed);
}
else{
alert("Invalid Password.");}
}


$(':text').focusin(function(){
$(this).css('background-color',  '#F0F0F0');

});

$(':text').blur(function(){
$(this).css('background-color', 'white');
});


$('#login').click(function(){
//$(this).attr('value', 'Please wait...');
process();

});