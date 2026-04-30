# YouTube — Intro Script

I’m going to show you a simple way to look at prime numbers that turns them into a small matrix system.

Take consecutive primes, reduce them modulo 30, and you get a sequence over 8 states.

Now track how those states transition. That gives you a transition matrix P.

If primes behaved like a simple memoryless process, then two-step behavior would match P².

But instead, if you compute it directly and subtract:

Δ = P^(2) − P²

you get a matrix that is not noise.

It has low-rank structure.

That means a small number of components explain most of the deviation.

This doesn’t prove a new theorem about primes.

But it gives you a concrete way to see where simple models stop working.
