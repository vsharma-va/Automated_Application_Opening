import dialog_box
import arguments
import os
import webbrowser


def main():
    all_files = []
    websites_list = []
    value = arguments.func()  # args.add_env, args.display_all_envs, args.run_existing, args.add_env_with_web
    if value[2] is not None:
        with open('env.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for element in lines:
                if element.strip('\n') == value[2]:
                    required_element = lines.index(element)
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

    if value[1] is True:
        counter = 0
        if os.path.isfile('env.txt'):
            with open('env.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    if i == 0:
                        print(lines[i].strip('\n'))
                    if lines[i] == '\n':
                        counter += 1
                        continue
                    if counter == 1:
                        print(lines[i].strip('\n'))
                        counter = 0


if __name__ == '__main__':
    main()
