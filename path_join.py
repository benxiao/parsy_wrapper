




def join_paths_with_overlay(p1, p2):
    components1 = p1.split('/')[1:]
    components2 = p2.split('/')[1:]



if __name__ == '__main__':
    p1 = '/Users/ranxiao'
    p2 = '/Users/ranxiao/Desktop'
    print(join_paths_with_overlay(p1, p2))