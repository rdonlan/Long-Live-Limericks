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
read to you the best limerick it creates. The method of selection used is rank. Recombination occurs by taking lines 1,2,5 from parents 1 and lines 3,4 from parents two because recombining this way keeps the integrity of the rhyme scheme. Mutation occurs by just randomly selecting a word from the limerick and replacing it. For this program I found that using 20 generations, 16 population size, and a mutation rate of 0.01 created regularly better poems, so I have set those parameters to these values.

Working on this challenged me because I had to find a bunch of external libraries to help me accomplish things like rhyming, random word generation, type of speech specific word generation and a few other things. I had to research and read the docs of many public libraries to determine if I wanted to use them, and then how they could be best utilized. This level or research is something that I haven't had to do for a project before.

Also, the text file named best_limericks.txt contains the parameters used to run the program 20 different times, and the limericks that were spit out!

Below are three academic papers that I got inspiration from when creating this program:

https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0074986
This paper explored what would responses from listeners would be if they were told a limerick that had some error, often changing the rhyming scheme and meter. They found that quite often there people had emotional responses in addition to their anomaly detection. This showed to me that these two things were very important for limericks and so I should calculate my fitness on them.

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.91.5363&rep=rep1&type=pdf#page=75
This article was really the inspiration for me to write limericks. I was just randomly searching different types of poetry, and at the beginning of this article it has two limericks that it generated and they were quite good! So I wanted to try as well!

https://www.hindawi.com/journals/mpe/2016/4076154/
This article helped to inspire me to use a Genetic Algorithm to generate the best poetry. They used a genetric algorithm and it turned out to be a superior generator than the previous method they were using so I thought it would be a good method for me to use.


