function processData(input) {
    let re = RegExp("^\\d{1,100} (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$");

    input = input.split("\n");
    let N = parseInt(input[0]);

    for (let line of input.slice(1)) {
        console.log(line.match(re) === null ? "INVALID" : "VALID");
    }
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
