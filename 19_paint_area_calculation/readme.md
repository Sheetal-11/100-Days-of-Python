# Paint Area Calculation

You are painting a wall. The instructions on the paint can says that $1$ can of paint can cover $5$ square meters of wall. Given a random height and width of the wall, calculate how many cans of paint you'll need to buy.

> $$\text{number of cans} = \frac{\text{wall height} \times \text{wall width}}{\text{coverage per can}}$$

e.g. $\text{Height} = 2, \text{Width} = 4, \text{Coverage} = 5$

> $\text{number of cans} = (2 * 4) / 5 = 1.6$

But because you can't buy $0.6$ of a can of paint, the result should be rounded up to $2$ cans.


### Example Input

> Height of wall in m: 15
> 
> Width of wall in m: 10


### Example Output

> The surface area to paint is 150sq.m.
> 
> You'll need 30 cans of paint.



