Spider JIT
===============
Spider JIT is a jitter which has been written mainly for educational purposes.
The entire code is 'mostly' written in python with some amount of C used where
necessary. However, speed is not the most important criteria in this case and
most of the emphasis has been on how to make this compiler more readily accessible
to read for newbies. This jitter doesn't attempt to compete with Numba/PyPy or the
likes of Pyston. Infact most of the motivation has come from these great projects
themselves. If you are looking for production quality code then I would suggest
the above projects.

Overall Design
----------------
Overall, Spider JIT can be conveniently broken down into 3 pieces (as is true for
most compilers). They are:

 * Frontend module (currently implements Python)
 * Midend module (Optimization layer)
 * Codegen module (Final x86 code generation)
