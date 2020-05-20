import testmodule
print(testmodule.multiplyer(2))

from testmodule import multiplyer
print(multiplyer(2))

import testmodule.multiplyer
print(multiplyer(2))

exec(open('testmodule.py').read())

