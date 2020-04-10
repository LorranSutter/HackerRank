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

function maxHourglassSum(A) {
    let aLength = A.length;
    let maxSum = Number.NEGATIVE_INFINITY, partialSum = 0;

    for (let i = 0; i < aLength - 2; i++) {
        for (let j = 0; j < aLength - 2; j++) {
            partialSum = A[i][j] + A[i][j + 1] + A[i][j + 2] + A[i + 1][j + 1] + A[i + 2][j] + A[i + 2][j + 1] + A[i + 2][j + 2];
            if (partialSum > maxSum)
                maxSum = partialSum;
        }
    }

    return maxSum;
}


function main() {
    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    console.log(maxHourglassSum(arr));
}
