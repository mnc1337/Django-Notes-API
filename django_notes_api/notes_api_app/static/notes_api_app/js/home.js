const serverURLAddress = window.location.origin;

const mainButton = document.querySelector("#mainButton");

mainButton.addEventListener("click", () => {
    window.location.href = `${serverURLAddress}/`;
});