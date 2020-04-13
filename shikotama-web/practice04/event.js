const $eventButton = document.getElementById("js-EventButton");
$eventButton.addEventListener("click", (event) => {
    console.log(event);
    event.target.textContent = "";
});

const $colorPullet = document.getElementById("js-text");
$colorPullet.addEventListener("click", (event) => {
    event.target.style.backgroundColor = ` rgb(${event.screenX}, ${event.screenY}, ${event.pageY})
    `});