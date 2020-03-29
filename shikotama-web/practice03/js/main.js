const helloWorld = (hikisu_1,hikisu_2) => {
    let sum = tashizan(hikisu_1, hikisu_2);
    console.log(sum);
}

const tashizan = (num1, num2) => {
    return num1 + num2
}

const chageBox = () => {
    const $box = document.getElementById("js-box");
    $box.textContent = "";
    // console.log($box);
}