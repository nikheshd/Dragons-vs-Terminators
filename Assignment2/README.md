# Assignment 2

There will be an Owner of the Loan contract, and he will have an initial balane of 100K MetaCoins, as in the constructor of the MetaCoin class. Assume that he has accumulated these 100K coins by taking loans. He would store the debt he is in to each creditor in a mapping called loans. You have to implement the following functions along with a constructor and modifier:


1. getCompoundInterest : allows anyone to use it to calculate the amount of interest for given values of P, R, T (in years). Remember that solidity does not have a good support for floats though, so enter the rate as a whole number (like if the rate is 83%, enter 83). We are looking for an iterative implementation to calculate the Compound Interest, which is compounded annually, to test if you understood the applications of loops. This is an inefficient method though, and we'll come back to that later, but we want it to be iterative. A few blogs to clue you in to how to perform percentage based calculations with just integers have been provided in the template.


2. reqLoan: anyone should be able to use it to request the Owner to settle his loan. The P, R, T entered is used to calculate the dues, and is added to a mapping. It should emit the Request event.


3. getOwnerBalance: anyone can use it to get the amount of MetaCoins owned by the owner. make use of MetaCoin contract's getBalance to implement this, to get a taste of inheritance!


4. viewDues : only the owner can access this to view the amount of loan he owes to the input address, which is stored in the loans mapping. Be sure to make use of the modifier!


5. settleDues: only the owner can use this to settle the amount of loan he owes to the input address, use MetaCoin's sendCoin function to settle these dues, with appropriate checks for the return values from sendCoin. Also remember to set the amount owed to 0 or whatever remains if sendCoin runs succesfully!


## How to run
Import the code to remix. Compile and deploy. All the functions work the same as they are stated above.

### Inputs --- Outputs (in order):
Address is Owner's
getOwnerBalance()
0: uint256: 100000


getCompoundInterest(100, 50 ,2)
0: uint256: 225


change address to creditor
reqLoan(100, 50 ,2)
0: bool: true


change address to Owner
viewDues(creditor's address)
0: uint256: 225


settleDues(creditor's address)
0: bool: true


getOwnerBalance()
0: uint256: 99775
