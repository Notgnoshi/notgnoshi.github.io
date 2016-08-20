---
layout: post
title: The difference between logical and arithmetic bitwise shifts
meta: An explanation of how logical and arithmetic bitwise shifts differ; namely in their treatment of the sign bit
---

The [Julia](julialang.org) language has two right shift operators. One for a logical right shift (`>>>`), and one for an arithmetic right shift (`>>`). Their difference is in how they treat the sign bit. The logical shift brings in a `0` no matter what, and the arithmetic shift brings in whatever the sign bit is.

We can use `convert(T, n)` to convert `n` to type `T`; you can't use `n::Int8 = ...` syntax in the global scope. There might be a better way to do this, but I'm far from a Julia expert. Either way, I'm only doing it here so they're short enough to easily read.

```julia
julia> x = convert(Int8, -2)
-2

julia> bits(x)
"11111110"

julia> bits(x >>> 1)
"01111111"

julia> bits(x >> 1)
"11111111"

julia> y = convert(Int8, 2)
2

julia> bits(y)
"00000010"

julia> bits(y >>> 1)
"00000001"

julia> bits(y >> 1)
"00000001"
```

We can do the same for an unsigned byte to see how the logical shift and the arithmetic shift act the same.

```julia
julia> x = convert(UInt8, -2)
ERROR: InexactError()
 in convert at ./int.jl:175

julia> x = convert(UInt8, 2)
0x02

julia> bits(x)
"00000010"

julia> bits(x >>> 1)
"00000001"

julia> bits(x >> 1)
"00000001"
```

Because the sign bit is the most significant bit, e.g. the right one, there is no difference between an arithmetic left shift and a logical left shift, so there is no separate operator for the logical left shift.

```julia
julia> bits(x << 1)
"00000100"

julia> bits(x <<< 1)
ERROR: syntax: "<" is not a unary operator
```

In a word, the arithmetic shift of `n` will preserve `n`'s sign, while the logical shift doesn't care.
