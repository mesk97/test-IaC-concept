import re
import sys
import yaml

def main(workflows):
    components = {}
    update_nums = len(workflows)
    update_names = []

    for update in range(update_nums):
        #print (workflows[update])
        m = re.match(r'.*/(\d+\.\d+)', workflows[update])
        update_names.append(str(m.group(1)))

        with open(workflows[update], "r") as stream:
            file = yaml.safe_load(stream)

        for (name, value) in file["component_dependencies"].items():
            if "update" in value["stages"] and bool(value["stages"]["update"]) == True:
                if not name in components:
                    components[name] = [None for i in range(update_nums)]
                components[name][update] = bool(value["enable_update"])

    print ("Name\t%s" % ("\t".join(update_names)))
    for (name, value) in components.items():
        print("%s\t%s" % (name, "\t".join([str(i) for i in value])))

if __name__ == "__main__":
    main(sys.argv[1:])