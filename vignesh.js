// let arr = [1,2,3,1,1,3,4,5];
// let i = 0;
// let j = i+1;
// while(i<arr.length-1){
//     if(arr[i]==arr[j]){
//         arr.splice(j,1)
//     }else{
//          j++;
//     }
//     if (j==arr.length) {
//         i++;
//         j=i+1;
//     }
// }
// console.log(arr);// output [ 1, 2, 3, 4, 5 ]

// let arr=[1,2,3,4,5]
// let arr1=[5,6,7,8,9]
// let c= arr1+arr1

// Calculate the Total Price of Groceries/
// let obj=[
// 	{ product: "Milk", quantity: 1, price: 1.50},
// 	{ product: "Eggs", quantity: 12, price: 0.10 },
// 	{ product: "Bread", quantity: 2, price: 1.60   },
// 	{ product: "Cheese", quantity: 1, price: 4.50 }
// ]

//   function getTotalPrice(groceries) {

//       let final=0
//     for (let i = 0; i < groceries.length; i++) {
//       let quantityItems=groceries[i].quantity
//       let pricOfItem=groceries[i].price
//          final+=quantityItems*pricOfItem

//     }
//     return final;

//  }

// console.log(getTotalPrice(obj));

// // simple pair
// function simplePair(arr, n) {
//   for (let i = 0; i < arr.length; i++) {
//     for (let j = i+1; j < arr.length; j++) {
//       if (arr[i] * arr[j]==n) {
//       return [arr[i],arr[j]]
//     }
//     }
//   }
//   return "null"
// }
// console.log(simplePair([2, 2, 3], 8));

// function colorPatternTimes(cols) {
// 	let temp=cols[0]
//     let paintingTime=cols.length*2
//     let switching=0
//     for (let i = 0; i < cols.length; i++) {
//          if (temp!=cols[i]) {
//             switching++
//             paintingTime+=switching
//             temp=cols[i]
//          }
//         }
//     return paintingTime
// }
// console.log(colorPatternTimes(["Blue", "Blue", "Blue", "Red", "Red", "Red"])); //output 13
