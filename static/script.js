document.addEventListener("DOMContentLoaded", function() {
    setInterval(fetchTankData, 1000);  // Fetch data every 1 second

    function fetchTankData() {
        fetch('/get_tank_data')
            .then(response => response.json())
            .then(data => {
                data.forEach(tank => {
                    document.getElementById(`tank-${tank.id}-temp`).textContent = `${tank.temperature}°C`;
                    document.getElementById(`tank-${tank.id}-weight`).textContent = `${tank.weight} Te`;
                });
            });
    }
});
