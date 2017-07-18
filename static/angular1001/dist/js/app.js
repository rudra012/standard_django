
// Select 2
function select2_var() {
    $( ".select-single" ).select2({
        minimumResultsForSearch: Infinity
    });
}

function select2_var_search() {
    $( ".select-single-with-search" ).select2();
}

// Date/Time Picker (https://eonasdan.github.io/bootstrap-datetimepicker/)
function datepicker_var() {
    $('.datepickershow').datepicker({
      autoclose: true,
      format: "dd/mm/yyyy"
    });
}

//Timepicker
$(".timepickershow").timepicker({
  showInputs: false,
  showMeridian: false
});

setTimeout(function(){
    datepicker_var();
    select2_var();
    select2_var_search();
});

$('body').on('click', '[data-toggle="tab"], [data-toggle="modal"]' , function () {
  select2_var();
  select2_var_search();
  datepicker_var();
});  