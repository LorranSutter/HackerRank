function processData(input) {
    //Enter your code here
    input = input.split('\n');

    let X = input[1].split(' ').map((x) => parseInt(x));
    let W = input[2].split(' ').map((x) => parseInt(x));

    let sum = 0;
    let weightSum = W.reduce((a, b) => a + b, 0);

    for (let k in X) {
        sum += X[k] * W[k];
    }

    console.log((sum / weightSum).toFixed(1));
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
