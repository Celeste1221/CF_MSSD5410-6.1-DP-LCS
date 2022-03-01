from algorithms import *
import string


# compare the the code from the internet with the modified code to see how much is similar

# read in file, clean it up to ready if for comparison to another file
def process_file(fname, enc):
    # open file for reading 'r'
    with open(fname, 'r', encoding=enc) as file:
        dat = file.read()  # TODO: get rid of comments
        return dat.split()  # return read data sans whitespace


def main():
    lcsf = "lcs-DP.txt"
    edit_distf = "edit_distance_DP.txt"
    classf = "prog_from_class_DP.txt"

    lcs_code = process_file(lcsf, "utf-8")
    edit_dist_code = process_file(edit_distf, "utf-8")
    class_code = process_file(classf, "utf-8")

    # print(lcs_code[:25])

    print("The LSC between {0} and {1} is {2}".format(classf, lcsf, lcs(class_code, lcs_code)))
    print("The LSC between {0} and {1} is {2}".format(classf, edit_distf, lcs(class_code, edit_dist_code)))

    print("The edit distance between {0} and {1} is {2}".format(classf, lcsf, editDistDP(class_code,
                                                                                         lcs_code,
                                                                                         len(class_code),
                                                                                         len(lcs_code))))

    print("The edit distance between {0} and {1} is {2}".format(classf, edit_distf, editDistDP(class_code,
                                                                                               edit_dist_code,
                                                                                               len(class_code),
                                                                                               len(edit_dist_code))))


if __name__ == "__main__":
    main()
