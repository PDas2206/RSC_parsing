# RSC_parsing
This is a colection of codes that were required to process the datasets such that they could be used for the Genzel-Charniak pipeline.
They modify the parsed files by adding their respective meta data from a version of theirs that had not been parsed. There are hundreds of such files, so this code scans two folders (target folder containing all the parsed files and a source folder containing files of the same name that are not parsed but containing meta data that the final version needs) to select files of the same name and do the necessary changes.
Other code snippets also make further changes as necessary for the project.
A sample target folder file, source folder file has also been provided in the dataset folder.
This code runs on the coli servers at Saarland University. One can reuse the code for their specific tasks just by changing the required path.
## File types
the source files are in vrt format but the target files are in conllu. The resultant file type can be of any type desired.
