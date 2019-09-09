from sample_module1.demo8 import foo

foo('mark')

import sample_module1.demo8

sample_module1.demo8.foo('kevin')

import sample_module1

print(sample_module1.package_global_variable1)