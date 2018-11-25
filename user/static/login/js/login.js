
// Get the modal
var modal = document.getElementById('myModal');
var scanned_output = document.getElementById('scanned_output');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
var span2 = document.getElementsByClassName("cross")[0];

    
// When the user clicks the button, open the modal 
function opencamera(){
    modal.style.display = "block";
    oncall();
}

// When the user clicks on <span> (x), close the modal
                
//this function will be called when JsQRScanner is ready to use

// function JsQRScannerReady()
// {
    //create a new scanner passing to it a callback function that will be invoked when
    //the scanner succesfully scan a QR code
         
// }

function oncall(staus){
    var jbScanner = new JsQRScanner(onQRCodeScanned);
    //reduce the size of analyzed image to increase performance on mobile devices
    jbScanner.setSnapImageMaxSize(300);
    var scannerParentElement = document.getElementById("scanner");
    if(scannerParentElement)
    {
    //append the jbScanner to an existing DOM element
        jbScanner.appendTo(scannerParentElement);
    }   
    span.onclick = function() {
        modal.style.display = "none";
        jbScanner.stopScanning();
        jbScanner.removeFrom(scannerParentElement);
    }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            jbScanner.stopScanning();
            jbScanner.removeFrom(scannerParentElement);
        }
        if (event.target == scanned_output){
            scanned_output.style.display = "none";
        }
    }
    function onQRCodeScanned(scannedText)
    {
        jbScanner.stopScanning();
        jbScanner.removeFrom(scannerParentElement);
        modal.style.display = "none";
        processQrCode(scannedText) 
  
    }
}
span2.onclick = function() { 
    scanned_output.style.display = "none";
}
                  
function processQrCode(uuid) {
    scanned_output.style.display = "block";
    $("analyze").remove()
    uuid_str = "'"+uuid+"'"
    $("#output").append(
        '<input type="password" id="pin" name="Pin Number" required autofocous><br><button class="btn btn-success" onclick="login('+uuid_str+')">Login</button>'
    )
}

function login(uuid){
    info = {
        'uuid':uuid,
        'pin_number':$('#pin').val()
    }
    $.ajax ({
        type: 'POST',
        url: '/user/qrlogin',
        data: JSON.stringify(info),
        success: function(data){
            if (data['status']){
                location.reload();
            }else{
                swal(data['error'], {
                    dangerMode: true,
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
        }   
    })
}