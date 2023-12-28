document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.quantity-inc').forEach(button => {
        button.addEventListener('click', () => {
            let productId = button.dataset.productId;
            let quantityInput = document.querySelector('#quantity-' + productId);
            quantityInput.value = parseInt(quantityInput.value) + 1;
            console.log('here')
        });
    });

    document.querySelectorAll('.quantity-dec').forEach(button => {
        button.addEventListener('click', () => {
            let productId = button.dataset.productId;
            let quantityInput = document.querySelector('#quantity-' + productId);
            if (parseInt(quantityInput.value) > 1) {
                quantityInput.value = parseInt(quantityInput.value) - 1;
                console.log('there')
            }
        });
    });
});
