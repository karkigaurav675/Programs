// Practice Challenge 1 -
// 1. Create a boolean variable called 'myBoolean' and set it to 'true'.
// 2. Create a string variable called 'myString' and set it to 'hello world'.
// 3. Create a number variable called 'firstNumber' and set it to equal to '20'.
// 4. Create another number variable called 'secondNumber' and set it equal to '40'.
// 5. Re-assign 'secondNumber' and set it equal to '80'.
// 6. Create an array called 'myArray' and put 'myBoolean' at index 0, and 'myString' at index 1.
// 7. Create an object called 'myObject' and assign 'myArray' to a property called 'firstProperty', and the sum of 'firstNumber' and 'secondNumber' to a property called 'sumProperty'.
// 8. Print 'myObject' to the console.
// 9. Print the 'sumProperty' of 'myObject' to the console.
// 10. Print the value at index 1 of 'firstProperty.'


const myBoolean = true;
const myString = 'hello world';
const firstNumber = 20;
let secondNumber = 40;
secondNumber = 80;
// console.log(secondNumber);
const myArray = [myBoolean, myString];
// console.log(myArray);
myObject = {firstProperty: myArray, sumProperty: firstNumber + secondNumber};
console.log(myObject);
console.log(myObject.sumProperty);
console.log(myObject.firstProperty[1]);