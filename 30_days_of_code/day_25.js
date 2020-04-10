function processData(input) {
    input = input.split('\n');
    input = input.slice(1).map(x => parseInt(x));
    let isPrime = true;

    for (let num of input) {
        if (num === 2 || num === 3) {
            isPrime = true;
        } else if (num % 2 === 0 || num === 1) {
            isPrime = false;
        } else {
            let sq = Math.ceil(Math.sqrt(num));
            for (let k = 3; k <= sq; k += 2) {
                if (num % k === 0) {
                    isPrime = false;
                    break;
                }
            }
        }

        console.log(isPrime ? 'Prime' : 'Not prime');
        isPrime = true;
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
