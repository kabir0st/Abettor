
var span2 = document.getElementsByClassName("cross");

function show_explore_table(){
    location.reload();
}


function getSelectedBook(id){
    var xhttp = new XMLHttpRequest();
    var book_info = {
        'search_type':'id',
        'id': id,
    };
    $.ajax ({
        type: 'POST',
        url: 'search',
        data: JSON.stringify(book_info),
        success: function(data){
            outputData(data);        
    }
    }); 

    function outputData(data){
        y = data['uuid'].length;
        $("tr").remove(".table-row");
        $('#book_name_show').remove();
        $('#insert_book_name').append(
            '<h2 class="mb-0" id="book_name_show"><u><b>Book Name : '+$("#book_name").val()+'</u></h2>');
        var null_assigned;
        var null_due_date;
        var table_property;
        while (y) {
            y = y -1;
            if(data['is_assigned'][y]){
                null_assigned = data['assigned_to'][y]
            }
            else {
                null_assigned = 'Avaible!'
                $('#assign').show();
            }
            if (data['is_overdue'][y]) {
                table_property = 'table-danger'
            }
            else { 
                if (data['is_assigned'][y]){
                    table_property = 'Success'
                }
            }
            $("#search_results").append(
                '<tr data-href="'+data['uuid'][y]+'" class="table-row"><td class = "'+table_property+'">'+null_assigned+'</td><td>'+data['due_date'][y]+'</td></tr>'
            )
        }
        $(".table-row").click(function() {
        window.document.location = $(this).data("href");
        });
        $('#order_table').hide();   
        $("#search_table").show();
        
    $('#explore_button').show();
    } 
}    

function getSemester(){
    var xhttp = new XMLHttpRequest();
    info = {
        'request': "get_semester",
    }
    $.ajax ({
        type: 'POST',
        url: 'get/sem',
        data: JSON.stringify(info),
        success: function(data){
            outputData(data);        
    },
    error: function(data){
            swal("An unexpected error occured, Please report to the devs.", {
                dangerMode: true,
                buttons: {
                    confirm: true,
                },
                })
        }
    });
    function outputData(data){
        y = y = data['semester'].length;
        while (y) {
        y = y -1;
        $("#select_sem").append(
            '<option value = '+data['semester'][y]+'>'+data['semester'][y]+'</option>'
        )
    }
    }
}

function getRegisteredBooks(x) {
    var xhttp = new XMLHttpRequest();
    var book_info = {
        'semester': x,
    };
    $.ajax ({
        type: 'POST',
        url: 'get/book',
        data: JSON.stringify(book_info),
        success: function(data){
            outputData(data);        
    },
    error: function(data){
            swal("An unexpected error occured, Please report to the devs.", {
                dangerMode: true,
                buttons: {
                    confirm: true,
                },
                })
        }
    });
    
    function outputData(data){
        y = data['book_name'].length;
        $("tr").remove(".table-row");
        while (y) {
            y = y -1;
            $("#order_results").append(
                '<tr data-href="'+data['id'][y]+'" class="table-row"><td>'+data['book_name'][y] +'</td><td>'+data['author'][y] +'</td><td>'+data['registered_units'][y] +'</td><td>'+data['avaible_units'][y] +'</td><td>'+data['borrowed_units'][y] +'</td></tr>'
            )
        }
        $(".table-row").click(function() {
        x = $(this).data("href");
        getSelectedBook(x);
        });
        $("#search_table").hide();
        $('#order_table').show();        
        $('#explore_button').hide();
    } 
}

function search_book(){
    var xhttp = new XMLHttpRequest();
    var book_name = $('#book_name').val();
    var book_info = {
        'search_type':'name',
        'book_name': book_name,
    };
    $.ajax ({
        type: 'POST',
        url: 'search',
        data: JSON.stringify(book_info),
        success: function(data){
            outputData(data);        
    }
}); 

function outputData(data){
    y = data['uuid'].length;
    $("tr").remove(".table-row");
    $('#book_name_show').remove();
    $('#insert_book_name').append(
        '<h2 class="mb-0" id="book_name_show"><u><b>Book Name : '+$("#book_name").val()+'</u></h2>');
    var null_assigned;
    var null_due_date;
    var table_property;
    while (y) {
        y = y -1;
        if(data['is_assigned'][y]){
            null_assigned = data['assigned_to'][y]
        }
        else {
            null_assigned = 'Avaible!'
            $('#assign').show();
        }
        if (data['is_overdue'][y]) {
            table_property = 'table-danger'
        }
        else { 
            if (data['is_assigned'][y]){
                table_property = 'Success'
            }
        }
        $("#search_results").append(
            '<tr data-href="'+data['uuid'][y]+'" class="table-row"><td class = "'+table_property+'">'+null_assigned+'</td><td>'+data['due_date'][y]+'</td></tr>'
        )
    }
    $(".table-row").click(function() {
    window.document.location = $(this).data("href");
    });
    $('#order_table').hide();   
    $("#search_table").show();
    $('#explore_button').show();
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
span2.onclick = function() { 
    scanned_output.style.display = "none";
}
                  
function processQrCode(uuid) {
    scanned_output.style.display = "block";
    window.location = "/library/"+uuid; 
}
