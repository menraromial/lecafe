

jQuery(document).ready(function(){

 // var ids = [];  // Tableau pour stocker les IDs



//Add to cart functionality
//From product details pages
jQuery('#add_to_cart_form').on('submit',function(e) { 
  var selectedCheckboxes = $('input[type="checkbox"]:checked');
  var ids = [];
  var qty = $('#qty').val()
  var token=$('input[name=csrfmiddlewaretoken]').val()
  var item_id = $('#item-id').val()
  var oqty = $('#oqty').val()
  // Parcours des cases à cocher sélectionnées
  selectedCheckboxes.each(function() {
    var checkboxValue = $(this).attr('data-index');
    ids.push(checkboxValue)
  }); 

    jQuery.ajax({
        url:'/cart/add/', 
        data:{
          'item-id':item_id,
          'qty':qty,
          'oqty':oqty,
          'ids':ids,
          csrfmiddlewaretoken:token
            },
        type:'POST',
        success:function(response){
        $('#cartpopper').html(response.data)
        $('#cart-len').text(response.total_items)
        console.log('Tous les ids', ids)

          //Success Message == 'Title', 'Message body', Last one leave as it is
        swal("Merci!", "Item ajouté au panier", "success");
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
      swal("Merci!", "Item ajouté au panier", "success");
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
    url:'/cart/remove/', 
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
    url:'/cart/remove/', 
    data:{'id':index},
    success:function(response){
    $('#cartpopper').html(response.cart_list)
    $('#cart-len').text(response.total_items)

    $('#total_price').html(response.total_price)
    //console.log(this_val )
    this_val.closest('tr').remove();
    swal("Hey!", "Item supprimé du panier", "success");

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

    $('#total_price').html(response.total_price)
    
    price.text(response.item_t_price)
    //$('#total-price-2').text(response.total_price)
   
    swal("Hey!", "Quantité mise à jour", "success");
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



// Apply Coupon
$('#apply-coupon-btn').click(function(e){
  e.preventDefault()

  let token=$('input[name=csrfmiddlewaretoken]').val()
  let code=$('input[name=coupon_code]').val()
  //console.log('qty', qty, 'oqty',oqty, 'index', index, token)

  $.ajax({
    url:'/coupons/apply/', //===PHP file name====
    data:{
      'code':code,
      csrfmiddlewaretoken:token
    },
    type:'POST',
    success:function(response){
    //$('#cartpopper').html(response.data)
    //$('#cart-len').text(response.total_items)
    if (response.data !== null){
    if(response.data=='exist'){swal("Hey!", "Vous avez déjà appliquer ce coupon", "info");}
    else if(response.data == 'DoesNotExist'){swal("Oops...", "Code incorrect", "error")}
    else{
      $('#total_price').html(response.data)
      swal("Hey!", "Coupon appliqué", "success")
    }
    }

    },
    error:function(data){
      //Error Message == 'Title', 'Message body', Last one leave as it is
    swal("Oops...", "Something went wrong :(", "error");
    }
  });

});

//Contact Us
jQuery('#contact-form').on('submit',function(e) {  
  jQuery.ajax({
      url:'/contacts/send/', 
      data:jQuery(this).serialize(),
      type:'POST',
      success:function(data){
      
        //Success Message == 'Title', 'Message body', Last one leave as it is
      swal("Hey!", "Message envoyé avec succès", "success");
      },
      error:function(data){
        //Error Message == 'Title', 'Message body', Last one leave as it is
      swal("Oops...", "Something went wrong :(", "error");
      }
    });
    e.preventDefault(); //This is to Avoid Page Refresh and Fire the Event "Click"
});


    // Sélectionnez tous les checkboxes dans le conteneur
    $('#checkboxContainer input[type="checkbox"]').change(function() {
      var value = parseFloat($(this).val()); // Valeur du checkbox en tant que nombre
      var index = $(this).attr('data-index')
      var name = $('#name-'+index).text()

      console.log("valeur", value, name)
      // Vérifiez si le checkbox est coché ou décoché
      if ($(this).is(':checked')) {
          // Ajoutez un nouvel élément à la liste avec la valeur du checkbox
          $('#itemList').append('<li data-index="' + index + '" data-value="' + value + '">' + name + '</li>');

          // Ajoutez la valeur du checkbox à la valeur actuelle du span
          var currentValue = parseFloat($('#total_price').text());
          var sum = currentValue + value;
          $('#total_price').text(sum);
      } else {
          // Supprimez l'élément correspondant de la liste
          $('#itemList li[data-index="' + index + '"]').remove();

          // Soustrayez la valeur du checkbox de la valeur actuelle du span
          var currentValue = parseFloat($('#total_price').text());
          var difference = currentValue - value;
          $('#total_price').text(difference);
      }
  });

})
