#!/bin/python
class Camel():
  def __init__(self,name):
    self.name = name
    self.age = "20"
  def get_class(k):
    print(k.__dict__)
    class Classy():
      def __init__(self,item):
        self.item = item
    out = Classy("whatever")
    return out

camely = Camel("caramel")
testClass = camely.get_class()
#print(testClass.__dict__)

