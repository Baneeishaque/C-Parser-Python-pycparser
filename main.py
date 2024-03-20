# import sys
import pycparser
import pycparser_fake_libc

fake_libc_arg = "-I" + pycparser_fake_libc.directory
# print(fake_libc_arg)
# sys.exit(0)

ast = pycparser.parse_file("sample.i", use_cpp=True, cpp_args=fake_libc_arg)