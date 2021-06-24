function solution(lines) {
	let n = parseInt(lines[0]);
	for(let i = 1; i <= 3; i++) {
		console.log(`${n} * ${i} = ${n * i}`);
	}
}

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const lines = [];
rl.on("line", function(line) {
	lines.push(line);
}).on("close", function() {
	solution(lines);
});