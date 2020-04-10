function processData(input) {
    //Enter your code here

    function mean(nums) {
        return nums.reduce((a, b) => a + b, 0) / nums.length;
    }

    function median(nums) {
        nums.sort(function (a, b) { return a - b });
        let length = nums.length;

        return length % 2 == 0 ? (nums[length / 2 - 1] + nums[length / 2]) / 2 : nums[length / 2];
    }

    function mode(nums) {
        let modeDict = {};
        let maxIndex = 0;
        for (let n of nums) {
            if (n in modeDict) modeDict[n]++;
            else modeDict[n] = 0;

            if (modeDict[n] > maxIndex) maxIndex = modeDict[n];
        }

        let modes = [];
        for (let key in modeDict) {
            if (modeDict[key] === maxIndex) {
                modes.push(key);
            }
        }

        return modes.sort(function (a, b) { return a - b })[0];
    }

    input = input.split("\n");
    let N = parseInt(input[0])

    let arr = input.slice(1)[0].split(' ').map((x) => parseInt(x));

    console.log(mean(arr).toFixed(1));
    console.log(median(arr).toFixed(1));
    console.log(mode(arr));
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
