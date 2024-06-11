$(document).ready(function() {
    $('.add-to-cart').on('click', function() {
        var productId = $(this).data('product-id');
        $.ajax({
            url: "{% url 'agregar_al_carrito' 0 %}".replace('0', productId),
            method: "GET",
            success: function(data) {
                alert('Producto agregado al carrito. Total items: ' + data.total_items);
            },
            error: function(xhr, status, error) {
                alert('Error al agregar el producto al carrito.');
            }
        });
    });
});