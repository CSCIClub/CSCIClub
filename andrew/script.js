$(document).ready(function() {
   $('.boxes').mouseenter(function() {
       $(this).animate({
           height: '+=10px'
       });
   });
   $('.boxes').mouseleave(function() {
       $(this).animate({
           height: '-=10px'
       });
   });
   $('.boxes').click(function() {
       $(this).toggle(1000);
   });
   $('#button1').click(function(){
       $('#output').append('<p> More Stuff! </p>');
   });
});
