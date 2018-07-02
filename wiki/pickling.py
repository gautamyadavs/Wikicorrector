import re, pickle, os, bz2
from string import ascii_lowercase


all = "static/extract/"
flag = 1
pickle_off = open("static/title_to_surface_names_with_uid.pickle","rb")
new_dict = pickle.load(pickle_off)
#new_dict = sorted(dict.items(), key=lambda s: s[0])


for n in new_dict.keys():
    directory = os.path.dirname(all+n[0].lower()+'/')
    if os.path.exists(directory):
        print(n+" writing at "+n[0].lower()+"/ folder")
        with open(all+n[0].lower()+'/data.pickle', 'wb') as f:
            example_dict = {}
            example_dict[n] = new_dict[n]
            pickle_out = open(all+n[0].lower()+'/data.pickle',"wb")
            pickle.dump(example_dict, pickle_out)
            pickle_out.close()
    else:
        print(n+" writing at "+n[0].lower()+"/ folder")
        os.makedirs(directory)
        example_dict = {}
        example_dict[n] = new_dict[n]
        with open(all+n[0].lower()+'/data.pickle', 'wb') as f:
            pickle.dump(example_dict, f, pickle.HIGHEST_PROTOCOL)
