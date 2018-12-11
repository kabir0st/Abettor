function generateQrCode(){
    info = {
        'uuid':$('#uuid').val()
    }
    $.ajax ({
            type: 'POST',
            data: JSON.stringify(info),
            success: function(data){
                swal("Generated", {
                    buttons: {
                        confirm: true,
                    },
                    })
                    .then(() => {
                        location.reload();                        
                    })
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
            }            
        });
}