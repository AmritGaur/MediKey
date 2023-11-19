document.addEventListener('DOMContentLoaded', function () {
    const textInput = document.getElementById('textInput');
    const virtualKeyboard = document.getElementById('virtualKeyboard');

    const keys = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Enter', 'Backspace'
    ];

    keys.forEach(key => {
        const keyElement = document.createElement('div');
        keyElement.className = 'key';
        keyElement.textContent = key;
        keyElement.addEventListener('click', () => handleKeyPress(key));
        virtualKeyboard.appendChild(keyElement);
    });

    textInput.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendDataToServerAndRunScript(textInput.value);
        }
    });

    function handleKeyPress(key) {
        switch (key) {
            case 'Enter':
                sendDataToServerAndRunScript(textInput.value);
                break;
            case 'Backspace':
                textInput.value = textInput.value.slice(0, -1);
                break;
            default:
                textInput.value += key;
        }
    }

    async function sendDataToServerAndRunScript(data) {
        try {
            // Send input data to the server
            const response = await fetch('http://127.0.0.1:5000/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ data }),
            });

            if (response.ok) {
                console.log('Data sent successfully');
            } else {
                console.error('Failed to send data');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }
});

