function changePrice(itemId, minusButton, plusOrMinus) {
    let subtotal = document.getElementById(`subtotal-${itemId}`);
    let price = document.getElementById(`price-${itemId}`).innerHTML;
    let quantity = document.getElementById(`quantity-${itemId}`).value;
    if (plusOrMinus === 'plus') {
        quantity = parseInt(quantity) + 1
    } else {
        quantity -= 1
    }
    if ((parseInt(quantity)) === 1 && plusOrMinus === 'minus') {
        minusButton.disabled = true;
    } else if (parseInt(quantity) > 1 && plusOrMinus === 'plus') {
        $(`#minusButton-${itemId}`).removeAttr('disabled');
    }
    subtotal.innerHTML = Number(price.replace(',', '.')) * Number(quantity);
    calcTotal();
}

function calcTotal() {
    let subtotalValues = document.getElementsByName('subtotal');
    let subtotalFinal = document.getElementById('subtotal-final');
    let total = document.getElementById('total');
    let shipping = document.getElementById('shipping');
    let subtotal_result = 0;
    for (let subtotalValue of subtotalValues) {
        subtotal_result += Number(subtotalValue.innerHTML.replace(',', '.'))
    }
    subtotalFinal.innerHTML = Number(subtotal_result).toFixed(2)
    shipping.innerHTML = Number(subtotal_result * 5 / 100).toFixed(2)
    total.innerHTML = Number(subtotal_result + (subtotal_result * 5 / 100)).toFixed(2)
}

function deleteItem(itemId) {
    document.getElementById(`tr-${itemId}`).remove();
    calcTotal();
    deleteOrderItem(itemId);
}

function deleteOrderItem(itemId) {
    $.ajax({
      method: "DELETE",
      url: deleteOrderItemUrl.replace('1', itemId),
      headers: { "X-CSRFToken": csrftoken_ },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
}


function getItems() {
    data = [];
    let items = document.getElementsByName('order-items'); // tr elements
    for (let item of items) {
      let itemId = item.getAttribute('data-id')
      let quantity = document.getElementById(`quantity-${itemId}`).value
      data.push({"id": itemId, "quantity": quantity})
    }
    return JSON.stringify(data)
} 

function createOrder() {
    $.ajax({
      method: "POST",
      url: createOrderUrl,
      headers: { "X-CSRFToken": csrftoken_ },
      data: {
        subtotal: document.getElementById("subtotal-final").innerHTML.replace(',', '.'),
        total: document.getElementById("total").innerHTML.replace(',', '.'),
        shipping: document.getElementById('shipping').innerHTML.replace(',', '.'),
        items: getItems()
      },
      dataType: "json",
      success: function () {
        window.location = "/checkout";
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }


window.addEventListener("load", calcTotal);