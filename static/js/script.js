// Booking list cards
const bookingCards = document.getElementsByClassName("bookingCardItem");

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
