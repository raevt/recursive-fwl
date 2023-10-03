This repository includes a Python program to estimate multiple regression models via OLS without any matrix algebra. This is done using the [Frisch-Waugh-Lovell Theorem](https://en.wikipedia.org/wiki/Frisch–Waugh–Lovell_theorem) in a recursive manner, allowing the estimation of a multiple regression model with a series of simple linear regressions.

# Files and usage

File: [multiple_regression.py](/multiple_regression.py)

Be sure that the data is in a .csv, and:
- the first row is the names of the variables
- the first column is the dependent variable
- there are no missing observations


# What does this do? (i.e., the theory)

The Frisch-Waugh-Lovell Theorem, referred to as "partialling out", allows the estimation of an independent variable's coefficient in a multiple regression through a regression of the dependent variable on the residuals from a regression of that independent variable on all other independent variables.

When I first learned of this approach, I had a very rabbit-hole inducing thought: is it possible to recursively partial out regressions such that a multiple regression of any number of independent variables can be estimated with a series of simple linear regressions?

Consider a regression model with one dependent variable and two independent variables. To estimate the coefficient on the first independent variable, we can run a simple linear regression of that variable on the other independent variable, and a second simple linear regression of the dependent variable on the residuals of that model. The coefficient on those residuals is the coefficient of that independent variable in the multiple regression model.

![Process for 2 independent variables](/images/two%20independent%20variables.png)

The primary takeaway here is that a multiple regression with two independent variables can be calculated as two linear regressions, which can easily be estimated without matrix algebra.

For a multiple regression with k independent variables:

![Process for k independent variables](/images/k%20independent%20variables.png)

Each variable's coefficient is estimated through a regression of y on the residuals from a regression of that variable on all other variables. For simplicity, I'll call these regressions (of each x on all other x's) "second-level regressions", because they are one "step down" from the initial regression.

Each second-level regression has one fewer independent variable than the initial regression. In other words, a multiple regression of k independent variables can be estimated through regressions of y on the residuals from the k second-level regressions. Each of those second-level regressions has k-1 independent variables.

This can be done recursively. Because any multiple regression can be estimated with k regressions of k-1 independent variables, and we know that a regression where k=2 can be estimated with two simple linear regressions, we can apply partialing out to a multiple regression recursively until every component regression has k=2. In other words, a multiple regression of any size can be estimated with some number of simple linear regressions. So, what is the function for that number?

With k=2, the answer is 2 simple linear regressions, as shown above. With k=3, each independent variable's coefficient is regressed on the other two independent variables, creating three multiple regressions with two independent variables each. Each of those three regressions are then estimated with two linear regressions, resulting in 6 simple linear regressions.

It seems the function for the number of simple linear regressions needed to estimate a multiple regression is k!:

Consider a situation with 5 independent variables. We start with 5 linear regressions of 4 independent variables each. Then, 5\*4=20 linear regressions, of 3 independent variables each. Then, 20\*3=60 linear regressions, of 2 independent variables each. Then, 60\*2=120 simple linear regressions. In other words, with k=5, you need 5\*4\*3\*2\*1=120, or 5!, simple linear regressions. This pattern is the same for any value of k.

In arriving at k!, I only considered what I'll call "moving down" regressions, i.e., the number of simple linear regressions resulting from partialing out regressions with k independent variables into k regressions of k-1 independent variables in a cascading manner, until only simple linear regressions remain. I did not consider the regressions used in "moving up" this chain, i.e., the regressions of the dependent variable of each model on the residuals of its partialed-out regressions.
