function processData(input) {
    //Enter your code here
    input = input.split("\n");
    n = parseInt(input[0]);

    for (str of input.slice(1)) {
        let odd = "", even = "";
        for (let k = 0; k < str.length; k++) {
            if (k % 2) odd += str[k];
            else even += str[k];
        }
        console.log(`${even} ${odd}`);
    }
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
