# GodelIncompleteness

This project was developed after taking PHIL 313, Advanced Symbolic Logic at Macalester College, in which I was exposed
to the proof of Godel's Incompleteness Theorem, which states that any system that uses arithmetic is incomplete -
there are sentences which are unprovable (and true). The basic idea behind the proof is to use numbers to encode formulas
of logic, and then to specify a sentence (the Godel sentence) which cannot be proven. 

In most versions of the proof, the details for the numbering and encoding are left to be an ambiguous portion
of the proof, presumably because from a theoretical perspective, the details of the encoding are unimportant
as long as it is doable and sound. However, the actual encoding procedure assembles an interesting
melange of skills from number theory, language theory, and presents a unique challenge to the coder to devise
an algorithm capable of handling arbitrary sentences of arithmetic. Since this area is one of the most important intersections of Mathematics, Computer Science, and Philosophy, I made it my goal to build this machine. 

The intention of this project is simply to provide a GUI in which the user is able to type in sentences of
arithmetic and have the program output the Godel number of the sentence, if it is well-formed by the syntax and
symbolization as provided by Crossley in "What is Mathematical Logic?". The project is largely split into four interplaying parts:

1. GodelIncompleteness.py: the main file which, when run, will initiate the GUI. This file combines the tools from the other portions of the project to display the encodings, decodings, axioms, etc. into one program.
2. parser.py: the parser built to handle the syntax of arithmetic expressions
3. mathHelperFunctions.py: a file which contains functions to generate prime numbers and find prime factorizations, 
4. translator.py: the file responsible for using the Crossley symbols to translate from Godel numbers to formulae and vice versa, and other helpful transitions.

Furthermore, users with a comfortable knowledge of parsers and lexers are encouraged to visit the yacc directory, which is a completely different approach to developing a parser for arithmetic (although PLY is really just a python implementation of .lex and .yacc). My original knowledge of building parsers was to write bison/yacc code in C and compile the lexers and parsers. The logic of the context-free grammars are identical, but these files present an alternative framework to approach the problem. Ultimately, the PLY version was preferred since it was easily imported into the GUI. 

Another important intention behind this project was to provide this interface as a teaching tool, especially in light of
the complex and abstract nature of the proof. Although Godel numbering is explained and then forgotten about, students are encouraged to remember that the entire proof hinges upon the ability to use such a numbering to use arithmetic to talk about arithmetic, which leads to the Godel sentence. Thus, although semantically a recursive process, the importance of this portion of the proof cannot be understated. The idea is that if this process can be automated and presented in an intuitive way, students will be able to understand the theoretical moves Godel makes more clearly.


### Further Notes

There are some acknowledged improvements which could be made including but not limited to the following:
- Text on the introductory window
- allowing user to specify their own encodings
- making use of the debugger tool of PLY to illustrate syntactic errors

For other suggestions or bug-catches, please contact me directly. 


### Copyright and Attributions

I'd like to thank Janet Folina of the Philosophy Department at Macalester College and Daniel Kluver of the Computer Science Department for their classes on Symbolic Logic and Language theory respectively, as well as their support and guidance outside of the classroom on this project. 

_What is Mathematical Logic?_ by John Crossley was one of the reference books for PHIL 313, and such contributed greatly to my understanding of the proof, and it is the lanugage, encoding scheme, and axiomatic system in this text which was used in the program and displayed in the "Symbols" and "Axioms" pages. 

**Citation:** Crossley, John N. What Is Mathematical Logic? Oxford: Oxford Univ. Press, 1978.

The Proof button redirects the reader to the Stanford Encyclopedia of Philosophy's page on Godel's Incompleteness Theorems, a reference I find comprehensive and easy-to-read for users interested in the rest of the proof. 

**Citation:** Raatikainen, Panu, "Gödel's Incompleteness Theorems", The Stanford Encyclopedia of Philosophy (Fall 2018 Edition), Edward N. Zalta (ed.), URL = <https://plato.stanford.edu/archives/fall2018/entries/goedel-incompleteness/>.


This repository uses the [PLY compiler](https://www.dabeaz.com/ply/ply.html), developed by David M. Beazley, to develop the parser for the CFG for arithmetic. This project makes no endorsement or promotion of a product, and is solely a personal project. In accordance with the copyright measures specified on David's page, the following copyright is included in full:

Copyright (C) 2001-2018
David M. Beazley (Dabeaz LLC)
All rights reserved.
