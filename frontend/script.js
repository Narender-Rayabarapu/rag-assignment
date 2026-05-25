async function sendMessage() {

    const input = document.getElementById("messageInput");

    const message = input.value;

    const response = await fetch("http://127.0.0.1:8000/api/chat", {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            sessionId:"123",
            message:message
        })
    });

    const data = await response.json();

    const messages = document.getElementById("messages");

    messages.innerHTML += `
        <p><b>You:</b> ${message}</p>
        <p><b>Bot:</b> ${data.reply}</p>
    `;

    input.value = "";
}