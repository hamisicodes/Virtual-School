//First jQuery
$(document).ready(function () {
  $(".image1").click(function () {
    $("#peek1").slideToggle();
    $("#boo1").slideToggle();
  });


    $(".image2").click(function () {
      $("#peek2").slideToggle();
        $("#boo2").slideToggle();
  
    });
      $(".image3").click(function () {
        $("#peek3").slideToggle();
        $("#boo3").slideToggle();
  
      });
    });






//Js function
 function nameOfUser(submit){
  
    var name = $("input#name").val();
    var email =$("input#email").val();

    alert("Hey " + name + ",Thanks for reaching to us.We have recieved your message .");
    event.preventDefault();
  };
