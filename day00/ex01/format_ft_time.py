from time import time
from datetime import datetime

sec = time()
formated_sec = f"{sec:,.4f}"
sci_sec = f"{sec:.2e}"

print("Seconds since January 1, 1970:", f"{sec:,.4f}","or", f"{sec:.2e}", "in scientific notation")
date = datetime.fromtimestamp(sec)

print(date.strftime("%b %d %Y"))
