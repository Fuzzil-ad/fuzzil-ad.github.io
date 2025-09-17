// Task 1
// Add an event listner to the button (the user drags his mouse over the button)
let btn = document.getElementById("justin-btn");
let result = document.getElementById("result");

btn.addEventListener("mouseover", mOver);
btn.addEventListener("mouseout", mOut);

function mOver(){
    result.innerText = "Welcome to My Heart";
    result.style.backgroundColor = 'pink';
    result.style.color = 'blue';
}

function mOut(){
    result.innerText = "Don't Leave Me Please";
    result.style.backgroundColor = 'black';
    result.style.color = 'red';
}

// Task 2
// Add an event listner to the button (the user drags his mouse out of the button)
