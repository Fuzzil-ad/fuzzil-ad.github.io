function calculate() {

    // YOUR CODE GOES HERE
    var num1 = Number(document.getElementById("number1").value);
    var num2 = Number(document.getElementById("number2").value);
    var sum = 0;
    for(i=num1 ; i <(num2+1); i++){
        sum += i;
    }
        
    var result = document.getElementById("result");
    // result.setAttribute("customAttribute", sum)
    result.innerText = sum;

}