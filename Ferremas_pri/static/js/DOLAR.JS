
document.addEventListener("DOMContentLoaded", function () {
    // Realiza una solicitud AJAX para obtener el precio del dólar
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "{% url 'get_dolar_price' %}", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
            var dolarPrice = response.dolar_price;

            // Obtiene el precio del producto en pesos chilenos desde el HTML
            var clpPrice = parseFloat(document.querySelector('{{ producto.precio }}').textContent.replace('$', '').replace(' CLP', '').replace(',', ''));

            // Calcula el precio del producto en dólares
            var usdPrice = clpPrice / dolarPrice;

            // Actualiza el elemento HTML con el precio en dólares
            document.getElementById("product-price-usd").innerText = usdPrice.toFixed(2) + " USD";
        }
    };
    xhr.send();
});
