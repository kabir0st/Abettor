

function search_student(uuid){
    var first_name = $('#first_name').val();
    var last_name = $('#last_name').val();
    var info = {
        'first_name': first_name,
        'last_name': last_name,
        'qr':false
    };
    $.ajax ({
        type: 'POST',
        url: '/payment/search',
        data: JSON.stringify(info),
        success: function(data){
            outputData(data,uuid);
        }
    });
}

function outputData(data,uuid){        
    $("tr").remove(".table-row");
    y = data['username'].length;
    while (y) {
        y = y -1;
        $("#results").append(
            '<tr class="table-row" data-href="'+data['username'][y]+'"><td>'+data['name'][y]+'</td><td>'+data['semester'][y]+'</td><td>'+data['username'][y]+'</td></tr>'
        )
    }
    $(".table-row").click(function() {
        var x = $(this).data("href");
        assign(x,uuid);    
        });
    $("#search_table").show();
}

function assign(username,uuid){ 
    info = {
        'qr':false,
        'username':username,
        'uuid':uuid,
        'action':'assign'
        }
    send_data(info);
}

function send_data(info) {
    if(info['action'] == 'return')
    {
        url = '/library/book/return';
        msg = "This Book is marked as returned.";
    } 
    else if (info['action'] == 'assign'){
        url = '/library/book/assign';
        msg = "This Book is assigned to the designated user.";
    }
    else if (info['action'] == 'extend') {
        url = '/library/book/extend';
        msg = "Due Date is extended by 2 weeks.";
    }
    else{
        error();
    }
    $.ajax ({
        type: 'POST',
        url: url,
        data: JSON.stringify(info),
        success: function(){
            swal(msg, {
                buttons: {
                    confirm: true,
                },
                })
                .then(() => {
                    location.reload();                        
                })
        },
        error: error()
    })
}


function error(){
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
                  
function processQrCode_send(uuid) {
    $.ajax ({
        type: 'POST',
        url: '/library/book/assign',
        data: JSON.stringify(info),
        success: function(data){
            swal("Book Assigned To The Selected User of username: "+data['username']+" ! ", {
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