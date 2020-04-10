function processData(input) {
    //Enter your code here
    input = input.split('\n')
    x = input[1].split(' ').map(x => parseInt(x));

    function mean(arr) {
        return arr.reduce((a, b) => a + b, 0) / arr.length;
    }

    function std(arr) {
        let m = mean(arr);

        let temp = 0;
        for (let elem of arr) {
            temp += (elem - m) ** 2;
        }

        return Math.sqrt(temp / arr.length);
    }

    console.log(std(x).toFixed(1));
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
