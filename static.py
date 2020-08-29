#!/usr/bin/python3

import os
import re
from shutil import copyfile
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


def find_lib_if_static(key, values, with_ctx, ctx):
    # libs_files_list = values.split()
    libs_dict = defaultdict(list)
    get_lib_name = re.compile(r"(?<=^LIB_)\w+|(?<=^STLIB_)\w+")
    lib_list_re_exclude_fullpath_static = re.compile(
        r"/(usr|usr/[a-zA-Z0-9._+-\/]*)/(lib|lib64)/[a-zA-Z0-9._+-\/]*(\.a|_static\.a)"
    )
    lib_list_re_exclude_so = re.compile(r"(c\b|GL\b|gomp\b|pthread\b|stdc\+\+\B|gcc_s\b|gcc\b|rt\b|dl\b|m\b)")
    for lib in values:
        lib_file_re_s = "lib{}".format(lib)
        lib_file_re = re.escape(lib_file_re_s)
        # compile_usr_re = r"/(usr|usr/[a-zA-Z0-9._+-\/]*)/(lib|lib64)/[a-zA-Z0-9._+-\/]*{}(\.a|_static\.a)$".format(lib_file_re)
        compile_usr_re = r"^/(usr|usr/[a-zA-Z0-9._+-\/]*)/(lib|lib64)/[a-zA-Z0-9._+-\/]*{}(\.a|_static\.a)$".format(lib_file_re)
        usr_re = re.compile(compile_usr_re)
        lib_name = re.search(get_lib_name, key).group(0)
        breakIt = False
        if lib_list_re_exclude_fullpath_static.match(lib):
            key_name = "STLIB_{}".format(lib_name)
            libs_dict[key_name].append("{}".format(lib))
            continue
        if lib_list_re_exclude_so.match(lib):
            key_name = "LIB_{}".format(lib_name)
            libs_dict[key_name].append("{}".format(lib))
            continue
        if lib_name == "shaderc_shared":
            key_name = "STLIB_{}".format(lib_name)
            libs_dict[key_name].append("{}".format("/usr/lib64/libshaderc_combined.a"))
            continue
        if lib == "shaderc_shared":
            key_name = "STLIB_{}".format(lib_name)
            libs_dict[key_name].append("{}".format("/usr/lib64/libshaderc_combined.a"))
            continue
        for dirpath, dirnames, filenames in os.walk("/usr/cuda/lib64", followlinks=True):
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
        # print_fatal("Not found {}: {}".format(rg_command, err))
        if breakIt is False:
            key_name = "LIB_{}".format(lib_name)
            libs_dict[key_name].append("{}".format(lib))

    for key, values in libs_dict.items():
        print("{} = {}\n".format(key, values))
        write_out("build/c4che/_cache.py", "{} = {}\n".format(key, values), "a")
        if with_ctx is True:
            ctx.env[key] = values


def main():
    with_ctx = False
    copyfile("build/c4che/_cache.py", "build/c4che/_cachebak.py")
    # with open_auto("build/c4che/_cache.py", "r") as cache_vars:
    # print ("tests: {}".format(c4che.LIB_gbm))
    # print([item for item in dir(c4che) if not (item.startswith("__") or item.startswith("_"))])
    # print([item for item in dir(c4che)])
    # print([v for v in dir(c4che) if v[:2] != "__"])
    # print("nome: {}".format("c4che"))
    c4che = importlib.import_module("build.c4che._cache")
    c4che_vars = {}
    c4che_vars = get_vars_from_cache(c4che)
    if os.path.exists("build/c4che/_cache.py"):
        os.remove("build/c4che/_cache.py")

    if with_ctx is True:
        for key, values in c4che_vars.items():
            ctx.env[key] = []

    # libs_dict = defaultdict(list)
    c4che_lib_try = re.compile(r"((^LIB_|^STLIB_)\w+)")
    # c4che_linkflags_try = re.compile(r"^LINKFLAGS_(ffmpeg|libavdevice)")
    # c4che_linkflags_try_name = re.compile(r"(?<=^LINKFLAGS_)(ffmpeg|libavdevice)")
    # c4che_linkflags_filter = re.compile(r"/(usr|usr/[a-zA-Z0-9._+-\/]*)/(lib|lib64)/[a-zA-Z0-9._+-\/]*(\.a|_static\.a)$")
    c4che_exclude_rpath = re.compile(r"(^RPATH_\w+)")
    for key, values in c4che_vars.items():
        if re.search(c4che_lib_try, key):
            if key != "LIB_ST" and key != "STLIB_ST" and key != "STLIB_MARKER":
                if isinstance(values, str):
                    # print("{} = '{}'".format(key, values))
                    print("Warning Error {} {}".format(key, values))
                else:
                    # print("{} = {}".format(key, values))
                    if with_ctx is True:
                        find_lib_if_static(key, values, with_ctx, ctx)
                    else:
                        find_lib_if_static(key, values, with_ctx, None)
                    continue
        """ if re.search(c4che_linkflags_try, key):
            # ctx.env[key] = []
            stlibs_list = []
            linkflags_list = []
            for entry in values:
                if re.search(c4che_linkflags_filter, entry):
                    stlibs_list.append(entry)
                else:
                    linkflags_list.append(entry)
            new_key_name = re.search(c4che_linkflags_try_name, key).group(0)
            new_key_stlib = "STLIB_{}".format(new_key_name)
            if with_ctx is True:
                ctx.env[new_key_stlib] = []
            new_key_linkflags = "LINKFLAGS_{}".format(new_key_name)
            if with_ctx is True:
                ctx.env[new_key_linkflags] = []
            print("{} = {}\n".format(new_key_stlib, stlibs_list))
            write_out("build/c4che/_cache.py", "{} = {}\n".format(new_key_stlib, stlibs_list), "a")
            if with_ctx is True:
                ctx.env[new_key_stlib] = stlibs_list
            print("{} = {}\n".format(new_key_linkflags, linkflags_list))
            write_out("build/c4che/_cache.py", "{} = {}\n".format(new_key_linkflags, linkflags_list), "a")
            if with_ctx is True:
                ctx.env[new_key_linkflags] = linkflags_list
            continue """

        if isinstance(values, str):
            if key == "STLIB_ST":
                print("{} = '%s'".format(key))
                write_out("build/c4che/_cache.py", "{} = '%s'\n".format(key), "a")
                if with_ctx is True:
                    ctx.env[key] = "%s"
            # elif key == "LIB_ST":
            #    print("{} = '-Wl,-Bdynamic -l%s'".format(key))
            #    write_out("build/c4che/_cache.py", "{} = '-Wl,-Bdynamic -l%s'\n".format(key), "a")
            else:
                print("{} = '{}'".format(key, values))
                write_out("build/c4che/_cache.py", "{} = '{}'\n".format(key, values), "a")
                if with_ctx is True:
                    ctx.env[key] = values
        else:
            if re.search(c4che_exclude_rpath, key):
                if key != "RPATH_ST":
                    if with_ctx is True:
                        ctx.env[key] = []
                    continue
            print("{} = {}".format(key, values))
            write_out("build/c4che/_cache.py", "{} = {}\n".format(key, values), "a")
            if with_ctx is True:
                ctx.env[key] = values


if __name__ == "__main__":
    main()
