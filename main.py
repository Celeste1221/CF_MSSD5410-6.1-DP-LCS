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


def main():
    lcsf = "lcs-DP.txt"
    edit_distf = "edit_distance_DP.txt"
    classf = "prog_from_class_DP.txt"

    lcs_code = process_file(lcsf, "utf-8")
    edit_dist_code = process_file(edit_distf, "utf-8")
    class_code = process_file(classf, "utf-8")

    # for testing:
    # print(lcs_code)

    print("\nThe LCS between the modifications done in class and the original lcs code copied from online"
          " is {0}".format(lcs(class_code, lcs_code)))
    print("The LCS between the modifications done in class and the original edit distance code copied from online"
          " is {0}".format(lcs(class_code, edit_dist_code)))

    print("\nThe edit distance between the modifications done in class and the original lcs code copied from online"
          " is {0}".format(editDistDP(class_code, lcs_code, len(class_code), len(lcs_code))))

    print("The edit distance between the modifications done in class and the original edit distance code "
          "copied from online is {0}".format(editDistDP(class_code, edit_dist_code, len(class_code),
                                                        len(edit_dist_code))))


if __name__ == "__main__":
    main()
