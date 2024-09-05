For now, this is just a place for me to put some content on regressions by hand.

## One independent variable
Regression of $y$ on $x$, where:

$`y=\left[ {\begin{array}{c}3 \\4\\3\\5\\6\\\end{array}} \right] X=\left[{\begin{array}{c}1\\2\\3\\4\\5\end{array}}\right]`$

$y$ is a $n \times 1$ matrix, where $n$ is the number of observations. 

$X$ is a $n \times k$ matrix, where $k$ is the number of covariates (in this case, 1).

We intend to estimate $\beta_{1}$ in:

$`y=\beta_{1}x_{1}+\epsilon`$

The regression coefficient is given by:

$`b=(X'X)^{-1}X'y`$

where $b$ is a $k \times 1$ matrix of estimated $\beta$

First, we find $X'$:

$`X'=\left[{\begin{array}{ccccc}1 & 2 & 3 & 4 & 5\end{array}}\right]`$

Next, find $X'X$:

$`X'X=\left[{\begin{array}{c}(1*1)+(2*2)+(3*3)+(4*4)+(5*5)\end{array}}\right]\\=\left[{\begin{array}{c}1+4+9+16+25\end{array}}\right]=\left[{\begin{array}{c}55\end{array}}\right]`$

To find the inverse of this $1 \times 1$ matrix (which is a scalar), we can simply take its reciprocal:

$`(X'X)^{-1}=\left[{\begin{array}{c}\frac{1}{55}\end{array}}\right]`$

Next, find $X'y$:

$`X'y=\left[{\begin{array}{c}(1*3)+(2*4)+(3*3)+(4*5)+(5*6)\end{array}}\right]=\left[{\begin{array}{c}3+8+9+20+30\end{array}}\right]=\left[{\begin{array}{c}70\end{array}}\right]`$

The final step:

$`b=(X'X)^{-1}X'y=\left[{\begin{array}{c}\frac{1}{55}\end{array}}\right]\left[{\begin{array}{c}70\end{array}}\right]=\left[{\begin{array}{c}\frac{70}{55}\end{array}}\right]=\left[{\begin{array}{c}1.272\end{array}}\right]`$

The estimated equation:

$`{y}=1.272x_{1}+\epsilon`$

## One independent variable (with a constant)