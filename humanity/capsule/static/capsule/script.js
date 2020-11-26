document.addEventListener('DOMContentLoaded', () => {
    let addGoalButton = document.querySelector('#add_goal');
    let addGoalForm = document.querySelector('#add_goal_form');
    let cancelButton = document.querySelector('#cancel_add');
    addGoalForm.style.display = 'none';
    cancelButton.style.display = 'none';
    addGoalButton.onclick = () => {
        addGoalButton.style.display = 'none';
        addGoalForm.style.display = 'block';
        cancelButton.style.display = 'block';
    }
    cancelButton.onclick = () => {
        addGoalButton.style.display = 'block';
        addGoalForm.style.display = 'none';
        cancelButton.style.display = 'none';
    }
});