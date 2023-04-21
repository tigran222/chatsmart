const messageInput = document.querySelector('#message-input');
const sendButton = document.querySelector('#send-button');
const messageContainer = document.querySelector('#messages');

sendButton.addEventListener('click', sendMessage);
fetchMessages();

function sendMessage(event) {
  event.preventDefault();

  const message = messageInput.value.trim();
  if (!message) return;

  fetch('/send-message/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken') },
    body: JSON.stringify({ message })
  })
  .then(response => response.json())
  .then(result => {
    if (result.success) {
      messageInput.value = '';
    } else {
      alert('Failed to send message');
    }
  })
  .catch(error => {
    alert('Network error');
  });
}

function fetchMessages() {
  fetch('/get-messages/')
  .then(response => response.json())
  .then(result => {
    result.messages.forEach(message => {
      const messageElement = document.createElement('div');
      messageElement.textContent = message;
      messageContainer.appendChild(messageElement);
    });
  })
  .catch(error => {
    alert('Network error');
  });
}

function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '=([^;]*)');
  return cookieValue ? cookieValue[2] : '';
}
