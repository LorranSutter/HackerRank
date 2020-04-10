'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the timeConversion function below.
 */
function timeConversion(s) {
    /*
     * Write your code here.
     */
    let ampm = s.slice(-2);
    let hour = s.slice(0, 2);
    let newHour = hour.toString();

    if (ampm === "PM") {
        if (hour === "12") newHour = "12";
        else newHour = (parseInt(hour) + 12).toString();
    } else if (hour === "12") {
        newHour = "00";
    }

    return s.replace(ampm, "").replace(hour, newHour);
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    let result = timeConversion(s);

    ws.write(result + "\n");

    ws.end();
}
