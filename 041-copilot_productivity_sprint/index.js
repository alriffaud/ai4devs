// index.js - Basic front-end component for CLI tool report visualization
// Prompt: "Create a simple CLI dashboard in JavaScript."
const fs = require('fs');

function loadReport() {
  const data = fs.readFileSync('report.json');
  return JSON.parse(data);
}

// Prompt: "Generate a function to print report table to console."
function printReportTable(report) {
  console.log('ID | Description                   | Estimate | Actual');
  console.log('---|-------------------------------|----------|-------');
  report.forEach(item => {
    console.log(
      `${item.id}  | ${item.description.padEnd(30)} | ${item.estimate.toString().padEnd(8)} | ${item.actual}`
    );
  });
}

// Main
const report = loadReport();
printReportTable(report);
