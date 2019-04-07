const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var num = parseInt(line);
	for(i = 1; i <= num; i++){	
		console.log(i + " Abracadabra");
	}
});