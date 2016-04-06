__author__ = 'josebermudez'


def findingOcurrences(textToSearch, subtext):

    if not textToSearch or not subtext:
        raise ValueError('Error in parameters.')

    result = []
    index = 0

    input_string = textToSearch.lower()
    ocurrence = subtext.lower()

    while index < len(textToSearch):
        if input_string[index] == ocurrence[0]:
            index2 = 1
            while index2 < len(ocurrence) and textToSearch[index + index2] == subtext[index2]:
                index2 += 1
            if index2 is len(ocurrence):
                result.append(index+1)
                index = index + index2
        index += 1
    return result
