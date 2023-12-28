// script.js

function showContent() {
    var book = document.getElementById('book-section');
    var pdfContainer = document.getElementById('pdf-container');
    // Hide other elements and show the PDF container and other content
    pdfContainer.style.display = 'block';
    book.style.display = 'block';
    hideOtherBoxes();
}


function hideOtherBoxes() {
    var learningBoxes = document.querySelectorAll('.learning-box');
    learningBoxes.forEach(function (box) {
        box.style.display = 'none';
    });
}

function goBackToOriginalPage() {
    var pdfContainer = document.getElementById('pdf-container');
    var learn = document.getElementById('learning-section');
    var game = document.getElementById('game-section');
    var diagram = document.getElementById('diagram-section');
    var videos = document.getElementById('videos-section');
    var maps = document.getElementById('maps-section');
    var revision = document.getElementById('revision-section');
    var book = document.getElementById('book-section');
    
    // Hide the e-reader and other content
    pdfContainer.style.display = 'none';
    book.style.display = 'none';
    learn.style.display = 'none';
    game.style.display = 'none';
    diagram.style.display = 'none';
    videos.style.display = 'none';
    maps.style.display = 'none';
    revision.style.display = 'none';

    // Show all the learning boxes
    var learningBoxes = document.querySelectorAll('.learning-box');
    learningBoxes.forEach(function (box) {
        box.style.display = 'block';
    });
}

function showPopup() {
    var learn = document.getElementById('learning-section');
    // Hide other elements and show the PDF container and other content
    learn.style.display = 'block';
    hideOtherBoxes();
}

function showPopupgame() {
    var game = document.getElementById('game-section');
    // Hide other elements and show the PDF container and other content
    game.style.display = 'block';
    hideOtherBoxes();
}

function showPopupdiagram() {
    var diagram = document.getElementById('diagram-section');
    // Hide other elements and show the PDF container and other content
    diagram.style.display = 'block';
    hideOtherBoxes();
}

function showPopupvideos() {
    var videos = document.getElementById('videos-section');
    // Hide other elements and show the PDF container and other content
    videos.style.display = 'block';
    hideOtherBoxes();
}

function showPopupmaps() {
    var maps = document.getElementById('maps-section');
    // Hide other elements and show the PDF container and other content
    maps.style.display = 'block';
    hideOtherBoxes();
}

function showPopuprevision() {
    var revision = document.getElementById('revision-section');
    // Hide other elements and show the PDF container and other content
    revision.style.display = 'block';
    hideOtherBoxes();
}

function sendMessage() {
    var userInput = document.getElementById('user-input');
    var message = userInput.value.trim();

    if (message !== '') {
        appendMessage('You', message, 'user-message');

        // Send the user's query to the Flask server for processing
        fetch('/process_query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_query: message
                }),
            })
            .then(response => response.json())
            .then(data => {
                // Display the server's response
                appendMessage('Server', data.response, 'bot-message');
            })
            .catch(error => console.error('Error:', error));

        userInput.value = '';
    }
}

function appendMessage(sender, content, className) {
    var chatMessages = document.getElementById('chat-messages');
    var messageDiv = document.createElement('div');
    messageDiv.className = className;
    messageDiv.textContent = sender + ': ' + content;
    chatMessages.appendChild(messageDiv);

    // Scroll to the bottom of the chatMessages div
    chatMessages.scrollTop = chatMessages.scrollHeight;
}