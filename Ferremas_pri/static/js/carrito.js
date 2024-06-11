$(document).on('click', '.add-to-cart', function() {
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

$(document).on('click', 'a[href="#Modal0"]', function() {
    $.ajax({
        url: "{% url 'obtener_contenido_carrito' %}",
        method: "GET",
        success: function(data) {
            $('#carrito-contenido').html(data.html);
            $('#Modal0').show(); // Muestra el modal después de cargar el contenido
        },
        error: function(xhr, status, error) {
            alert('Error al obtener el contenido del carrito.');
        }
    });
});

$(document).on('click', '.close-modal', function() {
    $(this).closest('.modal0').hide();
});

$(document).on('click', function(event) {
    if ($(event.target).is('.modal0')) {
        $('.modal0').hide();
    }
});