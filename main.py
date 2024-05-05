# from io import StringIO
# import sys
import subprocess
# import os

# f = open("yt-dlp.conf", "w")
# f.write("-o \'%temp%\\EasyDownloader\\%(title)s.%(ext)s\'")
# f.close()
# f = open("yt-dlp.conf", "rt")
# print(f.read())
# f.close()
# class Capturing(list):
#     def __enter__(self):
#         self._stdout = sys.stdout
#         sys.stdout = self._stringio = StringIO()
#         return self
#     def __exit__(self, *args):
#         self.extend(self._stringio.getvalue().splitlines())
#         del self._stringio    # free up some memory
#         sys.stdout = self._stdout
testvar = subprocess.run(["yt-dlp","https://www.youtube.com/watch?v=BQvGUyxbxWc -o \'%temp%\\EasyDownloader\\%(title)s.%(ext)s\'","-q"],capture_output=True, shell=True)
if testvar.stderr != 0:
    error_string = str(testvar.stderr)[2:]
    error_string = error_string.replace("\\n","\n")
    error_string_list = error_string.splitlines()
    error_dict = {}
    for n in range(len(error_string_list)):
        error_dict_label = str("event_n" + str(n))
        error_dict[error_dict_label] = error_string_list[n]
    error_dict.popitem()
    if testvar.returncode == 0:
        print("##\n## Warnings:")
    else:
        print("##\n## Errors:")
    for n in error_dict:
        print(f"## [{n}] - {error_dict[n]}")
    print("## Finish error writing\n##")

print("")

# with Capturing() as output:
#     print(testvar)
# print(testvar,end="\n\n")
# print(type(testvar))
# print("\n###\n")
# print(output)
# print(type(output))

