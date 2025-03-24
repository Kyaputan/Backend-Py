document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("sendDataBtn").addEventListener("click", sendData);
});

function sendData() {
    const data = { name: "John Doe", age: 25 };

    fetch("/api/data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Success:", data);
        document.getElementById("response").innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error("Error:", error));
}

