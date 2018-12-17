function search(){
    var xhttp = new XMLHttpRequest();
    var first_name = $('#first_name').val();
    var last_name = $('#last_name').val();
    var info = {
        'qr':false,
        'first_name': first_name,
        'last_name': last_name,
    };
    $.ajax ({
        type: 'POST',
        url: 'search',
        data: JSON.stringify(info),
        success: function(data){
            outputData(data);
    }
    });

    function outputData(data){
        $("tr").remove(".table-row");
        y = data['username'].length;
        while (y) {
            y = y -1;
            $("#results").append(
                    '<tr class="table-row" data-href="'+data['username'][y]+'"><td>'+data['name'][y]+'</td><td>'+data['semester'][y]+'</td><td>'+data['username'][y]+'</td></tr>'
            )
        }
        $(".table-row").click(function() {
        window.document.location = $(this).data("href");
        });
        $("#main-table").show();
    }
}

function opencamera(){
    modal.style.display = "block";
    oncall();
}

function oncall(staus){
    var jbScanner = new JsQRScanner(onQRCodeScanned);
    jbScanner.setSnapImageMaxSize(300);
    var scannerParentElement = document.getElementById("scanner");
    if(scannerParentElement)
    {
        jbScanner.appendTo(scannerParentElement);
    }   
    span.onclick = function() {
        modal.style.display = "none";
        jbScanner.stopScanning();
        jbScanner.removeFrom(scannerParentElement);
    }
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
function processQrCode(uuid) {
    scanned_output.style.display = "block";
    info = {
        'qr':true,
        'uuid':uuid,
        }
    $.ajax ({
        type: 'POST',
        url: '/payment/search',
        data: JSON.stringify(info),
        success: function(data){
            // console.log(data)
            window.location="/payment/"+data['username'][0]; 
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
