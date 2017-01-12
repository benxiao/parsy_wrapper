import subprocess
import os

# constants
ORIGINAL_DIR = os.curdir
MCPARFACE_DIR = '/Users/ranxiao/Desktop/models/syntaxnet'
WORD = 1
WORDTYPE = 4
EXAMPLE = 'Mr. Sessions also said he would recuse himself from any lingering investigations involving Hillary Clinton or her family’s foundation. During Mr. Trump’s campaign, “lock her up” was a Republican rallying cry. Mr. Sessions previously supported appointing a special prosecutor to investigate her. The F.B.I.’s investigation into Mrs. Clinton’s use of a private email server is closed. And while a preliminary investigation into the Clinton Foundation is open, senior career officials at the F.B.I. and Justice Department have said there is little basis for the case to move forward.'


def pos_tag(text, verbose=False):
    """
    :param text: accept a single str or a python list of strs or strs with '\n' as separator
    :optional param verbose: if True, will output extra printout from
    :return: [(word, word_type)...] or [[(word, word_type)...],...]
    """
    single = True
    if isinstance(text, list):
        text = '\n'.join(text)
        single = False

    if '\n' in text:
        single = False

    os.chdir(MCPARFACE_DIR)

    # command = """echo $'%s' | syntaxnet/my_parser.sh | grep -E '^[1-9]+\t'""" % (text)
    command = """echo $'%s' | syntaxnet/myparser.sh""" % (text)
    stderr=None
    if not verbose:
        stderr = open(os.devnull, 'w')
    result = subprocess.check_output([command], stderr=stderr, shell=True)
    result = result.decode()
    # print(result) # debug only
    individuals = []
    i, j = 0, 0
    while 1:
        j = result.find('\n1\t', i+1)
        if j != -1:
            individuals.append(result[i:j])
        else:
            break
        i = j
    if i < len(result):
        individuals.append(result[i:])
    individuals = [get_tuples_from_table(x) for x in individuals]
    if single:
        return individuals[0]

    os.chdir(ORIGINAL_DIR)
    return individuals


def get_tuples_from_table(text):
    result = []
    lines = text.split('\n')
    for line in lines:
        items = line.split('\t')
        try:
            result.append((items[WORD], items[WORDTYPE]))
        except IndexError:
            # avoid check items on every iteration
            pass
    return result


if __name__ == '__main__':
    ret = pos_tag(EXAMPLE, verbose=False)
    print(ret)
