# Replacing in string:

url = input("URL: ").strip();

username = url.replace("https://google.com/", "");

print(f"username: {username}");

# aliter:
username2 = url.removeprefix("https://google.com/");
print(f"username: {username2}");

# above using regex:

# re.sub: Syntax: (pattern, repl,string, count=0, flags=0)

"""
sub means Substitute
"""
print("-----------------------------------");

import re;

username = re.sub(r"^(https?://)?(www\.)?google\.com/.+", "", url);
print(f"username: {username}");

# aliter: above re.search:

print("-------------------");
matches = re.search(r"^https?://(?:www\.)?google\.com/([a-z0-9]+)$", url, re.IGNORECASE);
# print(matches);
# print(matches.group(0));
# print(matches.group(1));
# print(matches.group(2));

if(matches):
    print(f"username: {matches.group(1)}");


# now if we dont want to capture a group enclosed in (). we useL (?:) -  


