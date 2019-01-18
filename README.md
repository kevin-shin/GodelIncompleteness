# GodelIncompleteness

This project was initiated after taking PHIL 313, Advanced Symbolic Logic at Macalester College, in which I was exposed
to the proof of Godel's Incompleteness Theorem, which states that any system that uses arithmetic is incomplete -
there are sentences which are unprovable (and true). The basic idea behind the proof is to use numbers to encode formulas
of logic, and then to specify a sentence (the Godel sentence) which cannot be proven.

In most versions of the proof, the details for the numbering and encoding are left to be an ambiguous portion
of the proof, presumably because from a theoretical perspective, the details of the encoding are unimportant
as long as it is doable and sound. However, the actual encoding procedure assembles an interesting
melange of skills from number theory, language theory, and presents a unique challenge to the coder to devise
an algorithm capable of handling arbitrary sentences of arithmetic.

Thus, the intention of this project is simply to provide a GUI in which the user is able to type in sentences of
arithmetic and have the program output the Godel number of the sentence, if it is well-formed by the syntax and
symbolization as provided by Crossley in "What is Mathematical Logic?".

Another important intention behind this project was to provide this interface as a teaching tool, especially in light of
the complex and abstract nature of the proof. Although Godel numbering is explained as a necessary concept but then
bypassed, students are encouraged to remember that the entire proof hinges upon the ability to use such a numbering
to use arithmetic to talk about arithmetic, which leads to the Godel sentence. Thus, although semantically a recursive
process, the importance of this portion of the proof cannot be understated. The idea is that if this process can be
automated and presented in an intuitive way, students will be able to understand the theoretical moves Godel makes
more clearly.


#### Copyright and Attributions

I'd like to thank Janet Folina of the Philosophy Department at Macalester College and Daniel Kluver of the Computer Science Department for their classes on Symbolic Logic and Language theory respectively, as well as their support and guidance outside of the classroom on this project. 

_What is Mathematical Logic?_ was one of the reference books for PHIL 313, and such contributed greatly to my understanding of the proof, and it is the lanugage, encoding scheme, and axiomatic system in this text which was used in the program and displayed in the "Symbols" page. 

**Citation:** Crossley, John N. What Is Mathematical Logic? Oxford: Oxford Univ. Press, 1978.

The Proof button redirects the reader to the Stanford Encyclopedia of Philosophy's page on Godel's Incompleteness Theorems, a reference I find comprehensive and easy-to-read for users interested in the rest of the proof. 

**Citation:** Raatikainen, Panu, "Gödel's Incompleteness Theorems", The Stanford Encyclopedia of Philosophy (Fall 2018 Edition), Edward N. Zalta (ed.), URL = <https://plato.stanford.edu/archives/fall2018/entries/goedel-incompleteness/>.


This repository uses the [PLY compiler](https://www.dabeaz.com/ply/ply.html), developed by David M. Beazley, to develop the parser for the CFG for arithmetic. This project makes no endorsement or promotion of a product, and is solely a personal project. In accordance with the copyright measures specified on David's page, the following copyright is included in full:

Copyright (C) 2001-2018
David M. Beazley (Dabeaz LLC)
All rights reserved.
