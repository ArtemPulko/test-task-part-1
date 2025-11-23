def get_chromedriver_path(path):
  driver_name = 'chromedriver.exe'
  project_root = path.parents[2]
  return project_root / 'drivers' / driver_name