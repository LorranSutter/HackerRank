function processData(input) {
    //Enter your code here
    input = input.split('\n');
    n = parseInt(input[0]);
    x = input[1].split(" ").map(x => parseInt(x));
    f = input[2].split(" ").map(x => parseInt(x));

    let arr = [];
    for (let k in x) {
        for (let j = 0; j < f[k]; j++) {
            arr.push(x[k]);
        }
    }

    function median(nums) {
        let length = nums.length;
        let length2 = parseInt(length / 2);

        return length % 2 == 0 ? (nums[length2 - 1] + nums[length2]) / 2 : nums[length2];
    }

    function quartile(arr, q) {
        arr.sort(function (a, b) { return a - b });
        if (q === 1)
            return median(arr.slice(0, parseInt(arr.length / 2)));
        else if (q === 2)
            return median(arr);
        else if (q === 3)
            return median(arr.slice(parseInt((arr.length + 1) / 2)));
    }

    console.log((quartile(arr, 3) - quartile(arr, 1)).toFixed(1));
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
