function processData(input) {
    //Enter your code here
    function geometric(n, p) {
        return (1 - p) ** (n - 1) * p;
    }

    console.log(geometric(5, 1 / 3).toFixed(3));

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
