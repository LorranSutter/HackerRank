/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowels = "", consoants = "";
    for (let k in s) {
        if ("aeiou".includes(s[k])) {
            vowels += s[k];
        } else {
            consoants += s[k];
        }
    }

    for (let k in vowels) {
        console.log(vowels[k]);
    }

    for (let k in consoants) {
        console.log(consoants[k]);
    }
}

