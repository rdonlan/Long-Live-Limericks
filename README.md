# Long-Live-Limericks

Welcome to the LLL, or Long Live Limericks. This program works to make a special type of poem, a limerick. Limerick are 5 line poems with a 
rhyming scheme of AABBA. They are often about a person/object, and they originated in Ireland.

The first time you open this program, before running it, you must type the following commands into the terminal:

import nltk
nltk.download('words')
nltk.download('cmudict')

These commands are required to ensure that your machine has the resources required to generate the words for the poetry. After you have completed this
you may simply run the program (through the terminal or by pressing the run button on your IDE). You will then be prompted to give the program a 
noun that will be the subject of the generated limericks, and that noun's pronoun. Then the program will do its magic, utilizing a GA, and will
read to you the best limerick it creates. The method of selection used is rank. Recombination occurs by taking lines 1,2,5 from parents 1 and lines 3,4 from parents two because recombining this way keeps the integrity of the rhyme scheme. Mutation occurs by just randomly selecting a word from the limerick and replacing it.

Working on this challenged me because I had to find a bunch of external libraries to help me accomplish things like rhyming, random word generation, type of speech specific word generation and a few other things. I had to research and read the docs of many public libraries to determine if I wanted to use them, and then how they could be best utilized. This level or research is something that I haven't had to do for a project before.

Below are three academic papers that I got inspiration from when creating this program:
http://www.eecs.qmul.ac.uk/~mpurver/papers/mcgregor-et-al16ccnlg.pdf
