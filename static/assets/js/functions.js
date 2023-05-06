

jQuery(document).ready(function(){
//Add to cart functionality


jQuery('#add_to_cart_form').on('submit',function(e) {  //Don't foget to change the id form
    jQuery.ajax({
        url:'/cart/add/', //===PHP file name====
        data:jQuery(this).serialize(),
        type:'POST',
        success:function(response){
        $('#cartpopper').html(response.data)
        $('#cart-len').text(response.total_items)
        //console.log('total_item',response.total_items)
          //Success Message == 'Title', 'Message body', Last one leave as it is
        swal("Thank You!", "Your Message has been sent. Admin will respond you shortly", "success");
        },
        error:function(data){
          //Error Message == 'Title', 'Message body', Last one leave as it is
        swal("Oops...", "Something went wrong :(", "error");
        }
      });
      e.preventDefault(); //This is to Avoid Page Refresh and Fire the Event "Click"
});

// remove item from the cart
$('.remove-from-cart').on('click', function(){
  let index = $(this).attr('data-index')
  console.log('index', index)

  $.ajax({
    url:'/cart/remove/', //===PHP file name====
    data:{'id':index},
    success:function(response){
    $('#cartpopper').html(response.data)
    $('#cart-len').text(response.total_items)
   
    swal("Hey!", "Successfully remove item from cart", "success");
    },
    error:function(data){
      //Error Message == 'Title', 'Message body', Last one leave as it is
    swal("Oops...", "Something went wrong :(", "error");
    }
  });
})
})
