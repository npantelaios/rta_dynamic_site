import os 

# CHANGE THIS LINE EACH SEASON
season = "output_s15_sl2"

season_dir = "html/" + season
main_files = ["/main.html","/top100.html","/monsters.html"]
data_user_file = "data/" + season + "/users"
html_user_file = "html/" + season + "/users/"
html_template_file = "html/" + season + "/user_template.html"

def main() -> None:
    os.chdir("./..")
    create_dirs()
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

def create_users_html() -> None:
    template = open(html_template_file, 'r').read()
    for each in os.listdir(data_user_file):
        html_file = html_user_file + each + ".html"
        with open(html_file, 'w') as f:
            f.write(template)
    
if __name__ == "__main__":
    main()