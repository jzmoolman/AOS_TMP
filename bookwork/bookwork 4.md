Bookwork 4
==========

Zach Moolman

Question 1 
-----------

The goal of the layered protocol design is to hide the complexity as you move up
the model. Therefore, the model divides the problem into manageable pieces,
solving each piece on its own. Using a single header will place a lot of
complexity on the application developer and increase the possible error in the
software. More importantly, we will break the model of layered protocol.
Referring to the efficiency, I do not believe that using single or multiple
headers affects the performance but rather the additional overhead by encoding
and decoding the different headers at each layer. Furthermore, you will create fixed endpoint not is not easy changeable. 

Question 2
----------

If call by reference is used, the compiler pass a pointer the variable.
Therefore, if the incr(i,i) is called the first parameter will be increased by
1, which point to the var from the callers frame. Now when the second parameter
is increased by another 1 the same variable is increased.  Hence, once the incr
returns the variable will be increased by two.

Example 1
```
int i = 0; 
incr(i,i);
// i = 2
```

However if the variable is by copy/restore, the variable i will copied twice one
for each parameter.  The first and the second  variable will be increased to 1.
Once the procedure return the last parameter will over right the caller i
variable. Therefore i will be 1. Variable too.

Example 2
```
int i = 0; 
incr(i,i);
// i = 1
```


Question 3
----------

A major problem is for all parties to agree on how the communication paths will
send out information.  Human intervened  is often required  to manage the
process and because the is de facto standard ISP is reluctant to support
multicasting.

Other problems with multicasting:
standards
congestion control
reliable multicasting support
increase in network traffic
Not good two way communication channels

Question 4
----------

The best-suited place to add automatic routing capabilities is to expand the
channel control function to forward any new connections to a centralized
component capturing all the end-point. The centralized component can create a
routing table using different algorithms that best suites the network overlay.
The  newly created routing tables can then be sent to each queue manager.  


