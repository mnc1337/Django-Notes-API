const serverURLAddress = window.location.origin;

const redirectButton = document.querySelector("#redirectButton");

redirectButton.addEventListener("click", () => {
    window.location.href = `${serverURLAddress}/`;
});