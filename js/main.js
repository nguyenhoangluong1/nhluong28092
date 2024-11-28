async function fetchWeatherData() {
    try {
        const response = await fetch('/api/weather-data');
        const data = await response.json();
        
        document.getElementById('temperature').textContent = 
            `${data.temperature.toFixed(1)}°C`;
        document.getElementById('humidity').textContent = 
            `${data.humidity}%`;
        document.getElementById('precipitation').textContent = 
            `${data.precipitation.toFixed(1)} mm`;
        document.getElementById('wind-speed').textContent = 
            `${data.wind_speed.toFixed(1)} km/h`;
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}

// Fetch data immediately and then every 5 minutes
fetchWeatherData();
setInterval(fetchWeatherData, 7000);


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

// footer clock
function updateFooterClock() {
    const now_1 = new Date();
    const hours_1 = String(now_1.getHours()).padStart(2, '0');
    const minutes_1 = String(now_1.getMinutes()).padStart(2, '0');

    document.getElementById('footer-hours').textContent = hours_1;
    document.getElementById('footer-minutes').textContent = minutes_1;

    if (hours_1 >= 12) {
        document.getElementById('footer-ampm').textContent = 'PM';
    }
}

setInterval(updateFooterClock, 1000);
updateFooterClock();