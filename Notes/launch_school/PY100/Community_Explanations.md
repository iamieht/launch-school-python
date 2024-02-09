
This is quite simple when you visualise a number line: -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6Let's start at zero. Going right means the numbers _increase,_ whilst going left means the numbers _decrease_.So, integer division indeed returns the largest whole number _less than or equal to_ (<=) the floating-point result: 16//3 -> 5.33333...  -> 5 (because rounding 5.33333 _down_ gives us 5 (find the floating-point result on the number line and move _left_))So... now let's consider 16//-3.  
16//-3 -> -5.33333... -> ? (well, if we consult our number line again, our dear -5 "sits" between -6 and -5. Which of these two numbers is _less_ (i.e. to the _left_)? Well, -6. So, this means rounding -5.33333... _down_ results in -6)  ^Simones-explanation-Integer-Division