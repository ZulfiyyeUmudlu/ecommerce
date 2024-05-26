function getSelected(name) {
    const radioButtons = document.getElementsByName(name);
    let selectedValue = '';

    for (btn of radioButtons) {
        if (btn.checked) {
            selectedValue = btn.value;
            break;
        }
    }
    return selectedValue;
}


function createOrderItem() {
    $.ajax({
      method: "POST",
      url: createOrderItemUrl,
      headers: { "X-CSRFToken": csrftoken_ },
      data: {
        product: productId,
        quantity: document.getElementById("product-qty").value,
        size: getSelected('size'),
        color: getSelected('color'),
      },
      dataType: "json",
      success: function () {
        window.location.reload();
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }