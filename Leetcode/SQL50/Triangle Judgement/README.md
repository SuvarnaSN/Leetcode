 ### Triangle Judgement

 #### 3 sides form a triangle only if x+y > z, x+z > y and y+z > x.

SELECT x, y, z,
IF(((x + y) > z AND (x + z) > y AND (y + z) > x), "Yes", "No") AS triangle

FROM Triangle;
