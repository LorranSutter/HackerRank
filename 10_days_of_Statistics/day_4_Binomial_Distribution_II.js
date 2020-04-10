function processData(input) {
    //Enter your code here
    function factorial(n) {
        return n === 0 ? 1 : factorial(n - 1) * n;
    }

    function combinations(n, x) {
        return factorial(n) / (factorial(x) * factorial(n - x));
    }

    function binomial(n, x, p) {
        return combinations(n, x) * p ** x * (1 - p) ** (n - x);
    }

    let first = 0;
    let second = 0;
    for (let k = 0; k <= 2; k++) {
        first += binomial(10, k, 0.12);
    }
    for (let k = 2; k <= 10; k++) {
        second += binomial(10, k, 0.12);
    }

    console.log(first.toFixed(3));
    console.log(second.toFixed(3));
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});
