function processData(input) {
    //Enter your code here
    function geometric(n, p) {
        return (1 - p) ** (n - 1) * p;
    }

    let res = 0;
    for (let k = 1; k <= 5; k++) {
        res += geometric(k, 1 / 3);
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
