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

// Complete the plusMinus function below.
function plusMinus(arr) {
    let pos = 0, zero = 0, neg = 0;
    for (let k in arr) {
        if (arr[k] > 0) pos++;
        else if (arr[k] < 0) neg++;
        else zero++;
    }

    let arrLength = arr.length;
    console.log(pos / arrLength);
    console.log(neg / arrLength);
    console.log(zero / arrLength);
}

function main() {
    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
