function processData(input) {
    //Enter your code here
    function factorial(n) {
        if (n === 0) return 1;
        return factorial(n - 1) * n;
    }

    function poisson(lambda, k) {
        return lambda ** k * Math.E ** (-lambda) / (factorial(k));
    }

    console.log(poisson(2.5, 5).toFixed(3));
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
