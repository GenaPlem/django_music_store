let stripePublicKey = document.getElementById('id_stripe_public_key').text.slice(1, -1);

let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

let base = {

    base: {
        fontSize: '16px',
        color: "#32325d",
        fontFamily: 'Ubuntu, sans-serif',
        fontSmoothing: 'antialiased',
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

let card = elements.create('card', {style: base});
card.mount('#card-element');

card.on('change', function (event) {
    let displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

let form = document.getElementById('payment-form');
form.addEventListener('submit', function (event) {
    event.preventDefault();

    stripe.createPaymentMethod('card', card).then(function (result) {
        if (result.error) {
            // Show error in #card-errors
            let errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            // Send the payment method ID to your server
            stripePaymentMethodHandler(result.paymentMethod.id);
        }
    });
});

function stripePaymentMethodHandler(paymentMethodId) {
    let form = document.getElementById('payment-form');
    let hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'payment_method_id');
    hiddenInput.setAttribute('value', paymentMethodId);
    form.appendChild(hiddenInput);

    form.submit();
}
