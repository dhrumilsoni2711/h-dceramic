// alert.js

// Function to show an alert if a message is passed from Django
document.addEventListener("DOMContentLoaded", function() {
    // Select the alert message element
    const alertMessageElement = document.getElementById("alert-message");
    alert(alertMessageElement.textContent.trim());
   
});
