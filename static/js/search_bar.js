const searchIcons = document.querySelectorAll('.search-icon');
const searchBar = document.getElementById('searchBar');

searchIcons.forEach(icon => {
    icon.addEventListener('click', () => {
        searchBar.classList.toggle('show')
    });
});
