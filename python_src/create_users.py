'''
INSTRUCTIONS FOR NEW SEASON:
0) Change SEASON_OUTPUT IN myrtastats_analysis repository
1) on index.html add new div with the season
2) RUN python create_users.py AFTER CHANGING 'season' variable
'''

import os 

import shutil, errno

# CHANGE THIS LINE EACH SEASON
# season = "output_s15_sl2"
season = "output_s16"

season_dir = "html/" + season
main_files = ["/main.html","/top100.html","/monsters.html"]
data_user_file = "data/" + season + "/users"
html_user_file = "html/" + season + "/users/"
html_template_file = "html/" + season + "/user_template.html"

template_folder = "html/template_folder"

def main() -> None:
    os.chdir("./..")
    # create_dirs()
    # copy template to make new season directory
    copy_template()
    # replace XXX with season number in EVERY FILE
    replaceXXX()
    # # create users specified in `user_template.html`
    create_users_html()

def create_dirs() -> None:
    if not os.path.exists(season_dir):
        os.makedirs(season_dir)
    for each in main_files:
        main_file = season_dir + each
        if not os.path.exists(main_file):
            open(main_file, 'a').close()
    for user in os.listdir(data_user_file):
        if not os.path.exists(html_user_file):
            os.makedirs(html_user_file)
        user_file = html_user_file + user + ".html"
        if not os.path.exists(user_file):
            with open(user_file, 'a'):
                os.utime(user_file, None)
    user_main_html = html_user_file + "users.html"
    if not os.path.exists(user_main_html):
        with open(user_main_html, 'a'):
            os.utime(user_main_html, None)

def copy_template() -> None:
    src = template_folder
    dst = season_dir
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def replaceXXX() -> None:
    seasonNo = season.split('_s')[1]
    for each in os.listdir(season_dir):
        if each == "users":
            each += "/users.html"
        # Read in the file
        filename = season_dir + "/" + each
        with open(filename, 'r') as f :
            filedata = f.read()

        # Replace the target string
        filedata = filedata.replace('XXX', seasonNo)

        # Write the file out again
        with open(filename, 'w') as f:
            f.write(filedata)

def create_users_html() -> None:
    template = open(html_template_file, 'r').read()
    for each in os.listdir(data_user_file):
        html_file = html_user_file + each + ".html"
        with open(html_file, 'w') as f:
            f.write(template)
    
if __name__ == "__main__":
    main()