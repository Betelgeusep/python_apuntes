class A:
    def print_a(self):
        print('a')
class B:
    def print_b(self):
        print('b')
class C(A, B):
    def print_c(self):
        print('c')
c = C()
c.print_a()
c.print_b()
c.print_c()