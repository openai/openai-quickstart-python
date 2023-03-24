<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<script>
$(function() {
  // Handle form submission
  $('#chat-form').submit(function(event) {
    event.preventDefault();
    var formData = $(this).serialize();
    var senderLanguage = $('#sender-language').val();
    var recipientLanguage = $('#recipient-language').val();
    var messageInput = $('#message-input');

    $.post('/', formData, function(response) {
      // Display original or translated message, depending on the selected languages
      var message = response;
      if (senderLanguage != recipientLanguage) {
        message = 'Original message: ' + messageInput.val() + '<br>' +
                  'Translated message: ' + response;
      }

      // Add message to chat history
      $('#chat-history').append('<p>' + message + '</p>');

      // Clear message input field
      messageInput.val('');
    });
  });
});
</script>
