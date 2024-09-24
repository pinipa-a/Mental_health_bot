const chatBox = document.getElementById('chat-box');
const sendBtn = document.getElementById('send-btn');
const userInput = document.getElementById('user-input');

function appendMessage(message, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

sendBtn.addEventListener('click', () => {
    const message = userInput.value;
    if (message) {
        appendMessage(message, true);
        userInput.value = '';
        fetchMessageFromBot(message);
    }
});

async function fetchMessageFromBot(message) {
    try {
        const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });

        const botMessages = await response.json();
        botMessages.forEach(botMsg => {
            appendMessage(botMsg.text, false);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}
