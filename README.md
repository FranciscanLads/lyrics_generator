# lyrics_generator
A TensorFlow Model that Generates Lyrics.

# To just get it working run the {coldplay/top}_predictor.py file.

Natural Language Processing Project.

This is a mini project which tries to generate lyrics. 
Accuracy may vary by artists.
You are welcome to reproduce our work, until you give us the shoutout on your code, of the original idea.

First we scrape all the lyrics from azlyrics.com

Then we will try to implement it in a python file.


1) First we run coldplay_test.py
2) It will save a file with the name coldplay.html
3) Then we run coldplay_scrape.py
4) We save the generated links in the console in an array in another python file.
5) Now we will try to append all of these to a certain file.
6) Create a new .txt file and write its name in the last python file with the array, to open it.
7) After the script completes running you will have all the lyrics in the .txt file.
8) Scroll through it. Remove any mistakes.
9) Then just input the file into the python notebook and it should probably be easy.

After all is done the one thing that has a big room for improvement that is the hyper parameters selection.
Once you generate lyrics dataset of any artist, everything will work fine and the model will also return to you,
gibberish that will actually sound like the specified artist. But the main concern still is that it is gibberish. 
This one phase will take time. Once we get to the correct hyper parameters. The outputs will actually make good sense.
