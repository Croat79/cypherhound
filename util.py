import log
import re
import os

cypher_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "202", "203", "204", "205", "206"]
list_options = ["general", "user", "group", "computer", "regex", "all"]
set_options = ["user", "group", "computer", "regex"]


def validate_run_option(option):
    if option not in cypher_options:
        return False
    else:
        return True


def validate_export_command(f):
    result = 'exports/' + re.sub(r'(.txt|/)', '', f) + '.txt'
    return result


def validate_raw_command(c):
    if c == 'raw':
        return True
    else:
        return False


def validate_list_command(c):
    if c not in list_options:
        return False
    else:
        return True


def validate_set_option(option):
    if option not in set_options:
        return False
    else:
        return True


def validate_user_config(c):
    if c == "" or "@" not in c:
        return False
    else:
        return True


def validate_group_config(c):
    if c == "" or "@" not in c:
        return False
    else:
        return True


def validate_computer_config(c):
    if c == "":
        return False
    else:
        return True


def validate_regex_config(c):
    if c == "":
        return False
    else:
        return True


def validate_user_input(i):
    result = re.sub(r'(\'|")', '', i)
    return result


def handle_export(file, count, path):
    if count == 0:
        file.close()
        os.remove(path)
        log.log_no_results()
    else:
        file.close()
        log.log_successful_export(path)