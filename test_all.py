#!/bin/env python3
"""
A script to test all snippets in some undefined order by combining into
scenarios.
"""

print("Not implemented yet!")
exit(1)

"""
This is just a concept — it may not actually work well!

Simple algorithm:

1.  find all snippets/templates
2.  for each placeholder name, make a list of each snippet and each placeholder matching that name
3.  make a list of all snippets/templates which are not yet included in a scenario (i.e. all to start with)
4.  while above list is not empty:
    
    *   take first item
    *   while document does not start at the top level (scenario), find a template with this snippets placeholder and subsitute into that
    *   while required placeholders exist: find a snippet and substitute it in
    *   while optional placeholders exist: find a snippet, but only if not already included somewhere
    
    While doing this:
    
    *   prefer not-yet-included snippets/templates
    *   remove any included items from the list of those not yet used, and move to back of list of snippets/placeholders matching a name
    
    Then create a document, and repeat whole loop.

Caveats:

*   just because something is included does not mean it is used
*   there is no testing of outputs

Maybe an alternative would be to build test scenarios dynamically from snippets, but deterministically, checking for differences to old results?
"""
