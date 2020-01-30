$(document).ready(function() {
    $('input.flatpickr').flatpickr({
          defaultDate: $(this).val(),
          enableTime: true,
          time_24hr: false,
          dateFormat: 'Y-m-dTH:i:s', // SQLAlchemy format: 2020-01-29T20:39:43
          minuteIncrement: 1,
          altInput: true,
          altFormat: 'F j, Y at h:i K'
    });
});