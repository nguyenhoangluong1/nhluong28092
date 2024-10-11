// toggle theme
// const moonIcon = document.getElementById('moon-icon');
// const sunIcon = document.getElementById('sun-icon');
// const body = document.body;

// // check theme status from local storage
// if (localStorage.getItem('theme') === 'dark') {
//     body.classList.add('dark-mode');
//     moonIcon.style.display = 'none';
//     sunIcon.style.display = 'block';
// }

// // change theme to night mode and save status
// moonIcon.addEventListener("click", () => {
//     body.classList.add('dark-mode');
//     moonIcon.style.display = 'none';
//     sunIcon.style.display = 'block';
//     localStorage.setItem('theme', 'dark');
// });

// sunIcon.addEventListener("click", () => {
//     body.classList.remove('dark-mode');
//     sunIcon.style.display = 'none';
//     moonIcon.style.display = 'block';
//     localStorage.setItem('theme', 'light');
// });



// fetch("http://127.0.0.1:5000/app/api")
//     .then(response => response.json())
//     .then(data => {
//         console.log(data)
//     })

// digital clock script here
function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    document.getElementById('hours').textContent = hours;
    document.getElementById('minutes').textContent = minutes;
    document.getElementById('seconds').textContent = seconds;
}

setInterval(updateClock, 1000);
updateClock();