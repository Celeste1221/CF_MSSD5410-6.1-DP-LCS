from algorithms import *


# Compares code copied from the internet with modifications done in class to see how much is similar

# read in file, clean it up to ready if for comparison to another file
def process_file(fname, enc):
    # open file for reading 'r'
    with open(fname, 'r', encoding=enc) as file:
        dat = file.readlines()
        dat_str = ""
        # get rid of comments
        for line in dat:
            # ref: https://stackoverflow.com/questions/1706198/python-how-to-ignore-comment-lines-when-reading-in-a-file
            # returns the first index of a tuple of (right side, "separator", left side).
            right = line.partition("#")[0]
            if len(right) > 0:  # if the line is not empty
                dat_str += str(right)  # add it to the new data string
    return dat_str.split()


def percent_different(x, y):
    percent = (x / y) * 100
    return round(percent, 1)


def main():
    lcsf = "lcs-DP.txt"
    edit_distf = "edit_distance_DP.txt"
    classf = "prog_from_class_DP.txt"

    lcs_code = process_file(lcsf, "utf-8")
    edit_dist_code = process_file(edit_distf, "utf-8")
    class_code = process_file(classf, "utf-8")

    # for testing:
    # print(lcs_code)

    lcs_lcs = lcs(class_code, lcs_code)
    lcs_edit_dist = lcs(class_code, edit_dist_code)
    ed_lcs = editDistDP(class_code, lcs_code, len(class_code), len(lcs_code))
    ed_edit_dist = editDistDP(class_code, edit_dist_code, len(class_code), len(edit_dist_code))

    print("\nThe LCS between the modifications done in class and the original lcs code copied from online"
          " is {0}".format(lcs_lcs))
    print("The LCS between the modifications done in class and the original edit distance code copied from online"
          " is {0}".format(lcs_edit_dist))

    print("\nThe edit distance between the modifications done in class and the original lcs code copied from online"
          " is {0}".format(ed_lcs))

    print("The edit distance between the modifications done in class and the original edit distance code "
          "copied from online is {0}".format(ed_edit_dist))

    print("\nThe length of the class code is {0} chars. The length of the original lcs code is {1}. "
          "Based on the edit distance of {2}, the class code is {3}% different than the original lcs code."
          .format(len(class_code), len(lcs_code), ed_lcs, percent_different(ed_lcs, len(class_code))))

    print("\nThe length of the class code is {0} chars. The length of the original edit distance code is {1}. "
          "Based on the edit distance of {2}, the class code is {3}% different than the original edit distance code."
          .format(len(class_code), len(edit_dist_code), ed_edit_dist, percent_different(ed_edit_dist, len(class_code))))


if __name__ == "__main__":
    main()
