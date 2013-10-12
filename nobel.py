# The pound sign is used as a comment character in Python. Programmers
# use comments to annotate code. Python ignores everything after the
# comment character on a line.

# Notice how the 'print' command has been inserting a new line at the
# end of our strings.
print "The Nobel Prize categories are:"
# We can insert newlines ourselves, using "\n".
print "Physics\nChemistry\nLiterature\nPeace\nPhysiology or Medicine"

# "" Is the empty string. Since the print command will insert a
# newline at the end, this will print a newline by itself:
print ""

# Here's a new kind of printing: you can use triple quotes to create
# multiline strings.
print """Two laureates have voluntarily declined their Nobel Prizes. One was
Jean-Paul Sartre. In 1964, Sartre was awarded the Literature Prize but
refused, stating, \"A writer must refuse to allow himself to be
transformed into an institution, even if it takes place in the most
honourable form.\""""

print ""

# When you use triple quotes, whitespace is preserved.
print """In 2009,
    The monetary component of the prize was
        US $1.4 million"""
