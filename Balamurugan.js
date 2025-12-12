//  Question 1 — Array 
// const numbers = [1, 2, 3, 4, 5];
// let sum = 0;
// function addNumbers(arr) {
//   for (let i = 0; i < arr.length; i++) {
//     const value = arr[i];
//     sum += value;
//   }
//   return sum;
// }
// const result = addNumbers(numbers);
// console.log("Sum is:", result);
// console.log("Original array:", numbers);
// console.log("Length:", numbers.length);
// console.log("Done");

//  Expected Output
// Sum is: 15
// Original array: [1,2,3,4,5]
// Length: 5
// Done

// -------------------------------------------------------------------------------------------

//  Question 2 — Object Property Access 
// const user = {
//   name: "Arun",
//   age: 17,
//   city: "Chennai",
// };
// function getDetails(u) {
//   let info = "";
//   info += "Name: " + u.name + "\n";
//   info += "Age: " + u.age+ "\n";
//   info += "City: " + u.city+ "\n";
//   return info;
// }
// const output = getDetails(user);
// console.log("User Details:\n" + output);
// console.log("End of program");

//  Expected Output
// User Details:
// Name: Arun
// Age: 17
// City: Chennai
// End of program

// ------------------------------------------------------------------------------------------------

//  Question 3 — Missing  

// function multiply(a, b) {
//   let result = a * b;
//   console.log("Multiplying:", a, b);
//   console.log("Result calculated");
//   return result
// }
// const x = multiply(5, 4);
// console.log("Output:", x);
// console.log("Check complete");

// const y = multiply(3, 3);
// console.log("Output y:", y);


//  Expected Output
// Multiplying: 5 4
// Result calculated
// Output: 20
// Check complete
// Multiplying: 3 3
// Result calculated
// Output y: 9


// --------------------------------------------------------------------------------------------

//  Question 4 

// const marks = 85;

// function checkPass(score) {
//   if (score >= 85) {
//     return "Pass";
//   } else {
//     return "Fail";
//   }
// }

//  const status = checkPass(marks);
//  console.log("Marks:", marks);
//  console.log("Status:", status);


//  Expected Output
// Marks: 85
// Status: Pass




// ----------------------------------------------------------------------------------------------
//  Question 5 

// let items = ["pen", "book"];
// function addItem(list, item) {
//   console.log("Adding:", item);
//   list.push(item); 
//   console.log("Item added?");
//   return list;
// }
//  const result = addItem(items, "pencil");

//  console.log("Items now:", items);
//  console.log("Result:", result);
//  console.log("Length:", items.length);




//  Expected Output
// Adding: pencil
// Items now: ["pen", "book", "pencil"]
// Result: ["pen", "book", "pencil"]
// Length: 3

// ----------------------------------------------------------------------------
// 6.count words

// function countWords(wordss){
//     let words = wordss.split(" ").length;
//     return words
// }
// console.log(countWords("JavaScript is fun to learn"));

// expected : 5

// ------------------------------------------------------------------------------------------------

// question 7

// let str = "Race car";
// str = str.replace(/\s+/g,"").toLowerCase();
// let nstr = ""

// for (i=str.length-1; i>=0; i--){
//     nstr+=str[i]
// }
// console.log("Original:", str);
// console.log("Reversed:", nstr);

// if (str == nstr){
//     console.log("True")
// }else{
//     console.log("False")
// }


// Expedted :
// Original: racecar
// Reversed: racecar
// True


// ---------------------------------------------------------------------------------------------

// question 8

//  Remove null, undefined, false, 0, "", and NaN values from the array.

// let arr = [0, "hello", false, 42, "", null, "JS", undefined];
// let narr = []
// for (i=0;i<arr.length;i++){      
//     if(arr[i]){
//         narr.push(arr[i])
//     }
// }
// console.log(narr)

//output: [ 'hello', 42, 'JS' ]

// ------------------------------------------------------------------------------------------

// question 9

// sum of the elements let a = [1,2,3,4,5,true] 

// let a = [1,2,3,4,5,true,5]
// let sum = 0
// for (let i=0; i<a.length; i++){
//     if (parseInt(a[i])){
//     sum+=a[i]
// }
// }
// console.log("The sum of the Number is :",sum)

// output: The sum of the Number is : 20