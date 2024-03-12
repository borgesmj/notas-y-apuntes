let userName = "fast";
let age = 17;
let hasHobbies = true;
let points = [10, 20, 30];
let user = {
  name: "ryan",
  lastName: "ray",
};
const PI = 3.1415;

if (age >= 18) {
  console.log("tu eres  un adulto");
} else {
  console.log("No eres un adulto");
}

const names = ["jhon", "jon", "marco"];

for (let i = 0; i < names.length; i++) {
  console.log(names[i]);
}

const showUserInfo = (userName, userAge) =>
  `The username is ${userName}, the user is ${userAge} years old`;

console.log(showUserInfo("miguel", 30));
