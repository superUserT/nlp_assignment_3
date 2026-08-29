# Question 1 [25 Marks]

## Background:
In Chapter 2 of Jurafsky & Martin’s Speech and Language Processing, regular expressions are
formally mapped to Finite State Automata. When an automaton is non-deterministic (NFSA), a
search algorithm is required to explore alternative paths through the transition graph. Figure 2.21
(Page 39) defines the ND-RECOGNIZE framework, which uses an agenda-based approach to
determine string acceptance.
Depending on how the agenda is manipulated, the search strategy can behave as either Depth-
First Search (DFS) or Breadth-First Search (BFS).


### Requirements:
Write a robust, well-documented Python program using standard libraries only to implement the
ND-RECOGNIZE framework. Your solution must satisfy the following criteria:
1. Automaton Representation (5 Marks): Define an internal data structure (such as a
nested dictionary or object-oriented class structure) representing the NFSA from Figure
2.21. The structure must explicitly handle non-deterministic transitions (mapping a
single state and symbol to a list of potential next states) and ε-transitions (epsilon moves).
2. Search Strategy Configuration (10 Marks): Implement the pseudo-code function ND-
RECOGNIZE(tape, machine). Your code must explicitly allow the user to toggle the search
strategy via a configuration parameter (e.g., strategy="DFS" or strategy="BFS").
o DFS Configuration: Program the agenda to act as a Stack (LIFO) using native
Python lists or collections.deque.
o BFS Configuration: Program the agenda to act as a Queue (FIFO) using
collections.deque.popleft().
6
o Each item placed on the agenda must be a search-state tuple: (current_node,
tape_pointer).
3. Regular Expression Wrapper (5 Marks): Create a simple helper function that takes a
basic regular expression string matching the textbook example (e.g., baaa! or baa*!),
compiles it into your internal NFSA data structure, and feeds it into your configurable
recognition engine.
4. Execution Log and Comparison (5 Marks): Run your code against a valid target string
(e.g., "baaa!") using both strategies. Your program must print a clear, step-by-step console
log showing the contents of the agenda and the current search-state at every iteration.
Include a brief terminal printout comparing the total number of search steps taken by
DFS versus BFS to reach acceptance.

## Question 2 Text Preprocessing Pipeline Architecture and Implementation [25 Marks]
In NLP, text preprocessing is a critical foundational layer as it transforms unstructured raw strings
into clean, normalised linguistic tokens suitable for downstream machine learning architectures
or semantic analysis. In this assignment, you will design and program a highly controlled text
preprocessing pipeline using Python. You will process a specialized corpus sample, evaluate
structural engineering choices, and handle token normalization constraints.


### Scenario and Target Corpus
Imagine you are building a clinical text classifier. Your input pipeline must handle specific edge
cases like hyphenated medical jargon, morphological inflections, and noisy punctuation.
Use the following raw string snippet for your code execution and verification:
python
raw_text = "The intensive-care patients are recovering surprisingly quickly. Doctors are analyzing data
daily!"

1. Conceptual Design and Pipeline Constraints [5 Marks]

• 1.1 Draw a conceptual block diagram detailing the exact sequence of data
transformations from raw_text to your final output. (2)
• 1.2 In text preprocessing, a standard pipeline applies stopword removal before
lemmatisation, or vice versa. Discuss the architectural trade-off of both approaches
regarding computational efficiency and Parts-of-Speech (POS) tagging dependency.
Justify which order is optimal for your pipeline. (3)

2. Custom Tokenisation and Case Normalisation (6)

Write a Python function named custom_tokenize(text) that accepts a raw string and returns a
clean list of lowercased tokens.

• Constraint: You cannot use high-level NLP libraries (like NLTK, SpaCy, or HuggingFace)
for this specific task. You must rely solely on native Python string methods or the built-in
re (Regular Expressions) engine.

• Your function must convert all text to lowercase, strip trailing punctuation marks, and
handle hyphenated entities (e.g., "intensive-care"). Include inline code comments
explicitly stating your linguistic design choice regarding whether you split hyphenated
words or kept them bound as single tokens.

3. Deterministic Stopword Filtering (4)

• Write a Python function named remove_stopwords(token_list, custom_stopwords) that
strips structural words from your token stream.
COS4861/101/0/2026

• Define a hardcoded python set containing at least 5 standard English grammatical
stopwords relevant to the target snippet (e.g., "the", "are").

• Optimise this function using a list comprehension or generator expression to filter tokens
efficiently.

4. Context-Aware Lemmatisation (6)

• Write a Python function named lemmatize_tokens(token_list) using a reputable NLP
framework of your choice (such as nltk with WordNetLemmatizer or spacy).

• Crucial Requirement: A naive lemmatiser defaults to processing tokens as nouns, which
fails on verbs or adverbs (e.g., leaving "recovering" or "analyzing" unchanged). Your
code must programmatically determine or pass the correct POS tags to the lemmatiser.

• Ensure your final output correctly maps words to their base linguistic lemmas (e.g.,
"patients" → "patient", "recovering" → "recover").

5. Pipeline Orchestration and State Verification (4)

• Write a master execution script that chains your functions together sequentially:
raw_text →custom_tokenize → remove_stopwords → lemmatize_tokens

• Your script must print the intermediate output list at every stage of the process to prove
successful state mutation.