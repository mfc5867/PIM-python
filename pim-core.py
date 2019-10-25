class core:

  def __init__(self, N):
    self.N = N

  def setFunc(self, func):
    self.func = func
    evaluate(self):

  def setA(self, A):
    self.A = A
    evaluate(self)

  def setB(self, B):
    self.B = B
    evaluate(self)
