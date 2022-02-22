#!/usr/bin/env python
import dialog_box
import arguments
import os
import webbrowser


def main():
    all_files = []
    websites_list = []
    value = arguments.arguments()  # args.add_env, args.display_all_envs, args.run_existing,
    if value[2] is not None:       # args.add_env_with_web, args.del_all_envs, args.delete_env
        with open('env.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for element in lines:
                if element.strip('\n') == value[2]:
                    required_element = lines.index(element)
        file.close()
        cont = False
        link_cont = False
        for i in range(len(lines)):
            if i == required_element + 1 or cont:
                cont = True
                all_files.append(lines[i].strip('\n'))
                if lines[i] == '\n':
                    all_files.append(lines[i])
                    cont = False
                    break

        for z in all_files:
            if z == "Websites" or link_cont:
                link_cont = True
                websites_list.append(z)
                all_files.remove(z)
                if z == '\n':
                    link_cont = False
                    break

        for programs in all_files:
            os.startfile(programs)

        for links in websites_list:
            webbrowser.get('windows-default').open(links)
            print(links)

    if value[0] is True or value[3] is not None:
        dialog_box.main()

    if value[4]: # del_all_envs
        os.remove('env.txt')

    if value[5] is not None:  # del_env
        cont = False
        to_remove = []
        with open('env.txt', 'r', encoding='utf-8') as f:
            path = f.readlines()
        for i in range(len(path)):
            if path[i].strip('\n') == value[5] or cont:
                cont = True
                to_remove.append(path[i])
            elif path[i] == '\n':
                cont = False
                break
        final = [x for x in path if x not in to_remove]
        f.close()
        with open('env.txt', 'w', encoding='utf-8') as file_write:
            file_write.writelines(final)

    if value[1] is True:
        if os.path.isfile('env.txt'):
            with open('env.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for i in lines:
                    if '/' not in i:
                        print(i.strip('\n'))
            file.close()


if __name__ == '__main__':
    main()
