This repository includes a Python program to estimate multiple linear regression models with a series of bivariate linear regressions by recursively applying the [Frisch-Waugh-Lovell Theorem](https://en.wikipedia.org/wiki/Frisch–Waugh–Lovell_theorem) (FWL).

# Files and usage

File: [multiple_regression.py](/multiple_regression.py)

Be sure that the data is in a .csv, and:
- the first row is the names of the variables
- the first column is the dependent variable
- there are no missing observations

# What is FWL?

Assume we intend to estimate $\hat{\beta}_{j}$ in the MLR: $\hat{y}=\hat{\beta}_{j}x_{j}+...\hat{\beta}_{k}x_{k}+\epsilon$ 

The FWL theorem shows that $\hat{\beta}_{j}=\hat{\beta}^{*}_{j}$ from:

$`\hat{y}^{*}=\hat{\beta}^{*}_{j}\epsilon_{j}+\epsilon^{*}`$

where $\epsilon_{j}=\epsilon_{j}^{*}$ from the auxiliary regression: 

$\hat{x}^{*}_{j}=\hat{\beta}^{*}_{1}x_{1}+...\hat{\beta}^{*}_{k}x_{k}+\epsilon^{*}_{j}$

Intuitively, $\epsilon_{j}^{*}$ represents the part of $x_{j}$ that is unexplained by variation in the $k$ other covariates. A regression of $y$ on $\epsilon_{j}$ thus yields a coefficient that is equal to $\hat{\beta}_{j}$ in the main MLR.

# What does this script do?

It applies FWL recursively, where the base case is a bivariate regression.


# How many bivariate regressions result from recursive FWL?
A MLR with $k$ covariates is estimated with $k!$ auxiliary bivariate regressions.

As an intuitive proof of this, think of it like a leveled tree that expands from the main MLR. Consider a MLR with 5 covariates; in the first level, each covariate is regressed on the 4 other covariates, resulting in 5 regressions of 4 covariates each. Repeating this process on the second level, there are 20 regressions of 3 covariates. On the fourth level, 60 regressions of 2 covariates. And on the fifth level, 120 bivariate regressions. This is $k$ levels and $k!$ resulting auxiliary bivariate regressions.

The $k!$ number does not include the bivariate regressions on the residuals of the auxiliary regressions, which are what yield the coefficients for each regression in the tree. The number of these coefficient-yielding regressions is the total number of coefficients in the tree, which is the sum of the number of coefficients at each level:

$\Sigma^{k}_{j=1}\frac{k!}{(k-j)!}$

This is similarly straightforward to explain intuitively.

At each level, the number of coefficients is equal to the number of regressions multiplied by the number of covariates in each regression. Sticking with the example of $k=5$, we therefore know that the first level has 5 coefficients, the second 20, the third 60, the fourth 120, and the fifth also 120. This, in total, sums to 325.

The value of the expression where $j=1$ corresponds to the number of coefficients on the first level:

$\frac{5!}{(5-1)!}=\frac{(5)(5-1)(5-2)(5-3)(5-4)}{(5-1)(5-2)(5-3)(5-4)}=5$

I think of this as *dividing out* the eventual expansion in coefficients that has not occured on a given level. For example, level 2's denominator removes the $(5-1)$ from the above term, reflecting that expansion:

$\frac{5!}{(5-2)!}=\frac{(5)(5-1)(5-2)(5-3)(5-4)}{(5-2)(5-3)(5-4)}=5*4=20$

In full:

$\Sigma^{5}_{j=1}\frac{5!}{(5-j)!}=\frac{5!}{(5-1)!}+\frac{5!}{(5-2)!}+\frac{5!}{(5-3)!}+\frac{5!}{(5-4)!}+\frac{5!}{(5-5)!}=\frac{(5)(5-1)(5-2)(5-3)(5-4)}{(5-1)(5-2)(5-3)(5-4)}+\frac{(5)(5-1)(5-2)(5-3)(5-4)}{(5-2)(5-3)(5-4)}+\frac{(5)(5-1)(5-2)(5-3)(5-4)}{(5-3)(5-4)}+\frac{(5)(5-1)(5-2)(5-3)(5-4)}{(5-4)}+\frac{(5)(5-1)(5-2)(5-3)(5-4)}{1}=5+(5*4)+(5*4*3)+(5*4*3*2)+(5*4*3*2*1)=5+20+60+120+120=325$

The summation can also be thought of as the sum of component parts of $k!$. E.g., it is as though I performed the operation $k!$, recorded the value after each multiplication operation, and summed those values.

As an aside, this is a fun illustration of the relevance of $0!=1$. It is necessary to explain why levels $k$ and $k-1$ have the same number of coefficients, for in both cases the denominator is equal to 1.

# Why is this useful?

In undergraduate econometrics education, the FWL theorem is often used to explain the effect of controlling for a variable in OLS-estimated multiple linear regression. The theorem fills in for the intuitive reasoning that would have otherwise come from studying regression's matrix notation.

FWL can be a bit circular, in that (for k>2) you're using a multiple regression to explain a multiple regression. In its recursive form, however, MLR models can be estimated with a series of bivariate regressions, which students may more effectively understand.
