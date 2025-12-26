//1) Count vowels in a string
// let s = "apple";
// let count = 0;
// for (let i = 0; i < s.length; i++) {
//   if (s[i] == "a" ||s[i] =="e" ||s[i] == "i" || s[i] =="o" ||s[i] == "u") {
//     count++;
//   }
// }
// console.log(count);

// Expected output: 2

//2) Count Occurrences of Each Element
// let arr = ["apple", "mango", "apple", "cherry", "mango", "apple"];
// let obj = {}
// for(i=0;i<arr.length;i++){
//     if(obj[arr[i]]){
//        obj[arr[i]]++
//     }
//     else{
//         obj[arr[i]]=1
//     }
// }
// console.log(obj);

// Expected output: { apple: 3, mango: 2, cherry: 1 }


// 3)Sort Objects by Age
// let users = [
//   { name: "Alice", age: 25 },
//   { name: "Bob", age: 19 },
//   { name: "Charlie", age: 30 }
// ];
// let asc = [...users].sort((a,b) => a.age-b.age)
// console.log(asc);

// Expected output:[
//   { name: 'Bob', age: 19 },
//   { name: 'Alice', age: 25 },
//   { name: 'Charlie', age: 30 }
// ]


// 4) Remove Falsy Values (Using filter())
// let arr = [0, "hello", false, 42, "", null, "JS", undefined];
// let value = arr.filter(i => i )
// console.log(value);

// Expected output:[ 'hello', 42, 'JS' ]


// 5)Find the longest word
// let arr = ["apple", "banana", "kiwi", "strawberry"]
// let narr = ""
// for (i=0; i<arr.length; i++){
//         if (arr[i].length > narr.length){
//             narr=arr[i]
//         }
// }
// console.log(narr)




// 6) Find the missing numbers
// let arr = [1, 2, 6];
// function findMissing(arr) {
//     let missing = [];
//     let max = Math.max(...arr);

//     for (let i = 1; i < max; i++) {
//         if (!arr.includes(i)) {
//             missing.push(i);
//         }
//     }
//     return missing;
// }
// console.log(findMissing(arr));
//[3,4,5]


// 7) Not repeated first character
// function firstNonRepeatingChar(str) {
//     let count = {};
//     for (let ch of str) {
//         count[ch] = (count[ch] || 0) + 1;
//     }
//     for (let ch of str) {
//         if (count[ch] === 1) {
//             return ch;
//         }
//     }
//     return -1;
// }
// console.log(firstNonRepeatingChar("aabbfccd")); 


//8)
//  let n = 5; 
// for (let i = n; i >0; i--) {
//   let row = '';
//   for (let j = n-i; j < n; j++) {
//     row += '* ';
//   }
//   console.log(row);
// }

// Expected output:
// * * * * * 
// * * * * 
// * * * 
// * * 
// * 






