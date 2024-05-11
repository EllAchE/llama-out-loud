from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

output_string = StringIO()
with open("January2016.pdf", "rb") as fin:
    result = extract_text_to_fp(
        fin, output_string, laparams=LAParams(), output_type="html", codec=None
    )
    print(result)

print(output_string.getvalue())

# write to file
with open("January2016.html", "w") as fout:
    fout.write(output_string.getvalue())
