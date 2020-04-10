'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}



function main() {
    const n = parseInt(readLine(), 10);
    let bin = n.toString(2);
    let maxOne = 0, currentOnes = 0;

    for (let digit of bin) {
        if (digit === "1") {
            currentOnes++;
        } else {
            if (currentOnes > maxOne) {
                maxOne = currentOnes;
            }
            currentOnes = 0;
        }
    }
    if (currentOnes > maxOne) {
        maxOne = currentOnes;
    }

    console.log(maxOne);
}
