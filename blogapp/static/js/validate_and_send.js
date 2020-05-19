
$(function() {

  $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
    preventSubmit: true,
    submitError: function($form, event, errors) {
      // additional error messages or events
    },
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // get values from FORM
      var first_name = $("input#first_name").val();
      var last_name = $("input#last_name").val();
      var organisation = $("input#organisation").val();
      var role = $("input#role").val();
      var skills = $("textarea#skills").val();
      var description = $("textarea#description").val();; // For Success/Failure Message
      // Check for white space in name for Success/Fail message

      $this = $("#sendMessageButton");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: "/accounts/profile/create",
        type: "POST",
        headers: {'X-CSRFToken': token },
        data: {
          first_name: first_name,
          last_name: last_name,
          organisation: organisation,
          role: role,
          skills: skills,
          description: description,
        },
        cache: false,
        success: function() {
          // // Success message
          // $('#success').html("<div class='alert alert-success'>");
          // $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
          //   .append("</button>");
          // $('#success > .alert-success')
          //   .append("<strong>Profile successfully completed! </strong>");
          // $('#success > .alert-success')
          //   .append('</div>');
          //clear all fields
          console.log("hello")
          window.location.replace("/accounts/"+user+"/profile/view");
        },
        error: function() {
          // Fail message
          $('#success').html("<div class='alert alert-danger'>");
          $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-danger').append($("<strong>").text("Sorry "+ "it seems that server is not responding. Please try again later!"));
          $('#success > .alert-danger').append('</div>');
          //clear all fields
          $('#contactForm').trigger("reset");
        },
        complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });

  $("a[data-toggle=\"tab\"]").click(function(e) {
    e.preventDefault();
    $(this).tab("show");
  });
});

/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
  $('#success').html('');
});
