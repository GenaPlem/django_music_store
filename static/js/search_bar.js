const searchIcons = document.querySelectorAll('.search-icon');
const searchBar = document.getElementById('searchBar');
const searchBarForm = document.getElementById('searchBarForm');

searchIcons.forEach(icon => {
    icon.addEventListener('click', () => {
        searchBarForm.classList.toggle('show');
        searchBar.focus();
    });
});
