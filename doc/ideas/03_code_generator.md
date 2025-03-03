# Idea
What if your editor had built in hinting around HTML properties?

## Implementation
We take information from the HTML spec living document and MDN.

We place generated code in a separated directory, keeping magic out of the code.

the `tools` directory contains:
 * The spec generator `spec_generator.py`
   * Pull, parse, and dump json we think is interesting
 * The attribute code generator `generate_attributes.py`
   * Put that interesting information in generated class attributes using our formula defined in previous specs. If an attribute is a keyword or restricted by Python, append `_` to the end of the name so autocomplete works. Dump those in `src/html_compose/attributes`

* `tools/generated/*_attrs.py` is the intermediate directory so runs do not write to source control directory, but you can see when a new change has happened.

## Extension of this idea:
TBD

caniuse data can be used to generate warnings based on browser targets