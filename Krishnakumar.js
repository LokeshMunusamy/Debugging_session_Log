// Question 1 

// const user = {
//     name: "Karthik",
//     scores: [60, 70, 80]
// };
// function updateScores(data) {
//     let scores = data.scores;
//     data.scores = scores.map(s => s + 10);
//     data.total = data.scores.reduce((a, b) => a + b,0);
// }
// updateScores(user);
// console.log(user.scores);
// console.log(user.total);

// Expected Output //
// [70, 80, 90]
// 240


// Question 2

// const product = {
//     id: 101,
//     name: "Mobile",
//     price: 15000
// };
// function printProduct(obj) {
//     for (let key in obj) {
//         console.log(key + " = " + obj[key]);
//     }
// }
// printProduct(product);

// Expected Output //
// id = 101
// name = Mobile
// price = 15000


// Question 3

// const account = {
//     owner: "Jabakumar",
//     balance: 5000,
//     transactions: [],
//     deposit:(amount)=>{
//         account.balance += amount;
//         account.transactions.push(amount);
//     }
// };
// account.deposit(1000);
// console.log(account.balance);
// console.log(account.transactions);

// Expected Output //
// 6000
// [1000]


// Question 4

// const scores = [40, 50, 60];
// function addBonus(arr) {
//   arr=arr.map(v => v + 10);
//   return arr
// }
// ;
// console.log("Scores:", addBonus(scores));

// Expected Output //
// Scores: [50, 60, 70]


// Question 5

// const values = [0, 1, 2, 3, null, undefined, 4];
// const cleaned = values.filter(v => typeof v=="number");
// console.log(cleaned);

//  Expected Output //
// [0, 1, 2, 3, 4]


// Question 6

// const prices = [];
// const total = prices.reduce((sum, p) => sum + p,0);
// console.log("Total:", total);

//  Expected Output //
// Total: 0


// Question 7

// function runTimers() {
//   for (let i = 1; i <=3; i++) {
//     setTimeout(function () {
//       console.log(i);
//     }, i*1000);
//   }
// }
// runTimers();

// Expected Output //
// 1
// 2
// 3


// Question 8

const state = {
    user: {
        name: "Amit"
    }
};
const copy=JSON.parse(JSON.stringify(state))
copy.user.name = "Rahul";
console.log(state.user.name);


// Expected Output //
// Amit