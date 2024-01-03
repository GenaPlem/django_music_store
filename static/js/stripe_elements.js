let stripePublicKey = document.getElementById('id_stripe_public_key').text.slice(1, -1);
let clientSecret = document.getElementById('id_client_secret').text.slice(1, -1);

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
let submitBtn = document.getElementById('submit-btn');
form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    submitBtn.setAttribute('disabled', 'true');

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name.value,
                email: form.email.value,
                phone: form.phone_number.value,
                address: {
                    line1: form.address1.value,
                    line2: form.address2.value,
                    city: form.city.value,
                    postal_code: form.postal_code.value,
                    state: form.county.value
                }
            }
        }
    }).then(function (result) {
        if (result.error) {
            // Display error.message in your UI.
            let errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
            card.update({'disabled': false});
            submitBtn.removeAttribute('disabled');
        } else {
            // The payment has been processed!
            if (result.paymentIntent.status === 'succeeded') {
                // Submit the form with the paymentIntent id
                let paymentIntentId = result.paymentIntent.id;
                let hiddenInput = document.createElement('input');
                hiddenInput.setAttribute('type', 'hidden');
                hiddenInput.setAttribute('name', 'payment_intent_id');
                hiddenInput.setAttribute('value', paymentIntentId);
                form.appendChild(hiddenInput);
                form.submit();
            }
        }
    });
});
