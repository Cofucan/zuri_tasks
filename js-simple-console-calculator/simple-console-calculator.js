const op_symbol = ["+", "-", "/", "*"];
const op_word = ["addition", "subtraction", "division", "multiplication"];

let operator = window.prompt(
    "What operation do you want to perform?\n+ addition\n- subtraction\n/ division\n* multiplication"
);

while (!op_symbol.includes(operator) && !op_word.includes(operator)) {
    operator = window.prompt(
        "Pls enter one of the operations below.\nEnter the symbol or the spelling:\n+ addition\n- subtraction\n/ division\n* multiplication"
    );
}

let firstNum = window.prompt("Enter your first number: ");
firstNum = parseFloat(firstNum);

while (isNaN(firstNum)) {
    firstNum = window.prompt(
        "Pls enter a valid number."
        );
        firstNum = parseFloat(firstNum);
}

let secondNum = window.prompt("Enter your second number: ");
secondNum = parseFloat(secondNum);

while (isNaN(secondNum)) {
    secondNum = window.prompt(
        "Pls enter a valid number."
        );
        secondNum = parseFloat(secondNum);
}

let sum = firstNum + secondNum;
let difference = firstNum - secondNum;
let ratio = firstNum / secondNum;
let product = firstNum * secondNum;

// if (operator == "+" || operator == "addition") {
//   alert(`The sum of ${firstNum} and ${secondNum} is ${sum}`);
// } else if (operator == "-" || operator == "subtraction") {
//   alert(`The difference between ${firstNum} and ${secondNum} is ${difference}`);
// } else if (operator == "/" || operator == "division") {
//   alert(`The ratio between ${firstNum} and ${secondNum} is ${ratio}`);
// } else if (operator == "*" || operator == "multiplication") {
//   alert(`The product of ${firstNum} and ${secondNum} is ${product}`);
// }

switch (operator) {
    case "+":
        alert(`The sum of ${firstNum} and ${secondNum} is ${sum}`);
        break;
    case "addition":
        alert(`The sum of ${firstNum} and ${secondNum} is ${sum}`);
        break;
    case "-":
        alert(`The difference between ${firstNum} and ${secondNum} is ${difference}`);
        break;
    case"subtraction":
        alert(`The difference between ${firstNum} and ${secondNum} is ${difference}`);
        break;
    case "/":
        alert(`The ratio between ${firstNum} and ${secondNum} is ${ratio}`);
        break;
    case "division":
        alert(`The ratio between ${firstNum} and ${secondNum} is ${ratio}`);
        break;
    case "*":
        alert(`The product of ${firstNum} and ${secondNum} is ${product}`);
        break;
    case "multiplication":
        alert(`The product of ${firstNum} and ${secondNum} is ${product}`);
        break;
}
