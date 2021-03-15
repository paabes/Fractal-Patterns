# Fractal Patterns
## Brief Background:

My fascination with fractal patterns, in a way, was inspired by my fascination with cosmology. It began at a time when I was exploring the geometry of conformal compactifications of infinite hyperbolic spaces, first achieved by the legendary mathematical physicist Sir Roger Penrose in the limit of Euclidean spaces. His goal at a time was to come up with a way to map an infinite space-time such that coordinates would not blow up to infinity and all the internal angles would be preserved. This was a rather pressing issue in the physics of black holes and cosmology, in particular, because the universe we find ourselves in was believed to be asymptotically flat, i.e infinite.

One of such compactifications was depicted by the Dutch artist Maurits Cornelis Escher, in his **Circle Limit IV** - the final in the series of woodcuts inspired by the projection of a hyperbolic plane called **Poincare Disk**.

![alt text](https://github.com/paabes/Fractal-Patterns/blob/main/renders/circle%20limit%204.jpeg "Escher's Circle Limit IV")

This brings us to the idea behind this project: **simulating fractal patterns**. In rigorous mathematical terms, a fractal is a subset of Euclidean space with a fractal dimension that strictly exceeds its topological dimension, which in everyday terms means that they are **ever-repeating patterns that never end**, no matter how much you zoom-in.

## Barnsley Fern

### Overview:

The first fractal pattern in this project is Barnsley Fern, a lief-like structure that can be obtained by performing four very specific **Affine Transformations** (Fancy name for a type of geometric transformations that preserve lines and parralellism) to the individual scatter plot points. Here is a generic form:

![alt text](https://github.com/paabes/Fractal-Patterns/blob/main/renders/affine_transformation.png "Affine Transform")

Barnsley Fern is composed of four sub-structures, thus for obtaining each one a separate function has to be defined
with different coefficients, that transform the x-y coordinates in a specific way. Moreover, for any given point in a plot, only one function has to be applied for affine transformation, therefore, one has to assign probability of choosing each of the for founctions in a very specific manner. The following are coefficients and probability distribution of the four functions:

![alt text](https://github.com/paabes/Fractal-Patterns/blob/main/renders/probability_distribution.png "Coefficients")

* Running the code with marker size **s = 0.2** and 100,000 points gives us the following plot:

![alt text](https://github.com/paabes/Fractal-Patterns/blob/main/renders/Barnsley%20Fern%204k.jpg "fern")



## Julia Set

### Overview:

If you are not familiar with complex dynamics, the idea behind **Julia Set** will be impossible to explain in few lines, for it is not as intuitive as Barnsley Fern, while if you do know a thing or two about complex dynamics, you've almost certainly come across julia set before, so there is no point in explaining.

* In brief what julia.py does is the following: For each point, z0, in the complex plane such that −2 ≤ Re[z0]≤ 2 and −2 ≤ Im[z0] ≤ 2, it iterates according to zn+1=z2n+c where c is some (complex) constant. It then colours the pixel in an image corresponding to this region of the complex plane according to the number of iterations required for |z|to exceed some critical value, |z|max (or black if this does not happen before a certain maxmimum number of iterations nmax). Running this code produces the following image:

![alt text](https://github.com/paabes/Fractal-Patterns/blob/main/renders/Julia%20Set%204k.png "Julia Set")






















