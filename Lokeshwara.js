// 1 .  op : true
// let s1 = "tops".split("").sort().join("");
// let s2 = "stop".split("").sort().join("")

// console.log(s1);
// console.log(s2);
// console.log(s1===s2);

// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-


// 2. op: JavaScript

// let str = "JavaScript is very powerful";
// let words = str.split(" ");
// let longest = "";

// for (let i = 0; i < words.length; i++) {
//   if (words[i].length > longest.length) {
//     longest = words[i];
//   }
// }

// console.log(longest);

// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-

// 3. op : poain

// let str = "programming";
// let res = "";

// for (let i = 0; i < str.length; i++) {
//   if (str.indexOf(str[i]) === str.lastIndexOf(str[i])) {
//     res += str[i];
//   }
// }
// console.log(res);

// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-

// 4.Count Characters That Are Uppercase

// Input: "HeLLo" → Output: 3

// function countUpper(str) {
//     let c = 0;
//     for (let ch of str) {
//         if (ch >= "A" && ch <= "Z") c++;
//     }
//     return c;
// }
// x = countUpper("HeLLo");
// console.log(x)

// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-

//5. Get Last Even Number in Array

// Input: [3,5,8,7,12,9] → Output: 12

// function lastEven(arr) {
//     for (let i = arr.length - 1; i >= 0; i--) {
//         if (arr[i] % 2 === 0) return arr[i];
//     }
//     return null;
// }
// x = lastEven([3,5,8,7,12,7,9,8,5])
// console.log(x)

// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-

// 6. PROBLEM — Return Strings Ending With “ing”

// Input: ["go","swimming","bring","hello"] → Output: ["swimming","bring"]

// function endsWithIng(words) {
//     return words.filter(w=>w.endsWith("ing"));
// }
// x = endsWithIng(["go","swimming","bring","hello"])
// console.log(x);


// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-

// 7.PROBLEM — Find Longest Run of Same Number

// Input: [2,2,2,3,3,1] → Output: 3

// function longestRun(arr) {
//     let max = 0, cur = 1;
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] === arr[i+1]) cur++;
//         else cur = 1;
//         if (cur >= max) max = cur;
//     }
//     return max;
// }

// x = longestRun([2,2,2,2,2,2,2,3,3,3,3,3,1])
// console.log(x);
