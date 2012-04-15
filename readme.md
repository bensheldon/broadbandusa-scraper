BroadbandUSA App Parser
======================

This tool, `parse.py`, converts the BroadbandUSA.gov online application database into a more easily analyzable Tab-Separate-Value file that can be easily imported into Excel.

How to use it
-------------

1. Save the HTML of the BrandbandUSA applications to a file (a good place to put it would be in the `/applications` folder). You can acquire the HTML here: [http://ssl.ntia.doc.gov/broadbandgrants/applications/results.htm](http://ssl.ntia.doc.gov/broadbandgrants/applications/results.htm) (and click File -> Save As from the menu in your browser)
2. Edit the top of `parser.py` so that `htmlFile = ` points to the location of your file (e.g. `htmlFile = './applications/apps-1-28-11.html'`)
3. Run the parser and point its output to a file of your choosing; e.g. `python parser.py > applications.tsv`
4. Open the resulting file (e.g. `applications.tsv`) in Excel.
5. Celebrate!