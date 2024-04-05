document.addEventListener('DOMContentLoaded', function () {
    var shortenButton = document.getElementById('shortenButton');
    var urlInput = document.getElementById('urlInput');
    var shortenedURLTextarea = document.getElementById('shortenedURL');
    var copyButton = document.getElementById('copyButton');

    shortenButton.addEventListener('click', function () {
        var url = urlInput.value;

        // Send a POST request to the backend to shorten the URL
        fetch('http://127.0.0.1:5000/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Display the shortened URL to the user
            shortenedURLTextarea.value = data.shortened_url;
        })
        .catch(error => {
            console.error('Error:', error);
            shortenedURLTextarea.value = 'Error: Unable to shorten URL';
        });
    });

    // Copy shortened URL to clipboard when "Copy" button is clicked
    copyButton.addEventListener('click', function () {
        shortenedURLTextarea.select();
        document.execCommand('copy');
        alert('Shortened URL copied to clipboard');
    });
});
