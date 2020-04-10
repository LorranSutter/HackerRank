function processData(input) {
    //Enter your code here
    input = input.split('\n');
    let x = [], y = [];
    for (elem of input) {
        elem = elem.split(' ');
        x.push(parseInt(elem[0]));
        y.push(parseInt(elem[1]));
    }

    function mean(arr) {
        let len = arr.length;
        if (len <= 0) return 0;
        return arr.reduce((a, b) => a + b, 0) / len;
    }

    function linearRegression(x, y) {
        let n = x.length;
        let xSum = x.reduce((a, b) => a + b, 0);
        let x2Sum = x.map(a => a * a).reduce((a, b) => a + b, 0);
        let ySum = y.reduce((a, b) => a + b, 0);
        let xySum = 0;
        for (k in x) {
            xySum += x[k] * y[k];
        }

        let b = (n * xySum - xSum * ySum) / (n * x2Sum - xSum ** 2);
        let a = mean(y) - b * mean(x);

        return [a, b];
    }

    let [a, b] = linearRegression(x, y);

    console.log((a + b * 80).toFixed(3));
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
