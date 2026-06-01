## We have to find the average selling price 
#### Average means sum / count
#### And we need to find this output for every product_id irrespective of whether it has been sold or not. So some product_id's from Prices table might not be there
#### in the Sales table.

#### So inorder to get each product_id we need to do a LEFT JOIN.
#### Since product_id is the column that is common in both the tables we should put the condition based on product_id 

Prices as p LEFT JOIN UnitsSold as s
ON p.product_id = s.product_id

#### Condition check for purchase_date 
WHERE s.purchase_date >= p.start_date AND s.purchase_date <= p.end_date OR s.purchase_date is NULL

#### Then we need to group the new table based on product_id so that it will be easier for us to calculate the average
GROUP BY p.product_id

#### Then we need to find the average
SUM(p.price * s.units) / SUM(s.units)

#### This above statement will calculate the product of each row's price by multiplying the price with total number of units in the right table. 
#### Then after calculating the product for the first row, move to the second row and check if the product_id is same . If same calculate price * units 
#### After all the products are calculated add them. This will be the numerator
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96

#### Denominator will simply be the total number of units.
#### Now round off the obtained result by 2 decimal places and then check if null. If result table has average price as NULL then replace average by 0
