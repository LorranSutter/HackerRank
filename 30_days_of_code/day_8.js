function processData(input) {
    //Enter your code here
    input = input.split('\n');
    let n = parseInt(input[0]);
    let firstInput = input.slice(1, n + 1);
    let secondInput = input.slice(n + 1);

    let dict = {};
    for (let elem of firstInput) {
        elem = elem.split(' ');
        dict[elem[0]] = elem[1];
    }

    for (let elem of secondInput) {
        if (elem in dict)
            console.log(`${elem}=${dict[elem]}`);
        else
            console.log('Not found');
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
