//Define the Variable to track the selected option
let selectedOption = 0;
//Function to append user's message to the chat
function appendUserMessage(message) {
    const chatBody = document.getElementById("chat-body");
    const userMessage = document.createElement("div");
    userMessage.className = "chat-body user";
    userMessage.innerHTML = '<span class="message-sender">You:</span> ' + message;
    chatBody.appendChild(userMessage);
}
//Function to append Bot's message to the chat
function appendBotMessage(message) {
    const chatBody = document.getElementById("chat-body");
    const botMessage = document.createElement("div");
    botMessage.className = "chat-body bot";
    botMessage.innerHTML = '<span class="message-sender">Research Assistant:</span> ' + message;
    chatBody.appendChild(botMessage);
}
//Function to start conversation and display initial bot message
function startConversation() {
    appendBotMessage("Hello, I am your research assistant. I can help you with the below topics:");
    const buttonOptionsDiv = document.getElementById("button-options");
    buttonOptionsDiv.style.display = "block";
}
//Function to handle user's message input
function sendMessage() {
    const userInput = document.getElementById("user-input");
    const userTopic = userInput.value;

    if (userTopic.trim() === "") {
        return;
    }

    userInput.value = "";

    appendUserMessage(userTopic);

    // Send user message (option + topic) to the server using AJAX or fetch
    const userMessage = `${selectedOption}-${userTopic}`;
    fetch("/", {
        method: "POST",
        body: JSON.stringify({ user_message: userMessage }),
        headers: {
            "Content-Type": "application/json",
        },
    })
    //Handle Bot response and update the UI
    .then((response) => response.json())
    .then((data) => {
        const botResponse = data.bot_response;
        appendBotMessage(botResponse);

        const buttonOptionsDiv = document.getElementById("button-options");
        buttonOptionsDiv.style.display = "block";

        const userInputForm = document.getElementById("user-input-form");
        userInputForm.style.display = "none";
    })
    .catch((error) => {
        console.error("Error sending message:", error);
    });
}

//Function to hanlde button clicks and set selected options
function handleButtonClick(option) {
    selectedOption = option;

    const buttonOptionsDiv = document.getElementById("button-options");
    buttonOptionsDiv.style.display = "none";

    const userInputForm = document.getElementById("user-input-form");
    userInputForm.style.display = "block";
}
//Add active listener for user's  message input form 
document.getElementById("user-input-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const userInput = document.getElementById("user-input");
    const userTopic = userInput.value;

    if (userTopic.trim() === "") {
        return;
    }

    userInput.value = "";

    appendUserMessage(userTopic);

    // Send user message (option + topic) to the server using AJAX or fetch
    const userMessage = `${selectedOption}-${userTopic}`;
    fetch("/", {
        method: "POST",
        body: JSON.stringify({ user_message: userMessage }),  // Corrected key to "user_message"
        headers: {
            "Content-Type": "application/json",
        },
    })
    //Handle Bot's response and update the UI
        .then((response) => response.json())
        .then((data) => {
            const botResponse = data.bot_response;
            appendBotMessage(botResponse);

            const buttonOptionsDiv = document.getElementById("button-options");
            buttonOptionsDiv.style.display = "block";

            const userInputForm = document.getElementById("user-input-form");
            userInputForm.style.display = "none";
        })
        .catch((error) => {
            console.error("Error sending message:", error);
        });
});