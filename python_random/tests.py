import linked_lists as ll

a = ll.Node('A')
b = ll.Node('B')
c = ll.Node('C')
d = ll.Node('D')
a.next = b
b.next = c
c.next = d

e = ll.Node(2)
f = ll.Node(4)
g = ll.Node(6)
h = ll.Node(8)
e.next = f
f.next = g
g.next = h
arr = []


def test_linked_list():
    assert ll.print_link_list(a) == ['A', 'B', 'C', 'D']
    assert ll.print_link_list(b) == ['B', 'C', 'D']
    assert ll.print_link_list(c) == ['C', 'D']
    assert ll.print_link_list(d) == ['D']


def test_sum_list():
    assert ll.sum_linked_list(e) == 20
    assert ll.sum_linked_list(f) == 18
    assert ll.sum_linked_list(g) == 14
    assert ll.sum_linked_list(h) == 8


def test_find_value():
    assert ll.find_value(a, 'C') is True
    assert ll.find_value(f, 6) is True
    assert ll.find_value(c, 'A') is False
    assert ll.find_value(e, 11) is False


def test_find_val_by_index():
    assert ll.find_val_by_index(a, 2) == 'C'
    assert ll.find_val_by_index(a, 5) == None


def test_find_index():
    assert ll.find_index(a, 'C') == 2
    assert ll.find_index(a, 'E') == None
