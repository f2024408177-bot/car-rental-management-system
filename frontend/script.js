const API_URL = "https://car-rental-management-system-production-1c66.up.railway.app";


async function registerUser() {

    const name =
        document.getElementById("regName").value;

    const email =
        document.getElementById("regEmail").value;

    const password =
        document.getElementById("regPassword").value;

    const response = await fetch(
        `${API_URL}/register`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name,
                email,
                password
            })
        }
    );

    const data = await response.json();

    alert(data.message);
}



async function loginUser() {

    const email =
        document.getElementById("loginEmail").value;

    const password =
        document.getElementById("loginPassword").value;

    const response = await fetch(
        `${API_URL}/login`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email,
                password
            })
        }
    );

    const data = await response.json();

    alert(data.message);
}

async function loadCars() {

    const response = await fetch(
        `${API_URL}/cars`
    );

    const cars = await response.json();

    let html = "";

    cars.forEach(car => {

        html += `
        <div class="card">

            <h3>${car.car_name}</h3>

            <p>Model: ${car.model}</p>

            <p>Price: ${car.price_per_day} PKR/day</p>

            <p>Status: ${car.status}</p>

            <button class="btn">
                Book Now
            </button>

        </div>
        `;
    });

    document.getElementById(
        "carsContainer"
    ).innerHTML = html;
}

async function loadBookings() {

    const response = await fetch(
        `${API_URL}/bookings`
    );

    const bookings = await response.json();

    let html = "";

    bookings.forEach(booking => {

        html += `
        <tr>

            <td>${booking.id}</td>

            <td>${booking.user_id}</td>

            <td>${booking.car_id}</td>

            <td>${booking.status}</td>

        </tr>
        `;
    });

    document.getElementById(
        "bookingsTable"
    ).innerHTML = html;
}

async function loadDashboard() {

    const response = await fetch(
        `${API_URL}/dashboard`
    );

    const data = await response.json();

    document.getElementById(
        "totalCars"
    ).innerHTML =
        "Total Cars: " +
        data.total_cars;

    document.getElementById(
        "totalBookings"
    ).innerHTML =
        "Total Bookings: " +
        data.total_bookings;

    document.getElementById(
        "availableCars"
    ).innerHTML =
        "Available Cars: " +
        data.available_cars;
}