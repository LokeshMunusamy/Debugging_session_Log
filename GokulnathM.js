
// sum:1
// let a = {count:10};
// let b = {...a};
// b.count = 20;
// console.log(a.count);
// console.log(b.count);


//expected output:10
//but output :20


// sum:2
// function update(qty){
//   return qty ?? 10;
// }
// console.log(update(0));


//expected output:0
//but output :10

// sum:3
// let arr = [1,2,3];
// let sum = arr.reduce((a,b)=>{
//   return a + b;
// },0);
// console.log(sum);


//expected output:6
//but output :undefined

// sum:4
// function removeDuplicates(arr) {
//   for (let i = 0; i < arr.length; i++) {
//     if (arr.indexOf(arr[i]) !== i) {
//       arr.splice(i, 1);
//      i--
//     }
//   }
//   return arr;
// }

// let nums = [1, 2, 2, 3, 3, 3, 4];
// console.log(removeDuplicates(nums));

//expected output:[1,2,3,4]
//but output :[1,2,3,3,4]


// sum:5
// function createCounters() {
//   let counters = [];

//   for (let i = 0; i <3; i++) {
//     counters.push(function () {
//       return i;
//     });
//   }

//   return counters;
// }

// let result = createCounters();

// console.log(result[0]());
// console.log(result[1]());
// console.log(result[2]());

//expected output:[0,1,2]
//but output :[4,4,4]


// sum:6
// function commonElements(a, b) {
//   let result = [];

//   for (let i = 0; i < a.length; i++) {
//     for (let j = 0; j < b.length; j++) {
//       if (a[i] === b[j]) {
//         if(!result.includes(a[i])){
//         result.push(a[i]);
//         break
//         }
//       }
//     }
//   }

//   return result;
// }

// let arr1 = [1, 2, 2, 3];
// let arr2 = [2, 2,1, 3, 3];

// console.log(commonElements(arr1, arr2));

//expected output:[2,3]
//but output :[2,2,2,2,3,3]


// sum:7
// function removeCommon(a, b) {
//   for (let i = 0; i < a.length; i++) {
//     for (let j = 0; j < b.length; j++) {
//       if (a[i] === b[j]) {
//         a.splice(i, 1);
//         b.splice(j, 1);
//         j--
//       }
//     }
//   }
//   return { a, b };
// }

// let arr1 = [1, 2, 2, 3, 4];
// let arr2 = [2, 2, 3, 5];

// console.log(removeCommon(arr1, arr2));

// sum:8
// function countPairs(arr) {
//   let count = 0;

//   for (let i = 0; i < arr.length; i++) {
//     for (let j =i+1; j < arr.length; j++) {
//       if ( arr[i] + arr[j] == 5) {
//         count++;
//       }
//     }
//   }

//   return count;
// }

// console.log(countPairs([1, 2, 3, 4]));



//expected output:2
//but output :4








