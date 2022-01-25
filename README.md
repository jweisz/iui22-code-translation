# iui22-code-translation
Companion materials for IUI'22 paper "Better Together? An Evaluation of AI-Supported Code Translation"

## Overview

This repository contains the source code materials used in the code translation user study. We examined how people translated two data structures with and without support from a neural machine translation (NMT) model. The code & NMT-produced translations are organized as shown below. Participants in the study either received _1_ or _5_ of the translations, and they either received the _better-quality_ or _worse-quality_ translations. All source code files were renamed in each participant's workspace to remove any indicators of whether the translations were better or worse quality.

### Trie

Code for the Trie data structure is in the `Trie/` directory.

| File | Description |
|---|---|
| Trie.java | The source Java implementation of the Trie data structure |
| Trie-{1-5}-Better.py | Five better-quality, AI-produced Python translations |
| Trie-{1-5}-Worse.py | Five worse-quality, AI-produced Python translations |
| TrieTest.py | Testing code, appended to the end of participants' solutions |
| Codebook-Trie-Code-to-Errors.txt | Error codebook for the AI-produced translations, organized by source code segment |
| Codebook-Trie-Errors-to-Code.txt | Error codebook for the AI-produced translations, organized by error type |

All participants received `Trie.java`. Participants in the _5-Better_ condition received all 5 of the `Better` translations, and participants in the _5-Worse_ condition received all 5 of the `Worse` translations. Participants in the _1-Better_ condition only received `Trie-4-Better.py`, and participants in the `1-Worse` condition only received `Trie-3-Worse.py`.


### Priority Queue

Code for the Priority Queue data structure is in the `Priority Queue/` directory.

| **File** | **Description** |
| --- | --- |
| PriorityQueue.java | The source Java implementation of the Priority Queue data structure |
| PriorityQueue-{1-5}-Better.py | Five better-quality, AI-produced Python translations |
| PriorityQueue-{1-5}-Worse.py | Five worse-quality, AI-produced Python translations |
| PriorityQueueTest.py | Testing code, appended to the end of participants' solutions |
| Codebook-PriorityQueue-Code-to-Errors.txt | Error codebook for the AI-produced translations, organized by source code segment |
| Codebook-PriorityQueue-Errors-to-Code.txt | Error codebook for the AI-produced translations, organized by error type |

All participants received `PriorityQueue.java`. Participants in the _5-Better_ condition received all 5 of the `Better` translations, and participants in the _5-Worse_ condition received all 5 of the `Worse` translations. Participants in the _1-Better_ condition only received `PriorityQueue-1-Better.py`, and participants in the `1-Worse` condition only received `PriorityQueue-2-Worse.py`.

## Error Analysis

We examined each source code artifact in our study for the presence of various kinds of errors, detailed in Table 2 in the paper:

| **Error** | **Description** | **Operationalization** | **Source Error(s)** |
| --- | --- | --- | --- |
| Translation Error (TE) | Participant mistranslated a code statement by making an error in an assignment statement, a conditional statement, a looping conditional, an array lookup, whitespace, or other logical statement | Count the number of code segments that needed to be modified to fix assignments, conditionals, loops, array lookups, etc. | Translation error, logic error ([Panko 1998]()); Assignment bug, Iteration bug, Array bug ([Gould 1975]()); Logical bug ([Eisenberg & Peelle 1983]()); Lexical bugs ([Eisenstadt 1993]()) |
| Language Error (LE) | Participant included snippets of Java code within Python or failed to appropriately translate Java language idioms to Pythonic idioms | Count the number of code segments that needed to be modified because Java idioms were used or Python requirements were not met | Dummy bug ([Eisenberg & Peelle 1983]()); Language liability ([Knuth 1989]()); Language ([Eisenstadt 1993]()) |
| Spurious Error (SE) | Participant included functionality not part of the original Java program (e.g. by defining new methods) | Count the number of irrelevant, unnecessary, or extraneous code statements | Spurious ([Johnson et al. 1983]()) |
| Code Omission Error (COE) | Participant omitted the translation of a method or code statements within a method, or provided a trivial implementation (e.g. `pass`, `return None`, `print("not implemented"`, etc.) | Count the number of instances in which code was added due to missing, trivial, or incomplete method implementations | Missing ([Johnson et al. 1983]()); Forgotten function ([Knuth 1989]()); Omission error ([Panko 1998]()) |
| Documentation Omission Error (DOE) | Participant omitted translation of a function’s documentation (e.g. Javadoc comment) | Count the number of Python classes and methods that were missing documentation present in the Java source | Missing ([Johnson et al. 1983]()); Omission error ([Panko 1998]()) |
| Correctness Error (CE) | Participant's translation of a method was incorrect (e.g. did not pass unit tests) | Count the number of methods that required one or more modifications to pass unit tests, including methods that weren't implemented | Algorithm awry ([Knuth 1989]()) |

We provide two codebooks for each data structure: a `Code-To-Errors.txt` file and an `Errors-To-Code.txt` file. The `Code-To-Errors.txt` file provides a list of source code snippets and the errors we coded for those snippets, across all of the AI-generated translations. This file shows how, when the model produced identically-incorrect code across multiple trnaslations, those errors were consistently labeled. It has the following format, where `<Code>` is the code containing the error, `<File>:<Line>` lists the file in which that code was present, `<StartLine>:<EndLine>` lists the line range for which that code was present, `<Error Type>` is one of the error categories in the table above, and `<Error Description>` is our explanation for why the error was of that type.

```
```<Code>```
        <File>:<StartLine>:<EndLine> -> <Error Type>: <Error Description>
```

The `Errors-To-Code.txt` file shows the inverse: for each unique `<Error Type>: <Error Description>`, it lists which source lines in the AI-produced translations contained that error. This file has the following format:

```
```<Error Type>: <Error Description>```
       <File>:<StartLine>:<EndLine> -> <Code>
```

### Per-translation Error Statistics

The table below summarizes the error statistics for each AI-produced translation.

| Source | SLOC | Error Count | Error Rate | Translation Error | Language Error | Spurious Error | Code Omission Error | Documentation Omission Error | Correctness Error | Num Methods | Methods Modified | Proportion of Correct Methods (PCM) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | Source Lines of Code | Sum(TE + LE + SE + COE + DOE) | Error Count / SLOC | TE | LE | SE | COE | DOE | CE | Number of methods defined in corrected translation | Methods that were modified to produce a correct translation | Percentage of defined methods that were translated correctly |
| Trie-1-Better.py | 63 | 21 | 0.333333333333333 | 6 | 12 | 3 | 0 | 0 | 5 | 12 | `insert(), find(), delete(), enumerate(), merge()` | 0.583333333333333 |
| Trie-2-Better.py | 70 | 22 | 0.314285714285714 | 8 | 9 | 5 | 0 | 0 | 4 | 12 | `isEndOfWord(), insert(), delete(), enumerate()` | 0.666666666666667 |
| Trie-3-Better.py | 74 | 25 | 0.337837837837838 | 9 | 11 | 5 | 0 | 0 | 5 | 12 | `insert(), find(), delete(), enumerate(), merge()` | 0.583333333333333 |
| Trie-4-Better.py | 77 | 22 | 0.285714285714286 | 9 | 8 | 5 | 0 | 0 | 4 | 12 | `isEndOfWord(), insert(), delete(), enumerate()` | 0.666666666666667 |
| Trie-5-Better.py | 71 | 23 | 0.323943661971831 | 8 | 11 | 4 | 0 | 0 | 4 | 12 | `__init__(), insert(), delete(), enumerate()` | 0.666666666666667 |
| Trie-1-Worse.py | 65 | 28 | 0.430769230769231 | 8 | 15 | 5 | 0 | 0 | 5 | 12 | `insert(), find(), delete(), enumerate(), merge()` | 0.583333333333333 |
| Trie-2-Worse.py | 66 | 35 | 0.53030303030303 | 20 | 9 | 6 | 0 | 0 | 5 | 12 | `insert(), find(), delete(), enumerate(), merge()` | 0.583333333333333 |
| Trie-3-Worse.py | 70 | 42 | 0.6 | 22 | 13 | 7 | 0 | 0 | 5 | 12 | `insert(), find(), delete(), enumerate(), merge()` | 0.583333333333333 |
| Trie-4-Worse.py | 72 | 37 | 0.513888888888889 | 19 | 11 | 7 | 0 | 0 | 5 | 12 | `insert(), find(), delete(), enumerate(), merge()` | 0.583333333333333 |
| Trie-5-Worse.py | 67 | 25 | 0.373134328358209 | 10 | 11 | 4 | 0 | 0 | 5 | 12 | `insert(), find(), delete(), enumerate(), merge()` | 0.583333333333333 |
| PriorityQueue-1-Better.py | 57 | 9 | 0.157894736842105 | 5 | 3 | 0 | 0 | 1 | 5 | 9 | `insert(), remove(), peek(), empty(), enumerate()` | 0.444444444444444 |
| PriorityQueue-2-Better.py | 57 | 9 | 0.157894736842105 | 5 | 3 | 0 | 0 | 1 | 5 | 9 | `remove(), size(), peek(), empty(), enumerate()` | 0.444444444444444 |
| PriorityQueue-3-Better.py | 47 | 15 | 0.319148936170213 | 7 | 3 | 3 | 1 | 1 | 6 | 9 | `insert(), remove(), size(), empty(), enumerate(), _heapify()` | 0.333333333333333 |
| PriorityQueue-4-Better.py | 47 | 13 | 0.276595744680851 | 7 | 3 | 1 | 1 | 1 | 7 | 9 | `insert(), remove(), size(), peek(), is_empty(), enumerate(), heapify()` | 0.222222222222222 |
| PriorityQueue-5-Better.py | 57 | 11 | 0.192982456140351 | 8 | 0 | 2 | 0 | 1 | 4 | 9 | `remove(), size(), peek(), enumerate()` | 0.555555555555556 |
| PriorityQueue-1-Worse.py | 59 | 28 | 0.474576271186441 | 21 | 4 | 2 | 0 | 1 | 6 | 9 | `insert(), remove(), peek(), empty(), enumerate(), _heapify()` | 0.333333333333333 |
| PriorityQueue-2-Worse.py | 58 | 28 | 0.482758620689655 | 21 | 4 | 2 | 0 | 1 | 6 | 9 | `insert(), remove(), peek(), isEmpty(), enumerate(), _heapify()` | 0.333333333333333 |
| PriorityQueue-3-Worse.py | 58 | 22 | 0.379310344827586 | 16 | 2 | 3 | 0 | 1 | 7 | 9 | `insert(), remove(), size(), peek(), empty(), enumerate(), heapify()` | 0.222222222222222 |
| PriorityQueue-4-Worse.py | 60 | 27 | 0.45 | 20 | 5 | 1 | 0 | 1 | 8 | 9 | `insert(), remove(), size(), peek(), is_empty(), enumerate(), _heapify()` | 0.111111111111111 |
| PriorityQueue-5-Worse.py | 57 | 25 | 0.43859649122807 | 20 | 3 | 1 | 0 | 1 | 6 | 9 | `insert(), remove(), peek(), empty(), enumerate(), _heapify()` | 0.333333333333333 |

## A Note on Reproducibility

Our motivation in publishing this code is to enable others to reproduce of our work. However, we would instead challenge the community to extend our work, using these materials as a reference. The specific source examples in this repository are limited to only one kind of code-related task (Java to Python translation) for which generative code models can provide aid. There are many other kinds of tasks for which generative code models can provide support, such as natural language to code, code documentation, code autocomplete, test case generation, bug repair, and others. We encourage further research into these use cases, especially around how intelligent user interfaces can help users achieve successful outcomes when working in the presence of erroneous model output.

## Citation

If you found these supplemental materials useful in your work, we kindly request that you cite our paper.

### ACM Reference Format

> Justin D. Weisz, Michael Muller, Steven Ross, Fernando Martinez, Stephanie Houde, Mayank Agarwal, Kartik Talamadupula, and John T. Richards. 2022. Better Together? An Evaluation of AI-Supported Code Translation. In 27th International Conference on Intelligent User Interfaces (IUI ’22), March 22–25, 2022, Helsinki, Finland. ACM, New York, NY, USA, 35 pages. https://doi.org/10.1145/3490099.3511157

### BibTeX

```BibTex
@inproceedings{weisz2022better,
    title={Better Together? An Evaluation of AI-Supported Code Translation},
    author={Weisz, Justin D and Muller, Michael and Ross, Steven and Martinez, Fernando and Houde, Stephanie and Agarwal, Mayank and Talamadupula, Kartik and Richards, John T.},
    booktitle={Proceedings of the 27th International Conference on Intelligent User Interfaces},
    year={2022}
}
```
