function sendMessage() {
    let userText = document.getElementById("userInput").value.trim();
    if (userText === "") return;

    let chatBox = document.getElementById("messages");
    chatBox.innerHTML += `<p class='user-message'>You: ${userText}</p>`;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p class='bot-message'>Bot: ${data.reply}</p>`;
        document.getElementById("userInput").value = ""; // Clear input field
        chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll
    })
    .catch(error => {
        console.error("Error:", error);
        chatBox.innerHTML += `<p class='bot-message' style='color: red;'>Error: Chatbot server is not responding.</p>`;
    });
}
