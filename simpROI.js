
const weeks = [
  { amount_spent: 8000,  texts_sent: 40, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 55, texts_replied: 3 },
  { amount_spent: 9000,  texts_sent: 38, texts_replied: 4 },
  { amount_spent: 11000, texts_sent: 42, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 35, texts_replied: 3 },
];

let totalSpent = 0;
let totalSent = 0;
let totalReplies = 0;

for (const week of weeks) {
  totalSpent += week.amount_spent;
  totalSent += week.texts_sent;
  totalReplies += week.texts_replied;
}

const replyRate = Math.round((totalReplies / totalSent) * 100);

let verdict;

if (replyRate < 20) {
  verdict = "Cut your losses";
} else if (replyRate < 50) {
  verdict = "She might like you";
} else {
  verdict = "Keep going";
}

console.log(`Total spent: KES ${totalSpent}`);
console.log(`Texts sent: ${totalSent}`);
console.log(`Replies received: ${totalReplies}`);
console.log(`Reply rate: ${replyRate}%`);
console.log(`Verdict: ${verdict}`);