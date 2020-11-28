document.addEventListener('DOMContentLoaded', () => {
    let toggleFormButton = document.querySelector('#toggle_form');
    let form = document.querySelector('#form');
    let closeButton = document.querySelector('#close');
    let entry = document.querySelector('#entry')
    form.style.display = 'none';
    closeButton.style.display = 'none';
    toggleFormButton.onclick = () => {
        toggleFormButton.style.display = 'none';
        form.style.display = 'block';
        closeButton.style.display = 'block';
        if (entry) {
            entry.style.display = 'none';
        }
    }
    closeButton.onclick = () => {
        toggleFormButton.style.display = 'block';
        form.style.display = 'none';
        closeButton.style.display = 'none';
        if (entry) {
            entry.style.display = 'block';
        }
    }
});