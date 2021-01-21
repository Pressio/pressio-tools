
# Overview

`pressio-tools` is a collection of capabilities accessible from Python for:

- computing the QR factorization of a distributed tall-skinny matrix

- computing the SVD of a distributed matrix

- computing sample mesh indices for hyperreduction via

	- Discrete empirical interpolation method (DEIM)

	- other methods TBD

`pressio-tools` is being developed as an auxiliary library to the [pressio C++ library](https://pressio.github.io/pressio/html/index.html) and its [Python bindings library](https://pressio.github.io/pressio4py/html/index.html).

# When to use pressio-tools?

*`pressio-tools` is mainly intended to operate on large data distributed on large-scale machines.*
For example, suppose you want to use the SVD functionality. If you have a "small" matrix that fits on a single node, using pressio-tools to compute its SVD is excessive, and you (likely) can as easily use scipy.svd or other libraries for shared-memory computing like Eigen.
However, if you have a large tall-skinny matrix distributed over a large machine and need to compute its SVD, then `pressio-tools` is right for you.

# Installing 
See [this wiki page](https://github.com/Pressio/pressio-tools/wiki/Requirements-and-installation).

# Questions?
Find us on Slack: https://pressioteam.slack.com or open an issue on [github](https://github.com/Pressio/pressio-tools).

# License and Citation
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

The full license is available [here](https://pressio.github.io/various/license/).
