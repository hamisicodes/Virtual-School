function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
  
  /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
  }


  document.getElementById('message').onclick = function() {
    swal({
     title: 'Are you sure?',
     text: "You can't undo this!",
     type: 'warning',
     showCancelButton: true,
     confirmButtonColor: '#3085d6',
     cancelButtonColor: '#d33',
     confirmButtonText: 'Yes, sure!',
     cancelButtonText: 'No,not sure…'
   }).then((result) => {
     if (result.value) {
       swal(
         'Congrats!',
         'its deleted!',
         'success'
       )
     }
   })
  };