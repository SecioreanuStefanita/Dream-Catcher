import os


def get_os_homepath():
    return os.path.expanduser('~')


def create_or_get_dir_location(domain, service):
    path = get_os_homepath()
    full_path = path + "/Desktop/" + f"Dream_Catcher_Outputs/{domain}_results/{service}"
    if not os.path.exists(path+"/Desktop/" + f"Dream_Catcher_Outputs/{domain}_results/{service}"):
        os.makedirs(path+"/Desktop/" + f"Dream_Catcher_Outputs/{domain}_results/{service}")
        full_path = path+"/Desktop/" + f"Dream_Catcher_Outputs/{domain}_results/{service}"
        return full_path
    else:
        return full_path