from sll import *


def main():
    my_list = LinkedList()
    my_list.insert(10, my_list.head)
    print('List is: ', end='')
    my_list.print()
    my_list.insert(12, my_list.head.next)
    print('List is: ', end='')
    my_list.print()
    my_list.insert(2, my_list.head)
    print('List is: ', end='')
    my_list.print()
    print('Size of List:', my_list.len())
    my_list.delete(my_list.head)
    print('List is: ', end='')
    my_list.print()
    my_list.delete(my_list.head.next)
    print('List is: ', end='')
    my_list.print()
    print('List is empty?', my_list.empty())
    print('Size of my_list is:', my_list.len())
    my_list.delete(my_list.head)
    print('List is empty?', my_list.empty())
    print('Size of my_list is:', my_list.len())
    my_list.insert_at_index(2, 0)
    my_list.insert_at_index(1, 0)
    my_list.insert_at_index(4, 2)
    my_list.insert_at_index(3, 2)
    print('List is: ', end='')
    my_list.print()


if __name__ == '__main__':
    main()
