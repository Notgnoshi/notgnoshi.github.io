---
layout: post
title: 02 Truth Tables
categories: [notes, finite]
---
<!-- Custom styles for the truth tables -->
<link rel="stylesheet" href="{{ "/assets/styles/truth_tables.css" | prepend: site.baseurl }}">

The following is the **truth table** for $$\neg p$$. Truth tables of a proposition have a row for for every possible combination of truth values for each sub-proposition. In this table, there are only two possible combinations of truth values.

<table class="truth">
    <tr>
        <td>$$p$$</td>
        <td>$$\neg p$$</td>
    </tr>

    <tr>
        <td>T</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>T</td>
    </tr>
</table>

The following is the truth table for the **conjunction**.

<table class="truth">
    <tr>
        <td>$$p$$</td>
        <td>$$q$$</td>
        <td>$$p \land q$$</td>
    </tr>

    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>
</table>

This is the truth table for the **disjunction**.

<table class="truth">
    <tr>
        <td>$$p$$</td>
        <td>$$q$$</td>
        <td>$$p \lor q$$</td>
    </tr>

    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>T</td>
        <td>F</td>
        <td>T</td>
    </tr>

    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>
</table>

This is the truth table for the **exclusive or**.

<table class="truth">
    <tr>
        <td>$$p$$</td>
        <td>$$q$$</td>
        <td>$$p \oplus q$$</td>
    </tr>

    <tr>
        <td>T</td>
        <td>T</td>
        <td>F</td>
    </tr>

    <tr>
        <td>T</td>
        <td>F</td>
        <td>T</td>
    </tr>

    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>
</table>

This is the truth table for the **conditional** statement.

<table class="truth">
    <tr>
        <td>$$p$$</td>
        <td>$$q$$</td>
        <td>$$p \to q$$</td>
    </tr>

    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>F</td>
        <td>F</td>
        <td>T</td>
    </tr>
</table>

And finally, this is the truth table for the **bi-conditional** statement.

<table class="truth">
    <tr>
        <td>$$p$$</td>
        <td>$$q$$</td>
        <td>$$p \iff q$$</td>
    </tr>

    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>F</td>
        <td>T</td>
    </tr>
</table>

We can use the above logical **connectives** to build up complicated compound propositions, and we can use truth tables to determine the value of these propositions. Finding truth tables of more complicated expressions can be tricky, and takes some practice.

If a proposition such as $$(p \lor r) \to (p \land q)$$ has more than two sub-propositions, there are there are more combinations of **true** and **false** input values, and therefore the tables are larger. If there are $$n$$ propositions in a compound proposition, there are $$2^n$$ rows in the corresponding truth table.

The easiest way to logically organize the values in the truth table is to have $$\frac{n}{2}$$ **true** values followed by $$\frac{n}{2}$$ **false** values in the first column, and for each following column, decrease the number of **true** values by a factor of $$2$$ until in the last column the values alternate between **true** and **false**. For example, the following truth table corresponds to the proposition $$(p \lor r) \to (p \land q)$$.

<table class="truth">
    <tr>
        <td>$$p$$</td>
        <td>$$q$$</td>
        <td>$$r$$</td>
        <td>$$(p \lor r) \to (p \land q)$$</td>
    </tr>

    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>

    <tr>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>

    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
    </tr>

    <tr>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>

    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
    </tr>
</table>
