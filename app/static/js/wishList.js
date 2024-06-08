function selectWishFunc(productId) {
    let productHeart = document.getElementById(`heart-${productId}`);

    if (productHeart.style.color == 'red') {
        productHeart.style.color = '';
        removeFromWishList(productId);
    } else {
        productHeart.style.color = 'red'
        addToWishList(productId);
    }
}

function addToWishList(productId) {
    $.ajax({
        method: "POST",
        url: add_to_wish_list_url,
        headers: { "X-CSRFToken": csrftoken_ },
        data: {
          product: JSON.stringify([productId]),
        },
        dataType: "json",
        error: function(data) {
          console.log('error cixdiiiii', data);
        }
      });
}

function removeFromWishList(productId) {
    $.ajax({
        method: "POST",
        url: remove_to_wish_list_url,
        headers: { "X-CSRFToken": csrftoken_ },
        data: {
          product: JSON.stringify([productId]),
        },
        dataType: "json",
        error: function(data) {
          console.log('error cixdiiiii', data);
        }
      });
}