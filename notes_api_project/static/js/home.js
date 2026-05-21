const serverURLAddress = window.location.origin;

const routes = {
    "createUserButton": "/create_user",
    "createNoteViaDRFButton": "/api/notes",
    "createNoteViaGraphQLButton": "/graphql",
    "checkAllEndpointsButton": "/api/docs",
    "goToAppPageButton": "/app",
    "logInToYourAccountButton": "/login",
};

const buttons = [
    document.querySelector("#createUserButton"),
    document.querySelector("#createNoteViaDRFButton"),
    document.querySelector("#createNoteViaGraphQLButton"),
    document.querySelector("#checkAllEndpointsButton"),
    document.querySelector("#goToAppPageButton"),
    document.querySelector("#logInToYourAccountButton"),
];

buttons.forEach(btn => {
    if (!btn) return;

    btn.addEventListener("click", () => {
        const path = routes[btn.id];
        if (path) {
            window.location.href = `${serverURLAddress}${path}`;
        }
    });
});