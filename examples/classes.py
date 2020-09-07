from utils import create_subtitle

# classes
subtitle = create_subtitle('classes')

# ----------
print(next(subtitle))

class SampleClass:
  def __init__(self, arr):
    self.arr = arr

  def arrLength(self):
    return len(self.arr)

  def _softProtectedMethod(self):
    print('method 1')

  def __protectedMethod(self):
    print('method 2')

print(SampleClass([1, 2, 3]).arrLength())
