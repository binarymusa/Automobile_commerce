

const progressBar = document.querySelector('.progress-bar');

progressBar.addEventListener('animationend', () => {
    window.location.href = '/market_page';
});

document.addEventListener('DOMContentLoaded', function() {
    // Add click event listener to button
    var button1 = document.querySelector('.btn');

    button1.addEventListener('click', function() {
        // Redirect to login_page when button is clicked
        window.location.href = '/login_page';
    });
});