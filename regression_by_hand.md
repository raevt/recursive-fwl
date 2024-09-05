For now, this is just a place for me to put some content on regressions by hand.

## One independent variable
Regression of $y$ on $x$, where:
<p align="center">
$`y=\left[ {\begin{array}{c}3 \\4\\3\\5\\6\\\end{array}} \right] X=\left[{\begin{array}{c}1\\2\\3\\4\\5\end{array}}\right]`$
</p>
$y$ is a $n \times 1$ matrix, where $n$ is the number of observations. 

$X$ is a $n \times k$ matrix, where $k$ is the number of covariates (in this case, 1).

We intend to estimate $\beta_{1}$ in:

$$y=\beta_{1}x_{1}+\epsilon$$

The regression coefficient is given by:

$$b=(X'X)^{-1}X'y$$

where $b$ is a $k \times 1$ matrix of estimated $\beta$

## One independent variable (with a constant)