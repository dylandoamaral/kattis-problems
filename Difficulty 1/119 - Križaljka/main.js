const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function intersection(a, b){
    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < b.length; j++) {
            if (a[i] == b[j]){
                return [i, j]
            }     
        }
    }
}

rl.on('line', (line) => {
    var words = line.split(' ');
    var a = words[0]
    var b = words[1]
    values = intersection(a, b)
    word = ""
    for (let i = 0; i < b.length; i++) {
        if (i == values[1]){
            console.log(a)
        }else{
            for (let j = 0; j < a.length; j++) {
                if (j == values[0]){
                    word += b[i]
                }else{
                    word += "."
                }
            }
            console.log(word)
            word = ""
        }
    }
});