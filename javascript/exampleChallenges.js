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

/*
    11. Why is this code invalid? Edit this until it is valid.

    const objectVariable = {
        property1: 'i am property 1';
        property2: 'i am property 2';
        property3: [20,30,40];
    }
    
    conosle.log(objectVariable.property3[2]);
*/

/*
    12. Why does this code not work? Edit until it works.

    const myArray1 = [20,30,40];
    console.log(myArray1[3]);
*/

const myBoolean = true;
const myString = "hello world";
const firstNumber = 20;
let secondNumber = 40;
secondNumber = 80;

const myArray = [myBoolean, myString];

const myObject = {
  firstProperty: myArray,
  sumProperty: firstNumber + secondNumber,
};

console.log(myObject);

console.log(myObject.sumProperty);

console.log(myObject.firstProperty[1]);

const objectVariable = {
  property1: "i am property 1",
  property2: "i am property 2",
  property3: [20, 30, 40],
};

console.log(objectVariable.property3[2]);

const myArray1 = [20, 30, 40];
console.log(myArray1[2]);
