
var config = {
    // replace the publicKey with yours
    "publicKey": "test_public_key_7a2733a89fe04e07851792127b4e7daf",
    "productIdentity": UUID,
    "productName": USERNAME,
    "productUrl": window.location.href,
    "eventHandler": {
        onSuccess (payload) {
            verify(payload);
        },
        onError (error) {
            console.log(error);
        },
        onClose () {
            console.log('widget is closing');
        }
    }
};
var checkout = new KhaltiCheckout(config);
var btn = document.getElementById("payment-button");
btn.onclick = function () {
    amount  = $('#amount').val() * 100;
    if (amount>0){
        checkout.show({amount: amount});
    }
    else{
        swal("An unexpected error occured, Check if the entered amount is correct.", {
        dangerMode: true,
        buttons: {
            confirm: true,
        },
        })
        .then(() => {
            location.reload();                        
        })
    }
};


function verify(payload){
$("#maincont").hide();
$("#loading").show();
$.ajax ({
type: 'POST',
url: '/payment/khalti/verify',
data: JSON.stringify(payload),
success: function(data){
    if(data['status']){
        swal("Payment successful. Thank you for using our service.", {
        buttons: {
            confirm: true,
        },
        })
        .then(() => {
            location.reload();                        
        })    
    }else{
        swal("Payment unsuccessful. Please try again or contact customer service.", {
        buttons: {
            confirm: true,
        },
        })
        .then(() => {
            location.reload();                        
        })
    }
    },
error: function(data){
    swal("An unexpected error occured, Please report to the devs.", {
        dangerMode: true,
        buttons: {
            confirm: true,
        },
        })
        .then(() => {
            location.reload();                        
        })
},
complete: function(){
    $("#loading").hide();
    $("#maincont").show();
}            
});
}
