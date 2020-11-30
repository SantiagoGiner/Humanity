// Wait for page content to be loaded
document.addEventListener('DOMContentLoaded', () => {
    let toggleFormButton = document.querySelector('#toggle_form');
    let form = document.querySelector('#form');
    let closeButton = document.querySelector('#close');
    let entry = document.querySelector('#entry')
    // Initially hide the form and the close button
    form.style.display = 'none';
    closeButton.style.display = 'none';
    // When user clicks button to view form
    toggleFormButton.onclick = () => {
        // Show the form and close button; hide other elements
        toggleFormButton.style.display = 'none';
        form.style.display = 'block';
        closeButton.style.display = 'block';
        if (entry) {
            entry.style.display = 'none';
        }
    }
    // When user clicks button to close form
    closeButton.onclick = () => {
        // Hide the form and close botton; show other elements
        toggleFormButton.style.display = 'block';
        form.style.display = 'none';
        closeButton.style.display = 'none';
        if (entry) {
            entry.style.display = 'block';
        }
    }
});