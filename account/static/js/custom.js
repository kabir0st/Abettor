$('#date-picker').datepicker({
    format: "yyyy-mm-dd",
    startDate: '-0d',
    endDate: "+60d",
});

$("#date-picker").datepicker("setDate", new Date());

function validate (x) {

}