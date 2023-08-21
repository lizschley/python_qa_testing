# Utilities ReadMe

All of the methods in this folders are ones that were helpful at some point.

## date_time.py

Working with Dates and Times programmatically can be complex.  For example, there are so many time zones, lots of display formats, transforming from string to datetime (so you can do some arithmetic) and from datetime to string.  Plus, database formats can vary a lot.  This is why I wrote some unit tests to illustrate some of the functionality.

## delete_pickles.py

This is a program that can be run from the command line.

```bash

% python utilities/delete_pickles.py

```

Read through the code and comments to understand how to use:

* It is currently set up to NOT delete anything, but you can change that by turning DELETE to True.

* The purpose is to (depending on the DELETE switch) either list all the filepaths within a directory or to delete the specified files within the directories or subdirectories. It is recursive, so it lists or deletes them all.

* The program is currently set up to delete any ```.json``` files underneath the reports directory.

* It does not make sense and could potentially be a problem to send files generated in runtime to GitHub

* History
  * The reports were sorely needed in AAP in order to troubleshoot intermittent test errors. But the number of files grew to be too many to delete manually.
  * The same program, with a different setup, was used previously to delete pickle files that were used for caching data (something used frequently to speed up the tests).

## dt.py

This is a bit of throwaway code that was useful on a particular occasion.  It is run from the commandline:

```bash

% python dt.py

```

It displays the current date-time on the command line.  Useful to roughly time something and if you need it a lot, you can do it again with the up arrow and enter.

## json_methods.py

These are functions to read and write json files.  They are pretty useful for reports or reading input data sometimes (though usually dictionaries are better for that (see data folder))

## utils.py

These are functions that make common operations really simple. Some of the methods are used a lot in this code base and others were once useful.
