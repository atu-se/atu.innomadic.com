# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + {"slideshow": {"slide_type": "skip"}}
from itertools import product


# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Relational Algebra
#
# There are six basic relational algebra operators
#
# Symbol   | Name
# ---------|-----
# $\sigma$ | Selection 
# $\Pi$    | Projection 
# $\times$ | Cartesian Product 
# $\cup$   | Union 
# \-       | Set Difference 
# $\bowtie$| Natural Join 
#

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Example
#
# Let's pretend for a moment that our relationals only have one attribute each.  Let's consider one relation,
# $$A = \{1,4,5,7\}$$
# and another relation 
# $$B = \{2,4,6,8\}$$
#
#

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Union
#
# $$A = \{1,4,5,7\}, B = \{2,4,6,8\}$$
# What is $A\cup B$?

# + {"slideshow": {"slide_type": "fragment"}}
A = {1,4,5,7}
B = {2,4,6,8}
A.union(B)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Set Difference
#
# $$A = \{1,4,5,7\}, B = \{2,4,6,8\}$$
# What is $A-B$?

# + {"slideshow": {"slide_type": "fragment"}}
A-B

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Cartesian Product
#
# $$A = \{1,4,5,7\}, B = \{2,4,6,8\}$$
# What is $A \times B$?

# + {"slideshow": {"slide_type": "fragment"}}
list(product (A,B))

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Now with Relations
#
# Consider this relation `r`:
#
# A        | B       | C  | D
# ---------|---------|----|---
# $\alpha$ | $\beta$ | 1  | 7
# $\alpha$ | $\beta$ | 5  | 7
# $\beta$  | $\beta$ | 12 | 3
# $\beta$  | $\beta$ | 23 | 10
#

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Selection
#
# The selection operators allows us to choose some logical propositions to filter our tuples.  For example:
#
# $\sigma_{A=B \land D > 5} (r)$
#
# This selection returns all tuples in which A is equal to be, and D is greater than 5.
#
# $\sigma_{A=B \land D > 5} (r)$ = ?

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Selection
#
# $\sigma_{A=B \land D > 5} (r)$ =
#
# A        | B       | C  | D
# ---------|---------|----|---
# $\beta$  | $\beta$ | 23 | 10
#

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Projection
#
# The projection operators allows us to choose which attributes of a relation to return.  It allows us to filter our attributes.
#
# Given relation r = 
#
# A        | B  | C  
# ---------|----|----
# $\alpha$ | 10 | 1  
# $\alpha$ | 20 | 1 
# $\beta$  | 30 | 1 
# $\beta$  | 40 | 2 
#
# $\Pi_{A, C}(r)$ = ?

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Projection 
#
# $\Pi_{A, C}(r)$ = 
#
#
# A        | C  
# ---------|----
# $\alpha$ | 1  
# $\alpha$ | 1 
# $\beta$  | 1 
# $\beta$  | 2 
#     
# = 
#
# A        | C  
# ---------|----
# $\alpha$ | 1  
# $\beta$  | 1 
# $\beta$  | 2 
