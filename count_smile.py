'''Given an array (arr) as an argument complete the function countSmileys
that should return the total number of smiling faces.'''

'''
ALTERNATIVE ONE:

from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
'''

'''
ALTERNATIVE 2
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count
'''
countSmileys([':)', ';(', ';}', ':-D'])
countSmileys([';D', ':-(', ':-)', ';~)'])
countSmileys([';]', ':[', ';*', ':$', ';-D'])
countSmileys([';]', ':[', ';*', ':$', ';-D'])
