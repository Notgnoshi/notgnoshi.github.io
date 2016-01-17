---
layout: post
title: 01 Intro to MatLab
category: numerical
---

We've spent the first few classes in Numerical Analysis learning some basic Matlab syntax. The most basic commands are entered into the **Command Window** at the `>>` prompt. Matlab is an interpreted language, and is executed as soon as it's entered.

{% highlight matlab %}
>> 55 - 16
ans =
    39
{% endhighlight %}

Matlab stores the answer from the previous computation to the variable `ans`. You can then use `ans` in a subsequent calculation.

{% highlight matlab %}
>> ans + 11
ans =
    50
{% endhighlight %}

You can assign values to variables: `a = 4`. Matlab is case-sensitive. If you don't want Matlab to print the answer from the previous calculation then end the statement with a semicolon `a = 4;`.

Matlab displays four decimal places by default. If you desire more precision, enter `format long`. For more formats, enter `help format`.

You can define row vectors:

{% highlight matlab %}
>> a = [1 2 3 4]
a =
    1   2   3   4
{% endhighlight %}

And column vectors:

{% highlight matlab %}
>> b = [2; 3; 4; 5]
b = [2
3
4
5]
{% endhighlight %}

You can take the transpose of `a` with `a'`.
There are many ways to define a matrix.

{% highlight matlab %}
>> A = [1 2 3; 4 5 6; 7 8 9];
>> B = [1 2 3
        4 5 6
        7 8 9];
>> C = [[1 2 3]' [4 5 6]' [7 8 9]'];
{% endhighlight %}

You can access individual elements of vectors and matrices. Matlab is not zero-indexed.

{% highlight matlab %}
>> a = [1 2 3 4];
>> a(4)
ans =
    4
>> A = [1 2 3; 4 5 6; 7 8 9];
>> A(2, 3)
ans =
    6
{% endhighlight %}

There are multiple built-in functions to assist with defining matrices.

{% highlight matlab %}
>> A = zeros(2, 2)
A =
    0   0
    0   0
>> B = ones(1, 3)
B =
    1   1   1
>> A = randn(4, 4); % Random 4x4 matrix
>> inv( A ); % Find the inverse of A
>> diag( [5 5 5 5] ); % Create a 4x4 matrix with a main diagonal of 5s
{% endhighlight %}

You can create lists spanning a range very easily in Matlab.

{% highlight matlab %}
>> t = 1 : 5
t =
    1   2   3   4   5
>> s = 1 : 2 : 7
s =
    1   3   5   7
>> u = 10 : -1 : 5
u =
    10  9   8   7   6   5
{% endhighlight %}

If you don't want to figure out the right step size for some range of values, you can use `linspace(x1, x2, n)` to generate a row vector of equally spaced points from $$x_1$$ to $$x_2$$ with $$n$$ spaces.

{% highlight matlab %}
>> linspace(0, 1, 6)
ans =
    0   0.2   0.4   0.6   0.8   1
{% endhighlight %}

If you want to make reusable code, you can make what are called **M-Files**. They are simply a series of Matlab commands saved in a `.m` text file. Given a file named `func.m`, the script is executed in the command window:

{% highlight matlab %}
>> func
% output here...
{% endhighlight %}

**Function Files** are M-Files that define functions. The function name must be the same as the file name. The syntax is as follows.

{% highlight matlab %}
function out_variable = function_name(arg_list)
% Docstring Comments
statements
out_variable = value;
{% endhighlight %}

The function is then called in the command window `function_name(arg_list)`. Use `help function_name` to get the functions docstring.

You don't *have* to make a single file for every function, if you end the function with `end`, you can then define a new function (with a new name) later in the file. The first function defined is called the **main** or **primary function**. Any other functions defined in an M-File are called **subfunctions**.

You can get input from the user and print to the Command Window like so:

{% highlight matlab %}
function out_variable = function_name(arg_list)
% Docstring Comments
value = input( 'prompt string' )
disp( value )
out_variable = value;
{% endhighlight %}

You can also use `fprintf( 'string', x, ... )` to print a string along with variable values. `fprintf` is very similar to C-style `printf`.

{% highlight matlab %}
function out_variable = function_name(arg_list)
% Docstring Comments
value = input( 'prompt string' )
fprintf( 'The value is: %d', value )
out_variable = value;
{% endhighlight %}

`fprintf` does not have as extensive a list of format specifiers as `printf` does. A list of specifiers is given below:

```
%d....Integer
%e....Scientific with lowercase `e`
%E....Scientific with uppercase `E`
%f....Decimal
%g....More compact %e or %E
```

You can also use `\t` and `\n`.

`clear varname` and be used to delete a given variable, while `clear` will delete all of them. You can use `clc` to clear the Command Window.

### Control Structures:

{% highlight matlab %}
if condition
  statements
elseif condition
  statements
else
  statements
end
{% endhighlight %}

Matlab uses the following Boolean operators:

```
~....NOT
&....AND
|....OR
```

An alternative to a lengthy `if` statement is the `switch` statement.

{% highlight matlab %}
var = val;
switch var
  case val1
    statements
  case val2
    statements
  otherwise
    statements
end
{% endhighlight %}

Matlab has a built-in variable `nargin` that is analogous to `argc` in C/C++. `nargin` represents the number of arguments supplied to a function.

Matlab also has the basic loops found in other languages.

{% highlight matlab %}
for i = 1:5
  disp(i)
end

while true != false
  disp( 'yay infinite loops!' )
end
{% endhighlight %}
