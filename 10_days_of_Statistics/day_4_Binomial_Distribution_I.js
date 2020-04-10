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

    let res = 0;
    for (let k = 3; k <= 6; k++) {
        res += binomial(6, k, 1.09 / 2.09);
    }

    console.log(res.toFixed(3));
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
