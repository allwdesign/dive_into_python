# Dive into python
This repository contains completed homework for the Dive into Python course


# homework 1
Task 2. A triangle only exists if the sum of any two of its sides is greater than third. Given a, b, c - the sides of the proposed triangle.
It is required to compare the length of each segment-side with the sum of the other two. If in at least one case the segment is greater than the sum of the other two,
then a triangle with such sides does not exist.
Separately report whether the triangle is scalene, isosceles or equilateral.

Task 3. Write code that asks for a number and tells if it's prime or composite. Use the rule to check: “A number is prime if is only divisible by 1 and itself.
Limit the input of negative numbers and numbers greater than 100 thousand.


# homework 2
Task 1. Write an ATM program.
1. Initial amount is zero
2. Allowed actions: top up, withdraw, exit
3. The amount of replenishment and withdrawal is a multiple of 50 $.
4. Withdrawal interest — 1.5% of the withdrawal amount, but not less than 30 and not more than 600 $.
5. After every third deposit or withdrawal operation, interest is charged - 3%
6. You can not withdraw more than the account
7. If the amount exceeds 5 million, deduct 10% wealth tax before each
operation, even erroneous
8. Any action displays the amount of money

Task 2.Write a program that takes an integer and returns its hexadecimal string representation. Use the hex function to check your result.

Task 3.Write a program that takes two strings of the form 'a/b' - a fraction with a numerator and a denominator. The program should return the sum and product* of fractions. Use the fractions module to test your code.

Example:
    
    Input:
    1/2
    1/3
    Conclusion:
    5/6 1/6


# homework 3
Task 1.Given a list of repeating elements. Return a list with duplicate elements. The resulting list should not contain duplicates. 

    [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

Task 2.In a large text string, count the number of words encountered and return the 10 most frequent. Ignore punctuation marks and character case. As a basis, take any article from Wikipedia or from the documentation for the language. (The translate method from the string module can help)

Task 3.Create a dictionary with the list of things to hike as the key and their weight as the value. Determine what things will fit in the backpack by transferring its maximum carrying capacity. It is enough to return one valid option. *Return all possible backpack configuration options.
