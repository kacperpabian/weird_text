<h2>Weird Text</h2><br>
<h3>How to run it</h3>
<p>You can run it with docker: </p>
<p>docker build -t python-werid .</p>
<p>docker run python-weird</p>
<p>Or with pipenv:</p>
<p>pipenv install</p>
<p>pipenv run weird_text.py</p>
Task:<br>
<h3>WeirdText encoding and decoding</h3>
WeirdText is a text encoding.<br>
It is not "encryption" because humans can usually read it quite easily.  But
machines may find it difficult to read without the list of original words.  Except
of having fun, there are real-world applications for this, e.g. if encryption is
forbidden by law in your country, but you still don't want your email content to
get automatically processed somehow.<br>
<h3>Encoding</h3>
For each original word in the original text, leave the first and last character of it
in that position, but shuffle (permutate) all the characters in the middle of the
word.  If possible, the resulting "encoded" word MUST NOT be the same as the
original word. Keep everything else (whitespace, punctuation, etc.) like in the
original.  To make decoding by a machine possible, your encoder shall also
output a sorted list of original words (only include words that got shuffled, not
text that did not).<br>
The composite output of the encoder (see example below) contains encoded
text (WeirdText) and also the sorted list of original words.
<h3>Decoding</h3>
For decoding composite text, first do a simple check whether the text looks like
composite output of your encoder. If not, raise some reasonable exception.
Then, use the encoded text and the words list to decode the text.
Your decoded output should, as far as possible, be identical to the original
text. In case of ambiguities (some encoded word could have been multiple
original words), decoding errors are acceptable.
<h3>Example</h3>
Original Text (this is a single string formatted nicely for better viewing!)::<br>
'This is a long looong test sentence,\n'<br>
'with some big (biiiiig) words!'<br>
Encoded Text (see comment above):<br>
'\n---weird---\n'<br>
'Tihs is a lnog loonog tset sntceene,\n'<br>
'wtih smoe big (biiiiig) wdros!'<br>
'\n---weird---\n'<br>
'long looong sentence some test This with words'<br>
Decoded Text::<br>
'This is a long looong test sentence,\n'<br>
'with some big (biiiiig) words!'<br>