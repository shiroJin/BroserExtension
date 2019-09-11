#!/usr/local/bin/python3
import os
import re
import sys
import argparse
import plistlib
import json

def modifyPbxproj():
  data = ''
  flag = False
  end = False
  with open(filePath, 'r') as file:
    for line in file.readlines():
      if not end:
        find = line.find('3B02599D20F49A43001F9C82 /* Debug */')
        if find != -1:
          flag = True
        if flag and re.search('PRODUCT_BUNDLE_IDENTIFIER', line):
          line = line.replace('quanbin.jin-test.sharkORMDemo', 'quanbin.jin-test.Demo')
          end = True
      data += line

  with open(filePath, 'w') as file:
    file.writelines(data)

# modify display name, version and build in info.plist file
def modifyInfoPlist (displayName, version, build):
  plistPath = os.path.join(filePath, 'Butler/ButlerForRemain/ButlerForRemain-Info.plist')
  with open(plistPath, 'rb') as fp:
    plist = plistlib.load(fp)
    plist['CFBundleVersion'] = build
    plist['CFBundleDisplayName'] = displayName
    plist['CFBundleShortVersionString'] = version

  with open(plistPath, 'wb') as fp:
    plistlib.dump(plist, fp)

# 解析JSON文件, 验证数据完整性
def jsonParser(filePath):
  with open(filePath) as fp:
    jsonObj = json.load(fp)
  
  try:
    jsonObj["requestURL"]
    jsonObj["version"]
    jsonObj["build"]
    jsonObj["displayName"]
  except KeyError as undefinedKey:
    print(str(undefinedKey) + ' missed')
    exit(0)

  return jsonObj

def setRequestBaseURL(baseURL):
  
  with open as target:
    pass
  pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('filePath', help='工程根目录')
  filePath = parser.parse_args().filePath

  # modifyInfoPlist('物管APP', '1.9.2_A1', '2')
  config = jsonParser('/Users/remain/Desktop/pythonTest/jsonFile')

  exit(0)