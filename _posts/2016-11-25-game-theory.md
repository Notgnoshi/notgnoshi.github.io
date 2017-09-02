---
layout: post
title: Impartial Classic Combinatorial Games
meta: A review of impartial classic combinatorial games from a game theory perspective. Includes description of nimber (aka Sprague-Grundy) values and N and P states.
---

Game Theory is the mathematical modeling of conflict, cooperation, and the analysis and search of optimal solutions. The objects of study are **games**, which are composed of three pieces.

1. A set $$N$$ of $$n$$ players. $$n = 1$$ is decision theory, and not a part of typical game theory. $$n = 2$$ is the classic von Neumann-Morgenstern game theory. $$n > 2$$ is coalition gaming, which can be modeled as multiple $$n = 2$$ games, with coalitions as players.

    We make two assumptions, which are not necessarily valid in the real world:

    - **Intelligence** -- the players know the rules of the game

    - **Rationality** -- the players play to win as much as possible
2. **Rules** -- how the players agree to play.
3. **Payoff** -- a numerical value assigned to players or subsets of players.

Games are essentially functions that take sets of players as input, and give their payoffs as output. Games are characterized by intelligent and rational decision makers who interact, threaten, promise, form coalitions, etc., all with the promise of a payoff.

Let's define some terms:

**Perfect Information** -- We say a game is a game of perfect information when (under the assumption the players have perfect recall) the players know all past moves of the game, both their own and their opponent's. Chess is an example of a game of perfect information.

**Combinatorial Games** -- A 2-player game of perfect information with no moves determined by chance.

**Zero-Sum** -- A game is a zero-sum game if the payoffs to all the players sum to 0. For 2-player games, this means that my win is your loss.

**Classic Combinatorial Game** -- a 2-player game of perfect information with no chance moves that is zero sum. There cannot be secrets and/or bluffing (perfect information). There is no hope for cooperation (2-player, zero sum), and there is no probability involved.

The main result in Classic Combinatorial Game Theory is that there exists a winning strategy for exactly one of the players. This means one player could announce their strategy and their opponent may as well just hand him/her their payoff without even playing.

---

A game where each player has *exactly* the same set of moves at the same game state is called **impartial**. Otherwise we call it **partisan**. In an impartial classic combinatorial game, we say it is in **normal** play if the last player to make a legal move is the winner. If the last player to move loses, we say the game is in **misere** play.

---

In an impartial classic combinatorial game, we can label each game state with either an $$N$$ or a $$P$$. An **$$N$$-state** is a state for which there is a winning strategy for the player who starts at this position. A **$$P$$-state** is not an $$N$$-state. In other words, $$P$$-states are the *target* states of the current player. We have the following theorem called the **Characteristic Property** for impartial classic combinatorial games.

>The $$N$$ and $$P$$ states of an impartial classic combinatorial game are uniquely characterized by the following for a game in normal play.
>
>1. All terminal states are $$P$$-states
>
>2. All moves from $$P$$-states are to $$N$$-states
>
>3. All $$N$$-states have at least one move to a $$P$$-state

For games under misere play, terminal states become $$N$$-states.

---

>The $$P$$-states of an $$n$$-pile game of [Nim](https://en.wikipedia.org/wiki/Nim) are precisely those states whose nimsum of piles is zero.
>
>i.e., $$(P_1, P_2, \dots, P_n)$$ is a $$P$$-state if and only if $$P_1 \oplus P_2 \oplus \dots \oplus P_n = 0$$.

This is known as **Bouton's Theorem**.

The **nimsum** of $$a$$ and $$b$$, denoted as $$a \oplus b$$ is the bitwise [XOR](https://en.wikipedia.org/wiki/Exclusive_or) on $$a$$ and $$b$$'s bitstrings. For example, $$25_{10} \oplus 18_{10} = 11001_2 \oplus 10010_2 = 01011_2 = 11_{10}$$.

The nimsum has the following properties

* *Commutativity* -- $$a \oplus b = b \oplus a$$
* *Associativity* -- $$(a \oplus b) \oplus c = a \oplus(b \oplus c)$$
* *Idempotency* -- $$a \oplus a = 0$$
* $$a \oplus b \leq a + b$$.
* If $$a$$ and $$b$$ both have a $$k$$-bit binary expansion, then $$a \oplus b < a, b$$

Bouton formulated the following strategy to *always* win at a game of Nim. At an $$N$$-state, compute the nimsum of the piles and add the nimsum to any pile with a 1 in the $$k$$th bit where the nimsum is a $$k$$-bit number. This forces the game to a $$P$$-state, and guarantees a win for the player making the move, provided they are perfectly rational and intelligent.

---

In the mid 30s, two mathematicians R. Sprague and M. Grundy independently generalized Bouton's Theorem for *all* impartial classic combinatorial games in *normal* play. First though, we define the **Sprague-Grundy value**, or more commonly the **nimber value** for a game state as follows.

1. All terminal states $$S$$ get $$\operatorname{sg}(S) = 0$$
2. Non-termial states $$S$$ are assigned the *minimum excluded value* of $$\{\operatorname{sg}(T)\}$$ for all states $$T$$ one move away from $$S$$.

    $$\operatorname{sg}(S) = \min\{k \geq 0 \vert k \neq \operatorname{sg}(T) \text{ where $T$ is one move away from $S$}\}$$

    or equivalently,

    $$\operatorname{sg}(S) = \begin{cases}\text{the minimum nonnegative integer not equal to $\operatorname{sg}(T)$}\\\text{for any state $T$ attainable from $S$ in a single move}\end{cases}$$

Further, we can define the **disjoint sum** or a **direct sum** of games $$G_1$$ and $$G_2$$, denoted as $$G_1 + G_2$$, provided that $$G_1$$ and $$G_2$$ are both impartial classic combinatorial games, as follows

1. its states of play are $$(S, T)$$ where $$S$$ is a state of $$G_1$$ and $$T$$ is a state of $$G_2$$
2. a move to another state $$(S', T')$$ is valid if and only if either

    * $$T = T'$$ and $$S'$$ is one move away from $$S$$.
    * $$S = S'$$ and $$T'$$ is one move away from $$T$$.

---

The **[Sprague-Grundy Theorem](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)** for impartial classic combinatorial games then, is

>Let $$\operatorname{sg}$$ denote the Sprague-Grundy function for a game.
>
>1. $$\operatorname{sg}(S) = 0$$ if and only if $$S$$ is a $$P$$-state
>2. In a direct sum of games $$\operatorname{sg}(S, T) = \operatorname{sg}(S) \oplus \operatorname{sg}(T)$$

where $$\oplus$$ is the nimsum described above.

---

Given the following game with states $$\{a, b, \dots, o\}$$

<img class="centered-full" src="{{ "/assets/posts/game-theory/game_graph.svg" | prepend: site.baseurl }}" alt="polar coordinates">

we can assign nimber values to each state, starting at the terminal nodes and working inwards calculating the minimum excluded value of all states one move away.

<img class="centered-full" src="{{ "/assets/posts/game-theory/sg_graph.svg" | prepend: site.baseurl }}" alt="polar coordinates">

Take, for example, state $$n$$. $$n$$ is one move away from $$o$$, which is a terminal position with nimber value 0, so $$n$$ gets assigned the minimum positive integer that excludes 0, that is, 1. We can then calculate the nimber value for $$m$$, which is the minimum positive integer that excludes all nimber values for states attainable from $$m$$, which is only $$n$$, with a nimber value of 1. $$m$$'s nimber value is therefore 0, and is this a $$P$$-state.

---

My notes say that we can *always* assign a nimber value to every state because in this graph form we can never have any loops -- which is a property of classic combinatorial games. I'm unsure if "loops" in this context means cycles or self-loops.
