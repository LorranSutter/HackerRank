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

function filterEmails(emails) {
    let regex = new RegExp('@gmail.com');
    let emailsFiltered = emails.filter(x => x.email.match(regex))

    let nameList = [];

    for (let email of emailsFiltered) {
        nameList.push(email.name);
    }

    return nameList.sort();
}

function main() {
    const N = parseInt(readLine(), 10);
    let listEmails = [];

    for (let NItr = 0; NItr < N; NItr++) {
        const firstNameEmailID = readLine().split(' ');

        const firstName = firstNameEmailID[0];

        const emailID = firstNameEmailID[1];

        listEmails.push({ name: firstName, email: emailID });
    }

    let names = filterEmails(listEmails);

    for (let name of names) {
        console.log(name);
    }
}
