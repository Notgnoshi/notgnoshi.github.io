---
layout: post
title: Learning Boolean Functions with (simple) Neural Networks
meta: Reproducing the AND, OR, XOR, etc. boolean functions using neural networks implemented in Keras
---
<link rel="stylesheet" href="{{ "/assets/styles/truth_tables.css" | prepend: site.baseurl }}">

I'm currently taking a deep learning course, which used learning the [XOR](https://en.wikipedia.org/wiki/Exclusive_or) function as its first example of feedforward networks. The XOR function has the following truth table

<table class="truth">
    <tr><td>$$x$$</td><td>$$y$$</td><td>$$x \oplus y$$</td></tr>
    <tr><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>0</td><td>1</td><td>1</td></tr>
    <tr><td>1</td><td>0</td><td>1</td></tr>
    <tr><td>1</td><td>1</td><td>0</td></tr>
</table>

which when graphed, is not linearly separable (1s cannot be separated from the 0s by drawing a line)

<img class="centered-real" src="{{ "/assets/posts/boolean-nn/xor.svg" | prepend: site.baseurl }}" alt="XOR is not linearly separable">

So if a linear model won't work, I guess that means we need a nonlinear one. We can do this by using the $$relu(x)$$ activation function on the outputs of our neurons. $$relu(x)$$ is defined as

$$relu(x) = \max\{0, x\}$$

and graphed below.

<img class="centered-real" src="{{ "/assets/posts/boolean-nn/relu.svg" | prepend: site.baseurl }}" alt="The RELU function">

However, since $$relu(x)$$ has sharp corners, it is not differentiable at $$x = 0$$, so gradient based learning methods won't work as well. So we use the $$softplus(x)$$ function instead, which is a softened version of $$relu(x)$$ defined as

$$softplus(x) = \log(1 + \exp(x))$$

shown below.

<img class="centered-real" src="{{ "/assets/posts/boolean-nn/softplus.svg" | prepend: site.baseurl }}" alt="The softplus function">

---

We begin with your usual imports

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
```

Then define the inputs and expected outputs of the neural network

```python
inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

xor_outputs = np.array([0, 1, 1, 0])
```

Next, we define the structure of the neural network. Note that I had to increase the learning rate from the default value.

```python
XOR = Sequential()
XOR.add(Dense(2, activation='softplus', input_dim=2))
XOR.add(Dense(1, activation='sigmoid'))

# Make the model learn faster (take bigger steps) than by default.
sgd = SGD(lr=0.1)
XOR.compile(loss='binary_crossentropy',
            optimizer=sgd,
            metrics=['accuracy'])
```

This defines the network

<img class="centered-real" src="{{ "/assets/posts/boolean-nn/xor-nn.svg" | prepend: site.baseurl }}" alt="The XOR network">

where the hidden layer activation function is $$softplus(x)$$ and the output layer activation function is the traditional [sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) function used to output a number between 0 and 1, indicating the probability of the output being a logical 0 or a logical 1. Note that Keras does not require us to explicitly form the input layer.

Now we actually train the network.

```python
XOR.fit(inputs, xor_outputs, epochs=5000, verbose=0)
cost, acc = XOR.evaluate(inputs, xor_outputs, verbose=0)
print(f'cost: {cost}, acc: {acc * 100}%')
print(XOR.predict(inputs))
```

which outputs

```
cost: 0.007737404201179743, acc: 100.0%
[[0.00496492]
 [0.9978434 ]
 [0.98019916]
 [0.00380662]]
```

Training the network on other boolean functions work exactly the same way, so much so that the only difference is using a different output array.

---

This was my first experience with a neural network, so here are some things that I learned for your amusement:

* I originally expected this model to train very quickly because the problem was so small, so I only used 10-20 training epochs and got absolutely garbage results. Here, I'm using 5000 training epochs.
* I had to increase the learning rate to train in a reasonable amount of time.
* One should not blindly upgrade TensorFlow without reading the release notes. All-in-all, I spent more time trying to install the correct versions of Tensorflow and CUDA than I did trying to get even this simple of a neural network to work correctly.
* Even small models like this use quite a lot of GPU memory.

---

Note that boolean functions are bad functions for neural networks to learn. This is because their domain and ranges are discrete and (typically) small. Learning the function takes more time and space than simply listing a truth table.
