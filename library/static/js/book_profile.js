
//     function assign(is_assigned,uuid) {
//         console.log(is_assigned)
//         if (is_assigned == "true") {
//             swal({
//                 cancel: true,
                
//             })
//         }
//         else { 
//             swal({
//                 title: "Not Yet Assigned !",
//                 text: "Assign this book to a Student ?",
//                 buttons: {
//                     cancel: true,
//                     confirm: 'Assign'
//                     },
//                 dangerMode: true,
//             })
//             .then((assign) => {
//                 if (assign) {
//                     swal({
//                         title: "Enter Student Full Name",
//                         text: 'Fisrt_name Last_name',
//                         content: {
//                             element: "input",
//                             attributes: {
//                                 placeholder: "Full Name",
//                                 type: "text",
//                                 },
//                             },
//                         dangerMode: true
//                     })
//                     .then((full_name) => {
//                         $.ajax({
//                             type: "POST",
//                             url:'book/assign',
//                             data: JSON.stringify({
//                                 'uuid':uuid,
//                                 'full_name':full_name,
//                             }),
//                             success: function(data){
//                                 swal({
//                                     title: "Book Assigned !",
//                                     text: data['book_name']+" is assigned to "+data['full_name']+" for 2 weeks.",
//                                     buttons: {
//                                         confirm: 'OK !'
//                                     },
//                                 }).then((ok) => { 
//                                     search_book();
//                                 })
//                             },
//                             error: function() { 
//                                 swal({
//                                     title: "Sorry !",
//                                     text: "An unexpected Error occured.",
//                                     dangerMode: true,
//                                     buttons: { 
//                                         confirm: 'OK :( '
//                                     }  
//                                 })
//                             },                          

//                         });
//                     });
//                 } 
//             });
//         }
//     } -->