// const firstNumber = 20;
// const secondNumber = '20';
// const result = firstNumber === secondNumber;
// console.log(result);

// const expression1 = 100 % 50;
// // console.log(expression1); // 0
// const expression2 = 100 / 50;
// // console.log(expression2); // 2
// const expression3 = expression1 < expression2;
// // console.log(expression3); // true
// const expression4 = expression3 && 300 + 5 === 305;
// // console.log(expression4); // true
// const expression5 = !expression4;
// console.log(expression5);


// const expression = !(((100 % 50) < 100 / 50 && 300 + 5 === 305));
// console.log(expression)


// const myObj = {
//     prop1: 'first value',
//     prop2: 20
// };

// const myArray = [40, 50, 2];

// const result = myObj.prop2 === (myArray[0] / myArray[2]);
// console.log(result);

const myObj = {
    nestedObject1: {
        price: 100,
        quantity: 5
    },
    nestedObject2: {
        price: 150,
        quantity: 2
    }
};

const myArray = [myObj.nestedObject1, myObj.nestedObject2];

const result = (myArray[0].price * myArray[0].quantity) > (myArray[1].price * myArray[1].quantity);
console.log(result);