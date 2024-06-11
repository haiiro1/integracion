$(document).ready(function() {
    // Make AJAX request to fetch product details
    $.ajax({
        url: '/api/productos/1/',  // Replace '1' with the actual ID of the product
        method: 'GET',
        success: function(data) {
            // Render product details in the page
            var productHtml = `
                <p><strong>Name:</strong> ${data.name}</p>
                <p><strong>Description:</strong> ${data.description}</p>
                <p><strong>Price:</strong> ${data.price}</p>
                <!-- Add more details here as needed -->
            `;
            $('#product-info').html(productHtml);
        },
        error: function(xhr, status, error) {
            // Handle error
            console.error('Error fetching product details:', error);
        }
    });
});