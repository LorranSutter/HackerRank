function processData(input) {
    //Enter your code here
    let lambda1 = 0.88;
    let lambda2 = 1.55;

    console.log((160 + 40 * (lambda1 + lambda1 ** 2)).toFixed(3));
    console.log((128 + 40 * (lambda2 + lambda2 ** 2)).toFixed(3))

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
