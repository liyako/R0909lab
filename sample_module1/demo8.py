# use module

def foo(x):
    print("[demo8]:[foo]:parameter=%s" % str(x))
import sample_module1


def foo(x):
    print("[demo8]:[foo]:[%s]parameter=%s" % (sample_module1.package_global_variable1, str(x)))