function processData(input) {
    //Enter your code here
    input = input.split('\n');
    let [day1, month1, year1] = input[0].split(' ').map(x => parseInt(x));
    let [day2, month2, year2] = input[1].split(' ').map(x => parseInt(x));

    let date1 = new Date(`${month1}-${day1}-${year1}`);
    let date2 = new Date(`${month2}-${day2}-${year2}`);

    if (date1 - date2 <= 0)
        console.log(0);
    else if (year1 > year2)
        console.log(10000);
    else if (month1 > month2)
        console.log(500 * (month1 - month2));
    else if (day1 > day2)
        console.log(15 * (day1 - day2));
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
