// Booking list cards
const bookingCards = document.getElementsByClassName("bookingCardItem");
// Delete confirm modal
const deleteButton = document.getElementById("delete-button");


for (let i = 0; i < bookingCards.length; i++) {
    // Add event listener for mouseover
    bookingCards[i].addEventListener("mouseover", function () {
        this.classList.add("drop-shadow");
    });

    // Add event listener for mouseout
    bookingCards[i].addEventListener("mouseout", function () {
        this.classList.remove("drop-shadow");
    });
}


// Checks if deleteButton exists before adding event listener.
// Throws errors in dev tools if there's no conditional
if (deleteButton) {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

    deleteButton.addEventListener("click", function() {
        deleteModal.show();
    });
}
