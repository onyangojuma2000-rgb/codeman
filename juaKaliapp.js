// Simulates what the DOM event listener would log when a craftsman submits an order
const processOrder = (clientName, jobType, quoteKes) => {
  const isLargeJob = quoteKes >= 10000;
  const priority   = isLargeJob ? "High" : "Normal";
  return `Client: ${clientName} | Job: ${jobType} | Quote: KES ${quoteKes.toLocaleString()} | Priority: ${priority}`;
};

// Three orders submitted via the form
const orders = [
  ["Wanjiku Homes",    "Sliding gate",  32000],
  ["Mwangi Hardware", "Window grills",  7200],
  ["Ochieng Shop",    "Security door", 18500],
];

console.log("Order board:");
for (const [client, job, quote] of orders) {
  console.log("  " + processOrder(client, job, quote));
}

const totalQuoted = orders.reduce((sum, o) => sum + o[2], 0);
console.log(`\nTotal quoted today: KES ${totalQuoted.toLocaleString()}`);
