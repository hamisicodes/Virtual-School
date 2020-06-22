

$('.carousel').carousel({
  interval: 3000
})

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










  //sending message function
  $(document).ready(function () {

  $('form#contactForm').submit(function (event) {
    event.preventDefault();
    var name = $('#name').val();
    var pass = $('#email').val();
    var mess = $('#mess').val();
    confirm("Hi " + name + ",  We have received your message and We will  be getting in touch with you shortly. Thank you for contacting us.");
});


});