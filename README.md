This is the OpenMalaria snippet library.
========================================

## Organisation

Snippets appear as XML (text) files, sometimes with a version number in the file name.
This version number is the OpenMalaria schema version that the snippet was
written for or checked against, however most snippets will be
forward-compatible.

There are no requirements about the directory structure or where files are in
the library.

## Format ##

Each file contains some comments and a chunk of XML code which can be pasted
into a larger OpenMalaria scenario XML.

Some special comments may appear at the beginning of the file:

    <!-- min-version: 30 -->
    <!-- max-version: 36 -->
    <!-- snippet: om:demography -->

The min- and max-version tags specify limits to the range of compatible
OpenMalaria versions. They do not need to appear; e.g. if the snippet is
compatible with the latest version it doesn't make sense to specify the
max-version (unless it is expected that the next version will be incompatible).

The `snippet:` tag is used to specify where the snippet may appear; e.g. there
should be a comment like the following somewhere in another snippet (a
*template*):

    <!-- placeholder: om:demography -->

Variations on this hint at how many items can be inserted here (optional: zero
or one, any: zero or more):

    <!-- placeholder optional: om:pharmacology -->
    <!-- placeholder any: om:intervention-elt -->

In addition, each file should contain some commentry of its source, its
purpose and how its parameters were obtained.


## Contributions ##

Contributions of new publishable and documented snippets are welcomed. If you can edit this wiki you should also be able to amend this library yourself, by cloning the git repository with this git-specific link: `git://github.com:SwissTPH/openmalaria.snippets`; alternatively contact the OpenMalaria developer.

## Schema documentation ##

If you need to consult XML elements and attributes for a certain version select
[the appropriate version from here](https://github.com/SwissTPH/openmalaria/wiki/schema-index)
