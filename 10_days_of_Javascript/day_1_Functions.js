/*
 * Create the function factorial here
 */
function factorial(n) {
    let res = 1;
    for (let k = 2; k <= n; k++) {
        res *= k;
    }
    return res;
}