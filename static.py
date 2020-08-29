#!/usr/bin/python3

import argparse
import os
import re
import sys
import importlib

# import build.c4che._cache as c4che
from collections import defaultdict


def write_out(filename, content, mode="w"):
    """File.write convenience wrapper."""
    with open_auto(filename, mode) as require_f:
        require_f.write(content)


def open_auto(*args, **kwargs):
    """Open a file with UTF-8 encoding.

    Open file with UTF-8 encoding and "surrogate" escape characters that are
    not valid UTF-8 to avoid data corruption.
    """
    # 'encoding' and 'errors' are fourth and fifth positional arguments, so
    # restrict the args tuple to (file, mode, buffering) at most
    assert len(args) <= 3
    assert "encoding" not in kwargs
    assert "errors" not in kwargs
    return open(*args, encoding="utf-8", errors="surrogateescape", **kwargs)


def get_vars_from_cache(module_name):
    module = module_name
    c_vars = {}
    c_vars = {key: module.__getattribute__(key) for key in dir(module) if not (key.startswith("__") or key.startswith("_"))}
    return c_vars


def find_lib_if_static(key, values, libs_dictt):
    # libs_files_list = values.split()
    libs_dict = defaultdict(list)
    get_lib_name = re.compile(r"(?<=^LIB_)\w+|(?<=^STLIB_)\w+")
    lib_list_re_exclude_so = re.compile(r"(c\b|GL\b|gomp\b|pthread\b|stdc\+\+\B|gcc_s\b|gcc\b|rt\b|dl\b|m\b)")
    for lib in values:
        lib_file_re_s = "lib{}".format(lib)
        lib_file_re = re.escape(lib_file_re_s)
        compile_usr_re = r"/(usr|usr/[a-zA-Z0-9._+-\/]*)/(lib|lib64)/[a-zA-Z0-9._+-\/]*{}(\.a|_static\.a)$".format(lib_file_re)
        usr_re = re.compile(compile_usr_re)
        lib_name = re.search(get_lib_name, key).group(0)
        breakIt = False
        if lib_list_re_exclude_so.match(lib):
            key_name = "LIB_{}".format(lib_name)
            libs_dict[key_name].append("{}".format(lib))
            continue
        if lib_name == "shaderc_shared":
            key_name = "STLIB_{}".format(lib_name)
            libs_dict[key_name].append("{}".format("/usr/lib64/libshaderc_combined.a"))
            continue
        for dirpath, dirnames, filenames in os.walk("/usr/lib64", followlinks=True):
            if breakIt is False:
                for filename in filenames:
                    if breakIt is False:
                        full_match = os.path.join(dirpath, filename)
                        if usr_re.match(full_match):
                            # print("Found usr_re 1: {}".format(full_match))
                            key_name = "STLIB_{}".format(lib_name)
                            # print("Found usr_re 1: {}".format(key_name))
                            libs_dict[key_name].append("{}".format(full_match))
                            breakIt = True
                    else:
                        break
            else:
                break
        for dirpath, dirnames, filenames in os.walk("/usr/lib", followlinks=True):
            if breakIt is False:
                for filename in filenames:
                    if breakIt is False:
                        full_match = os.path.join(dirpath, filename)
                        if usr_re.match(full_match):
                            # print("Found usr_re 2: {}".format(full_match))
                            key_name = "STLIB_{}".format(lib_name)
                            # print("Found usr_re 2: {}".format(key_name))
                            libs_dict[key_name].append("{}".format(full_match))
                            breakIt = True
                    else:
                        break
            else:
                break
        for dirpath, dirnames, filenames in os.walk("/usr/cuda", followlinks=True):
            if breakIt is False:
                for filename in filenames:
                    if breakIt is False:
                        full_match = os.path.join(dirpath, filename)
                        if usr_re.match(full_match):
                            # print("Found usr_re 3: {}".format(full_match))
                            key_name = "STLIB_{}".format(lib_name)
                            # print("Found usr_re 3: {}".format(key_name))
                            libs_dict[key_name].append("{}".format(full_match))
                            breakIt = True
                    else:
                        break
            else:
                break
        for dirpath, dirnames, filenames in os.walk("/usr/nvidia", followlinks=True):
            if breakIt is False:
                for filename in filenames:
                    if breakIt is False:
                        full_match = os.path.join(dirpath, filename)
                        if usr_re.match(full_match):
                            # print("Found usr_re 4: {}".format(full_match))
                            key_name = "STLIB_{}".format(lib_name)
                            # print("Found usr_re 4: {}".format(key_name))
                            libs_dict[key_name].append("{}".format(full_match))
                            breakIt = True
                    else:
                        break
            else:
                break
        # print_fatal("Not found {}: {}".format(rg_command, err))
        if breakIt is False:
            key_name = "LIB_{}".format(lib_name)
            libs_dict[key_name].append("{}".format(lib))

    for key, values in libs_dict.items():
        print("{} = {}\n".format(key, values))
        write_out("build/c4che/my_cache.py", "{} = {}\n".format(key, values), "a")


def main():
    # with open_auto("build/c4che/_cache.py", "r") as cache_vars:
    # print ("tests: {}".format(c4che.LIB_gbm))
    # print([item for item in dir(c4che) if not (item.startswith("__") or item.startswith("_"))])
    # print([item for item in dir(c4che)])
    # print([v for v in dir(c4che) if v[:2] != "__"])
    # print("nome: {}".format("c4che"))
    c4che = importlib.import_module("build.c4che._cache")
    c4che_vars = {}
    c4che_vars = get_vars_from_cache(c4che)
    if os.path.exists("build/c4che/my_cache.py"):
        os.remove("build/c4che/my_cache.py")

    libs_dict = defaultdict(list)
    c4che_lib_try = re.compile(r"((^LIB_|^STLIB_)\w+)")
    c4che_linkflags_try = re.compile(r"^LINKFLAGS_(ffmpeg|libavdevice)")
    c4che_linkflags_try_name = re.compile(r"(?<=^LINKFLAGS_)(ffmpeg|libavdevice)")
    c4che_linkflags_filter = re.compile(r"/(usr|usr/[a-zA-Z0-9._+-\/]*)/(lib|lib64)/[a-zA-Z0-9._+-\/]*(\.a|_static\.a)$")
    for key, values in c4che_vars.items():
        if re.search(c4che_lib_try, key):
            if key != "LIB_ST" and key != "STLIB_ST" and key != "STLIB_MARKER":
                if isinstance(values, str):
                    # print("{} = '{}'".format(key, values))
                    print("Error {} {}".format(key, values))
                else:
                    # print("{} = {}".format(key, values))
                    libs_dict = find_lib_if_static(key, values, libs_dict)
                    continue
        if re.search(c4che_linkflags_try, key):
            stlibs_list = []
            linkflags_list = []
            for entry in values:
                if re.search(c4che_linkflags_filter, entry):
                    stlibs_list.append(entry)
                else:
                    linkflags_list.append(entry)
            new_key = re.search(c4che_linkflags_try_name, key).group(0)
            print("STLIB_{} = {}\n".format(new_key, stlibs_list))
            write_out("build/c4che/my_cache.py", "STLIB_{} = {}\n".format(new_key, stlibs_list), "a")
            print("{} = {}\n".format(key, linkflags_list))
            write_out("build/c4che/my_cache.py", "{} = {}\n".format(key, linkflags_list), "a")
            continue

        if isinstance(values, str):
            if key == "STLIB_ST":
                print("{} = '-Wl,-Bstatic %s'".format(key))
                write_out("build/c4che/my_cache.py", "{} = '-Wl,-Bstatic %s'\n".format(key), "a")
            elif key == "LIB_ST":
                print("{} = '-Wl,-Bdynamic -l%s'".format(key))
                write_out("build/c4che/my_cache.py", "{} = '-Wl,-Bdynamic -l%s'\n".format(key), "a")
            else:
                print("{} = '{}'".format(key, values))
                write_out("build/c4che/my_cache.py", "{} = '{}'\n".format(key, values), "a")
        else:
            print("{} = {}".format(key, values))
            write_out("build/c4che/my_cache.py", "{} = {}\n".format(key, values), "a")


def test():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--libfile", dest="libs_file", action="store", default="ffbuild/libs.mak", help="Set lib file to use",
    )
    args = parser.parse_args()
    libs_file = args.libs_file

    libs_re = re.compile(
        r"(?<=EXTRALIBS-)"
        + r"(|avutil|avcodec|avformat|avdevice|avfilter|avresample|postproc|)"
        + r"(swscale|swresample|cpu_init|cws2fws|ffplay|ffprobe|ffmpeg)"
        + r"(?==)"
    )
    libs_files_re = re.compile(r"(?<==).+$")
    lib_list_re_exclude = re.compile(r"(-L[a-zA-Z0-9_\-+\/.]*|-W[a-zA-Z0-9_\-+\/.,]*)")
    lib_list_re_exclude_so = re.compile(
        r"(-lc\b|-lGL\b|-lgomp\b|-lpthread\b|-lstdc\+\+\B|-lgcc_s\b|-lgcc\b|-lrt\b|-ldl\b|-lm\b|-pthread\b)"
    )
    Bstatic = "-Wl,-Bstatic"
    Bdynamic = "-Wl,-Bdynamic"

    lib_list_re_try = re.compile(r"(?<=-l)[a-zA-Z0-9_\-+\/.]*")
    libs_dict = defaultdict(list)

    libs_out_file = os.path.join(os.path.dirname(libs_file), "libs_var.sh")
    if os.path.exists(libs_out_file):
        os.remove(libs_out_file)

    if os.path.exists(libs_file):
        with open_auto(libs_file, "r") as libs:
            libs_lines = libs.readlines()
            # print("{} \n".format(libs_lines))
            for line in libs_lines:
                # print("{} \n".format(line))
                # print("{} = {} \n".format(re.search(libs_re, line).group(0), re.search(libs_files_re, line).group(0).split()))
                # libs_dict[re.search(libs_re, line).group(0)] = re.search(libs_files_re, line).group(0).split()
                ff_lib = re.search(libs_re, line).group(0)
                # print("{} \n".format(re.search(libs_re, line).group(0)))
                match = re.search(libs_files_re, line)
                if not match:
                    continue
                libs_files_list = match.group(0).split()
                shared = 0  # shared on: 1 shared off: 2
                for lib in libs_files_list:
                    if re.search(lib_list_re_exclude, lib):
                        libs_dict[ff_lib].append(lib)
                        # print("exclude: {}".format(lib))
                        continue
                    if re.search(lib_list_re_exclude_so, lib):
                        if (shared == 2) or (shared == 0):
                            libs_dict[ff_lib].append("{} {}".format(Bdynamic, lib))
                            shared = 1
                        else:
                            libs_dict[ff_lib].append(lib)
                            shared = 1
                        # print("exclude: {}".format(lib))
                        continue
                    if re.search(lib_list_re_try, lib):
                        lib_file_pre = re.search(lib_list_re_try, lib).group(0)
                        lib_file_re_s = "lib{}".format(lib_file_pre)
                        lib_file_re = re.escape(lib_file_re_s)
                        compile_usr_re = r"^/(usr/|usr.*)(lib|lib64)/[a-zA-Z0-9._+-\/]*{}(\.a|_static\.a)$".format(lib_file_re)
                        usr_re = re.compile(compile_usr_re)
                        breakIt = False
                        for dirpath, dirnames, filenames in os.walk("/usr/lib64", followlinks=True):
                            if breakIt is False:
                                for filename in filenames:
                                    if breakIt is False:
                                        full_match = os.path.join(dirpath, filename)
                                        if usr_re.match(full_match):
                                            if (shared == 1) or (shared == 0):
                                                libs_dict[ff_lib].append("{} {}".format(Bstatic, full_match))
                                                # print("Found usr_re: {}".format(full_match))
                                                breakIt = True
                                                shared = 2
                                            else:
                                                libs_dict[ff_lib].append(full_match)
                                                # print("Found usr_re: {}".format(full_match))
                                                breakIt = True
                                                shared = 2
                                    else:
                                        break
                            else:
                                break
                        for dirpath, dirnames, filenames in os.walk("/usr/lib", followlinks=True):
                            if breakIt is False:
                                for filename in filenames:
                                    if breakIt is False:
                                        full_match = os.path.join(dirpath, filename)
                                        if usr_re.match(full_match):
                                            if (shared == 1) or (shared == 0):
                                                libs_dict[ff_lib].append("{} {}".format(Bstatic, full_match))
                                                # print("Found usr_re: {}".format(full_match))
                                                breakIt = True
                                                shared = 2
                                            else:
                                                libs_dict[ff_lib].append(full_match)
                                                # print("Found usr_re: {}".format(full_match))
                                                breakIt = True
                                                shared = 2
                                    else:
                                        break
                            else:
                                break
                        for dirpath, dirnames, filenames in os.walk("/usr/cuda", followlinks=True):
                            if breakIt is False:
                                for filename in filenames:
                                    if breakIt is False:
                                        full_match = os.path.join(dirpath, filename)
                                        if usr_re.match(full_match):
                                            if (shared == 1) or (shared == 0):
                                                libs_dict[ff_lib].append("{} {}".format(Bstatic, full_match))
                                                # print("Found usr_re: {}".format(full_match))
                                                breakIt = True
                                                shared = 2
                                            else:
                                                libs_dict[ff_lib].append(full_match)
                                                # print("Found usr_re: {}".format(full_match))
                                                breakIt = True
                                                shared = 2
                                    else:
                                        break
                            else:
                                break
                        for dirpath, dirnames, filenames in os.walk("/usr/nvidia", followlinks=True):
                            if breakIt is False:
                                for filename in filenames:
                                    if breakIt is False:
                                        full_match = os.path.join(dirpath, filename)
                                        if usr_re.match(full_match):
                                            if (shared == 1) or (shared == 0):
                                                libs_dict[ff_lib].append("{} {}".format(Bstatic, full_match))
                                                # print("Found usr_re: {}".format(full_match))
                                                breakIt = True
                                                shared = 2
                                            else:
                                                libs_dict[ff_lib].append(full_match)
                                                # print("Found usr_re: {}".format(full_match))
                                                breakIt = True
                                                shared = 2
                                    else:
                                        break
                            else:
                                break
                        # print_fatal("Not found {}: {}".format(rg_command, err))
                        if breakIt is False:
                            if (shared == 2) or (shared == 0):
                                libs_dict[ff_lib].append("{} -l{}".format(Bdynamic, lib_file_pre))
                                shared = 1
                            else:
                                libs_dict[ff_lib].append("-l{}".format(lib_file_pre))
                                shared = 1
                print('{}_extralibs="{}"'.format(ff_lib, " ".join(libs_dict[ff_lib])))
                print("\n\n")
                write_out(
                    libs_out_file, '{}_extralibs="{}"\n'.format(ff_lib, " ".join(libs_dict[ff_lib])), "a",
                )


if __name__ == "__main__":
    main()
