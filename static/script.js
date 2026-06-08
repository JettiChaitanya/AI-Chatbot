async function sendMessage() {

    let inputBox = document.getElementById("user-input");
    let message = inputBox.value;

    if(message.trim() === ""){
        return;
    }

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += "<b>You:</b> " + message + "<br>";

    inputBox.value = "";

    // Send message to backend (Flask)
    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    let data = await response.json();

    chatBox.innerHTML += "<b>Bot:</b> " + data.response + "<br>";
}