async function fetchData() {

    try {
        const curr_car_id = document.getElementById("curr_car").value;
        const response = await fetch(`https://api.mercedes-benz.com/configurator/v2/markets/en_DE/models/${curr_car_id}/configurations/initial`);

        const data = await response.json();
        const curr_car_image = data.images;
    } catch (error) {
        console.error(error);
    }
}