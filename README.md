# things-acquisition-age
## Overview
`things-acquisition-age` is a program for acquiring "ages of acquisition" for objects in the THINGS database - that is, ages at which children understand the objects of the THINGS database.

More specifically, what this program is doing is looking at a list of words that describe the objects of the THINGS database and deriving an age of acquisition using known ones for those words.
Essentially, then, some of the outputs of this program (see Methods/Outputs for specifics) are for the most part upper bounds of the ages children understand THINGS objects for most of the objects.

## Methods
This program takes the Kuperman et al. age of acquisition dataset for words 
(Kuperman, V., Stadthagen-Gonzalez, H. & Brysbaert, M. Age-of-acquisition ratings for 30,000 English words. _Behav Res_ **44**, 978–990 (2012). <https://doi.org/10.3758/s13428-012-0210-4>)
to produce ages of acquisition for each of the objects of the THINGS dataset
(Hebart MN, Dickter AH, Kidder A, Kwok WY, Corriveau A, et al. (2019) THINGS: A database of 1,854 object concepts and more than 26,000 naturalistic object images. PLOS ONE 14(10): e0223792. <https://doi.org/10.1371/journal.pone.0223792>)
in the following manner:

For each object in the THINGS dataset, take the set of synonyms describing it (the WordNet Synset, provided as part of the THINGS dataset).
Acquire the age of acquisition for each of these synonyms, or none if the synonym is not present in the Hebart et al. AoA dataset, as a set of ages of acquisition for the object.
Prepare three different final ages of acquisition for the object using this set of ages by taking:
+ The highest of the ages of acquisition for the object (none/infinity if any of the ages are none/infinity)
+ The lowest of the ages of acquisition for the object
+ The highest of the ages of acquisition for the object (ignoring any none/infinite ages)

## Output
A tab-separated-value document with four columns: one for a canonical name of each THINGS object, and one column each for each of the three ways of acquiring an object's age (see Methods for specifics)

