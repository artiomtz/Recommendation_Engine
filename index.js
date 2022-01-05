console.log("\n########## Attempting to run matching in Python ##########\n");

var testJsonData = {};

if (process.argv[2]) {
    console.log(`### Passing the argument to matching in Python ###\n`);
    testJsonData = process.argv[2]
} else {
    console.log(`### Passing a test file to matching in Python ###\n`);
    testJsonData = require('./python/input_test_data/input_test_data_1.json');
}

const { spawn } = require("child_process");
const runPython = spawn("venv/Scripts/python.exe", ["python/main.py", "node", JSON.stringify(testJsonData)]);

runPython.stdout.on("data", (data) => {
    console.log(`${data.toString()}`);
});

runPython.stderr.on("data", (data) => {
    console.error(`### Errors during matching in Python ###\n${data.toString()}`);
});

runPython.on("close", (data) => {
    console.log(`### Completed matching in Python with code: ${data.toString()} ###\n`);
});
