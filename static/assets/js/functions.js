

jQuery(document).ready(function(){


//Add to cart functionality
//From product details pages
jQuery('#add_to_cart_form').on('submit',function(e) {  //Don't foget to change the id form
    jQuery.ajax({
        url:'/cart/add/', 
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

//From Menus or Home page
jQuery('.add_to_cart').on('click',function(e) { 
  let index = $(this).attr('data-index')
  let qty = $('#qty-'+index).val()
  let oqty = $('#oqty-'+index).val()
  let token=$('input[name=csrfmiddlewaretoken]').val()

  jQuery.ajax({
      url:'/cart/add/', 
      data:{
      'item-id':index,
      'qty':qty,
      'oqty':oqty,
      csrfmiddlewaretoken:token
         },
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
//cart poppup
$('.remove-from-cart').on('click', function(){
  let index = $(this).attr('data-index')
  //console.log('index', index)

  $.ajax({
    url:'/cart/remove/', //===PHP file name====
    data:{'id':index},
    success:function(response){
    //$('#cartpopper').html(response.data)
    $('#item-'+index).remove()
    $('#cart-len').text(response.total_items)
    $('#cartpopper-total-price').text( 'fcfa ' +response.get_total_price)
   
    swal("Hey!", "Item supprimé avec succès", "success");
    },
    error:function(data){
      //Error Message == 'Title', 'Message body', Last one leave as it is
    swal("Oops...", "Quelque chose s'est mal passée :(", "error");
    }
  });
});




// remove item from the cart
$('.delete-item-btn').click(function(){
  let index = $(this).attr('data-index')
  let this_val = $(this)

  $.ajax({
    url:'/cart/remove/', //===PHP file name====
    data:{'id':index},
    success:function(response){
    $('#cartpopper').html(response.cart_list)
    $('#cart-len').text(response.total_items)

    $('#total_price').html(response.total_price)
    //console.log(this_val )
    this_val.closest('tr').remove();
    swal("Hey!", "Successfully remove item from cart", "success");

    },
    error:function(data){
      //Error Message == 'Title', 'Message body', Last one leave as it is
    swal("Oops...", "Something went wrong :(", "error");
    }
  });

});




// Update quantity
$('.update-item-btn').click(function(e){
  e.preventDefault()
  let index = $(this).attr('data-index')
  let qty = $('#qty-'+index).val()
  let oqty = $('#oqty-'+index).val()
  let token=$('input[name=csrfmiddlewaretoken]').val()
  let price = $('#price-'+index)
  //console.log('qty', qty, 'oqty',oqty, 'index', index, token)

  $.ajax({
    url:'/cart/add/', //===PHP file name====
    data:{
      'item-id':index,
      'qty':qty,
      'oqty':oqty,
      csrfmiddlewaretoken:token
    },
    type:'POST',
    success:function(response){
    $('#cartpopper').html(response.data)
    $('#cart-len').text(response.total_items)

    $('#total_price').html(response.total_price)
    
    price.text(response.item_t_price)
    //$('#total-price-2').text(response.total_price)
   
    swal("Hey!", "Successfully remove item from cart", "success");
    },
    error:function(data){
      //Error Message == 'Title', 'Message body', Last one leave as it is
    swal("Oops...", "Something went wrong :(", "error");
    }
  });

});


//Order details

$('.open-order-details').click(function(){
  let index = $(this).attr('data-index')
  let modal = $('#modal-body')

  $.ajax({
    url:'/orders/details/', 
    data:{'id':index},
    success:function(response){
      $('#exampleModal').modal('show')
     $('#modal-body').html(response.data)
    
    },
    error:function(data){
      //Error Message == 'Title', 'Message body', Last one leave as it is
    swal("Oops...", "Something went wrong :(", "error");
    }
  });

});

//Valider une commande

$('.validate-order').click(function(e){
  e.preventDefault()
  let index = $(this).attr('data-id')
  let token=$('input[name=csrfmiddlewaretoken]').val()

  $.ajax({
    url:'/orders/update/', 
    data:{
      'index':index,
      csrfmiddlewaretoken:token
    },
    type:'POST',
    success:function(response){
      if (response.data=='Ok'){
        $('#valided-'+index).html('<i class="fa-solid fa-circle-check" style="color: #1fd143;"></i>')
        //$('#modal-body').html(response.data)
        var toastLiveExample = document.getElementById('liveToast')
        var toast = new bootstrap.Toast(toastLiveExample)
        toast.show()
      }
      else{
        swal("Oops...", "Something went wrong :(", "error");
      }
      
    
    },
    error:function(data){
      //Error Message == 'Title', 'Message body', Last one leave as it is
    swal("Oops...", "Something went wrong :(", "error");
    }
  });

});

//Add review
$('.add-review-btn').click(function(e){
  e.preventDefault()
  let index = $(this).attr('data-index')
  let token=$('input[name=csrfmiddlewaretoken]').val()
  let fullname = $('input[name=fullname]').val()
  let rating=$('#rating').val()
  let review = $('#review').val()
  //console.log('click', review, fullname)

  $.ajax({
    url:'/review/add/', 
    data:{
      'item_id':index,
      'fullname':fullname,
      'rating':rating,
      'review':review,
      csrfmiddlewaretoken:token
    },
    type:'POST',
    success:function(response){
      $('#comment-container').html(response.data)
    },
    error:function(data){
      //Error Message == 'Title', 'Message body', Last one leave as it is
    swal("Oops...", "Something went wrong :(", "error");
    }
  });

});


})
