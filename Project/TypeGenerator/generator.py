#!/usr/bin/env python3.4

import re

def generate_enum(type_list):
    code = \
"""/*
** Code generated by ECSess in c++11
*/

#pragma once

namespace ECSTypes {
\tenum class ComponentsTypes {
"""
    for i, t in enumerate(type_list):
        code += "\t\t" + t + " = " + str(i) + ("," if i < len(type_list) else "") + "\n"
        
    code += "\t};\n}\n"
    return code

def get_derived_classes(files, baseClass):
    classes = []
    for f in files:
        op_file = open(f, "r")
        content = op_file.read()
        content = content.replace('\n', '')
        # print("class.*?" + baseClass + "[' '|'\t']*\{.*?\};")
        m = re.findall("class.*?\{.*?\};", content, re.DOTALL)
        for _class in m:
            strs = _class.split()
            for strr in strs:
                if strr == baseClass:
                    classes.append(strs[1])
        op_file.close()
    return classes

##print(generate_enum(["CollideBox", "SpriteComp", "CoordComp"]))
f = open("ECSTypes.hpp", "w")
f.write(generate_enum(get_derived_classes(["test.cpp"], "titi")))
f.close()
